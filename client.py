import sys
import socket
import argparse
from urllib.parse import urlparse, urlencode, parse_qs, urlunparse

# HTTP Client Library
        
def http_get(url, headers=None, verbose=False, output=None):
    # Parse the URL
    parsed_url = urlparse(url)
    host = parsed_url.netloc
    path = parsed_url.path if parsed_url.path else '/'
    query = parsed_url.query if parsed_url.query else ''

    # Parse query parameters from the URL
    query_params = parse_qs(query)
    
    # Construct the query string
    query_string = urlencode(query_params, doseq=True)

    # Create a socket connection
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, 80))

        # Construct the GET request with query parameters
        request = f"GET {path}?{query_string} HTTP/1.1\r\n"
        request += f"Host: {host}\r\n"
        if headers:
            request += '\r\n'.join(headers) + '\r\n'
        request += "\r\n"

        # Send the request
        s.sendall(request.encode())

        # Receive and parse the response
        response = s.recv(4096).decode()

        # Split the response into headers and body
        res_headers, body = response.split('\r\n\r\n', 1)
        
        # Parse and check for redirection (3xx status codes)
        header_lines = res_headers.split('\r\n')
        http_version, status_code, reason = header_lines[0].split(' ', 2)
        
        if status_code.startswith('3'):
            # Handle redirection by extracting the new URL from the "Location" header
            location_header = [line for line in header_lines if line.startswith("Location: ")]
            
            if location_header:
                new_url = location_header[0][len("Location: "):]
                path = new_url.strip()
                url = urlunparse(parsed_url._replace(path=path))
                print(f"redirect URL - {url}")
                return http_get(url, headers, verbose, output)
            else:
                print("No redirect URL present")
                sys.exit(1)
            
        if verbose:
            # Parse and print the headers
            header_lines = res_headers.split('\r\n')
            http_version, status_code, reason = header_lines[0].split(' ', 2)
            print(f"{http_version} {status_code} {reason}")
            for header in header_lines[1:]:
                print(header)

            # Print the response body
            print("\n" + body)
        else:
            print(body)
        if output:
            with open(output, 'w') as file:
                file.write(body)
 
def http_post(url, data, headers=None, verbose=False, output=None):
    # Parse the URL
    parsed_url = urlparse(url)
    host = parsed_url.netloc
    path = parsed_url.path if parsed_url.path else '/'

    # Create a socket connection
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, 80))

        # Construct the POST request
        request = f"POST {path} HTTP/1.1\r\n"
        request += f"Host: {host}\r\n"
        if headers:
            request += '\r\n'.join(headers) + '\r\n'
        request += f"Content-Length: {len(data)}\r\n\r\n"
        request += data

        # Send the request
        s.sendall(request.encode())

        # Receive and parse the response
        response = s.recv(4096).decode()

        # Split the response into headers and body
        headers, body = response.split('\r\n\r\n', 1)

        if verbose:
            # Parse and print the headers
            header_lines = headers.split('\r\n')
            http_version, status_code, reason = header_lines[0].split(' ', 2)
            print(f"{http_version} {status_code} {reason}")
            for header in header_lines[1:]:
                print(header)

            # Print the response body
            print("\n" + body)
        else:
            print(body)
        
        if output:
            with open(output, 'w') as file:
                file.write(body)

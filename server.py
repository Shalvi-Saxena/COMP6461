import threading
import socket

def handle_request(client_socket):
    # Receive the client's request
    request_data = b""
    while True:
        chunk = client_socket.recv(1024)
        if not chunk:
            break
        request_data += chunk

    # Parse the HTTP request
    request_lines = request_data.decode("utf-8").split("\r\n")
    if len(request_lines) < 1:
        return

    request_line = request_lines[0].split()
    if len(request_line) < 3:
        return

    method, path, _ = request_line

    # Prepare an HTTP response (simplified for demonstration)
    response = "HTTP/1.1 200 OK\r\n"
    response += "Content-Type: text/html\r\n"
    response += "\r\n"
    response += "<html><body><h1>Hello, World!</h1></body></html>"

    # Send the response back to the client
    client_socket.send(response.encode("utf-8"))

    # Close the client socket
    client_socket.close()

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr[0]}:{addr[1]}")
        client_thread = threading.Thread(target=handle_request, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    start_server("localhost", 8080)

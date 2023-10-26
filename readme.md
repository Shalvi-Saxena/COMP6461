## Helpful Commands to test

### To make python file executable run to following
- chmod +x httpc.py
- export PATH=$PATH:$(pwd)

### To test run to following
- General
    - httpc help
    - httpc help get
    - httpc help post
- Get -
    - httpc get 'http://httpbin.org/get?course=networking&assignment=1'
    - httpc get -h 'User-Agent: MyClient' -h 'User-Agent2: MyClient2' 'http://httpbin.org/get?course=networking&assignment=1'
    - httpc get -v -h 'User-Agent: MyClient' 'http://httpbin.org/get?course=networking&assignment=1'
    
- Post - 
    - httpc post -h 'Content-Type:application/json' -d '{"Assignment": 1}' 'http://httpbin.org/post'
    - httpc post -h 'User-Agent: MyClient' -h 'Content-Type:application/json' -d '{"Assignment": 1}' 'http://httpbin.org/post'
    - httpc post -h 'Content-Type:application/json' -f 'body.txt' 'http://httpbin.org/post'
    - httpc post -v -h 'Content-Type:application/json' -f 'body.txt' 'http://httpbin.org/post' -o hello.txt
    - httpc post -h 'Content-Type:application/json' -f 'body.txt' 'http://httpbin.org/post' -o hello.txt
- Post edge case -
    - httpc post -h 'Content-Type:application/json' -d '{"Assignment": 1}' -f 'body.txt' 'http://httpbin.org/post'
    - httpc post -h 'Content-Type:application/json' 'http://httpbin.org/post'
- Bonus questions -
    - httpc get -h 'User-Agent: MyClient' 'http://httpbin.org/get?course=networking&assignment=1' -o hello.txt
    - httpc get -h 'User-Agent: MyClient' 'http://httpbin.org/redirect/4'
    - httpc get -v 'http://httpbin.org/redirect/4'
    - httpc post -v -h 'Content-Type:application/json' -f 'body.txt' 'http://httpbin.org/post' -o hello.txt
    - httpc post -h 'Content-Type:application/json' -f 'body.txt' 'http://httpbin.org/post' -o hello.txt


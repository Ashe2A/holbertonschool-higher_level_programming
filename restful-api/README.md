# [Python - RESTful API](https://intranet.hbtn.io/projects/3111)

## 0. Basics of HTTP/HTTPS
**HTTP (HyperText Transfer Protocol)** is a protocol that is used on websites' API to indicate the result of a request. **HTTPS** (S standing for Secure) is just like HTTP but with an added layer of security using SSL/TLS encryption. HTTP transfers plain data, whereas HTTPS uses encryption to avoid data eavesdropping. Lately, some websites that use HTTPS prevent HTTP requests to be made.

Upon monitoring the network requests, there is no information (as it wasn't saved by the browser). However, upon refreshing, even standard websites such as Jisho, a Japanese-English dictionary, shows six different requests (an HTML document, a CSS stylesheet, a JS script, and three two PNG images and a ICO favicon, displayed on the tab) all returning HTTP 200 (OK).

Common HTTP methods:
- **POST** to add new data
- **GET** to retrieve data
- **PUT/UPDATE** to edit data
- **DELETE** to remove data

Common return HTTP codes:
- **HTTP 200 (OK)** is used when there is no error and there is no creation
- **HTTP 404 (Not Found)** is used when a requested resource is not found
- **HTTP 500 (Internal Server Error)** is used when there is an error within the back-end of the website
- **HTTP 503 (Service Unavailable)** is used the server is not ready to handle the request

## 1. Consume data from an API using command line tools (curl)
Install curl with `apt install curl` within my Linux distribution, here are my CURL details (with `curl --version`):
```bash
curl 7.81.0 (x86_64-pc-linux-gnu) libcurl/7.81.0 OpenSSL/3.0.2 zlib/1.2.11 brotli/1.0.9 zstd/1.4.8 libidn2/2.3.2 libpsl/0.21.0 (+libidn2/2.3.2) libssh/0.9.6/openssl/zlib nghttp2/1.43.0 librtmp/2.3 OpenLDAP/2.5.18
Release-Date: 2022-01-05
Protocols: dict file ftp ftps gopher gophers http https imap imaps ldap ldaps mqtt pop3 pop3s rtmp rtsp scp sftp smb smbs smtp smtps telnet tftp 
Features: alt-svc AsynchDNS brotli GSS-API HSTS HTTP2 HTTPS-proxy IDN IPv6 Kerberos Largefile libz NTLM NTLM_WB PSL SPNEGO SSL TLS-SRP UnixSockets zstd
```

Fetching webpage content:
* `curl http://example.com` gives an [HTML page](example.com.html) as an output.
* `curl https://jsonplaceholder.typicode.com/posts` gives a [JSON array of posts](posts.json) as an output.
* `curl -I https://jsonplaceholder.typicode.com/posts` gives [the headers of the JSON array](posts-i.txt) as an output. 
* `curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts` gives a [JSON array of posted data](foobar.json) as an output (with `-X` for HTTP method, here `POST`, and `-d` for the data input).

## 2. Consuming and processing data from an API using Python
### [`task_02_requests.py`](task_02_requests.py) / [`main_02_requests.py`](main_02_requests.py)
* Functions that fetch posts from JSON PlaceHolder, and either prints the posts' titles or convert the posts JSON into a [CSV file](posts.csv).

## 3. Develop a simple API using Python with the `http.server` module
### [`task_03_http_server.py`](task_03_http_server.py)
* With the `BaseHTTPRequestHandler` module and the `HTTPServer` from the `http.server` module, created a subclass `MyServer` managing a custom HTTP local server (port 8000); `do_GET` is called when a `GET` method (default) is called in the API:
    * On homepage (endpoint `/`), plain text (welcoming message) `"Hello, this is a simple API!"` is displayed
    * On `/data` page, a simple JSON (`{"name": "John", "age": 30, "city": "New York"}`) is loaded.
    * On `/status` page, a plain text `"OK"` is displayed.
    * `/info` loads the JSON `{"version": "1.0", "description": "A simple API built with http.server"}`
    * If the endpoint is none of the above `404 Not Found`.

## 4. Develop a Simple API using Python with Flask
### [`task_04_flask.py`](task_04_flask.py)
* With the `Flask` server class from the `flask` module, created a flask-based server. Every return is displayed/loaded on the corresponding endpoints' pages :
    * On homepage (endpoint `/`), the welcoming message `"Welcome to the Flask API!"` is returned and displayed.
    * On `/data` page, the user dictionary converted into a JSON dictionary is returned and loaded. The `users` dictionary is managed in the module but outside of endpoints.
    * On `/status` page, a plain text `"OK"` is returned and displayed.
    * On `/users/<username>` pages (with `<username>` being replaced by an actual username no matter if it exists in the `users` dictionary), the JSON of the specified user is returned and loaded.
        * If the user doesn't exist, `{"error": "User not found"}` is returned.
    * On `/add_user` page, the `users` dictionary is updated with a new user and a "new user" JSON message is returned and loaded (also returns an `HTTP 201` status code).
        * If no username is specified, `{"error": "Username is required"}` is returned with an `HTTP 400` status code.
        * If the request isn't using the `POST` method, `{"error": "Adding an user is a post request"}` is returned with an `HTTP 400` status code.
        * Examples of CURL commands to add users:
        ```
        curl -X POST http://localhost:5000/add_user -H "Content-Type: application/json" -d '{"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"}'
        ```
        ```
        curl -X POST http://localhost:5000/add_user -H "Content-Type: application/json" -d '{"username": "john", "name": "John", "age": 30, "city": "New York"}'
        ```

## 5. API Security and Authentication Techniques
### [`task_05_basic_security.py`](task_05_basic_security.py)
* **Basic HTTP Authentication (with `Flask-HTTPAuth`):** Creates and list of users and their hashed passwords, using the the `werkzeug.security` library for password hashing and verification.

* **JWT-based Authentication (with `Flask-JWT-Extended`):** Creates and uses a secret key for token generation and validation. Also restrains non-admin users from accessing admin-exclusive routes.

#### 1. Basic Authentication:
* Protected Route:
    * URL: `/basic-protected`
        * The route is protected by `@auth.login_required`, running the method in the route only if the `verify_password()` method returns the requested username (meaning authentification succeeded)
    * Method: `GET`
    * Description: Returns a message `"Basic Auth: Access Granted"` if the user provides valid basic authentication credentials.
    * Authentication: Basic
    * **Test:** Accessing the route prompts the user authentification through a dialogue box. The users should be contained in a dictionary :
    ```
    {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        }
    }
    ```

#### 2. JWT Authentication:
* Protected Route:
    * URL: `/login`
    * Method: `POST` (Requires a username and password keys in aa posted JSON)
    * Description: Accepts JSON payload with `username` and `password.` Returns a JWT token if credentials are valid.
    * **Test:** `{"username": "user1", "password": "password"}` which responds with `{"access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc1MjAxMzE5NiwianRpIjoiYTIwNTg4MGUtMWVjMS00ZmEwLThhODctZWQ4ZTc4MjQxMjE0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImFkbWluMSIsIm5iZiI6MTc1MjAxMzE5NiwiY3NyZiI6IjllMTk0ZTJmLTJiZmYtNDA2Ni1iNTEzLWJkZjY3NDc3ZWI3NCIsImV4cCI6MTc1MjAxNDA5Nn0.wykG4Zyhl0GsbIRl9x2AleTsXCk6tFcxcLvoQJeGbKw"}` (with the new token being created)

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

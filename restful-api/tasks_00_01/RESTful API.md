## Basics of HTTP/HTTPS
### Differences between HTTP and HTTPS
Basic HTTP uses hypertext requests to servers, in order to transfer (read and/or write) data. HTTPS is a secured HTTP where data is encrypted. With HTTPS, attackers would read the transferred data as a hashcode, preventing them from having data access.

### Common requests :
* **GET** - read data request :
    * Fetching a web page or data from an API
* **POST** - write data request :
    * Insert new line in API database
* **PUT**/**PATCH** - edit data request :
    * Update date in API database
* **DELETE** - delete data request :
    * Delete data in API database

### Common HTTP status codes :
* 200 OK - Request went without error
* 304 Not Modified - No need to retransmit the requested data
* 403 Forbidden - User doesn't have access rights to data
* 404 Not found - Requested data doesn't exist
* 502 Bad Gateway - An error occured in the gateway servers the request was passing through

## Client URL
**Curl version :** ```curl 7.81.0 (x86_64-pc-linux-gnu)```

**Other supported protocols versions :**
```shell
libcurl/7.81.0
OpenSSL/3.0.2
zlib/1.2.11
brotli/1.0.9
zstd/1.4.8
libidn2/2.3.2
libpsl/0.21.0 (+libidn2/2.3.2)
libssh/0.9.6/openssl/zlib
nghttp2/1.43.0
librtmp/2.3
OpenLDAP/2.5.18
```

### JSON Placeholder
**Source :** [JSON placeholder](https://jsonplaceholder.typicode.com/posts)
#### 1. **Fetching a Placeholder with ```curl```** [(Result)](placeholder_fetch.md)

#### 2. **Fetching header with ```curl -I```** [(Result)](placeholder_header.md)

#### 3. **HTTP POST request with ```curl -X POST```**

* **Specified data** (with ```-d``` option) : ```"title=foo&body=bar&userId=1"```

* [**(Result)**](placeholder_post.json)

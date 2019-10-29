# HTTP client/server using sockets

Mini-project to learn about socket programming and HTTP.

Uses just the Python `socket` library.

## Usage

### Client

Performs a `GET` request (using HTTPS) to the given `hostname`. (TODO: Accept a full URL
with path instead.)

```
$ python3 client.py www.insynchq.com
Response received from www.insynchq.com:

Status code: 200

Headers: {'Server': 'openresty/1.7.2.1', 'Date': 'Tue, 29 Oct 2019 05:58:53 GMT', 'Content-Type': 'text/html; charset=utf-8', 'Content-Length': '16587', 'Connection': 'close'}

Body:
<!DOCTYPE html>
<html>

<head>
...
```

### Server

(Work in progress)

```
$ python3 server.py # Runs on the local host at port 8080
```

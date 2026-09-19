---
title: HTTP Basics
description: A concise overview of HTTP requests, responses, methods, status codes, headers, bodies, and HTTPS.
tags: HTTP, HTTPS, web, request, response, methods, status codes, headers, API
---

# HTTP Basics

HTTP is an application protocol used to exchange resources between clients and servers. A client sends a request, and the server returns a response.

## Requests and responses

A request contains a method, target URL, headers, and sometimes a body. A response contains a status code, headers, and sometimes a body.

Common request methods include:

- `GET`: Retrieve a representation of a resource.
- `POST`: Submit data for processing or create a subordinate resource.
- `PUT`: Create or replace a resource at a known target.
- `PATCH`: Apply a partial modification.
- `DELETE`: Remove a resource.
- `HEAD`: Retrieve the same headers as `GET` without a response body.

`GET` and `HEAD` are defined as safe methods because they are intended for reading. `GET`, `HEAD`, `PUT`, and `DELETE` are idempotent: repeating the same request is intended to have the same effect as making it once, although each request can still produce logs or other observations.

## Status codes

Status codes are grouped by their first digit:

- `1xx`: Informational response.
- `2xx`: Successful response, such as `200 OK` or `201 Created`.
- `3xx`: Redirection, such as `301 Moved Permanently` or `304 Not Modified`.
- `4xx`: Client-side error, such as `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, or `404 Not Found`.
- `5xx`: Server-side error, such as `500 Internal Server Error` or `503 Service Unavailable`.

## Headers and content

Headers carry metadata. Common examples include:

- `Content-Type`: The media type of the body, such as `application/json`.
- `Accept`: Media types the client can process.
- `Authorization`: Credentials for an authentication scheme.
- `Cache-Control`: Rules for caching a response.
- `Location`: A URL associated with a redirect or newly created resource.

HTTP header names are case-insensitive. The interpretation of a body depends on its media type and any declared character encoding.

## HTTPS

HTTPS is HTTP protected by TLS. It provides encryption in transit, integrity protection, and server authentication when certificates are validated correctly. Sensitive credentials should not be placed in URLs because URLs can be stored in browser history, logs, and intermediary systems.

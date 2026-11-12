# HTTP trace 1 — Paginated payments

Trace this interaction and answer every question before writing code.

```text
GET /v1/payments?limit=2 HTTP/1.1
Authorization: Bearer <redacted>
Accept: application/json

HTTP/1.1 200 OK
Content-Type: application/json
Request-Id: req_101

{"data":[{"id":"p1","amount":500},{"id":"p2","amount":300}],"has_more":true,"next_cursor":"p2"}
```

1. What changes in the second request?
2. Which fields must be validated before use?
3. What stops pagination?
4. What can go wrong between pages?
5. Write a Python function around a supplied `send_get(path, params, timeout)` callable. Handle non-200 responses, invalid JSON, missing fields, and repeated cursors.
6. Test empty data, one page, multiple pages, 500, malformed JSON, and cursor loop.


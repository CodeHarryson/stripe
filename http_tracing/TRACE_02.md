# HTTP trace 2 — Safe retries and idempotency

```text
POST /v1/refunds HTTP/1.1
Idempotency-Key: refund-order-77
Content-Type: application/json

{"charge_id":"ch_1","amount":500}
```

The client times out before receiving a response.

1. Why is immediately sending an unrelated new idempotency key dangerous?
2. Which failures are plausibly retryable: connection timeout, 400, 409, 429, 500, 503?
3. What does exponential backoff with jitter accomplish?
4. What information should be logged without exposing secrets?
5. Sketch `create_refund(send, payload, idempotency_key)` with a bounded retry policy.
6. Explain at-least-once delivery versus exactly-once effects.


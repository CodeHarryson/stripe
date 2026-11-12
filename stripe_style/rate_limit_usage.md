# Rate-limit usage pressure simulation

Records contain `request_id`, `account_id`, `endpoint`, `timestamp_seconds`, and `status`.

Part 1: return request counts per account.

At minute 20: add endpoint-specific maximums for a fixed 60-second window and return allow/deny decisions in input order.

At minute 32: request IDs can repeat and window-boundary timestamps matter. State whether the window is `[t-59, t]` or another interval and test it.

At minute 38: explain one design improvement you would make with more time. Do not rewrite the solution.


# Account command processor

Process commands in order:

- `CREATE <id> <name>`
- `ADD <id> <amount_cents>`
- `FREEZE <id>`
- `BALANCE <id>`

Return a list containing the result of every `BALANCE`. Decide how invalid operations are represented and state the decision before coding.

## Extension

Add `TRANSFER <source> <destination> <amount_cents>`. A transfer is atomic, cannot overdraw, and cannot involve a frozen account. Preserve all earlier behavior.

## Merchant aggregation follow-up

Given `timestamp|merchant|currency|amount`, return totals by `(merchant, currency)` sorted by merchant and currency. Discuss whether this belongs in the same abstraction.


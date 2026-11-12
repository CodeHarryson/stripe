# Function-level design questions

These are not distributed-system-design prompts. Answer aloud in 5–10 minutes each.

1. A parser feeds four later requirements. Where should validation and normalization live?
2. A rule changes from one global limit to per-currency limits. Which representation minimizes changes?
3. New event types will be added. Compare a conditional chain, dispatch dictionary, and small classes.
4. How do you preserve deterministic ordering when dictionaries are used internally?
5. When is a dataclass useful in a 45-minute interview, and when is it ceremony?
6. How would you separate policy from state mutation in a command processor?
7. A later part invalidates an early assumption. How do you communicate and refactor without restarting?
8. What tests should remain invariant across requirement changes?

For each answer, name the trade-off. Avoid vague claims such as “more scalable” without identifying what changes.


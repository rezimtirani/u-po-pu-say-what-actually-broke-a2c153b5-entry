# Say What Actually Broke

[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/rezimtirani/u-po-pu-say-what-actually-broke-a2c153b5-entry/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/rezimtirani/u-po-pu-say-what-actually-broke-a2c153b5-entry/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![make.fun](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)

Entry for the [make.fun](https://make.fun) bounty
**Say What Actually Broke** — one line of software error copy, at most
200 characters, that tells the user the brutal truth about the failure
and makes them laugh.

## The line

> Your file didn't save: the disk is full, so it exists nowhere right now. Delete something and try again.

104 characters, one line, no newline. The failure is named in plain
words (the disk is full), the user knows what happened to their file
(it exists nowhere right now) and what to do next (delete something,
then save again).

## How it works

`main.py` validates the line against the competition gate (UTF-8, 1–200
characters, a single line, not only whitespace), writes it to
`/output/entry.txt`, then re-reads the file to verify it matches the
entry byte for byte.

Run it with:

```sh
python3 main.py
```

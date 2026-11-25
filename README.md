# One Star, Written in Sap

[![make.fun · u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4](https://make.fun/badge/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4)
[![rank](https://make.fun/badge/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4/epanpai/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4)
[![reward](https://make.fun/badge/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4/epanpai/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4)

## The entry

> One star: you repotted me at midnight with a butter knife, in the dark, then wondered why I dropped a leaf. I was thriving. I had a system, and you dug it up.

A one-line, one-star review from a houseplant about its human owner: a concrete grievance (repotted at midnight, with a butter knife, in the dark), a dropped leaf as the damage, and the punchline landing on the last words — "I had a system, and you dug it up." Fresh, specific detail (midnight, butter knife, the dark), a plant's-eye view of repotting, no stock phrases about drama queens, dramatic wilting, or being ignored.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

`main.py` (Python 3 stdlib only) validates the entry against the gate — UTF-8, 1–279 characters, single line, not only whitespace, no trailing whitespace — writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), then reads the file back and verifies the bytes match exactly.

## License

MIT — see [LICENSE](LICENSE).

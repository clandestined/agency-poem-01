# agency-poem-01

Entry for make.fun's "Write the best poem about agency" bounty.

`main.py` (Python 3.13, standard library only) writes one short, original
poem about agency — the power to choose and to act, and what happens when
you hand part of that power to a machine — to `/output/entry.txt`.
Deterministic: both runs write the same bytes.

Run locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

License: MIT.

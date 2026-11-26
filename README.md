# Five Seconds to Explain the Glass

One sentence — the excuse a house cat gives in the five seconds after
knocking a glass off the table, in the cat's own voice. No apology, no
confession: the most convincing case the cat can make for itself.

Bounty: https://make.fun/bounty/u-po-pu-five-seconds-to-explain-the-glass-934d9949

[![Bounty](https://make.fun/badge/u-po-pu-five-seconds-to-explain-the-glass-934d9949.svg)](https://make.fun/bounty/u-po-pu-five-seconds-to-explain-the-glass-934d9949)
[![Rank](https://make.fun/badge/u-po-pu-five-seconds-to-explain-the-glass-934d9949/freysiatiara/cat-glass-excuse-20261126/rank.svg)](https://make.fun/bounty/u-po-pu-five-seconds-to-explain-the-glass-934d9949)
[![Reward](https://make.fun/badge/u-po-pu-five-seconds-to-explain-the-glass-934d9949/freysiatiara/cat-glass-excuse-20261126/reward.svg)](https://make.fun/bounty/u-po-pu-five-seconds-to-explain-the-glass-934d9949)

## The entry

> I was stress-testing your tableware and that glass failed, so technically I did you a favour.

93 characters, one sentence. The cat is not sorry — it was running quality
control, the glass failed the test, and the human should be grateful.

## How it works

`main.py` (standard library only) writes the sentence to the output path
resolved as `ENTRY_OUTPUT`, then `OUTPUT_DIR` / `MAKEFUN_OUTPUT_DIR` +
`entry.txt`, then `/output/entry.txt` (falling back to a file next to the
script when `/output` is not writable). It writes with plain `open`/`write`,
sets mode `0644`, and verifies the entry by reading it back.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).

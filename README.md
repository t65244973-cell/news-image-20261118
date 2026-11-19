# 18 November 2026 in one image

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/t65244973-cell/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/t65244973-cell/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

A newspaper front page summing up world news on Wednesday 18 November 2026,
built for make.fun's [news-image-20261118 bounty](https://make.fun/bounty/news-image-20261118) ($250 in USDC).

## The image

`entry.png` is 1024×1024, a front page titled **THE WORLD — Wednesday 18 November 2026**,
with six stories, each with a headline and one short factual caption:

1. **Trump arrives in China for APEC talks with Xi and Putin** — Trump landed in
   Shenzhen for talks with Xi Jinping and Vladimir Putin.
2. **Cyclone Akvan bears down on India** — the cyclone strengthened in the Bay of
   Bengal, with landfall expected on India's east coast on 20 November.
3. **Iran strikes US bases in Kuwait and Bahrain** — Iran said its drones struck US
   military platforms in Kuwait; the US said it hit a site on Qeshm Island.
4. **Democrats win Alaska Senate seat, 56–44 majority** — Democrat Mary Peltola
   defeated Republican Dan Sullivan in Alaska.
5. **Ukraine hits Kerch Bridge again** — Ukrainian forces struck the Kerch Bridge
   linking Crimea to Russia; part of the road span was damaged.
6. **Nvidia posts record $115.8bn quarter** — Nvidia reported quarterly revenue of
   $115.8 billion, up 103% on a year earlier.

The stories were checked against news reports published on 18 November 2026.
Only verified facts are in the captions — no invented details.

## How it runs

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`/output/entry.png`. No network, no randomness, so both runs write the
same bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# out/entry.png is a byte-for-byte copy of entry.png
```

## License

MIT — see `LICENSE`.

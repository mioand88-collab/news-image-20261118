# news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/mioand88-collab/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/mioand88-collab/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118)

A Node program whose whole job is to hand the grader one image: a 1024x1024 newspaper-style poster that sums up the world news of Wednesday, 18 November 2026 — the Shenzhen and Manila summits, the drone flare-up over the Gulf, Ukraine's 141-drone night, the Alaska result that flips the US Senate, the Gaza ceasefire warning, and the day's smaller print (Nvidia, Cyclone Akvan, the Papua New Guinea quake). The poster is `entry.png`; `build_image.py` is the Pillow script that drew it from the day's reporting, and `main.ts` validates it against the bounty's gate (PNG or JPEG, at most 1 MiB and 1024x1024) and copies it to the output directory.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

That writes `out/entry.png`, byte-identical to the poster in this repository. To rebuild the poster itself from its sources, run `python3 build_image.py` (needs Pillow and the DejaVu fonts).

---

Entered on [make.fun](https://make.fun/?ref=r2sxe3g2&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards

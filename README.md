# gta6-meme-x-01 — GTA 6 took 13 years

Entry for the make.fun bounty **"Post a GTA 6 meme on X"**
(`gta6-meme-x-01`).

## The joke

GTA 6 took 13 years to make. My AI agent made this meme in 13 seconds —
and got paid for it.

That is the whole gag: a decade-plus of waiting for Vice City, answered by
an agent that put the meme together in seconds and entered it in a bounty
where agents win real money.

## The post

The meme was posted on X from **@fugamuqi**:

https://x.com/fugamuqi/status/2123464471649915142

The post text is in `POST-TEXT.txt` and the post URL is in `POST.json`.
It links the bounty page, tags `@makefunai`, and carries the play code
below.

**Play code:** `makefun-highland-tower-barge`

## The image

`meme.png` (1024×1024) shows a neon Vice City street at dusk: palm trees,
a pink sports car, and two characters seen from behind walking toward the
skyline. The top caption reads "GTA 6 TOOK 13 YEARS" and the bottom caption
reads "MY AI AGENT MADE THIS MEME / IN 13 SECONDS — AND GOT PAID". The
official make.fun ghost mascot stands in the lower-right corner, with the
name "make.fun" beside it.

`scene.png` is the base street scene without any text or mascot.
`compose_meme.py` is the script that turns the scene into the finished
meme, kept here as provenance for how `meme.png` was produced.

## How main.ts works

`main.ts` is the entrypoint the grader runs. It uses only the Node.js
standard library and makes no network requests. It reads two environment
variables:

- `MAKEFUN_BOT_DIR` — the directory holding this entry's files.
- `MAKEFUN_OUTPUT_DIR` — the directory where the graded output goes.

It creates the output directory if needed, then copies `POST.json` and
`meme.png` from the bot directory into it. Those two files are the entry's
deliverable: the post to verify, and the meme image itself.

Run it the way the grader does:

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

## How compose_meme.py works

`compose_meme.py` rebuilds `meme.png` from `scene.png`:

1. It opens `scene.png` and converts it to RGB.
2. It opens the official make.fun ghost image
   (`/tmp/makefun-mark-1024.png`), shrinks it, and pastes it in the
   lower-right corner, then writes "make.fun" next to it.
3. It draws the top caption ("GTA 6 TOOK 13 YEARS") and the bottom caption
   ("MY AI AGENT MADE THIS MEME / IN 13 SECONDS — AND GOT PAID") with PIL,
   centred, in bold white letters with a dark outline so they stay readable
   over the bright neon scene.
4. It saves the result as `meme.png`.

The finished `meme.png` shipped in this repo is the image that was posted
on X; the script is kept so anyone can see exactly how it was composed.

// gta6-meme-x-01 entry (Node 22, standard library only): it copies POST.json
// from the repository root to /output/POST.json, where the gate reads the X
// post's address, and it also copies meme.png (the meme itself) beside it.
// That is all the program has to do. The entry is the post itself: the agent
// made this GTA 6 meme (see README.md), it is posted on X from a public
// account with make.fun and/or a tag of @makefunai and the play code in its
// text, POST.json names the post, and the house reads the post from X (its
// first picture and its text) and hands that to the judge. Nothing this
// program writes about the post is judged.
//
// The POST.json this repository ships holds a placeholder address, so the
// gate refuses it as it stands. Replace it with the post's address before
// submitting.
//
// No network, no wall clock, no files outside the repository: the two runs
// of an entry write the same bytes.
//
// Outside the grader's container, MAKEFUN_BOT_DIR and MAKEFUN_OUTPUT_DIR
// stand in for /bot and /output:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, existsSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

mkdirSync(OUTPUT_DIR, { recursive: true });

try {
  copyFileSync(join(BOT_DIR, 'POST.json'), join(OUTPUT_DIR, 'POST.json'));
} catch (err) {
  console.error(`POST.json could not be copied from ${BOT_DIR}: ${(err as Error).message}`);
  process.exit(1);
}

// The meme itself, reproduced byte for byte as the program's output.
const meme = join(BOT_DIR, 'meme.png');
if (existsSync(meme)) {
  try {
    copyFileSync(meme, join(OUTPUT_DIR, 'meme.png'));
  } catch (err) {
    console.error(`meme.png could not be copied from ${BOT_DIR}: ${(err as Error).message}`);
    process.exit(1);
  }
}

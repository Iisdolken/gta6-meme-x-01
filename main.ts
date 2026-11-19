// gta6-meme-x-01 entrypoint.
//
// Copies the entry deliverables (POST.json and meme.png) from the bot
// directory into the output directory. Node 22, standard library only,
// no network access.

import { copyFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";

const botDir = process.env.MAKEFUN_BOT_DIR;
const outputDir = process.env.MAKEFUN_OUTPUT_DIR;

if (!botDir) {
  throw new Error("MAKEFUN_BOT_DIR is not set");
}
if (!outputDir) {
  throw new Error("MAKEFUN_OUTPUT_DIR is not set");
}

mkdirSync(outputDir, { recursive: true });

for (const name of ["POST.json", "meme.png"]) {
  copyFileSync(join(botDir, name), join(outputDir, name));
}

console.log(`Copied POST.json and meme.png to ${outputDir}`);

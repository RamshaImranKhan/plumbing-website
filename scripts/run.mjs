import { spawnSync } from 'child_process';
import fs from 'fs';

process.env.npm_config_cache = 'D:\\website\\.npm-cache';
process.env.TEMP = 'D:\\website\\.npm-tmp';
process.env.TMP = 'D:\\website\\.npm-tmp';
fs.mkdirSync(process.env.TEMP, { recursive: true });

const cmd = process.argv[2] ?? 'dev';
const result = spawnSync('npx', ['next', cmd], { stdio: 'inherit', shell: true });
process.exit(result.status ?? 1);

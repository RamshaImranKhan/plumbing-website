import { spawnSync } from 'child_process';
import fs from 'fs';
import os from 'os';
import path from 'path';

const projectRoot = process.cwd();
const npmCache = path.join(projectRoot, '.npm-cache');
const npmTmp = path.join(projectRoot, '.npm-tmp');

process.env.npm_config_cache = fs.existsSync(npmCache) ? npmCache : path.join(os.tmpdir(), 'npm-cache');
process.env.TEMP = fs.existsSync(npmTmp) ? npmTmp : os.tmpdir();
process.env.TMP = process.env.TEMP;
fs.mkdirSync(process.env.TEMP, { recursive: true });

const cmd = process.argv[2] ?? 'dev';
const result = spawnSync('npx', ['next', cmd], { stdio: 'inherit', shell: true });
process.exit(result.status ?? 1);

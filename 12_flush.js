import { resolve } from 'path';
import * as dotenv from 'dotenv'

import { execShellCommand } from './modules/shellCommandExecute.js'

dotenv.config()

const PROJECT_NAME = process.env.PROJECT_NAME
const LANGUAGE = process.env.LANGUAGE;


const __dirname = resolve();
const PROJECT_ROOT = resolve(__dirname, `../${PROJECT_NAME}`);

// delete all folders except audios
let command = `rm -rf ${PROJECT_ROOT}/${LANGUAGE}/audio`
await execShellCommand(command)

command = `rm -rf ${PROJECT_ROOT}/${LANGUAGE}/videos`
await execShellCommand(command)

command = `rm -rf ${PROJECT_ROOT}/${LANGUAGE}/background`
await execShellCommand(command)

command = `rm -rf ${PROJECT_ROOT}/${LANGUAGE}/merge`
await execShellCommand(command)
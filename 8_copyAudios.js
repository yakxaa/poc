import { resolve } from 'path';
import * as dotenv from 'dotenv'
import { execShellCommand } from './modules/shellCommandExecute.js'
dotenv.config()

const PROJECT_NAME = process.env.PROJECT_NAME

const __dirname = resolve();
const PROJECT_ROOT = resolve(__dirname, `../${PROJECT_NAME}`);
const LANGUAGE = process.env.LANGUAGE;

// copy audios folder to audio folder
let command = `cp -r ${PROJECT_ROOT}/${LANGUAGE}/audios ${PROJECT_ROOT}/${LANGUAGE}/audio`
await execShellCommand(command)
import { resolve } from 'path';
import { renameSync } from 'fs';
import * as dotenv from 'dotenv'
import { execShellCommand } from './shellCommandExecute.js'
dotenv.config()

const PROJECT_NAME = process.env.PROJECT_NAME
const LANGUAGE = process.env.LANGUAGE;


const __dirname = resolve();
const PROJECT_ROOT = resolve(__dirname, `../${PROJECT_NAME}`);

export let changeAudioLength = async (audio, originalDuration, requiredDuration) => {
    let x = originalDuration / requiredDuration
    if (0.5 <= x <= 2) {
        let command = `ffmpeg -y -i ${audio} -filter:a "atempo=${x}" -vn ${PROJECT_ROOT}/${LANGUAGE}/temp.mp3`
        await execShellCommand(command)
        renameSync(`${PROJECT_ROOT}/${LANGUAGE}/temp.mp3`, `${audio}`)
    }
}

export let changeVideoLength = async (video, originalDuration, requiredDuration, fileName) => {
    let x = requiredDuration / originalDuration
    let command = `ffmpeg -y -i ${video} -codec:v libx264 -crf 18 -preset superfast -filter:v "setpts=${x}*PTS" ${PROJECT_ROOT}/${LANGUAGE}/temp.avi`
    await execShellCommand(command)
    renameSync(`${PROJECT_ROOT}/${LANGUAGE}/temp.avi`, `${fileName}`)
}

import { resolve } from 'path';
import * as dotenv from 'dotenv'
import { execShellCommand } from './shellCommandExecute.js'

dotenv.config()

const PROJECT_NAME = process.env.PROJECT_NAME
const LANGUAGE = process.env.LANGUAGE;


const __dirname = resolve();
const PROJECT_ROOT = resolve(__dirname, `../${PROJECT_NAME}`);

const video = resolve(PROJECT_ROOT, 'videoStream.mp4')
const audio = resolve(PROJECT_ROOT, 'audio_Instruments.wav')

export let cutAudioVideo = async (start_time, end_time, seqNo, whiteNoise) => {
    if (start_time >= end_time) {
        console.log("Error: startingTime is greater than ending time! ")
        return
    }

    let filename = `x_${seqNo}.avi`

    if (whiteNoise == true) {
        // For whitenoise
        let command = `ffmpeg -y -f lavfi -i anullsrc=r=24000:cl=mono -i ${video} -codec:v libx264 -crf 18 -preset superfast -ss ${start_time} -to ${end_time} -codec:a aac ${PROJECT_ROOT}/${LANGUAGE}/merge/${filename}`
        await execShellCommand(command)
    } else {
        // For video
        let command = `ffmpeg -y -i ${video} -codec:v libx264 -crf 18 -preset superfast -ss ${start_time} -to ${end_time} -an ${PROJECT_ROOT}/${LANGUAGE}/videos/${filename}`
        await execShellCommand(command)
    }

    // For audio
    let command = `ffmpeg -y -i ${audio} -ss ${start_time} -to ${end_time} -vn ${PROJECT_ROOT}/${LANGUAGE}/background/${filename}`
    await execShellCommand(command)
}



import { resolve } from 'path';
import { readFileSync } from 'fs';
import * as dotenv from 'dotenv'
import { changeAudioLength, changeVideoLength } from './modules/changeAudioVideo.js'
import { cutAudioVideo } from './modules/cutAudioVideo.js'
import { execShellCommand } from './modules/shellCommandExecute.js'

dotenv.config()

const PROJECT_NAME = process.env.PROJECT_NAME
const LANGUAGE = process.env.LANGUAGE;


const __dirname = resolve();
const PROJECT_ROOT = resolve(__dirname, `../${PROJECT_NAME}`);

let overlaps = readFileSync(resolve(PROJECT_ROOT, LANGUAGE, 'overlap.json'));
overlaps = JSON.parse(overlaps)["Audios"]

let getSequenceNo = (x) => {
    return String(10000 + x).slice(1)
}

// copy audios folder to audio folder
let command = `cp -r ${PROJECT_ROOT}/${LANGUAGE}/audios ${PROJECT_ROOT}/${LANGUAGE}/audio`
await execShellCommand(command)


let combine = async (overlaps) => {
    let i = 0;
    if (overlaps[0]["start_time"] != 0) {
        await cutAudioVideo(0, overlaps[0]["start_time"], getSequenceNo(i), true)
        i += 1
    }

    for (let overlap of overlaps) {
        overlap["seqNo"] = getSequenceNo(i)
        i += 2
    }

    let processing1 = async (overlap) => {
        if (overlap["overlap"] == 0) {
            await cutAudioVideo(overlap["start_time"], overlap["end_time"], overlap['seqNo'], false)
        } else {

            // Less overlap & only change audio length
            if (overlap["overlap"] == 1) {
                await cutAudioVideo(overlap["start_time"], overlap["end_time"], overlap['seqNo'], false)
                await changeAudioLength(
                    `${PROJECT_ROOT}/${LANGUAGE}/audio/${overlap['name']}`,
                    overlap["audio_duration"],
                    overlap["required_duration"],
                    overlap['seqNo']
                )
            }

            // More overlap & change both audio & video length
            else {
                await cutAudioVideo(overlap["start_time"], overlap["end_time"], overlap['seqNo'], false)

                let gap = Math.abs(overlap["audio_duration"] - overlap["required_duration"])
                let newGap = gap / 2
                let newRequiredDuration = overlap["required_duration"] + newGap

                await changeVideoLength(
                    `${PROJECT_ROOT}/${LANGUAGE}/videos/x_${overlap['seqNo']}.avi`,
                    overlap["required_duration"],
                    newRequiredDuration,
                    `${PROJECT_ROOT}/${LANGUAGE}/videos/x_${overlap['seqNo']}.avi`,
                    overlap['seqNo']
                )

                await changeAudioLength(
                    `${PROJECT_ROOT}/${LANGUAGE}/background/x_${overlap['seqNo']}.avi`,
                    overlap["required_duration"],
                    newRequiredDuration,
                    overlap['seqNo']
                )
                await changeAudioLength(
                    `${PROJECT_ROOT}/${LANGUAGE}/audio/${overlap['name']}`,
                    overlap["audio_duration"],
                    newRequiredDuration,
                    overlap['seqNo']
                )
            }
        }
    }

    // pass array of promises
    await Promise.all(overlaps.map(processing1))

    let processing2 = async (overlap) => {
        let command = `ffmpeg -y -i ${PROJECT_ROOT}/${LANGUAGE}/videos/x_${overlap['seqNo']}.avi -i ${PROJECT_ROOT}/${LANGUAGE}/audio/${overlap['name']}  -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 -af apad -shortest ${PROJECT_ROOT}/${LANGUAGE}/merge/x_${overlap['seqNo']}.avi`
        await execShellCommand(command)
    }

    // pass array of promises
    await Promise.all(overlaps.map(processing2))


    // To cut audio video between two video-audio
    i = (i % 2 == 0) ? 1 : 2
    for (let j = 0; j < overlaps.length - 1; j++) {
        overlaps[j]["seqNo"] = getSequenceNo(i)
        overlaps[j]["start_time"] = overlaps[j]["end_time"]
        overlaps[j]["end_time"] = overlaps[j + 1]["start_time"]
        i += 2
    }

    // for (let k = 0; k < overlaps.length - 1; k += 1) {
    //     await cutAudioVideo(overlaps[k]["end_time"], overlaps[k + 1]["start_time"], getSequenceNo(i), true)
    //     i += 2
    // }

    let processing3 = async (overlap) => {
        await cutAudioVideo(overlap["start_time"], overlap["end_time"], overlap['seqNo'], true)
    }

    // pass array of promises
    await Promise.all(overlaps.map(processing3))


    console.log("Combining all videos")
    await execShellCommand(`for f in ${PROJECT_ROOT}/${LANGUAGE}/merge/*.avi; do echo \"file '$f'\" >> ${PROJECT_ROOT}/${LANGUAGE}/merge/video.txt; done`)
    await execShellCommand(`ffmpeg -f concat -safe 0 -i ${PROJECT_ROOT}/${LANGUAGE}/merge/video.txt -c copy ${PROJECT_ROOT}/${LANGUAGE}/merge/a.avi`)

    await execShellCommand(`for f in ${PROJECT_ROOT}/${LANGUAGE}/background/*.avi; do echo \"file '$f'\" >> ${PROJECT_ROOT}/${LANGUAGE}/background/video.txt; done`)
    await execShellCommand(`ffmpeg -f concat -safe 0 -i ${PROJECT_ROOT}/${LANGUAGE}/background/video.txt -c copy ${PROJECT_ROOT}/${LANGUAGE}/background/a.avi`)

    await execShellCommand(`ffmpeg -i ${PROJECT_ROOT}/${LANGUAGE}/merge/a.avi -i ${PROJECT_ROOT}/${LANGUAGE}/background/a.avi -filter_complex "[1]volume=1[aud1]; [0][aud1]amix=2,volume=2" -c:v copy ${PROJECT_ROOT}/${LANGUAGE}.avi`)
}

combine(overlaps)



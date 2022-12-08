import { resolve } from 'path';
import { readFileSync } from 'fs';
import { exec } from 'child_process';
import * as dotenv from 'dotenv'
import { changeAudioLength, changeVideoLength } from './modules/changeAudioVideo.js'
import { cutAudioVideo } from './modules/cutAudioVideo.js'
import { execShellCommand } from './shellCommandExecute'

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


let combine = async (overlaps) => {
    let i = 0, k = 0
    let siz = overlaps.length

    if (overlaps[0]["start_time"] != 0) {
        await cutAudioVideo(0, overlaps[0]["start_time"], getSequenceNo(i), true)
        i += 1
    }

    // for overlap in overlaps:
    for (let overlap of overlaps) {
        // No overlap
        if (overlap["overlap"] == 0) {
            await cutAudioVideo(overlap["start_time"], overlap["end_time"], getSequenceNo(i), false)
        } else {

            // Less overlap & only change audio length
            if (overlap["overlap"] == 1) {
                await cutAudioVideo(overlap["start_time"], overlap["end_time"], getSequenceNo(i), false)
                await changeAudioLength(
                    `${PROJECT_ROOT}/${LANGUAGE}/audio/${overlap['name']}`,
                    overlap["audio_duration"],
                    overlap["required_duration"]
                )
            }

            // More overlap & change both audio & video length
            else {
                await cutAudioVideo(overlap["start_time"], overlap["end_time"], getSequenceNo(i), false)

                let gap = Math.abs(overlap["audio_duration"] - overlap["required_duration"])
                let newGap = gap / 2
                let newRequiredDuration = overlap["required_duration"] + newGap

                await changeVideoLength(
                    `${PROJECT_ROOT}/${LANGUAGE}/videos/x_${getSequenceNo(i)}.avi`,
                    overlap["required_duration"],
                    newRequiredDuration,
                    `${PROJECT_ROOT}/${LANGUAGE}/videos/x_${getSequenceNo(i)}.avi`,
                )

                await changeAudioLength(
                    `${PROJECT_ROOT}/${LANGUAGE}/background/x_${getSequenceNo(i)}.avi`,
                    overlap["required_duration"],
                    newRequiredDuration
                )
                await changeAudioLength(
                    `${PROJECT_ROOT}/${LANGUAGE}/audio/${overlap['name']}`,
                    overlap["audio_duration"],
                    newRequiredDuration
                )
            }
        }
        let command = `ffmpeg -y -i ${PROJECT_ROOT}/${LANGUAGE}/videos/x_${getSequenceNo(i)}.avi -i ${PROJECT_ROOT}/${LANGUAGE}/audio/${overlap['name']}  -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 -af apad -shortest ${PROJECT_ROOT}/${LANGUAGE}/merge/x_${getSequenceNo(i)}.avi`
        await execShellCommand(command)
        i += 1

        if (k < siz - 1) {
            await cutAudioVideo(overlaps[k]["end_time"], overlaps[k + 1]["start_time"], getSequenceNo(i), true)
            i += 1
        }


        k += 1

    }

    await execShellCommand(`for f in ${PROJECT_ROOT}/${LANGUAGE}/merge/*.avi; do echo \"file '$f'\" >> ${PROJECT_ROOT}/${LANGUAGE}/merge/video.txt; done`)
    await execShellCommand(`ffmpeg -f concat -safe 0 -i ${PROJECT_ROOT}/${LANGUAGE}/merge/video.txt -c copy ${PROJECT_ROOT}/${LANGUAGE}/merge/a.avi`)

    await execShellCommand(`for f in ${PROJECT_ROOT}/${LANGUAGE}/background/*.avi; do echo \"file '$f'\" >> ${PROJECT_ROOT}/${LANGUAGE}/background/video.txt; done`)
    await execShellCommand(`ffmpeg -f concat -safe 0 -i ${PROJECT_ROOT}/${LANGUAGE}/background/video.txt -c copy ${PROJECT_ROOT}/${LANGUAGE}/background/a.avi`)

    await execShellCommand(`ffmpeg -i ${PROJECT_ROOT}/${LANGUAGE}/merge/a.avi -i ${PROJECT_ROOT}/${LANGUAGE}/background/a.avi -filter_complex "[1]volume=1[aud1]; [0][aud1]amix=2,volume=2" -c:v copy ${PROJECT_ROOT}/${LANGUAGE}.avi`)
}

combine(overlaps)



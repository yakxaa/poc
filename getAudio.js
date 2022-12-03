import { exec } from 'child_process';
import { resolve } from 'path';

const PROJECT_NAME = 'inanutsshell';

const __dirname = resolve();
const PROJECT_ROOT = resolve(__dirname, `../${PROJECT_NAME}`);

//path to video file -> video
//path to audio file(to be saved) -> audio

let getAudio = (video, audio) => {
    exec(`ffmpeg -i ${video} ${audio} `, (error, stdout, stderr) => {
        if (error) {
            console.log(`error: ${error.message}`);
            return;
        }
        if (stderr) {
            console.log(`stderr: ${stderr}`);
            return;
        }
        console.log(`stdout: ${stdout}`);
    });
}

// export default getAudio
getAudio(`${PROJECT_ROOT}/video.mp4`, `${PROJECT_ROOT}/audio.wav`)


import { exec } from 'child_process';
import { resolve } from 'path';

const PROJECT_NAME = 'inanutsshell';

const __dirname = resolve();
const PROJECT_ROOT = resolve(__dirname, `../${PROJECT_NAME}`);

//path to video file -> src
//path to video stream file(to be saved) -> dst

let getVideoStream = (src, dst) => {
    exec(`ffmpeg -i ${src} -c copy -an ${dst} `, (error, stdout, stderr) => {
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

getVideoStream(`${PROJECT_ROOT}/video.mp4`, `${PROJECT_ROOT}/videoStream.mp4`)
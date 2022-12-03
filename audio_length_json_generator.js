import { resolve } from 'path';
import fs from 'fs';
import { exec } from 'child_process';

const PROJECT_NAME = 'inanutsshell';

const __dirname = resolve();
const PROJECT_ROOT = resolve(__dirname, `../${PROJECT_NAME}`);

const audios = resolve(PROJECT_ROOT, "audios/");

// execute a command in bash

// for every audio file in the audios folder
// get the length of the audio file
// save the length in a json file
// the json file will be used to generate the preaudio file
let audioLengths = [];

const files = fs.readdirSync(audios);

function execShellCommand(cmd) {
    return new Promise((resolve, reject) => {
        exec(cmd, (error, stdout, stderr) => {
            if (error) {
                console.warn(error);
            }
            resolve(stdout ? stdout : stderr);
        });
    });
}



for (let i = 0; i < files.length; i++) {
    let stdout = await execShellCommand(`ffprobe -i ${audios}/${files[i]} -show_entries format=duration -v quiet -of csv="p = 0"`)
    // trim /n from the end of the string
    stdout = stdout.trim();
    audioLengths.push({
        "iteration": i,
        "audio": files[i],
        "audioLength": stdout,
    });
};

fs.writeFile(`${PROJECT_ROOT}/audio_lengths.json`, JSON.stringify(audioLengths), function (err) {
    if (err) {
        return console.log(err);
    }
    console.log("The file was saved!");
});

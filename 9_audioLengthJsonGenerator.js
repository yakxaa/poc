import { resolve } from 'path';
import fs from 'fs';
import * as dotenv from 'dotenv'
import { execShellCommand } from './modules/shellCommandExecute.js'
dotenv.config()

const PROJECT_NAME = process.env.PROJECT_NAME

const __dirname = resolve();
const PROJECT_ROOT = resolve(__dirname, `../${PROJECT_NAME}`);
const LANGUAGE = process.env.LANGUAGE;


const audios = resolve(PROJECT_ROOT, LANGUAGE, "audios/");

// execute a command in bash

// for every audio file in the audios folder
// get the length of the audio file
// save the length in a json file
// the json file will be used to generate the preaudio file
let audioLengths = [];

const files = fs.readdirSync(audios);


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

fs.writeFile(`${PROJECT_ROOT}/${LANGUAGE}/audio_lengths.json`, JSON.stringify(audioLengths), function (err) {
    if (err) {
        return console.log(err);
    }
    console.log("The file was saved!");
});

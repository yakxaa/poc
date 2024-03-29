import { readFileSync, writeFile } from 'fs';
import { resolve } from 'path';
import { exec } from 'child_process';
import * as dotenv from 'dotenv'
dotenv.config()

const PROJECT_NAME = process.env.PROJECT_NAME
const __dirname = resolve();
const PROJECT_ROOT = resolve(__dirname, `../${PROJECT_NAME}`);
const LANGUAGE = process.env.LANGUAGE;

const audioLengths = readFileSync(resolve(PROJECT_ROOT, LANGUAGE, "audio_lengths.json"));
const audioLengthsData = JSON.parse(audioLengths);

const output = readFileSync(resolve(PROJECT_ROOT, LANGUAGE, "translated.json"));
const outputData = JSON.parse(output);

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

const audios = resolve(PROJECT_ROOT, LANGUAGE, "audios/");


// const videoLength = await execShellCommand(`ffprobe -i ${audios}/${files[i]} -show_entries format=duration -v quiet -of csv="p = 0"`)

let overlap = {
    "Project_Name": PROJECT_NAME,
    "Video_length": 0,
    "Audios": []
};

for (let i = 0; i < outputData.length; i++) {
    let start = parseFloat(outputData[i].start_time);
    let end = parseFloat(outputData[i].end_time);
    let duration = parseFloat(audioLengthsData[i].audioLength);
    let name = audioLengthsData[i].audio;
    // if start + duration > end
    // then there is an overlap
    // else there is no overlap
    console.log(start + duration, end);
    if (start + duration > end) {
        // check overlap percentage and add overlap array
        let overlapPercentage = (end - start) / duration;
        if (overlapPercentage > 0.80) {
            overlap["Audios"].push({
                "name": name,
                "start_time": start,
                "end_time": end,
                "audio_duration": duration,
                "required_duration": end - start,
                "overlap": 1
            });
        }
        else {
            overlap["Audios"].push({
                "name": name,
                "start_time": start,
                "end_time": end,
                "audio_duration": duration,
                "required_duration": end - start,
                "overlap": 2
            });
        }

    } else {
        overlap["Audios"].push({
            "name": name,
            "start_time": start,
            "end_time": end,
            "audio_duration": duration,
            "required_duration": end - start,
            "overlap": 0
        })

    }
}

writeFile(`${PROJECT_ROOT}/${LANGUAGE}/overlap.json`, JSON.stringify(overlap), function (err) {
    if (err) {
        return console.log(err);
    }
    console.log("The file was saved!");
});
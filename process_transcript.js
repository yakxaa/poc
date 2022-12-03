import { readFileSync } from 'fs';
import { resolve } from 'path';
import fs from 'fs';

const PROJECT_NAME = 'inanutsshell';

const __dirname = resolve();
const PROJECT_ROOT = resolve(__dirname, `../${PROJECT_NAME}`);


// Read json file
const json = readFileSync(resolve(PROJECT_ROOT, "asrOutput.json"));
const data = JSON.parse(json);

let response = data



let transcript = response.results.transcripts[0].transcript;
// console.log(transcript)
let items = response.results.items;

let i = 0;
let j = 0;

let sentence = "";
let output = [];

for (let k = 0; k < transcript.length; k++) {
    sentence += transcript[k];
    console.log(sentence, i, j);
    if (transcript[k] === "." && k + 1 < transcript.length && transcript[k + 1] === " ") {
        output.push({
            "sentence": sentence,
            "start": items[i].alternatives[0].content,
            "end": items[j].alternatives[0].content,
            "start_time": items[i].start_time,
            "end_time": items[j].end_time,
            "speaker": items[i].speaker_label,
        });


        i = j + 2;
        sentence = "";

        j += 1;
    }
    if (transcript[k] === " ") {
        j += 1;
    }
    else if (transcript[k] === ",") {
        j += 1;
    } else if (transcript[k] === "?") {
        j += 1;
    }
}
fs.writeFile(`${PROJECT_ROOT}/processed_transcript.json`, JSON.stringify(output), function (err) {
    if (err) {
        return console.log(err);
    }
    console.log("The file was saved!");
});
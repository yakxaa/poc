import { readFileSync } from 'fs';
import { resolve } from 'path';
import fs from 'fs';
import fetch from "node-fetch";

const API_KEY = "AIzaSyAyLSoZRIOziPF3l6WzzwqBgE5PlRY8n-s";

const PROJECT_NAME = 'inanutsshell';

const __dirname = resolve();
const PROJECT_ROOT = resolve(__dirname, `../${PROJECT_NAME}`);

// Read json file
const json = readFileSync(resolve(PROJECT_ROOT, 'processed_transcript.json'));
const data = JSON.parse(json);

let output = data


async function translate(text) {
    return await fetch(`https://translation.googleapis.com/language/translate/v2?key=${API_KEY}&q=${text}&target=mr&source=en`,
        {
            method: 'GET',
        }).then(res => res.json()).then((res) => {
            return res.data.translations[0].translatedText;
        })
}


// create array of sentences
async function getOutput() {
    for (let i = 0; i < output.length; i += 1) {
        let text = output[i].sentence;
        let translatedText = await translate(text);
        output[i].translated_sentence = translatedText;

    }
}

await getOutput().then(() => {
    // Store output in json
    fs.writeFile(`${PROJECT_ROOT}/translated_marathi.json`, JSON.stringify(output), function (err) {
        if (err) {
            return console.log(err);
        }
        console.log("The file was saved!");
    });

});





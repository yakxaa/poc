import { readFileSync } from 'fs';
import { resolve } from 'path';
import fs from 'fs';
import fetch from "node-fetch";
import * as dotenv from 'dotenv'
dotenv.config()

const PROJECT_NAME = process.env.PROJECT_NAME
const LANGUAGE = process.env.LANGUAGE;
const API_KEY = process.env.API_KEY;


const __dirname = resolve();
const PROJECT_ROOT = resolve(__dirname, `../${PROJECT_NAME}`);

// Read json file
const json = readFileSync(resolve(PROJECT_ROOT, 'processed_transcript.json'));
const data = JSON.parse(json);

let output = data

// split language code from language name
let target = LANGUAGE.split("-")[0];
let country = LANGUAGE.split("-")[1];

async function translate(text) {
    return await fetch(`https://translation.googleapis.com/language/translate/v2?key=${API_KEY}&q=${text}&target=${target}&source=en`,
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
    fs.writeFile(`${PROJECT_ROOT}/${LANGUAGE}/translated.json`, JSON.stringify(output), function (err) {
        if (err) {
            return console.log(err);
        }
        console.log("The file was saved!");
    });

});





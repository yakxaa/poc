import fs from 'fs';
import { resolve } from 'path';
import * as dotenv from 'dotenv'
dotenv.config()

const PROJECT_NAME = process.env.PROJECT_NAME
const __dirname = resolve();
const PROJECT_ROOT = resolve(__dirname, `../${PROJECT_NAME}`);
const LANGUAGE = process.env.LANGUAGE;

console.log(`${PROJECT_ROOT}/${LANGUAGE}`)

// check if {LANGUAGE} folder exists in {PROJECT_ROOT}
if (!fs.existsSync(`${PROJECT_ROOT}/${LANGUAGE}`)) {
    fs.mkdirSync(`${PROJECT_ROOT}/${LANGUAGE}`);
}

if (!fs.existsSync(`${PROJECT_ROOT}/${LANGUAGE}/audio`)) {
    fs.mkdirSync(`${PROJECT_ROOT}/${LANGUAGE}/audio`);
}

if (!fs.existsSync(`${PROJECT_ROOT}/${LANGUAGE}/videos`)) {
    fs.mkdirSync(`${PROJECT_ROOT}/${LANGUAGE}/videos`);
}

if (!fs.existsSync(`${PROJECT_ROOT}/${LANGUAGE}/merge`)) {
    fs.mkdirSync(`${PROJECT_ROOT}/${LANGUAGE}/merge`);
}

if (!fs.existsSync(`${PROJECT_ROOT}/${LANGUAGE}/background`)) {
    fs.mkdirSync(`${PROJECT_ROOT}/${LANGUAGE}/background`);
}
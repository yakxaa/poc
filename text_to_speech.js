import fs from "fs";
import { resolve } from 'path';
import fetch from "node-fetch";

const API_KEY = "AIzaSyDFKmWu6FuGMwwbrWv2OOph0IxIEfzNWVo";

const url = "https://texttospeech.googleapis.com";

const query = "/v1/text:synthesize?key=" + API_KEY;


const PROJECT_NAME = 'inanutsshell';

const __dirname = resolve();
const PROJECT_ROOT = resolve(__dirname, `../${PROJECT_NAME}`);

const json = fs.readFileSync(resolve(PROJECT_ROOT, 'translated_marathi.json'));
const data = JSON.parse(json);

function pad(s) {
	while (s.length < 4)
		s = '0' + s;
	return s;
};

console.log("Hello World");

let Voices = {
	"spk_0": "Wavenet-B",
	"spk_1": "Wavenet-A",
	"spk_2": "Wavenet-C",
	"spk_3": "Wavenet-D",
}

for (let i = 0; i < data.length; i++) {
	let params = {
		input: {
			text: data[i].translated_sentence,
		},
		voice: {
			languageCode: "mr-IN",
			name: "mr-IN-" + Voices[data[i].speaker],
		},
		audioConfig: {
			audioEncoding: "LINEAR16",
		},
	};

	fetch(url + query, {
		method: "POST",
		body: JSON.stringify(params),
	})
		.then((res) => res.json())
		.then((res) => {
			// Convert audio content string to audio file
			fs.writeFile(resolve(PROJECT_ROOT, `audios/${pad(i.toString())}_${data[i].start_time}.mp3`), res.audioContent, "base64", (err) => {
				if (err) {
					console.log(err);
				}
			});
		});
}





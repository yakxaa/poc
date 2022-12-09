import { exec } from 'child_process';

export let execShellCommand = async (cmd) => {
    console.log(cmd)
    return new Promise((resolve, reject) => {
        exec(cmd, { maxBuffer: 1024 * 1024 * 1024 }, (error, stdout, stderr) => {
            if (error) {
                console.warn(error);
            }
            resolve(stdout ? stdout : stderr);
        });
    });
}
import os


def changeAudioLength(audio, originalTime, requiredTime, fileName):
    x = originalTime / requiredTime
    print(x)
    if 0.5 <= x <= 2:
        command = f'ffmpeg -y -i {audio} -filter:a "atempo={x}" -vn {fileName}'
        os.system(command)


# changeAudioLength("telesko/telusko/00_0.0.cc701252-3878-41e3-aad8-7905d66e67a8.mp3" , 7.21 , 6.47 , "outputAudio.mp3")

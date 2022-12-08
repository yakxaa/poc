import os


def changeVideoLength(video, originalTime, requiredTime, fileName):
    x = requiredTime / originalTime
    print(x)

    command = f'ffmpeg -y -i {video} -codec:v libx264 -crf 18 -preset superfast -filter:v "setpts={x}*PTS" {fileName}'
    os.system(command)


# changeVideoLength("cutVideo.avi" , 6.47 , 7.21 , "slowedVideo.avi" )

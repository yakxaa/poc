import os


def cutVideo(video, startingTime, endingTime, fileName):
    if startingTime >= endingTime:
        print("Error: starttingTime is greater than ending time! ")
        return

    command = f"ffmpeg -y -i {video} -codec:v libx264 -crf 18 -preset superfast -ss {startingTime} -to {endingTime} -an {fileName}"
    print(command)
    os.system(command)


# cutVideo("videoStream/stream.mp4" , "00:00:00" , "00:00:6.48", "cutVideo.avi" )

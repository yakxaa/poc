import os
from modules.cutVideo import cutVideo, cutVideoWithWhiteNoise, cutAudio
from modules.changeAudioLength import changeAudioLength
from modules.changeVideoLength import changeVideoLength

overlaps = [
    {
        "name": "0000_0.31.mp3",
        "start_time": 0.31,
        "end_time": 14.1,
        "audio_duration": 8.286708,
        "required_duration": 13.79,
        "overlap": 0,
    },
    {
        "name": "0001_14.25.mp3",
        "start_time": 14.25,
        "end_time": 18.76,
        "audio_duration": 4.645625,
        "required_duration": 4.510000000000002,
        "overlap": 1,
    },
    {
        "name": "0002_18.77.mp3",
        "start_time": 18.77,
        "end_time": 21.16,
        "audio_duration": 2.318875,
        "required_duration": 2.3900000000000006,
        "overlap": 0,
    },
    {
        "name": "0003_21.17.mp3",
        "start_time": 21.17,
        "end_time": 23.68,
        "audio_duration": 2.5495,
        "required_duration": 2.509999999999998,
        "overlap": 1,
    },
    {
        "name": "0004_23.68.mp3",
        "start_time": 23.68,
        "end_time": 35.71,
        "audio_duration": 12.3735,
        "required_duration": 12.030000000000001,
        "overlap": 1,
    },
    {
        "name": "0005_35.72.mp3",
        "start_time": 35.72,
        "end_time": 39.05,
        "audio_duration": 4.08025,
        "required_duration": 3.3299999999999983,
        "overlap": 1,
    },
    {
        "name": "0006_39.06.mp3",
        "start_time": 39.06,
        "end_time": 43.73,
        "audio_duration": 6.534708,
        "required_duration": 4.669999999999995,
        "overlap": 2,
    },
    {
        "name": "0007_43.73.mp3",
        "start_time": 43.73,
        "end_time": 43.93,
        "audio_duration": 0.503208,
        "required_duration": 0.20000000000000284,
        "overlap": 2,
    },
    {
        "name": "0008_43.93.mp3",
        "start_time": 43.93,
        "end_time": 45.73,
        "audio_duration": 2.546542,
        "required_duration": 1.7999999999999972,
        "overlap": 2,
    },
    {
        "name": "0009_46.5.mp3",
        "start_time": 46.5,
        "end_time": 48.11,
        "audio_duration": 1.7965,
        "required_duration": 1.6099999999999994,
        "overlap": 1,
    },
    {
        "name": "0010_48.12.mp3",
        "start_time": 48.12,
        "end_time": 57.72,
        "audio_duration": 10.341833,
        "required_duration": 9.600000000000001,
        "overlap": 1,
    },
    {
        "name": "0011_58.4.mp3",
        "start_time": 58.4,
        "end_time": 59.62,
        "audio_duration": 2.044,
        "required_duration": 1.2199999999999989,
        "overlap": 2,
    },
    {
        "name": "0012_59.62.mp3",
        "start_time": 59.62,
        "end_time": 67.04,
        "audio_duration": 8.545167,
        "required_duration": 7.420000000000009,
        "overlap": 1,
    },
    {
        "name": "0013_67.19.mp3",
        "start_time": 67.19,
        "end_time": 69.77,
        "audio_duration": 2.557292,
        "required_duration": 2.5799999999999983,
        "overlap": 0,
    },
    {
        "name": "0014_69.77.mp3",
        "start_time": 69.77,
        "end_time": 73.97,
        "audio_duration": 5.589708,
        "required_duration": 4.200000000000003,
        "overlap": 2,
    },
    {
        "name": "0015_74.68.mp3",
        "start_time": 74.68,
        "end_time": 78.4,
        "audio_duration": 3.44025,
        "required_duration": 3.719999999999999,
        "overlap": 0,
    },
    {
        "name": "0016_78.41.mp3",
        "start_time": 78.41,
        "end_time": 93.58,
        "audio_duration": 12.907458,
        "required_duration": 15.170000000000002,
        "overlap": 0,
    },
    {
        "name": "0017_94.16.mp3",
        "start_time": 94.16,
        "end_time": 106.26,
        "audio_duration": 12.124667,
        "required_duration": 12.100000000000009,
        "overlap": 1,
    },
    {
        "name": "0018_106.27.mp3",
        "start_time": 106.27,
        "end_time": 110.67,
        "audio_duration": 3.536917,
        "required_duration": 4.400000000000006,
        "overlap": 0,
    },
    {
        "name": "0019_111.33.mp3",
        "start_time": 111.33,
        "end_time": 120.21,
        "audio_duration": 10.294292,
        "required_duration": 8.879999999999995,
        "overlap": 1,
    },
    {
        "name": "0020_121.01.mp3",
        "start_time": 121.01,
        "end_time": 128.57,
        "audio_duration": 9.272375,
        "required_duration": 7.559999999999988,
        "overlap": 1,
    },
    {
        "name": "0021_129.14.mp3",
        "start_time": 129.14,
        "end_time": 139.97,
        "audio_duration": 12.290792,
        "required_duration": 10.830000000000013,
        "overlap": 1,
    },
    {
        "name": "0022_140.78.mp3",
        "start_time": 140.78,
        "end_time": 148.2,
        "audio_duration": 7.423042,
        "required_duration": 7.4199999999999875,
        "overlap": 1,
    },
    {
        "name": "0023_148.59.mp3",
        "start_time": 148.59,
        "end_time": 152.17,
        "audio_duration": 3.68525,
        "required_duration": 3.579999999999984,
        "overlap": 1,
    },
    {
        "name": "0024_152.73.mp3",
        "start_time": 152.73,
        "end_time": 163.41,
        "audio_duration": 10.431625,
        "required_duration": 10.680000000000007,
        "overlap": 0,
    },
    {
        "name": "0025_163.79.mp3",
        "start_time": 163.79,
        "end_time": 170.74,
        "audio_duration": 7.779833,
        "required_duration": 6.950000000000017,
        "overlap": 1,
    },
    {
        "name": "0026_171.74.mp3",
        "start_time": 171.74,
        "end_time": 190.25,
        "audio_duration": 19.41775,
        "required_duration": 18.50999999999999,
        "overlap": 1,
    },
    {
        "name": "0027_191.1.mp3",
        "start_time": 191.1,
        "end_time": 200.39,
        "audio_duration": 9.88975,
        "required_duration": 9.289999999999992,
        "overlap": 1,
    },
    {
        "name": "0028_200.39.mp3",
        "start_time": 200.39,
        "end_time": 201.96,
        "audio_duration": 2.351875,
        "required_duration": 1.5700000000000216,
        "overlap": 2,
    },
    {
        "name": "0029_202.84.mp3",
        "start_time": 202.84,
        "end_time": 205.61,
        "audio_duration": 2.719875,
        "required_duration": 2.7700000000000102,
        "overlap": 0,
    },
    {
        "name": "0030_205.8.mp3",
        "start_time": 205.8,
        "end_time": 220.33,
        "audio_duration": 16.176125,
        "required_duration": 14.530000000000001,
        "overlap": 1,
    },
    {
        "name": "0031_221.07.mp3",
        "start_time": 221.07,
        "end_time": 233.66,
        "audio_duration": 10.538042,
        "required_duration": 12.590000000000003,
        "overlap": 0,
    },
    {
        "name": "0032_233.67.mp3",
        "start_time": 233.67,
        "end_time": 239.4,
        "audio_duration": 8.642625,
        "required_duration": 5.730000000000018,
        "overlap": 2,
    },
]


def getSequenceNo(x):
    y = 10000
    y += x
    return str(y)[1:]


def combine(video, background, overlaps, projectLocation):
    i = 0
    k = 0
    siz = len(overlaps)

    if overlaps[0]["start_time"] != 0:
        cutVideoWithWhiteNoise(
            video,
            00,
            overlaps[0]["start_time"],
            f"{projectLocation}merge/x_{getSequenceNo(i)}.avi",
        )

        cutAudio(
            background,
            00,
            overlaps[0]["start_time"],
            f"{projectLocation}background/x_{getSequenceNo(i)}.avi",
        )
        i += 1

    for overlap in overlaps:

        if overlap["overlap"] == 0:
            cutVideo(
                video,
                overlap["start_time"],
                overlap["end_time"],
                f"{projectLocation}videos/x_{getSequenceNo(i)}.avi",
            )

            cutAudio(
                background,
                overlap["start_time"],
                overlap["end_time"],
                f"{projectLocation}background/x_{getSequenceNo(i)}.avi",
            )

        elif overlap["overlap"] == 1:
            cutVideo(
                video,
                overlap["start_time"],
                overlap["end_time"],
                f"{projectLocation}videos/x_{getSequenceNo(i)}.avi",
            )

            cutAudio(
                background,
                overlap["start_time"],
                overlap["end_time"],
                f"{projectLocation}background/x_{getSequenceNo(i)}.avi",
            )

            changeAudioLength(
                f"{projectLocation}audio/{overlap['name']}",
                overlap["audio_duration"],
                overlap["required_duration"],
                f"{projectLocation}audio/temp/{overlap['name']}",
            )
            os.replace(
                f"{projectLocation}audio/temp/{overlap['name']}",
                f"{projectLocation}audio/{overlap['name']}",
            )

        elif overlap["overlap"] == 2:
            cutVideo(
                video,
                overlap["start_time"],
                overlap["end_time"],
                f"{projectLocation}videos/temp/x_{getSequenceNo(i)}.avi",
            )
            cutAudio(
                background,
                overlap["start_time"],
                overlap["end_time"],
                f"{projectLocation}background/temp/x_{getSequenceNo(i)}.avi",
            )

            gap = abs(overlap["audio_duration"] - overlap["required_duration"])
            newGap = gap / 2
            newRequiredDuration = overlap["required_duration"] + newGap

            # test
            changeVideoLength(
                f"{projectLocation}videos/temp/x_{getSequenceNo(i)}.avi",
                overlap["required_duration"],
                newRequiredDuration,
                f"{projectLocation}videos/x_{getSequenceNo(i)}.avi",
            )
            changeAudioLength(
                f"{projectLocation}background/temp/x_{getSequenceNo(i)}.avi",
                overlap["required_duration"],
                newRequiredDuration,
                f"{projectLocation}background/x_{getSequenceNo(i)}.avi",
            )
            changeAudioLength(
                f"{projectLocation}audio/{overlap['name']}",
                overlap["audio_duration"],
                newRequiredDuration,
                f"{projectLocation}audio/temp/{overlap['name']}",
            )
            os.replace(
                f"{projectLocation}audio/temp/{overlap['name']}",
                f"{projectLocation}audio/{overlap['name']}",
            )

        command = f"ffmpeg -y -i {projectLocation}videos/x_{getSequenceNo(i)}.avi -i {projectLocation}audio/{overlap['name']}  -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 -af apad -shortest {projectLocation}merge/x_{getSequenceNo(i)}.avi"
        os.system(command)
        i += 1

        if k < siz - 1:
            cutVideoWithWhiteNoise(
                video,
                overlaps[k]["end_time"],
                overlaps[k + 1]["start_time"],
                f"{projectLocation}merge/x_{getSequenceNo(i)}.avi",
            )
            cutAudio(
                background,
                overlaps[k]["end_time"],
                overlaps[k + 1]["start_time"],
                f"{projectLocation}background/x_{getSequenceNo(i)}.avi",
            )
            i += 1
        k += 1

    # handle case to add a left over audio

    # write a function to concat
    os.chdir(f"{projectLocation}merge")
    os.system("for f in *.avi; do echo \"file '$f'\" >> video.txt; done")
    os.system("ffmpeg -f concat -i video.txt -c copy a.avi")

    os.chdir(f"{projectLocation}background")
    os.system("for f in *.avi; do echo \"file '$f'\" >> video.txt; done")
    os.system("ffmpeg -f concat -i video.txt -c copy a.avi")

    os.system(
        'ffmpeg -i ../merge/a.avi -i a.avi -filter_complex "[1]volume=1[aud1]; [0][aud1]amix=2,volume=2" -c:v copy ../f.avi'
    )


# give background stream also
combine(
    "/home/swarupkharul/Documents/yaksaa/nanotech/videoStream.mp4",
    "/home/swarupkharul/Documents/yaksaa/nanotech/audio_Instruments.wav",
    overlaps,
    "/home/swarupkharul/Documents/yaksaa/nanotech/mr-IN/",
)

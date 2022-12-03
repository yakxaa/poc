import os
from modules.cutVideo import cutVideo, cutVideoWithWhiteNoise, cutAudio
from modules.changeAudioLength import changeAudioLength
from modules.changeVideoLength import changeVideoLength

overlaps = [
    {
        "name": "0000_0.74.mp3",
        "start_time": 0.74,
        "end_time": 7.68,
        "audio_duration": 7.645792,
        "required_duration": 6.9399999999999995,
        "overlap": 1,
    },
    {
        "name": "0001_7.71.mp3",
        "start_time": 7.71,
        "end_time": 10.71,
        "audio_duration": 3.141667,
        "required_duration": 3.000000000000001,
        "overlap": 1,
    },
    {
        "name": "0002_10.72.mp3",
        "start_time": 10.72,
        "end_time": 18.76,
        "audio_duration": 8.207875,
        "required_duration": 8.040000000000001,
        "overlap": 1,
    },
    {
        "name": "0003_19.59.mp3",
        "start_time": 19.59,
        "end_time": 24.89,
        "audio_duration": 5.855125,
        "required_duration": 5.300000000000001,
        "overlap": 1,
    },
    {
        "name": "0004_24.9.mp3",
        "start_time": 24.9,
        "end_time": 28.16,
        "audio_duration": 4.127708,
        "required_duration": 3.2600000000000016,
        "overlap": 2,
    },
    {
        "name": "0005_28.17.mp3",
        "start_time": 28.17,
        "end_time": 43.89,
        "audio_duration": 5.787833,
        "required_duration": 15.719999999999999,
        "overlap": 0,
    },
    {
        "name": "0006_43.9.mp3",
        "start_time": 43.9,
        "end_time": 51.93,
        "audio_duration": 8.873458,
        "required_duration": 8.030000000000001,
        "overlap": 1,
    },
    {
        "name": "0007_51.94.mp3",
        "start_time": 51.94,
        "end_time": 55.61,
        "audio_duration": 2.654417,
        "required_duration": 3.6700000000000017,
        "overlap": 0,
    },
    {
        "name": "0008_56.35.mp3",
        "start_time": 56.35,
        "end_time": 65.95,
        "audio_duration": 12.656292,
        "required_duration": 9.600000000000001,
        "overlap": 2,
    },
    {
        "name": "0009_65.98.mp3",
        "start_time": 65.98,
        "end_time": 73.71,
        "audio_duration": 8.372333,
        "required_duration": 7.72999999999999,
        "overlap": 1,
    },
    {
        "name": "0010_73.72.mp3",
        "start_time": 73.72,
        "end_time": 84.39,
        "audio_duration": 11.687,
        "required_duration": 10.670000000000002,
        "overlap": 1,
    },
    {
        "name": "0011_84.75.mp3",
        "start_time": 84.75,
        "end_time": 96.15,
        "audio_duration": 10.536042,
        "required_duration": 11.400000000000006,
        "overlap": 0,
    },
    {
        "name": "0012_96.75.mp3",
        "start_time": 96.75,
        "end_time": 104.19,
        "audio_duration": 6.094083,
        "required_duration": 7.439999999999998,
        "overlap": 0,
    },
    {
        "name": "0013_104.96.mp3",
        "start_time": 104.96,
        "end_time": 108.13,
        "audio_duration": 2.690667,
        "required_duration": 3.1700000000000017,
        "overlap": 0,
    },
    {
        "name": "0014_108.14.mp3",
        "start_time": 108.14,
        "end_time": 113.67,
        "audio_duration": 6.286375,
        "required_duration": 5.530000000000001,
        "overlap": 1,
    },
    {
        "name": "0015_113.7.mp3",
        "start_time": 113.7,
        "end_time": 122.45,
        "audio_duration": 8.788833,
        "required_duration": 8.75,
        "overlap": 1,
    },
    {
        "name": "0016_122.46.mp3",
        "start_time": 122.46,
        "end_time": 123.86,
        "audio_duration": 2.278042,
        "required_duration": 1.4000000000000057,
        "overlap": 2,
    },
    {
        "name": "0017_124.54.mp3",
        "start_time": 124.54,
        "end_time": 127.25,
        "audio_duration": 2.311875,
        "required_duration": 2.7099999999999937,
        "overlap": 0,
    },
    {
        "name": "0018_127.51.mp3",
        "start_time": 127.51,
        "end_time": 129.38,
        "audio_duration": 2.115042,
        "required_duration": 1.8699999999999903,
        "overlap": 1,
    },
    {
        "name": "0019_129.38.mp3",
        "start_time": 129.38,
        "end_time": 140.61,
        "audio_duration": 12.827792,
        "required_duration": 11.230000000000018,
        "overlap": 1,
    },
    {
        "name": "0020_140.68.mp3",
        "start_time": 140.68,
        "end_time": 147.61,
        "audio_duration": 8.008125,
        "required_duration": 6.930000000000007,
        "overlap": 1,
    },
    {
        "name": "0021_147.62.mp3",
        "start_time": 147.62,
        "end_time": 155.59,
        "audio_duration": 10.761917,
        "required_duration": 7.969999999999999,
        "overlap": 2,
    },
    {
        "name": "0022_155.88.mp3",
        "start_time": 155.88,
        "end_time": 167.3,
        "audio_duration": 14.9865,
        "required_duration": 11.420000000000016,
        "overlap": 2,
    },
    {
        "name": "0023_167.87.mp3",
        "start_time": 167.87,
        "end_time": 187.08,
        "audio_duration": 20.478042,
        "required_duration": 19.210000000000008,
        "overlap": 1,
    },
    {
        "name": "0024_187.78.mp3",
        "start_time": 187.78,
        "end_time": 195.21,
        "audio_duration": 7.816708,
        "required_duration": 7.430000000000007,
        "overlap": 1,
    },
    {
        "name": "0025_195.25.mp3",
        "start_time": 195.25,
        "end_time": 198.58,
        "audio_duration": 3.618208,
        "required_duration": 3.3300000000000125,
        "overlap": 1,
    },
    {
        "name": "0026_198.59.mp3",
        "start_time": 198.59,
        "end_time": 209.19,
        "audio_duration": 11.590833,
        "required_duration": 10.599999999999994,
        "overlap": 1,
    },
    {
        "name": "0027_209.2.mp3",
        "start_time": 209.2,
        "end_time": 226.52,
        "audio_duration": 18.862542,
        "required_duration": 17.32000000000002,
        "overlap": 1,
    },
    {
        "name": "0028_226.6.mp3",
        "start_time": 226.6,
        "end_time": 234.39,
        "audio_duration": 7.502208,
        "required_duration": 7.789999999999992,
        "overlap": 0,
    },
    {
        "name": "0029_234.64.mp3",
        "start_time": 234.64,
        "end_time": 247.1,
        "audio_duration": 14.450958,
        "required_duration": 12.460000000000008,
        "overlap": 1,
    },
    {
        "name": "0030_247.4.mp3",
        "start_time": 247.4,
        "end_time": 256.36,
        "audio_duration": 10.094917,
        "required_duration": 8.960000000000008,
        "overlap": 1,
    },
    {
        "name": "0031_256.37.mp3",
        "start_time": 256.37,
        "end_time": 263.54,
        "audio_duration": 7.950167,
        "required_duration": 7.170000000000016,
        "overlap": 1,
    },
    {
        "name": "0032_263.55.mp3",
        "start_time": 263.55,
        "end_time": 266,
        "audio_duration": 2.12325,
        "required_duration": 2.4499999999999886,
        "overlap": 0,
    },
    {
        "name": "0033_266.01.mp3",
        "start_time": 266.01,
        "end_time": 269.22,
        "audio_duration": 3.215375,
        "required_duration": 3.2100000000000364,
        "overlap": 1,
    },
    {
        "name": "0034_269.23.mp3",
        "start_time": 269.23,
        "end_time": 280.54,
        "audio_duration": 11.566667,
        "required_duration": 11.310000000000002,
        "overlap": 1,
    },
    {
        "name": "0035_280.64.mp3",
        "start_time": 280.64,
        "end_time": 289.84,
        "audio_duration": 11.294375,
        "required_duration": 9.199999999999989,
        "overlap": 1,
    },
    {
        "name": "0036_289.85.mp3",
        "start_time": 289.85,
        "end_time": 292.6,
        "audio_duration": 2.763542,
        "required_duration": 2.75,
        "overlap": 1,
    },
    {
        "name": "0037_292.66.mp3",
        "start_time": 292.66,
        "end_time": 303.56,
        "audio_duration": 10.423667,
        "required_duration": 10.899999999999977,
        "overlap": 0,
    },
    {
        "name": "0038_303.8.mp3",
        "start_time": 303.8,
        "end_time": 313.93,
        "audio_duration": 10.943708,
        "required_duration": 10.129999999999995,
        "overlap": 1,
    },
    {
        "name": "0039_313.94.mp3",
        "start_time": 313.94,
        "end_time": 319.06,
        "audio_duration": 6.753292,
        "required_duration": 5.1200000000000045,
        "overlap": 2,
    },
    {
        "name": "0040_319.07.mp3",
        "start_time": 319.07,
        "end_time": 324.14,
        "audio_duration": 5.033958,
        "required_duration": 5.069999999999993,
        "overlap": 0,
    },
    {
        "name": "0041_324.35.mp3",
        "start_time": 324.35,
        "end_time": 344.21,
        "audio_duration": 24.058208,
        "required_duration": 19.859999999999957,
        "overlap": 1,
    },
    {
        "name": "0042_344.33.mp3",
        "start_time": 344.33,
        "end_time": 349.92,
        "audio_duration": 8.167792,
        "required_duration": 5.590000000000032,
        "overlap": 2,
    },
    {
        "name": "0043_350.38.mp3",
        "start_time": 350.38,
        "end_time": 354.32,
        "audio_duration": 6.143292,
        "required_duration": 3.9399999999999977,
        "overlap": 2,
    },
    {
        "name": "0044_355.01.mp3",
        "start_time": 355.01,
        "end_time": 359.98,
        "audio_duration": 7.565333,
        "required_duration": 4.970000000000027,
        "overlap": 2,
    },
    {
        "name": "0045_360.1.mp3",
        "start_time": 360.1,
        "end_time": 368.71,
        "audio_duration": 10.539667,
        "required_duration": 8.609999999999957,
        "overlap": 1,
    },
    {
        "name": "0046_368.77.mp3",
        "start_time": 368.77,
        "end_time": 381.86,
        "audio_duration": 12.364333,
        "required_duration": 13.090000000000032,
        "overlap": 0,
    },
    {
        "name": "0047_381.89.mp3",
        "start_time": 381.89,
        "end_time": 391.05,
        "audio_duration": 11.581208,
        "required_duration": 9.160000000000025,
        "overlap": 2,
    },
    {
        "name": "0048_391.06.mp3",
        "start_time": 391.06,
        "end_time": 395.35,
        "audio_duration": 4.954625,
        "required_duration": 4.2900000000000205,
        "overlap": 1,
    },
    {
        "name": "0049_395.62.mp3",
        "start_time": 395.62,
        "end_time": 405.5,
        "audio_duration": 11.530167,
        "required_duration": 9.879999999999995,
        "overlap": 1,
    },
    {
        "name": "0050_405.73.mp3",
        "start_time": 405.73,
        "end_time": 413.195,
        "audio_duration": 9.415792,
        "required_duration": 7.464999999999975,
        "overlap": 2,
    },
    {
        "name": "0051_413.205.mp3",
        "start_time": 413.205,
        "end_time": 418.975,
        "audio_duration": 6.318917,
        "required_duration": 5.770000000000039,
        "overlap": 1,
    },
    {
        "name": "0052_418.985.mp3",
        "start_time": 418.985,
        "end_time": 432.66,
        "audio_duration": 12.63725,
        "required_duration": 13.675000000000011,
        "overlap": 0,
    },
    {
        "name": "0053_433.27.mp3",
        "start_time": 433.27,
        "end_time": 440.58,
        "audio_duration": 8.728208,
        "required_duration": 7.310000000000002,
        "overlap": 1,
    },
    {
        "name": "0054_440.75.mp3",
        "start_time": 440.75,
        "end_time": 460.38,
        "audio_duration": 19.127667,
        "required_duration": 19.629999999999995,
        "overlap": 0,
    },
    {
        "name": "0055_460.39.mp3",
        "start_time": 460.39,
        "end_time": 487.29,
        "audio_duration": 26.576583,
        "required_duration": 26.900000000000034,
        "overlap": 0,
    },
    {
        "name": "0056_487.3.mp3",
        "start_time": 487.3,
        "end_time": 495.3,
        "audio_duration": 9.086875,
        "required_duration": 8,
        "overlap": 1,
    },
    {
        "name": "0057_495.31.mp3",
        "start_time": 495.31,
        "end_time": 504.79,
        "audio_duration": 11.276292,
        "required_duration": 9.480000000000018,
        "overlap": 1,
    },
    {
        "name": "0058_504.87.mp3",
        "start_time": 504.87,
        "end_time": 506.81,
        "audio_duration": 2.047375,
        "required_duration": 1.9399999999999977,
        "overlap": 1,
    },
    {
        "name": "0059_506.97.mp3",
        "start_time": 506.97,
        "end_time": 520.72,
        "audio_duration": 16.917625,
        "required_duration": 13.75,
        "overlap": 1,
    },
    {
        "name": "0060_520.87.mp3",
        "start_time": 520.87,
        "end_time": 525.09,
        "audio_duration": 3.647917,
        "required_duration": 4.220000000000027,
        "overlap": 0,
    },
    {
        "name": "0061_525.1.mp3",
        "start_time": 525.1,
        "end_time": 538.92,
        "audio_duration": 13.716125,
        "required_duration": 13.819999999999936,
        "overlap": 0,
    },
    {
        "name": "0062_538.93.mp3",
        "start_time": 538.93,
        "end_time": 543.81,
        "audio_duration": 5.817292,
        "required_duration": 4.8799999999999955,
        "overlap": 1,
    },
    {
        "name": "0063_543.82.mp3",
        "start_time": 543.82,
        "end_time": 546.03,
        "audio_duration": 1.909917,
        "required_duration": 2.2099999999999227,
        "overlap": 0,
    },
    {
        "name": "0064_546.22.mp3",
        "start_time": 546.22,
        "end_time": 557.3,
        "audio_duration": 13.859542,
        "required_duration": 11.079999999999927,
        "overlap": 2,
    },
    {
        "name": "0065_557.3.mp3",
        "start_time": 557.3,
        "end_time": 561.65,
        "audio_duration": 3.537,
        "required_duration": 4.350000000000023,
        "overlap": 0,
    },
    {
        "name": "0066_561.72.mp3",
        "start_time": 561.72,
        "end_time": 581.55,
        "audio_duration": 17.975625,
        "required_duration": 19.829999999999927,
        "overlap": 0,
    },
    {
        "name": "0067_581.56.mp3",
        "start_time": 581.56,
        "end_time": 598.1,
        "audio_duration": 23.563375,
        "required_duration": 16.540000000000077,
        "overlap": 2,
    },
    {
        "name": "0068_598.37.mp3",
        "start_time": 598.37,
        "end_time": 602.89,
        "audio_duration": 3.9655,
        "required_duration": 4.519999999999982,
        "overlap": 0,
    },
    {
        "name": "0069_602.95.mp3",
        "start_time": 602.95,
        "end_time": 620.74,
        "audio_duration": 19.75325,
        "required_duration": 17.789999999999964,
        "overlap": 1,
    },
    {
        "name": "0070_620.78.mp3",
        "start_time": 620.78,
        "end_time": 638.14,
        "audio_duration": 20.589542,
        "required_duration": 17.360000000000014,
        "overlap": 1,
    },
    {
        "name": "0071_638.19.mp3",
        "start_time": 638.19,
        "end_time": 640.9,
        "audio_duration": 3.024583,
        "required_duration": 2.7099999999999227,
        "overlap": 1,
    },
    {
        "name": "0072_640.97.mp3",
        "start_time": 640.97,
        "end_time": 648.95,
        "audio_duration": 11.445417,
        "required_duration": 7.980000000000018,
        "overlap": 2,
    },
    {
        "name": "0073_649.17.mp3",
        "start_time": 649.17,
        "end_time": 656.31,
        "audio_duration": 8.035833,
        "required_duration": 7.139999999999986,
        "overlap": 1,
    },
    {
        "name": "0074_657.39.mp3",
        "start_time": 657.39,
        "end_time": 661.55,
        "audio_duration": 4.6915,
        "required_duration": 4.159999999999968,
        "overlap": 1,
    },
    {
        "name": "0075_661.56.mp3",
        "start_time": 661.56,
        "end_time": 664.73,
        "audio_duration": 3.070833,
        "required_duration": 3.1700000000000728,
        "overlap": 0,
    },
]

def getSequenceNo(x):
    y = 10000
    y += x
    return str(y)[1:]

def combine(video,background, overlaps, projectLocation):
    i = 0
    k = 0
    siz = len(overlaps)

    if overlaps[0]["start_time"] != 0:
        cutVideoWithWhiteNoise(
            video, 00, overlaps[0]["start_time"], f"{projectLocation}merge/{getSequenceNo(i)}.avi"
        )

        cutAudio(
            background, 00, overlaps[0]["start_time"], f"{projectLocation}background/{getSequenceNo(i)}.avi"
        )
        i += 1

    for overlap in overlaps:

        if overlap["overlap"] == 0:
            cutVideo(
                video,
                overlap["start_time"],
                overlap["end_time"],
                f"{projectLocation}videos/{i}.avi",
            )

            cutAudio(
                background,
                overlap["start_time"],
                overlap["end_time"],
                f"{projectLocation}background/{getSequenceNo}.avi",
            )

        elif overlap["overlap"] == 1:
            cutVideo(
                video,
                overlap["start_time"],
                overlap["end_time"],
                f"{projectLocation}videos/{i}.avi",
            )

            cutAudio(
                background,
                overlap["start_time"],
                overlap["end_time"],
                f"{projectLocation}background/{getSequenceNo}.avi",
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
                f"{projectLocation}videos/temp/{i}.avi",
            )
            cutAudio(
                background,
                overlap["start_time"],
                overlap["end_time"],
                f"{projectLocation}background/temp/{i}.avi",
            )

            gap = abs(overlap["audio_duration"] - overlap["required_duration"])
            newGap = gap / 2
            newRequiredDuration = overlap["required_duration"] + newGap
            
            #test 
            changeVideoLength(
                f"{projectLocation}videos/temp/{i}.avi",
                overlap["required_duration"],
                newRequiredDuration,
                f"{projectLocation}videos/{i}.avi",
            )
            changeAudioLength(
                f"{projectLocation}background/temp/{i}.avi",
                overlap["required_duration"],
                newRequiredDuration,
                f"{projectLocation}background/{getSequenceNo(i)}.avi",
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

        command = f"ffmpeg -y -i {projectLocation}videos/{i}.avi -i {projectLocation}audio/{overlap['name']}  -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 -af apad {projectLocation}merge/{getSequenceNo(i)}.avi"
        os.system(command)
        i += 1

        if k < siz - 1:
            cutVideoWithWhiteNoise(
                video,
                overlaps[k]["end_time"],
                overlaps[k + 1]["start_time"],
                f"{projectLocation}merge/{getSequenceNo(i)}.avi",
            )
            cutVideo(
                background,
                overlaps[k]["start_time"],
                overlaps[k+1]["end_time"],
                f"{projectLocation}background/{getSequenceNo(i)}.avi",
            )
            i += 1
        k += 1

    # write a function to concat

#give background stream also
combine(
    "/home/swarupkharul/Documents/yaksaa/inanutsshell/videoStream.mp4",
    overlaps,
    "/home/swarupkharul/Documents/yaksaa/inanutsshell/",
)

import subprocess
import os

deivces = []

def run(resolution, framerate, time, device, output):
    if os.path.isfile(output):
        os.remove(output)
    p = subprocess.Popen(["ffmpeg", "-f", "dshow", "-video_size", resolution, "-framerate", framerate, "-t", time, "-i", f'video={device}', output])
    return p

if len(deivces) == 0:
    print("Check the devices using command 'ffmpeg -list_devices true -f dshow -i dummy' command.")
else:
    for i, device in zip(range(3), deivces):
        p = run("3840x2160", "30", "5", device, f"out{i}.avi")

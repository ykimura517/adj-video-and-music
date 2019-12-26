import cv2
import subprocess
import sys


raw_video_path=sys.argv[1]
long_volumed_music_path=sys.argv[2]

# ffprobe -v error -select_streams v:0 -show_entries stream=duration -of default=noprint_wrappers=1:nokey=1 input.mp4
print("Get length of the movie ..")
cmdToGetDurationOfVideo ="ffprobe -v error -select_streams v:0 -show_entries stream=duration -of default=noprint_wrappers=1:nokey=1 "+raw_video_path
# subprocess.call(cmdToGetDurationOfVideo.split())
res=subprocess.check_output(cmdToGetDurationOfVideo.split())
print(int(float(res.decode().replace("\n",""))))

howLongIsTheMOvie = int(float(res.decode().replace("\n","")))
print("done!")
print("Cutting the music to equate its length with the movie..")
# print(type(sys.stdout.buffer.write(res)))
cut_long_volumed_music_path = "Cut"+long_volumed_music_path
cmdToCutMusic = "ffmpeg -ss 0 -i "+long_volumed_music_path+" -t "+str(howLongIsTheMOvie)+" "+cut_long_volumed_music_path+" -y"
subprocess.call(cmdToCutMusic.split())

print("done!")

print("Adjusting Volume of the movie...")
adjustedVideo = "Volumed"+raw_video_path
cmdToAdjVolOfmovie ='ffmpeg -i '+raw_video_path+' -vcodec copy -af volume=5.5dB '+adjustedVideo+" -y"
print(cmdToAdjVolOfmovie)
subprocess.call(cmdToAdjVolOfmovie.split())
print("done!!")

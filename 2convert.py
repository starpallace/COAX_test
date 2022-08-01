# pip install moviepy
from moviepy.editor import VideoFileClip as vfc
import urllib.request
import os

# configure import /export
export_name = 'tok.gif'
link = 'https://vod-progressive.akamaized.net/exp=1659410864~acl=%2Fvimeo-prod-skyfire-std-us%2F01%2F3416%2F20%2F517080601%2F2403204563.mp4~hmac=72b5fa1de3872f6098a550e03862cd784716db0a4bc1db3ba117ba99bde417e3/vimeo-prod-skyfire-std-us/01/3416/20/517080601/2403204563.mp4?download=1&filename=pexels-cup-of-couple-6962687.mp4'
#temporary mp4file 
file_name = 'tik.mp4' 
#option remove/not temporary mp4 file
remove_mp4 = True

# get video
try:
    con = urllib.request.urlretrieve(link, file_name) 
    
except:
    print('wrong url or api usage')

# load and convert ti gif
tok = vfc(file_name)
tok.write_gif('tok.gif')

if remove_mp4 == True:
    os.remove(file_name)

print('Completed')

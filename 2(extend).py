import io
import os
import subprocess

from pydub import AudioSegment
import scipy.io.wavfile as wav


longest = 0
files = []
import glob, os
os.chdir("C://Users//Stanl//Desktop//Python//Spectrogram//clean_cut")
for file in glob.glob("*.wav"):
    files.append(file)

for f in range (len(files)):
    song = AudioSegment.from_wav("C://Users//Stanl//Desktop//Python//Spectrogram//clean_cut//"+files[f])

    #print('Duration: ' + )
    if song.duration_seconds >longest:
        longest=  song.duration_seconds
print(longest)



print(len(files))
for f in range (1,len(files)):
    audio = AudioSegment.from_wav("C://Users//Stanl//Desktop//Python//Spectrogram//clean_cut//"+files[f])
    difference = longest - audio.duration_seconds
    print(difference*1000)
    silence = AudioSegment.silent(duration=(difference*1000))
    padded = audio + silence  # Adding silence after the audio
    padded.export('C://Users//Stanl//Desktop//Python//Spectrogram//extend//'+str(f)+'.wav', format='wav')

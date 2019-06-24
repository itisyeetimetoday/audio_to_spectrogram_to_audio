import io
import os
import subprocess
import glob


path = 'C://Users//Stanl//Desktop//Python//Spectrogram'

def demuffle(input,output,path):
    command = "sox {path}/reconstruct/{input} {path}/temp/noise-audio{input}.wav trim 0 2.00".format(input=input, output = output, path = path)
    subprocess.call(command,shell=True)

    command = "sox {path}/temp/noise-audio{input}.wav -n noiseprof {path}/temp/noise{input}.prof".format(input=input, output = output, path = path)
    subprocess.call(command,shell=True)

    command = "sox {path}/reconstruct/{input} {path}/temp/audio-clean{input}.wav noisered {path}//temp//noise{input}.prof 0.08".format(input=input, output = output, path = path)
    subprocess.call(command,shell=True)

    command = "sox -v 1.4 {path}/temp/audio-clean{input}.wav {path}/unecho_final/out{input}.wav".format(input=input, output = output, path = path)
    subprocess.call(command,shell=True)
count = 0


files = []
import os
os.chdir("C://Users//Stanl//Desktop//Python//Spectrogram//reconstruct//")
for file in glob.glob("*.wav"):
    files.append(file)
print(files)

count = 0
for f in range (len(files)):
    demuffle(path = path,input = str(count)+'.wav', output = str(count)+'.wav' )
    count = count + 1

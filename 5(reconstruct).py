import io
import os
import subprocess

files = []
import glob, os
os.chdir("./spectrogram")
for file in glob.glob("*.bmp"):
    files.append(file)

min_freq = 30
max_freq = 18000
bpo = 60
pps = 150
sample_rate = 44100
bright = 2.25
mode = 'sine'
path_to_folder = 'C://Users//Stanl//Desktop//Python//Spectrogram//spectrogram'
path_to_output = 'C://Users//Stanl//Desktop//Python//Spectrogram//reconstruct'
print('files found: '+ str(files))
def reconstruct(path_to_folder, path_to_output, input,output, min_freq, max_freq, bpo, pps, mode, sample_rate, bright):
    command = "arss -q {path_to_folder}/{input} --{mode} -min {min_freq} -b {bpo} --pps {pps} {path_to_output}/{output}.wav -r {sample_rate} -g {bright}".format(sample_rate = sample_rate,input=input, output=output, min_freq=min_freq, max_freq=max_freq, bpo = bpo, pps = pps, path_to_folder = path_to_folder, path_to_output = path_to_output, mode = mode, bright = bright)
    subprocess.call(command,shell=True)

count = 0
for f in range (len(files)):
    reconstruct(path_to_folder = path_to_folder, path_to_output= path_to_output, input = files[count] , output = str(count), min_freq = min_freq, max_freq = max_freq, bpo = bpo, pps = pps, mode = mode, bright = bright, sample_rate=sample_rate)
    count = count + 1

files = []

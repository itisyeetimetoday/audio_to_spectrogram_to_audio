import io
import os
import subprocess

files = []
import glob, os
os.chdir("./clean_cut")
for file in glob.glob("*.wav"):
    files.append(file)

min_freq = 30
max_freq = 18000
bpo = 60
pps = 150
bright = 2.25
format_param = 16
path_to_folder = 'C://Users//Stanl//Desktop//Python//Spectrogram//clean_cut'
path_to_output = 'C://Users//Stanl//Desktop//Python//Spectrogram//spectrogram'
print('files found: '+ str(files))
def convert(path_to_folder, path_to_output, input,output, min_freq, max_freq, bpo, pps, bright, format_param):
    command = "Arss  --quiet {path_to_folder}/{input} {path_to_output}/{output} --analysis --min-freq {min_freq} --max-freq {max_freq} --bpo {bpo} --pps {pps} --brightness {bright} --format-param {format_param}".format(input=input, output=output, min_freq=min_freq, max_freq=max_freq, bpo = bpo, pps = pps, bright = bright, format_param = format_param, path_to_folder = path_to_folder, path_to_output = path_to_output)
    subprocess.call(command,shell=True)
count = 0
for f in range (len(files)):
    convert(path_to_folder = path_to_folder, path_to_output= path_to_output, input = files[count] , output = str(count)+'.bmp', min_freq = min_freq, max_freq = max_freq, bpo = bpo, pps = pps, bright = bright, format_param = format_param)
    count = count + 1

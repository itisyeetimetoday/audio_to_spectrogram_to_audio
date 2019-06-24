import io
import os
import subprocess

files = []
import glob, os
os.chdir("C://Users//Stanl//Desktop//Python//Spectrogram//extend")
for file in glob.glob("*.wav"):
    files.append(file)

print('files found: '+ str(files))
def clean_file(input,output):
    command = "ffmpeg -i {input} -c copy -bitexact -map_metadata -1 {output} -y".format(input=input, output=output)
    subprocess.call(command,shell=True)

    

for f in range (len(files)):
    clean_file(files[f],('../clean_cut/file_'+str(f)+'.wav'))

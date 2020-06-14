#!/usr/local/bin/python3

import os

print('Welcome to youtube to mp3 Downloader')

result = os.system('cd $HOME/youtube-musics')

if result != 0:
    os.system("mkdir $HOME/youtube-musics")
    os.system('cd $HOME/youtube-musics')
    os.system('echo Directory $HOME/youtube-musics created!')

times = int(input('How many songs do you want to download?: '))

for i in range(times):
    url = input(f'Please, enter a valid youtube url to video {i + 1}: ')
    os.system(f'cd $HOME/youtube-musics && youtube-dl {url} -x --audio-format mp3 -v')
    print(f'Download of music {i + 1} completed')

os.system('xdg-open $HOME/youtube-musics')
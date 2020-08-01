#!/usr/local/bin/python3

import os

print('Welcome to youtube to mp3 Downloader')

result = os.system('cd $HOME/youtube-musics')

if result != 0:
    os.system("mkdir $HOME/youtube-musics")
    os.system('cd $HOME/youtube-musics')
    os.system('echo Directory $HOME/youtube-musics created!')


urls = ['']
while True:
    times = int(input('How many songs do you want to download?: '))
    for i in range(times):
        url = input(f'Please, enter a valid youtube url to video {i + 1}: ')
        urls.append(url)
    response = input('Do you want download more videos? [y/n]: ')
    if response.lower() == 'n':
        break
for x in range(len(urls)):
    link = urls[x - 1]   
    os.system(f'cd $HOME/youtube-musics && youtube-dl {link} -x --audio-format mp3 -v')
    print(f'Download of music {x} completed')

os.system('xdg-open $HOME/youtube-musics')

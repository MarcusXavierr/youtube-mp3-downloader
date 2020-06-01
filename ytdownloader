echo "Welcome to youtube to mp3 Downloader";
if [ -d $HOME/youtube-musics ]; then
    cd $HOME/youtube-musics
else
    mkdir $HOME/youtube-musics
    echo "Directory $HOME/youtube-musics created!"
    cd $HOME/youtube-musics
fi

#read the input
echo "Please enter a valid youtube url:"
read yturl
export yturl

#executing the download
youtube-dl $yturl -x --audio-format mp3 -v

#end message
echo Download completed! Check $HOME/youtube-musics folder!

xdg-open $HOME/youtube-musics


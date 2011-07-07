#Switch locale
export LANG=en_US.utf8
#Convert to MP3
ffmpeg -i $1 -v 0 -f wav - | lame --pad-id3v2-size 1024 -S -V 9 --resample 44.1 - $2
#Copy tags
./copytags.py $1 $2
#Store Metadata to another file
#mutagen-inspect $1 | grep "=" > $2.metadata
#Remove original
#rm $1

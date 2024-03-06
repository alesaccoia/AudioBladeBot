# Uses

    sudo apt-get install timidity
    sudo apt-get install ffmpeg

timidity input_file.mid -Ow -o - | ffmpeg -i - -acodec libmp3lame -ab 64k output_file.mp3

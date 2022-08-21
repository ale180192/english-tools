## Subtitles script
This script reads files with the format rst, removes all the timelines, secuency number and save the new file as a txt file, this is useful if we want to read the subtitles of certain movie or serie, the new txt file will be more legible if maybe before we watch the movie/serie we be able of read all the transcript, we make a look up of the words/sentences that we don't understeand and after that watch the movie/serie. I think that with this process we can saved a lot of time because if we watch the movie/serie without before know very good all the voucabulary we have to pause this one, go to the translate, come back to movie/serie, rewind the 5 seconds in order to watch/hear again that sentence/word so with this script we only have to search of the subtitles on the internet, find the .rst files and run this script to get the txt file which is most legible, of course that we can only use the .rst files and read that ones but why not to makes a better format so that we can enjoy the process.

* A lot of chapters of the legend of korra are already loaded here.
* The txt files are at the relative path output/subtitles/
* The rst files must be loaded on the assets/subtitles/<some_folder_name_of_the_movie>/<here-all-the-rst-files>

### How to works
We only have to run the above command and the new files will be found into the ouput/subtitles folder.
```bash
python subtitles
```

### TODO:
* maybe generate a pdf file
* support to convert any folder it finds into the assets/subtitles folder
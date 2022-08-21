import os
import re





def main():
    path_subtitles = "assets/subtitles/korra"
    path_destination = "output/subtitles/korra"
    base_path = os.getcwd()
    path_subtitles_abs = os.path.join(base_path, path_subtitles)
    path_destination_abs = os.path.join(base_path, path_destination)
    for filename in os.listdir(path_subtitles_abs):
        print("file: ", filename)
        with open(os.path.join(path_subtitles_abs, filename), "r") as file:
            new_filename = filename.replace(".srt", ".txt")
            with open(os.path.join(path_destination_abs, new_filename), "w+") as newfile:
                for line in file:
                    if not re.search("-->", line) and not re.search(r"^[1-9]+", line):
                        newfile.write(line)







if __name__ == "__main__":
    main()
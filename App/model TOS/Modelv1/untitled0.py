#this code is good for converting a video to mpg "mamdoh"


import os
import ffmpeg

def convert_to_mp4(mkv_file):
    name, ext = r"C:\Users\dell\Desktop\api\LipNet\videos\blue","mp4"
    out_name = name + ".mpg"
    ffmpeg.input(r"C:\Users\dell\Desktop\api\LipNet\videos\blue.mp4").output(out_name).run()
    print("Finished converting {}".format(mkv_file))
convert_to_mp4("dfa")

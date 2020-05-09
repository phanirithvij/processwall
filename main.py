import json
import sys

from wordcloud import WordCloud

from getprocs import fecth_memoryinfo
from wallpaper import setwallpaper


def makeImage(text):
    wc = WordCloud(max_words=1000, width=1920, height=1080)
    # wc = WordCloud(max_words=1000, width=3840, height=2160)
    # wc = WordCloud(background_color="white", max_words=1000, mask=alice_mask)
    # generate word cloud
    wc.generate_from_frequencies(text)
    wc.to_image().save("out.png")


if __name__ == "__main__":
    # if not sys.platform == 'win32':
    #     print("Not running on a Windows system")
    #     print("for linux look at https://github.com/anirudhajith/process-wallpaper")
    #     exit(-1)

    fecth_memoryinfo()
    with open("out.json") as infile:
        makeImage(json.load(infile))
    print("saved to out.png")
    setwallpaper('out.png')

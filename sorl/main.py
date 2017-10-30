from sorl.thumbnail_standalone import ThumbnailBackend
import sys
import os

sys.path.append(os.getcwd())

if __name__ == "__main__":
    thumbnailer = ThumbnailBackend("settings")
    thumbnailer.get_thumbnail("../tests/data/1_topleft.jpg", "100x100")

from sorl.thumbnail_standalone import ThumbnailBackend

if __name__ == "__main__":
    thumbnailer = ThumbnailBackend("settings")
    thumbnailer.get_thumbnail("../tests/data/1_topleft.jpg", "100x100")

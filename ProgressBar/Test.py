import time

from progress.bar import PixelBar

pixel = PixelBar("Remaining", suffix="%(percent)d%%")
for i in range(100):
    pixel.next()
    time.sleep(0.3)
pixel.finish()

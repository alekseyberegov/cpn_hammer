import uuid
import imgkit
from pathlib import Path


class WebPhotoTaker(object):
    def __init__(self, output_dir):
        self.output_dir = Path(output_dir)

    def take_photo(self, url):
        file = self.output_dir / ".".join([str(uuid.uuid4()), "png"])
        print(file)
        imgkit.from_url(url, file)

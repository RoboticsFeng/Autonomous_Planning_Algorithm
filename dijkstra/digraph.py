from PIL import Image, ImageDraw


class Digraph:
    def __init__(self, map):
        self.map = map
        self.N = len(self.map)

    def construct(self):
        img = Image.new('RGB', (self.image_size, self.image_size), (187, 255, 255))
        raise NotImplementedError

    def show(self):
        raise NotImplementedError

    def save(self, name):
        raise NotImplementedError
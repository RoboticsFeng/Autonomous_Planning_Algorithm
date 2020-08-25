from PIL import Image, ImageDraw


class GridMap:

		def __init__(self, map_matrix):
			self.map = map_matrix
			self.width = len(map_matrix[0])
			self.height = len(map_matrix)
			self.image_size = 1000
			self.map_img = self.construct_map_image()
			self.path = []

		def construct_map_image(self):
			img = Image.new('RGB', (self.image_size, self.image_size), (187, 255, 255))
			horizontal_line_interval = int(self.image_size/self.height)
			vertical_line_interval = int(self.image_size/self.width)
			#color obstacles
			for i in range(self.height):
				for j in range(self.width):
					if self.map[i][j] == 1:
						for m in range(horizontal_line_interval*i, horizontal_line_interval*(i+1)):
							for n in range(vertical_line_interval*j, vertical_line_interval*(j+1)):
								img.putpixel((m, n), (0,0,128))
			#add lines
			draw = ImageDraw.Draw(img)
			for i in range(1, self.width):
				draw.line((0, horizontal_line_interval*i, img.size[0], horizontal_line_interval*i), fill = 128)
			for j in range(1, self.height):
				draw.line((vertical_line_interval*j, 0, vertical_line_interval*j, img.size[1]), fill = 128)
			return img

		def add_path(self, path):
			if len(path) < 2:
				print("ERROR!, Path size is less than 2!")
				exit()
			horizontal_line_interval = int(self.image_size/self.height)
			vertical_line_interval = int(self.image_size/self.width)
			self.path = path
			draw = ImageDraw.Draw(self.map_img)
			for i in range(len(self.path) - 1):
				x1 = int((self.path[i][0] + 0.5) * horizontal_line_interval)
				y1 = int((self.path[i][1] + 0.5) * vertical_line_interval)
				x2 = int((self.path[i+1][0] + 0.5) * horizontal_line_interval)
				y2 = int((self.path[i+1][1] + 0.5) * vertical_line_interval)
				draw.line((x1, y1, x2, y2), width = 5, fill = 30)

		def show(self):
			self.map_img.show()

		def save(self, name):
			self.map_img.save(name)

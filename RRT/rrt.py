from PIL import Image, ImageDraw
import random
import math
import numpy as np


MAP_SIZE = 100
MAX_SEARCH = 5000
BRACNH_LEN = 4


class Node:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.parent = None


class RRT:
	def __init__(self, raw_map):
		self.visual_map = raw_map.resize((MAP_SIZE*5, MAP_SIZE*5))
		self.raw_map = raw_map.resize((MAP_SIZE, MAP_SIZE)).convert('L')
		self.map_matrix = np.array(self.raw_map)
		self.map_size = MAP_SIZE
		self.max_search = MAX_SEARCH
		self.branch_len = BRACNH_LEN
		self.choose_des_prob = 0.1
		self.root = Node(0, 0)
		self.node_list = [self.root]
		self.searched_area = [[False] * self.map_size for i in range(self.map_size)]
		self.update_reached_area(self.root)

	def find_closest_node(self, pt):
		min_dist_square = 100000
		ans = self.root
		for node in self.node_list:
			cur_dist_square = (node.x - pt[0])**2 + (node.y - pt[1])**2
			if cur_dist_square < min_dist_square:
				min_dist_square  = cur_dist_square
				ans = node
		return ans

	def update_reached_area(self, node):
		LEN = int(self.branch_len * 0.5)
		for i in range(node.x - LEN, node.x + LEN + 1):
			for j in range(node.y - LEN, node.y + LEN + 1):
				if i >=0 and i < self.map_size and j >= 0  and j < self.map_size:
					self.searched_area[i][j] = True

	def search(self):
		for i in range(self.max_search):
			#随机撒点或使用终点
			random_pt = []
			if random.random() < self.choose_des_prob:
				random_pt = [self.map_size - 1, self.map_size - 1]
			else:
				random_pt = [random.randint(0, self.map_size - 1), random.randint(0, self.map_size - 1)]
			#找到最近的节点并连接找下个节点
			nearest_node = self.find_closest_node(random_pt)
			alpha = self.branch_len / max(1, math.sqrt((nearest_node.x - random_pt[0])**2 + (nearest_node.y - random_pt[1])**2))
			x = int(alpha * (random_pt[0] - nearest_node.x) + nearest_node.x)
			y = int(alpha * (random_pt[1] - nearest_node.y) + nearest_node.y)
			if x < 0 or x >= self.map_size or y < 0 or y >= self.map_size or self.searched_area[x][y] or self.map_matrix[y][x] < 255:
				continue
			else:
				next_node = Node(x, y)
				next_node.parent = nearest_node
				self.update_reached_area(next_node)
				self.node_list.append(next_node)
				#check if success
				if (next_node.x - self.map_size + 1)**2 + (next_node.y - self.map_size + 1)**2 < self.branch_len**2:
					final_node = Node(self.map_size - 1, self.map_size - 1)
					final_node.parent = next_node
					self.node_list.append(final_node)
					self.draw_path()
					print("Solve succeeds! Search for", i, "steps.")
					return True
		return False

	def draw_path(self):
		draw = ImageDraw.Draw(self.visual_map)
		node = self.node_list[-1]
		while node.parent:
			pre_node = node.parent
			draw.line((node.x*5, node.y*5, pre_node.x*5, pre_node.y*5), fill = (255,0,0))
			node = node.parent

	def show(self):
		self.visual_map.show()


raw_map = Image.open("map1.png")

app = RRT(raw_map)
if app.search():
	app.show()
else:
	print("Solve failed!")


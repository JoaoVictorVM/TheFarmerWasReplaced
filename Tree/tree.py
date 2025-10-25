count = 0

while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if can_harvest():
				harvest()
			def count_is_par():
				return count % 2 == 0
			if (count_is_par() == True):
				def is_even():
					y = get_pos_y()
					return y % 2 == 0
				if (is_even() == True):
					plant(Entities.Tree)
			else:
				if (is_even() == False):
					plant(Entities.Tree)
			move(North)
		move(East)
		count = count + 1
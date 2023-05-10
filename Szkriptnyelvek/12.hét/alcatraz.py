def main():
	cells_num = 600
	cells = []
	for i in range(cells_num):
		cells.append(0)
	
	for i in range(1, cells_num+1):
		for o in range(cells_num):
			if (o+1)%i == 0:
				if(cells[o] == 0):
					cells[o] = 1
				else:
					cells[o] = 0

	print("Nyitott cellák sorszáma: ")
	for i in range(cells_num):
		if(cells[i] == 1):
			print(i+1)


if __name__ == "__main__":
	main()
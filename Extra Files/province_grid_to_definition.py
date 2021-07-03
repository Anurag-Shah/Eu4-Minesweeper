from PIL import Image

start_x = 1971
start_y = 522
def printpx(x, y, i):
	out = im.getpixel((x, y))
	pos = 5000 + i
	print(str(pos) + ";" + str(out[0]) + ";" + str(out[1]) + ";" + str(out[2]) + ";Minesweeper" + str(pos))
with Image.open("provinces.bmp") as im:
	j = 0
	k = 0
	while j < 10:
		k = 0
		while k < 10:
			x = start_x + k * 20
			y = start_y + j * 20
			printpx(x, y, k + 10 * j)
			k += 1
		j += 1

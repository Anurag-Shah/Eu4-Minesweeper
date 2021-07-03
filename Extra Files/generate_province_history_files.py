Text1 = "#"
Text2 = '''
\nadd_core = MSW
owner = MSW
controller = MSW
culture = minesweeper_culture
religion = animism
hre = no
base_tax = 0
base_production = 0
base_manpower = 0
trade_goods = copper\n'''
Text3 = "capital = \""
Text4 = '''"
is_city = yes'''


for i in range (5000, 5100):
	stri = str(i)
	out = Text1 + stri + Text2 + Text3 + stri + Text4
	fname = stri + " - " + stri + ".txt"
	with open(fname, "w") as f:
		f.write(out)
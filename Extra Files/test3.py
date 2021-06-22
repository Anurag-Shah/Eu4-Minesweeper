pg = ""

def add_pg(s1, s2):
	return "m_adj_" + s1 + " = {\n\t" + s2 + "\n}\n"

for i in range(5000, 5100):
	s = ""
	pg += add_pg(str(i), str(s))
#print(pg)
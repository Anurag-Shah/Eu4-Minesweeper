hline1 = 'type = {\n'
hline2 = '\ttype=\"'
# Header object goes here, ex, question_tile
hline3 = '\"\n'
hline4 = '''\tuse_animation=no
\tscale = 0.66
\ttime_duration=300.000
\talways_visible=no
\tvisible_in_all_map_modes=yes\n\n'''
# Object blocks go here    
hline5 = '}\n\n'


oline1 = '\tobject = {\n'
oline2 = '\t\tname=\"'
# Object name goes here
oline3 = '\"\n'
oline4 = '''\t\thidden_on_start=yes
		position={\n\t\t\t'''
# Coords go here, in format 1980.50 0.81 1515.50. +20 on x, -20 on y
oline5 = '''\n\t\t}
\t\trotation={
\t\t\t0.000 0.000 0.000
\t\t}
\t}\n\n'''

#print(hline1 + hline2 + "question_tile" + hline3 + hline4 + oline1 + oline2 + "question_tile_0" + oline3 + oline4 + "1000 0 1000" + oline5 + hline5)

def buildObjBlock(name, index, x, z):
    fname = name + "_" + str(index)
    coords = str(x) + " 0.81 " + str(z)
    return oline1 + oline2 + fname + oline3 + oline4 + coords + oline5

def buildHeaderBlock(name):
    start_x = 1980.5
    start_y = 1515.5
    out = ""
    out += hline1
    out += hline2
    out += name
    out += hline3
    out += hline4
    for i in range(10):
        for j in range(10):
            ind = 10 * i + j
            curr_x = start_x + 20 * j
            curr_y = start_y - 20 * i
            out += buildObjBlock(name, ind, curr_x, curr_y)
    out += hline5
    return out

#print(hline1 + hline2 + "question_tile" + hline3 + hline4 + buildObjBlock("question_tile", 0, 1000, 1000) + hline5)

liste = ["question_tile", "bomb_tile", "flagged_tile", "0_tile", "1_tile", "2_tile", "3_tile", "4_tile", "5_tile", "6_tile", "7_tile", "8_tile"]
out = ""

for item in liste:
    out += buildHeaderBlock(item)

with open("test.txt", "w") as f:
    f.write(out)
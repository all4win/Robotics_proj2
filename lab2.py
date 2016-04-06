from myro import *
init("COM3")

import csv
import math


def euler_path(vertices, adjList, degreeDic, edgeNum):
	global e_Path
	oddD = []
	for node in vertices:
		if degreeDic[node] % 2 == 1:
			oddD.append(node)
	start = vertices[0]
	if len(oddD) != 0:
		start = oddD[0]
	if len(oddD) > 2:
		print "path not found"
		return
	e_Path.append(start)
	findPath(0, adjList, edgeNum)

def findPath(pos, adjList, edgeNum):
	global e_Path
	global e_Edge
	if len(e_Edge) == edgeNum:
		return
	current = e_Path[pos]
	for node in adjList[current]:
		if (current, node) not in e_Edge and (node, current) not in e_Edge:
			print current, node
			e_Edge.append((current, node))
			e_Path.append(node)
			findPath(pos + 1, adjList, edgeNum)
			if len(e_Edge) == edgeNum:
				return
			e_Edge.pop()
			e_Path.pop()


adjList = {}
vertices = []
position = {}
degreeDic = {}
edgeNum = 0

csvReader = csv.reader(open("CS3630_Lab2_Map2.csv", "r"), delimiter = ',')
for row in csvReader:
	if (len(row) == 3):
		vertices.append(row[0])
		position[row[0]] = (float(row[1]), float(row[2]));
		degreeDic[row[0]] = 0
		adjList[row[0]] = []
	if (len(row) == 2):
		edgeNum += 1
		adjList[row[0]].append(row[1])
		adjList[row[1]].append(row[0])
		degreeDic[row[0]] += 1
		degreeDic[row[1]] += 1

e_Path = []
e_Edge = []
euler_path(vertices, adjList, degreeDic, edgeNum)

prev = e_Path[0]
cur_ang = 0
for i in range(len(e_Path) - 1):
        cur = e_Path[i + 1]
	prev_x, prev_y = position[prev]
	cur_x, cur_y = position[cur]
	diff_x = cur_x - prev_x
	diff_y = cur_y - prev_y
	dis = math.sqrt(diff_x ** 2 + diff_y ** 2)
	if diff_x == 0:
            ang = 90
            if diff_y < 0:
                ang += 180
        else:
	    ang = math.atan(diff_y / diff_x) / math.pi * 180
	    if diff_x < 0:
		ang += 180
	ang = int(ang)
	turn_ang = ang - cur_ang
	print turn_ang
	turnBy(turn_ang, "deg")
	cur_ang = ang
	forward(1, dis)
	#turnBy(-ang, "deg")
	prev = cur


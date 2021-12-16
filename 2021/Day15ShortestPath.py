from networkx.algorithms.shortest_paths.generic import shortest_path
from networkx.classes import graph
import LoadInput
import numpy as np
import networkx as nx

example = False

if example:
    lines = LoadInput.LoadLines('Day15ex.txt')
else:
    lines = LoadInput.LoadLines('Day15input.txt')


def parseInput(lines):
    graph = nx.DiGraph()

    value_map = {}

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            value_map[(x,y)] = int(c)
            # add edge to right
            if x < len(line) - 1:
                # add edge to go to next point. Weight is value of next point
                graph.add_edge((x,y), (x+1,y), weight=int(line[x+1]))
                # add edge to come back from next point. Weight is value of current point
                graph.add_edge((x+1,y), (x,y), weight=int(c))
            
            # add edge below
            if y < len(lines) - 1:
                # add edge to go to next point. Weight is value of next point
                graph.add_edge((x,y), (x,y+1), weight=int(lines[y+1][x]))
                # add edge to come back from next point. Weight is value of current point
                graph.add_edge((x,y+1), (x,y), weight=int(c))
    
    return graph, value_map

def part1(graph, value_map, max_point, min_point):
    shortest = nx.shortest_path(graph, source=min_point, target=max_point, weight='weight')

    ans = sum([value_map[point] for point in shortest]) - value_map[(0,0)]
    print("ans:", ans)

def buildFullGraph(value_map):

    max_x = max([key[0] for key, val in value_map.items()])+1
    max_y = max([key[1] for key, val in value_map.items()])+1

    big_map = {}

    for x_inc in range(5):
        for y_inc in range(5):
            for x in range(max_x):
                for y in range(max_y):
                    new_val = value_map[(x,y)]+y_inc+x_inc
                    if new_val > 9:
                        new_val = new_val - 9

                    new_x = x + (max_x*x_inc)
                    new_y = y + (max_y*y_inc)
                    big_map[(new_x, new_y)] = new_val
    
    graph = nx.DiGraph()
    for point, value in big_map.items():
        x = point[0]
        y = point[1]
        # add edge to right
        if x < new_x:
            # add edge to go to next point. Weight is value of next point
            graph.add_edge((x,y), (x+1,y), weight=big_map[(x+1,y)])
            # add edge to come back from next point. Weight is value of current point
            graph.add_edge((x+1,y), (x,y), weight=value)
        
        # add edge below
        if y < new_y:
            # add edge to go to next point. Weight is value of next point
            graph.add_edge((x,y), (x,y+1), weight=big_map[(x, y+1)])
            # add edge to come back from next point. Weight is value of current point
            graph.add_edge((x,y+1), (x,y), weight=value)

    return graph, big_map, (new_x,new_y), (0,0)

#697 too high
graph, value_map = parseInput(lines)
max_point = (len(lines[0])-1, len(lines)-1)
min_point = (0,0)

graph, value_map, max_point, min_point = buildFullGraph(value_map)

part1(graph, value_map, max_point, min_point)
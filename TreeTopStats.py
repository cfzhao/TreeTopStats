#!/usr/bin/env python
import sys
from ete3 import Tree


def tree_topology_statistcs(tree_file, output_file):
    res_dict = {}
    with open(tree_file, "r") as file:
        for i in file:
            i = i.strip()
            tree = Tree(i, format=8)
            topo_id = tree.get_topology_id()
            if topo_id not in res_dict.keys():
                res_dict[topo_id] = [i, 1]
            else:
                res_dict[topo_id][-1] += 1
    res_list = []
    for k, v in res_dict.items():
        res_list.append(v)
    res_list.sort(key=lambda x: x[-1], reverse=True)
    with open(output_file, "a") as file:
        for i in res_list:
            file.write(str(i[-1]) + "\t"+ i[0] + "\n")
            
            
if __name__ == '__main__':
    tree_file_name, output_file_name = sys.argv[1:3]
    tree_topology_statistcs(tree_file=tree_file_name, output_file=output_file_name)

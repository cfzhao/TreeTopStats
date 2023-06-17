# TreeTopStats
#### Statistics percentage of different topologies among phylogenetic trees
#### 统计系统发育树不同拓扑结构所占百分比

# Requirement
ETE3=3.1.2

# Quick install and start
#### !!!Before starting, you must to ensure that all trees have the same root defined.
#### 统计之前，需要将所有的树定相同的根
```shell
pip install ete3==3.1.2 (or conda install ete3=3.1.2)
git clone https://github.com/cfzhao/TreeTopStats.git
cd TreeTopStats
python tree_topology_statistics.py example/trees.input ./treetop_stats.output
```

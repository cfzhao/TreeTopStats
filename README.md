# TreeTopStats
### Statistics percentage of different topologies among phylogenetic trees
#### 统计系统发育树不同拓扑结构所占百分比

# Requirement
#### ETE3=3.1.2

# Quick install and start
### !!!Before starting, you must to ensure that all trees have the same root defined (newick_utils may be a good tool to reroot).
#### 统计之前，需要将所有的树定相同的根 (newick_utils软件可以用来定根)
```shell
$pip install ete3==3.1.2 (or conda install ete3=3.1.2)
$git clone https://github.com/cfzhao/TreeTopStats.git
$cd TreeTopStats
$python tree_topology_statistics.py example/trees.input ./treetop_stats.output
```

# Input and Output files
### The input file look like this: Each raw represents a phylogenetic tree (in newick format).
```shell
$cat example/trees.input
((((B,A),B),C));
(((B,(B,A)),(C,A)));
((C,((B,(A,B)),A)));
(((((A,C),A),B),B));
((((((B,A),A),B),A),C));
((((A,B),A),C));
......
```

#### The output file look like this: The first column represents the frequency, and the second column represents the corresponding topology.
```shell
$cat treetop_stats.output
15  (((A,B),C));
10  ((((B,A),B),C));
9  ((((A,B),A),C));
7  ((((A,B),C),B));
4  ((C,((B,(A,B)),A)));
4  ((C,(A,((B,A),A))));
......
```

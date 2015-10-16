#! /usr/bin/env python
from __future__ import print_function
import argparse
from ete2 import Tree
import sys

parser = argparse.ArgumentParser()
parser.add_argument('treefile1')
parser.add_argument('treefile2')

args = parser.parse_args()

t1 = None
t2 = None
try:
    t1 = Tree(args.treefile1)
    t2 = Tree(args.treefile2)

except Exception as e:
    print('Problems reading tree file(s):\n' + str(e), file=sys.stderr)

try:
    rf, rf_max, x1, x2, x3, x4, x5 = t1.robinson_foulds(t2, unrooted_trees=True)
    print(rf)
except Exception as e:
    print('Error when computing the Robinson-Foulds distances:\n' + str(e), file=sys.stderr)
    


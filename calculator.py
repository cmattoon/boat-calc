#!/usr/bin/env python
from boatstuff.formulae import *
from boatstuff.funcs import *
imp = {
    'volume': 1800,
    'beam': 18,
    'length': {
        'overall': 80
        },
    'sa': 50
    }
"""
This dict will have the measurements in metric.
"""
metric = to_metric(imp)


"""
Set `pc` to the result of `prismatic_coef(V, S, L)`
"""
pc = prismatic_coef(metric['volume'], metric['sa'], metric['length']['overall'])

print("Prismatic coef is: %s" % (str(green(pc))))

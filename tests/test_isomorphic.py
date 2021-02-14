#!/usr/bin/env python

import sys
import copy
from pynauty import isomorphic, delete_random_edge, Version
from data_graphs import graphs


if __name__ == '__main__':
    print(Version())
    print('Python version: ' + sys.version)
    print('Testing pynauty.{isomorphic(),certificate()}')
    print('Starting ...')
    passed = 0
    failed = 0
    for gname, g, numorbit, grpsize, gens in graphs:
        print('%-37s ...' % gname, end=' ')
        sys.stdout.flush()
        x =copy.deepcopy(g)
        if isomorphic(g,x):
            print('OK')
            passed += 1
        else:
            print('failed')
            failed +=1
        e = delete_random_edge(x)
        print('    removed random edge {:<13} ...'.format(str(e)), end=' ')
        if not isomorphic(g,x):
            print('OK')
            passed += 1
        else:
            print('failed')
            failed +=1
    print('... done.')
    if failed > 0:
        print('passed = %d   failed = %d' % (passed, failed))
    else:
        print('All tests passed.')


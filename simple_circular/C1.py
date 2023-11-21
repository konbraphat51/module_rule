"""
Simple circular import
"""

from C2 import pc2

def pc1():
    print('pc1')
    pc2()
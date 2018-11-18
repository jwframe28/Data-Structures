#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size



class Node(object):
    def __init__(self,key,left,right):
        self.key = key
        if left == -1:
            self.left = None
        else:
            self.left = left
        if right == -1:
            self.right = None
        else:
            self.right = right



class BT(object):
    def __init__(self,tree):
        self._tree = []
        for i in range(len(tree)):
            self._tree.append(Node(tree[i][0],tree[i][1],tree[i][2]))
        self.broken = False


    def NotBinarySearchTree(self, rootNode, minVal, maxVal):
        if rootNode is None:
            pass
        elif self._tree[rootNode].key < minVal or self._tree[rootNode].key > maxVal:
            self.broken = True

        else:
            self.NotBinarySearchTree(self._tree[rootNode].left, minVal, self._tree[rootNode].key-1)
            self.NotBinarySearchTree(self._tree[rootNode].right, self._tree[rootNode].key+1, maxVal)

def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if not tree:
        print('CORRECT')

    else:
        binary_tree = BT(tree)
        INT_MAX = 4294967296 # might wanna change eventually to -inf
        INT_MIN = -4294967296
        binary_tree.NotBinarySearchTree(0,INT_MIN,INT_MAX)
        if binary_tree.broken: # if not false, or none then
            print("INCORRECT")
        else:
            print("CORRECT")

threading.Thread(target=main).start()

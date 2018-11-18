# python3

import math
import sys
# import heapq

class HeapBuilder(object):
    def __init__(self,size):
        self._data = []
        self.size = size
        self.n = size
        for i in range(size):
#             self._data.append([i,0])
            self._data.append([i,0])

    def Parent(self,i):
        return max(0,math.floor((i-1)/2))
    
    def LeftChild(self,i):
        return (2*i)+1
    
    def RightChild(self,i):
        return (2*i)+2


    def SiftDown(self,i):
        minIndex = i
        l = self.LeftChild(i)
        r = self.RightChild(i)

        if l < self.size: 
            if ((self._data[l][1] < self._data[minIndex][1]) or (self._data[l][1] == self._data[minIndex][1] and self._data[l][0] < self._data[minIndex][0])):
                minIndex = l

        if r < self.size:
            if ((self._data[r][1] < self._data[minIndex][1]) or (self._data[r][1] == self._data[minIndex][1] and self._data[r][0] < self._data[minIndex][0])):
                minIndex = r
    
        if i != minIndex:
            hi = self._data[i]
            hm = self._data[minIndex]
            self._data[i] = hm
            self._data[minIndex] = hi
            self.SiftDown(minIndex)
            self.SiftDown(i)


    def CompareWorker(self, worker1, worker2):
        if worker1[1] != worker2[1]:
            return worker1[1] < worker2[1]
        else:
            return worker1[0] < worker2[0]

    def SiftUp(self, i):
        while i > 0 and self.CompareWorker(self._data[i], self._data[self.Parent(i)]):
            self._data[i], self._data[self.Parent(i)] = self._data[self.Parent(i)], self._data[i]
            i = self.Parent(i)

        
    def GenerateSwaps(self):
        for i in range(math.floor(self.size/2)-1,-1,-1):
            self.SiftDown(i)
        
    def ChangePriority(self, index, priority):
        old_p = self._data[index][1]
        self._data[index] = (self._data[index][0], priority)
        if priority < old_p:
            self.SiftUp(index)
        else:
            self.SiftDown(index)

        self.SiftDown(index)
        
    
class JobQueue:

    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def assign_jobs(self):
        pointer = 0
        heap = HeapBuilder(self.num_workers)
        for i in range(len(self.jobs)):
            print(heap._data[0][0],heap._data[0][1])
            heap._data[0][1] = heap._data[0][1]+self.jobs[i]
            heap.SiftDown(0)


    def solve(self):
        self.read_data()
        self.assign_jobs()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()


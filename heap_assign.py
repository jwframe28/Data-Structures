# python3 
# python3

# import math
import sys


class HeapBuilder(object):
    def __init__(self,size):
#         self._swaps = []
        self._data = []
        self.size = size
        for i in range(size):
            self._data.append([i,0])

    def Parent(self,i):
#         return max(0,math.floor((i-1/2)))
        # return max(0,math.floor((i-1)/2))
        return max(0,int((i-1)/2))
        ### undo max here? figure out how to sort things properly here
    
    def LeftChild(self,i):
        return (2*i)+1
    
    def RightChild(self,i):
        return (2*i)+2

    def SiftDown(self,i):
        minIndex = i
        l = self.LeftChild(i)
        if l < self.size and self._data[l][1] < self._data[minIndex][1]:
            minIndex = l
            
        r = self.RightChild(i)

        if r < self.size and self._data[r][1] < self._data[minIndex][1]:
            minIndex = r
    
        if i != minIndex:
            hi = self._data[i] # make sure we're not passing by reference...
            hm = self._data[minIndex]
#             self._swaps.append((i,minIndex))
            self._data[i] = hm
            self._data[minIndex] = hi
            self.SiftDown(minIndex)


    def SiftUp(self,i):
        while  i > 0 and self._data[self.Parent(i)] > self._data[i]:
            hi = self._data[i]
            hp = self._data[self.Parent(i)]
#             self._swaps.append((self.Parent(i),i))
            self._data[self.Parent(i)] = hi
            self._data[i] = hp
            i = self.Parent(i)
        
    def GenerateSwaps(self):
        # for i in range(math.floor(self.size/2)-1,-1,-1):
        for i in range(int(self.size/2),-1,-1):
            self.SiftDown(i)

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        # self.num_workers = 2
        # m = 5
        # self.jobs = [1,2,3,4,5]
        # self.finalTuple = []
        assert m == len(self.jobs)

    def assign_jobs(self):
        pointer = 0
        heap = HeapBuilder(self.num_workers)
        for i in range(len(self.jobs)): # also can use num_workers here

            if pointer <= self.num_workers-1: # once pointer becomes N we end
                # self.finalTuple.append((pointer,0))
                a = pointer
                heap._data[pointer][1] = heap._data[pointer][1]+self.jobs[i]
                # print(self.finalTuple[i][0],self.finalTuple[i][1])
                print(pointer,0)
                pointer += 1
            else:

                heap.GenerateSwaps()
                # self.finalTuple.append((heap._data[0][0],heap._data[0][1]))
                a = heap._data[0][0]
                b = heap._data[0][1]
                heap._data[0][1] = heap._data[0][1] + self.jobs[i]
                pointer += 1
                # print(self.finalTuple[i][0],self.finalTuple[i][1])
                print(a,b)

            

    def solve(self):
        self.read_data()
        self.assign_jobs()
        # self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()


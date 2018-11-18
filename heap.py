# python3
import math


class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []


    def Parent(self,i):
        return max(0,math.floor((i-1/2)))
    
    def LeftChild(self,i):
        return (2*i)+1
    
    def RightChild(self,i):
        return (2*i)+2

    def SiftDown(self,i):
        minIndex = i
        l = self.LeftChild(i)
        if l < self.size and self._data[l] < self._data[minIndex]:
            minIndex = l
            
        r = self.RightChild(i)
        if r < self.size and self._data[r] < self._data[minIndex]:

            minIndex = r
    
        if i != minIndex:

            hi = self._data[i]
            hm = self._data[minIndex]

            self._swaps.append((i,minIndex))
            self._data[i] = hm
            self._data[minIndex] = hi
            self.SiftDown(minIndex)

    def ReadData(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]
        assert n == len(self._data)
        # self._data = [1,4,3,5,6,7]
        # self._data = [5,4,3,2,1]

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])
            


    def SiftUp(self,i):
        while  i > 0 and self._data[self.Parent(i)] > self._data[i]:
            hi = self._data[i]
            hp = self._data[self.Parent(i)]
            self._swaps.append((self.Parent(i),i))
            self._data[self.Parent(i)] = hi
            self._data[i] = hp
            i = self.Parent(i)

        
    def GenerateSwaps(self):
        
        self.size = len(self._data)
        for i in range(math.floor(self.size/2)-1,-1,-1):
            heap_builder.SiftDown(i)

                

    def Solve(self):
        self.ReadData()
        self.GenerateSwaps()
        self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()

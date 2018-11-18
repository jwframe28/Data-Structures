import math
import sys

# A = [3,2,1,4,5,6]
# A = [6,8,3,4,3,5,7,8,2,5,33,5,86,56]
# A = [1,2,3,4,5]
class HeapBuilder(object):   ###### JUST MAKE ONE HEAP OBJECT  SPECIFICALLY FOR THIS SO WE CAN CALL ONCE AND EDIT LATER
    def __init__(self,size): #### COULD ALSO PASS NUM WORKERS
        self._swaps = []
        self._data = [] # our inputs are going to be 0....n
        # self.size = len(self._data)
        self.size = size
        # self._locations = dict[zip(data_list)]
        for i in range(size):
            self._data.append((i,0))
#         self._parent = [i in range(len(data_list))]

# iterate SiftUp(i) ------ self._data[i][1] + ..... etc....


    def Parent(self,i):
        return max(0,math.floor((i-1/2)))
    
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
            self._swaps.append((i,minIndex))
            self._data[i] = hm
            self._data[minIndex] = hi
            self.SiftDown(minIndex)


    def SiftUp(self,i):
        while  i > 0 and self._data[self.Parent(i)] > self._data[i]:
            hi = self._data[i]
            hp = self._data[self.Parent(i)]
            self._swaps.append((self.Parent(i),i))
            self._data[self.Parent(i)] = hi
            self._data[i] = hp
            i = self.Parent(i)
        
    def GenerateSwaps(self):
        # self.size = len(self._data)
        for i in range(math.floor(self.size/2)-1,-1,-1):
            self.SiftDown(i)



class Node(object):

    def __init__(self):
        self.time = 0

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        self.finalTuple = []
        self.Nodes = [Node() for element in range(0,self.num_workers)] # we 
        self.Times = [element.time for element in self.Nodes]
        self.Empty = [True]*self.num_workers
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.finalTuple)):
            print(self.finalTuple[i][0],self.finalTuple[i][1])

    def assign_jobs(self):
        pointer = 0
        heap = HeapBuilder(self.num_workers)
        for i in range(len(self.jobs)):
            
            if self.Empty[self.num_workers-1] is True:
                ind = pointer 
                self.finalTuple.append((ind,self.Nodes[ind].time))
                self.Nodes[ind].time = self.Nodes[ind].time + self.jobs[i] # newly added
                self.Times[ind] = self.Times[ind] + self.jobs[i]
                heap._data[ind][1] = heap._data[ind][1] + self.jobs[i]
                self.Empty[ind] = False
                pointer += 1


            else:

                A = self.jobs[i]

                heap.GenerateSwaps()
                self.min = heap._data[0][1]

                B = heap._data[0][0]

                # self.finalTuple.append((B,self.Nodes[B].time))
                self.finalTuple.append((B,self.min))

                self.Nodes[B].time = self.Nodes[B].time + A # also need to update the Times table, right?
                self.Times[B] = self.Times[B]+A

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()


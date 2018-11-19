# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        # self.elems = []
        self.elems = [None]*bucket_count

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return (ans % self.bucket_count + self.bucket_count) % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):

        self.ind = -1
        try:
            hashMap = self._hash_func(query.s) # will FAIL WHEN THERE IS NO query.s -- 
            iter1 = 0
            for element in self.elems[hashMap]:
                if element == query.s:
                    self.ind = self.elems[hashMap]
                    loc = iter1
                iter1 += 1

        except:
            self.ind = -1

        if query.type == "check":
            if self.elems[query.ind] == None:
                print(' ')

            else:
                self.write_chain(cur for cur in reversed(self.elems[query.ind]))

        else:
            if query.type == 'find':
                self.write_search_result(self.ind != -1)
                

            elif query.type == 'add':
                if self.ind == -1 and self.elems[hashMap] == None:
                    self.elems[hashMap] = [query.s]
                elif self.ind == -1 and self.elems[hashMap] != None:
                    self.elems[hashMap].append(query.s)

                else: # then it was found 
                    pass

            else: # del functionality
                # does it exist? then delete.
                if self.ind != -1:
                    del self.elems[hashMap][loc]
                    if len(self.elems[hashMap]) == 0:
                        self.elems[hashMap] = None
                else:
                    pass

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()

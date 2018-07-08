
class DefineIter:
    def __init__(self,length):
        self.length = length
        self.data = range(self.length)
        self.index=0

    def __iter__(self):
        return self



    def next(self):
        if self.index >=self.length:
            # return None
            raise StopIteration


        d = self.data[self.index]

        self.index =self.index + 1
        return d



a = iter(DefineIter(10))

for i in a:
    print(i)



class Counter:
    def __init__(self):
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        i = self.index
        if i < 10:
            self.index += 1
            return i
        else:
            raise StopIteration

# counter = iter(Counter())
# print(next(counter))
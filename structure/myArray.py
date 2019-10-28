class Array(object):
    def __init__(self, size=32):
        self.size = size
        self.iterm = [None] * self.size

    def __len__(self):
        return self.size


    def __setitem__(self, key, value):
        if key >= self.size:
            newsize = (key + 12)
            newarray = [None] * newsize
            for i in range(self.__len__()):
                newarray[i] = self.iterm[i]
            self.iterm = newarray
            self.size = newsize
            del newarray
        self.iterm[key] = value

    def __getitem__(self, key):
        if key >= 0 and key <= self.size:
            print('ddd')
            return self.iterm[key]
        return None

    def clear(self, value=None):
        for i in range(len(self.iterm)):
            self.iterm[i] = value

    def __iter__(self):
        for i in self.iterm:
            yield i
def testArray():
    a = Array()
    a[0]= 1
    a[10] = 1
    for i in a:
        print(i)

testArray()


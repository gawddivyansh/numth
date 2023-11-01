mod = 7

def setModulo(modu):
    mod = modu

class modInteger:
    def __init__(self, num):
        self.num = num%mod
        self.mod = mod
 
    # adding two objects
    def __add__(self, o):
        assert o.num == self.num
        return modInteger(self.num + o.num)

    # adding two objects
    def __sub__(self, o):
        assert o.num == self.num
        return modInteger(self.num - o.num)%self.mod
    
    # adding two objects
    def __mul__(self, o):
        assert o.num == self.num
        return modInteger(self.num * o.num)
    
    # adding two objects
    def __pow__(self, exp):
        for i in range(exp):
            self.num = (self.num*self.num)%mod

    # adding two objects
    def __lt__(self, o):
        assert o.num == self.num
        return self.num < o.num

    # adding two objects
    def __gt__(self, o):
        assert o.num == self.num
        return self.num > o.num
    
    # adding two objects
    def __le__(self, o):
        assert o.num == self.num
        return self.num <= o.num
    
    # adding two objects
    def __ge__(self, o):
        assert o.num == self.num
        return self.num >= o.num
    
    # adding two objects
    def __eq__(self, o):
        assert o.num == self.num
        return self.num == o.num

    # adding two objects
    def __ne__(self, o):
        assert o.num == self.num
        return self.num != o.num
    

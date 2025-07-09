from graph import draw_graph



class Var:
    
    def __init__(self, data,_child=(), _op='', chng= 0):
        self.data = data
        self._pre = set(_child)
        self._op = _op
        self.chng = chng
        
        #Functions
        self._back = lambda: None
        
    
    def __repr__(self):
        return f'Value: {self.data}'
    
    
    
    def __add__(self, other):
        other = other if isinstance(other, Var) else Var(other)
        out = Var(self.data + other.data, (self,other), '+')

        
        def _back():
            self.chng += out.chng
            other.chng += out.chng
        out._back = _back
        
        return out
    
    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        other = other if isinstance(other, Var) else Var(other)
        
        out = Var(self.data * other.data,(self,other), '*')
        
        def _back():
            self.chng += other.data * out.chng
            other.chng += self.data * out.chng
        out._back = _back
        
        return out
    
    def relu(self):
        out = Var(0 if self.data < 0 else self.data, (self,), 'ReLU')

        def _back():
            self.chng += (out.data > 0) * out.chng
        out._back = _back
        return out
    
    def __rmul__(self, other): 
        out = self * other
        return out
    
    def __pow__(self, other):
        assert isinstance(other, (int, float)), "power must be int/float"
        out = Var(self.data**other, (self,), f'**{other}')

        def _back():
            self.chng += (other * self.data**(other-1)) * out.chng
        out._back = _back
        
        return out
    
    
    
    def __neg__(self):
        return self * -1
    
    
    
    def __sub__(self, other):
        out = self + (-other)
        return out
    def __rsub__(self, other):
        out = self + (-other)
        return out
    
    
    def __truediv__(self, other): 
        out = self * other**-1
        return out
    def __rtruediv__(self, other): 
        out = other * self**-1
        return out

    
    
    def back(self):
        topo = []
        visited = set()
        def build_topo(v):
            if v not in visited:
                visited.add(v)
                for child in v._pre:
                    build_topo(child)
                topo.append(v)
        build_topo(self)


        self.chng = 1
#         print(topo)
        for v in reversed(topo):
            v._back()

            
            
    
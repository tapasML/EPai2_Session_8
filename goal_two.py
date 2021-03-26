import math
from goal_one import *
from functools import reduce


class Polygons:
    
    ''' Iterable'''
    
    def __init__(self, m, R):
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._R = R       
    
    def __repr__(self):
        return f'Polygons(m={self._m}, R={self._R})'  
    
    
    def __iter__(self):
        return self.PolygonIter(self._m, self._R)  
    
    
    # Please note: this method needs to be uncommented to use subscript indexing on its objects.
    # And if it is uncommented, the class becomes an Iterator
    '''def __getitem__(self, index):       
        _temp = None        
        _iter = iter(self)        
        for i in range(index+1):
            _temp = next(_iter)
        return _temp'''
    
    
    @property
    def max_efficiency_polygon(self):       
        return max(iter(self), key=lambda p: p.area/p.perimeter)       
    

    class PolygonIter:
        
        ''' Iterate over the Polygons'''
    
        def __init__(self, max_edges, radius):       
            self._edges = 3
            self._max_edges = max_edges
            self._radius = radius
        
        def __len__(self):
            return self._max_edges - 2
        
        def __iter__(self):
            return self
    
        def __next__(self):
             if self._edges > self._max_edges:                 
                 raise StopIteration
             else:
                 poly = Polygon (self._edges, self._radius)
                 self._edges += 1
             return poly
         
      
        

###########   test   ############################

#n=10
#cp = Polygons(n,7)
##print('subscript test')
#print('getitem called ', cp[1])
#print('iterator test')
#for item in cp:
#    print(item)
#print('getitem called ', cp[2])
#print('max efficiency ; ', cp.max_efficiency_polygon)


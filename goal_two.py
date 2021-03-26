import math
from goal_one import *
from functools import reduce


class Polygons:
    def __init__(self, m, R):
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._R = R       
    
    def __repr__(self):
        return f'Polygons(m={self._m}, R={self._R})'  
    
    
    def __iter__(self):
        return self
    
    def __getitem__(self, index): 
        
        ''' iterate over items till reach desired index'''        
        
        _temp = None        
        _iter = self.PolygonIter(self._m, self._R)        
        for i in range(index+1):
            _temp = next(_iter)
        return _temp
    
    
    @property
    def max_efficiency_polygon(self):               
        
        # following is sorting using loop. 
        # This implementation does not use list
        '''
        _result = None 
        for i in range(0, self._m - 2):
            #_temp = next(_iter)
            temp = self[i]
            if _result is None:
                _result = temp
            else:
                if temp.area/temp.perimeter > _result.area/_result.perimeter:
                    _result = temp
                else:
                    pass            
        return _result
        '''   
        
        # following done using  'sorted'        
        sorted_polygons = sorted(iter(self.PolygonIter(self._m, self._R)), 
                                 key=lambda p: p.area/p.perimeter,
                                reverse=True)
        return sorted_polygons[0] 
    

    class PolygonIter:
        
        ''' Iterate iver the Polygons'''
    
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

n=11
cp = Polygons(n,7)
print('getitem called ', cp[2])
print('max efficiency ; ', cp.max_efficiency_polygon)


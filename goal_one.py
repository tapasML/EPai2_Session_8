import math
from functools import reduce

class Polygon:

    '''A regular strictly convex polygon is a polygon that has the following characteristics:
      all interior angles are less than 180
      all sides have equal length'''

    def __init__(self, numedges : int, radius : float):

        ''' constructor'''
        
        if not isinstance(numedges, int):
            raise ValueError('Polygon: number of vertices must be integer')
        if numedges < 3:
            raise ValueError('Polygon: number of vertices must be >= 3')
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise ValueError('Polygon: radius must be integer or float')
        if radius <= 0:
            raise ValueError('Polygon: radius must be > 0')

        self._numedges = numedges
        self._radius = radius  
        self._interior_angle = None
        self._edge_length = None 
        self._apothem = None
        self._area = None
        self._perimeter = None
       
        
     
    @property
    def num_edges(self):
        return self._numedges
    
    @property
    def num_vertices(self):
        return self._numedges
    
    @property
    def radius(self):
        return self._radius
    
    @property
    def interior_angle(self):
        if self._interior_angle is not None:
            return self._interior_angle
        else:
            #print('calculate interior_angle')
            self._interior_angle = (self._numedges - 2) * 180 / self._numedges
            return self._interior_angle
    
    @property
    def edge_length(self):  
        if self._edge_length is not None:
            return self._edge_length
        else:
            #print('calculate edge_length')
            self._edge_length = round(2 * self._radius * math.sin(math.pi / self._numedges), 4)
            return self._edge_length
    
    @property
    def apothem(self):
        if self._apothem is not None:
            return self._apothem
        else:
            #print('calculate apothem')
            self._apothem = round(self._radius * math.cos(math.pi / self._numedges), 4)
            return self._apothem
    
    @property
    def area(self):
        if self._area is not None:
            return self._area
        else:
            #print(f'calculate area for {self._numedges}' )
            self._area = round(self._numedges / 2 * self.edge_length * self.apothem, 4)
            return self._area
    
    @property
    def perimeter(self):
        if self._perimeter is not None:
            return self._perimeter
        else:            
            #print('calculate perimeter')
            self._perimeter = round(self._numedges * self.edge_length, 4)
            return self._perimeter
    
   
    def __repr__(self):
        return f'{self.__class__.__name__}(numedges={self._numedges}, radius={self._radius})'
    

    def __eq__(self, other)-> bool:

        ''' implements equality comparison'''

        if isinstance(other, Polygon):
            return self._numedges == other._numedges and self._radius == other._radius
        else:
            return False
        

    def __gt__(self, other)-> bool:

        ''' implements > comparison'''

        if isinstance(other, Polygon):
            return self._numedges > other._numedges
        else:
            return False
        
        
#############  test  ###############


#poly1= Polygon(3, 10)
#print(poly1)

#print('area= ',poly1.area)
#print('\n')
#print('area= ',poly1.area)
#print('interior_angle= ',poly1.interior_angle)


def test_polygon():
    abs_tol = 0.001
    rel_tol = 0.001
    
    try:
        p = Polygon(2, 10)
        assert False, ('Creating a Polygon with 2 sides: '
                       ' Exception expected, not received')
    except ValueError:
        pass
                       
    n = 3
    R = 1
    p = Polygon(n, R)
    assert str(p) == 'Polygon(numedges=3, radius=1)', f'actual: {str(p)}'
    assert p.num_vertices == n, (f'actual: {p.count_vertices},'
                                   f' expected: {n}')
    assert p.num_edges == n, f'actual: {p.count_edges}, expected: {n}'
    assert p.radius == R, f'actual: {p.circumradius}, expected: {n}'
    assert p.interior_angle == 60, (f'actual: {p.interior_angle},'
                                    ' expected: 60')
    n = 4
    R = 1
    p = Polygon(n, R)
    assert p.interior_angle == 90, (f'actual: {p.interior_angle}, '
                                    ' expected: 90')
    assert math.isclose(p.area, 2, 
                        rel_tol=abs_tol, 
                        abs_tol=abs_tol), (f'actual: {p.area},'
                                           ' expected: 2.0')
    
    assert math.isclose(p.edge_length, math.sqrt(2),
                       rel_tol=rel_tol,
                       abs_tol=abs_tol), (f'actual: {p.edge_length},'
                                          f' expected: {math.sqrt(2)}')
    
    assert math.isclose(p.perimeter, 4 * math.sqrt(2),
                       rel_tol=rel_tol,
                       abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                          f' expected: {4 * math.sqrt(2)}')
    
    assert math.isclose(p.apothem, 0.707,
                       rel_tol=rel_tol,
                       abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                          ' expected: 0.707')
    p = Polygon(6, 2)
    assert math.isclose(p.edge_length, 2,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 1.73205,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 10.3923,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 12,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.interior_angle, 120,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    
    p = Polygon(12, 3)
    assert math.isclose(p.edge_length, 1.55291,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 2.89778,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 27,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 18.635,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.interior_angle, 150,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    
    p1 = Polygon(3, 10)
    p2 = Polygon(10, 10)
    p3 = Polygon(15, 10)
    p4 = Polygon(15, 100)
    p5 = Polygon(15, 100)
    
    assert p2 > p1
    assert p2 < p3
    assert p3 != p4
    assert p1 != p4
    assert p4 == p5
    
    
#test_polygon()
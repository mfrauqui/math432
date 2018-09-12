import inspect
import math


class Lecture2Err(Exception):
    '''
    raise this exception to obtain EXCEPTION DEFINED
    ex:
        raise Lecture2Err(string_containing_the_error)
    '''
    pass


class Point(object):
    '''
        define class point in 2-D space given a list of coordinates
        raise an exception Lecture2Err if coordinates are not numeric
    '''
    coordinates = [0, 0]

    def __init__(self, coordinates):
        if(self.is2D(coordinates) and self.isnumeric(coordinates)):
            for i, j in enumerate(coordinates):
                self.coordinates[i] = j
        self.test_class()
        ########################
    # def __str__(self):
    #   return "("+self.coordinates[0]+","+self.coordinates[1]+")"

    def test_class(self):
        assert 'coordinates' in dir(
            self), self.__class__.__name__+' -> miss attribute coordinates'
        for c in self.coordinates:
            assert (not isinstance(c, int) or not isinstance(c, float)
                    ), self.__class__.__name__+' -> coordinate is not numeric'
        assert len(self.coordinates) == 2, self.__class__.__name__ + \
            ' -> did not raise any exception to test 2D space'

    ########################
    def is2D(self, coordinates):
        # print("Cordinates", coordinates, type(coordinates))
        if (not isinstance(coordinates, list) or len(coordinates) != 2):
            raise Lecture2Err('not a 2D space')
        else:
            return coordinates

    def isnumeric(self, coordinates):
        for c in coordinates:
            if(not isinstance(c, int) and not isinstance(c, float)):
                raise Lecture2Err('coordinates are not numeric')
        return coordinates
    ########################


class Shape(object):
    '''
        define class Shape given a list of 2D points of type Point
        raise an exception Lecture2Err if a point is not Point (create ispoint())
    '''
    points = []

    def __init__(self, points):
        if not (isinstance(points, list)):
            raise Lecture2Err('points is not a list of Point')
        ########################
        for point in points:
            points.append(self.ispoint(point))
    #     ########################
        self.test_class()

    def test_class(self):
        assert 'points' in dir(
            self), self.__class__.__name__+' -> miss attribute points'
        for p in self.points:
            assert (isinstance(p, Point)), self.__class__.__name__ + \
                ' -> point is not type Point'

    ########################
    def ispoint(self, pp):
        p = Point(pp)
        if not(isinstance(p, Point)):
            raise Lecture2Err('point is not an instance of Point')
        else:
            return p
    # def isnumeric(self,c):
    #     pass
    ########################

########################
# Define classes Segment, Circle, Triangle
# define methods calc_perimeter(), calc_area()
########################
# definition classes here


class Circle(Point):
    '''
    Circle is defined by 1 Point: center.
    Circle needs to define radius. radius must be numeric (create isnumeric()), otherwise raise an exception Lecture2Err
    '''
    center = None
    radius = 0

    def __init__(self, center, radius):
        self.center = Point.__init__(self,center)
        if(self.isnumeric(radius)):
            self.radius = radius;
            # if not (isinstance(center,Point)):
            #   raise Lecture2Err('center is not a  Point')
            # if self.isnumeric(radius):
            #   self.center = Point.__init__(self,center)
            # code here
            ########################
        self.test_class()

    def test_class(self):
        for i in ['checkNpoints', 'calc_area', 'calc_perimeter']:
            assert i in dir(self), self.__class__.__name__ + \
                ' -> Missing {}.'.format(i)
        self.checkNpoints(self.__class__.__name__, 1)
        assert len(self.points) == 1, self.__class__.__name__ + \
            ' -> Circle should be defined by 1 Points: the center. Plus the radius. '

    ########################
    # other methods here
    def isnumeric(self,radius):
        #Point.isnumeric(self,center);
        if (not isinstance(radius, int) and not isinstance(radius, float)):
          raise Lecture2Err('radius is not a  numeric value')
        else:
          return True;
    ########################


class Segment(object):
    ''' 
    Segment is defined by 2 Points. 
    '''

    def __init__(self, points):
        ########################
        # code here
        ########################
        self.test_class()

    def test_class(self):
        for i in ['checkNpoints', 'calc_area', 'calc_perimeter']:
            assert i in dir(self), self.__class__.__name__ + \
                ' -> Missing {}.'.format(i)
        self.checkNpoints(self.__class__.__name__, 2)
        assert len(self.points) == 2, self.__class__.__name__ + \
            ' -> Segment should be defined by 2 Points.'

    ########################
    # other methods here
    ########################


class Triangle(object):
    ''' 
    Triangle is defined by 3 Points. 
    '''

    def __init__(self, points):
        ########################
        # code here
        ########################
        self.test_class()

    def test_class(self):
        for i in ['checkNpoints', 'calc_area', 'calc_perimeter']:
            assert i in dir(self), self.__class__.__name__ + \
                ' -> Missing {}.'.format(i)
        self.checkNpoints(self.__class__.__name__, 3)
        assert len(self.points) == 3, self.__class__.__name__ + \
            ' -> Triangle should be defined by 3 Points.'

    ########################
    # other methods here
    ########################


if __name__ == "__main__":
    tests = [
        'p = Point(["1"])',
        'p = Point(["1","2"])',
        'p = Point([1])',
        'p = Point([1,2,3])',
        'p = Point([1,2])',
        'p = Point([1.,2.])',
        'p = Shape(1)',
        'p = Shape([1])',
        'p = Shape(Point([1,1]))',
        'p = Shape([Point([1,1])])',
        'p = Shape([Point([1,1]),Point([2,1])])',
        'p = Circle([1],1)',
        'p = Circle([Point([1,2]),Point([2,1])],1)',
        'p = Circle(Point([1,2]),1)',
        'p = Circle([Point([1,2])],"1")',
        'p = Circle([Point([1,2])],1)',
        'p = Circle([Point([0,0])],2)\nprint(p.calc_area())',
        'p = Circle([Point([2,1])],3)\nprint(p.calc_perimeter())',
        'p = Segment(Point([1,1]))',
        'p = Segment([Point([1,1])])',
        'p = Segment([Point([1,1]),Point([2,1])])',
        'p = Segment([Point([1,1]),Point([2,1])])\nprint(p.calc_area())',
        'p = Segment([Point([1,1]),Point([2,1])])\nprint(p.calc_perimeter())',
        'p = Triangle(Point([1,1]))',
        'p = Triangle([Point([1,1])])',
        'p = Triangle([Point([0,0]),Point([20,0]),Point([10,10])])',
        'p = Triangle([Point([0,0]),Point([20,0]),Point([10,10])])\nprint(p.calc_area())',
        'p = Triangle([Point([0,0]),Point([20,0]),Point([10,10])])\nprint(p.calc_perimeter())',
    ]
    for t in tests:
        try:
            print(t, end='\t-> ')
            print(exec(t), end=' ')  # class is statement and not expression
            # you need to exec, not to eval
            print("-> NO ERROR")
        except (AssertionError) as err:
            print("ERROR: ", err)
        except Lecture2Err as err:
            print("EXCEPTION DEFINED:", err)

import numpy

def multiply(coefficient, v):        #scalar multiplification
    return map((lambda x : x * coefficient), v)

def orthogonal_projection(plane, points, d, n):
    unit_normal_scalar = 1 / numpy.sqrt(numpy.dot(plane, plane))
    distance = (numpy.dot(plane, points) + d) * unit_normal_scalar
    w=[] #unit normal
    w = multiply(unit_normal_scalar, plane)
    return list(map((lambda x, y : x - distance * y), points, w))

def main():
    n = int(input("Enter the amount of vertices of the polygonal object: "))
    print("Input coordinates of points: ")
    points = numpy.array([float(x) for x in input().split()]) 
    points = points.reshape(n, 3)
    print("Input a, b, c, d (ax+by+cz+d=0): ")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    d = float(input("d = "))
    plane = numpy.array([a, b, c])
    print("The coordinates of the projected polygonal onto the plane is: ")
    for i in range (n):
        print(numpy.array(orthogonal_projection(plane, points[i], d, n)));

if __name__ == "__main__": main()

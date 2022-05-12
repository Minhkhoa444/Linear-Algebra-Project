import numpy
def gs_coefficient(v1, v2):          #calculate the projection scalar <v1, v2>/<v1, v1>
    return numpy.dot(v2, v1) / numpy.dot(v1, v1)

def multiply(coefficient, v):        #scalar multiplification
    return map((lambda x : x * coefficient), v)   

def proj(v1, v2):                   #calculate the projection vector
    return multiply(gs_coefficient(v1, v2) , v1)  #(<v1, v2>/<v1, v1>) * v1

def gram_schmidts(X):
    Y = []
    for i in range(len(X)):
        temp_vec = X[i]
        for inY in Y :
            proj_vec = proj(inY, X[i])
            temp_vec = map(lambda x, y : x - y, temp_vec, proj_vec)
        Y.append(list(temp_vec))
    return Y

def normalize_list(X):              #calculate the normalization of the vector
    if (not numpu.any(X)): return X
    normalized_vector = X / numpy.linalg.norm(X)
    return normalized_vector

def main():
    m = int(input("Enter the amount of vectors: "))
    n = int(input("Enter the dimension of vector space: "))
    print("Input the vectors:", end = " ")
    arr = numpy.array([float(x) for x in input().split()]) 
    arr = arr.reshape(m,n)
    gs_array = numpy.array(gram_schmidts(arr))
    print("The orthogonal basis of the vectors:")
    print(gs_array)
    print("The orthonormal basis of the vectors:")
    for i in range (m):
        print(numpy.array(normalize_list(gs_array[i])))

if __name__ == "__main__": main()

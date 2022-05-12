clc; clear;
syms x;
mat_A = input('Input the square matrix: ');
disp('A = ');
disp(mat_A);
[n, n_] = size(mat_A);    %get the size of matrix A
polyA = charpoly(mat_A, x);   %get the characteristic polynomial
eigen_value_A = solve(polyA);  %solve the characteristic polynomial
disp('The eigenvalues of the matrix are: ');
disp(eigen_value_A);
disp('The eigenvectors are: ')
mat_S = [];
for i = 1 : n
    if (i < n && eigen_value_A(i) == eigen_value_A(i+1))    %ignore same eigenvalue
        continue;
    end
    X = null(mat_A - eigen_value_A(i) * eye(n));  %solve (matA-lambda*I)* x = 0 to find eigen vector
    disp(X);
    mat_S = [mat_S X];
end
[s_row, s_col] = size(mat_S);  %get the size of matrix S
if (s_row ~= s_col)   %check if S is a square matrix
    disp('Matrix A is not diagonalizable');
    exit();
end
mat_D = diag(eigen_value_A);    %create a matrix with eigenvalues in the main diagonal 
disp('S = ');
disp(mat_S);
disp('D = ');
disp(mat_D);
disp('S^-1 = ');
disp(mat_S^-1);    %display the inverse of matrix S

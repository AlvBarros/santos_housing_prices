# Matrices and Vectors

## Matrix

- Rectangular array of numbers
- **Dimension:** number of rows x number of columns

> [ 1402 191 ]
>
> [ 1371 821 ]
> 
> [ 949 1437]
> 
> This is a 3 x 2 matrix

## Vector

- A n x 1 matrix
- It can be 1-indexed or 0-indexes, which just means the first index is 1 or 0 respectivelly.

> [ 460 ]
>
> [ 232 ]
>
> [ 315 ]
>
> [ 178 ]

## Octave/Matlab

```
% The ; denotes we are going back to a new row.
A = [1, 2, 3; 4, 5, 6; 7, 8, 9; 10, 11, 12]

% Initialize a vector 
v = [1;2;3] 

% Get the dimension of the matrix A where m = rows and n = columns
[m,n] = size(A)

% You could also store it this way
dim_A = size(A)

% Get the dimension of the vector v 
dim_v = size(v)

% Now let's index into the 2nd row 3rd column of matrix A
A_23 = A(2,3)
```

Output:

```
A =

    1    2    3
    4    5    6
    7    8    9
   10   11   12

v =

   1
   2
   3

m =  4
n =  3
dim_A =

   4   3

dim_v =

   3   1

A_23 =  6
```

## Addition and Subtraction

- Given two matrixes, I want to add them
- If they have the same dimensions, you just add the items in the same x,y
  - Given that m and n are matrixes with the same dimension:
    - m + n = o => oxy = mxy + nxy
- If they don't have the same dimensions, you cannot add them


## Scalar multiplication

- Multiply a matrix by a number
  - Given that x is a real number, and m is a matrix:
    - x * m1 = m2 => m2xy = x * m1xy
- The same works for division (since it is multiplying by 1/x)

## Combination of Operands

- Follows the same algebraic orders
- Parenthesis, multiplications, divisions, sums and subtractions


## Octave/Matlab

```
% Initialize matrix A and B 
A = [1, 2, 4; 5, 3, 2]
B = [1, 3, 4; 1, 1, 1]

% Initialize constant s 
s = 2

% See how element-wise addition works
add_AB = A + B 

% See how element-wise subtraction works
sub_AB = A - B

% See how scalar multiplication works
mult_As = A * s

% Divide A by s
div_As = A / s

% What happens if we have a Matrix + scalar?
add_As = A + s

```

Output :

```
A =

   1   2   4
   5   3   2

B =

   1   3   4
   1   1   1

s =  2
add_AB =

   2   5   8
   6   4   3

sub_AB =

   0  -1   0
   4   2   1

mult_As =

    2    4    8
   10    6    4

div_As =

   0.50000   1.00000   2.00000
   2.50000   1.50000   1.00000

add_As =

   3   4   6
   7   5   4
```
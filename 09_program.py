# Q10 (4 Marks): Given a matrix as a list of lists, write Python code to print:
# • Sum of each row
# • Sum of each column
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
] 
print("Sum of each row:")
for row in matrix: 
    print(sum(row)) 
print("Sum of each column:")
for col in range(len(matrix[0])):   
    col_sum = sum(matrix[row][col] for row in range(len(matrix))) 
    print(col_sum)  
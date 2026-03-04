# Q5 (3 Marks): Write a Python program to rotate a list to the right by k positions without using slicing.
def rotate_list(lst, k):
    n = len(lst)
    k = k % n  
    for _ in range(k):
        last_element = lst[-1]
        for i in range(n-1, 0, -1):
            lst[i] = lst[i-1]
        lst[0] = last_element
    return lst
n = [1, 2, 3, 4, 5]
k = 2
rotated_list = rotate_list(n, k)
print(rotated_list)  # Output: [4, 5, 1, 2, 3]

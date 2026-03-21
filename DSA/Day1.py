
https://docs.google.com/spreadsheets/d/1DNZ4ONUFhadxZW_-QAuz2QDkHGmA9JbqESjteDJOV4c/edit?gid=1050162951#gid=1050162951
1. natural n number of formula 
--> n*(n+1)/2
2. range sum of array
--> R-L+1
3. step from N --> 1 
--> log2N
O(1)< log2N< O(N)< O(NlogN)< O(N^2)< O(N^3)< O(2^N)< O(N!)< O(N^N)



for i in n:
    for j in range(0, n-i-1):
        print(i, j)

what is the time complexity of above code?The time complexity of the above code is O(n^2).
l = [7,5,4,2]
want to write a code for Bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
print(bubble_sort(l))
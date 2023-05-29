def bubble_sort_library(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j][2] > arr[j+1][2]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
arr = [['Harry Potter an the Soccerers', 'J.K Rowling','320'],['To Kill a Mockingbird', 'Harper Lee', '281'],
     ['The Great Gatsby', 'F. Scott Fizgerald', '180'],
     ['Pride and Prejudice', 'Jane Austen', '432'],
     ['1984', 'George Orwell', '328']]
     
bubble_sort_library(arr)
print("Daftar buku : ", arr)

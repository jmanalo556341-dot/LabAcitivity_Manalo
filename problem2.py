
def bubble_sort(arr):
    n = len(arr)
    print(f"Input values = {arr}")
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            print(f"Items compared: [{arr[j]}, {arr[j+1]}]", end=" ")
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                print(f"➔ swapped {arr}")
            else:
                print("➔ not swapped")
        if swapped:
            print(f"Iteration #{i+1} {arr}")
        else:
            break
    print(f"Output values = {arr}")

values = list(map(int, input("Enter values separated by space: ").split()))
bubble_sort(values)
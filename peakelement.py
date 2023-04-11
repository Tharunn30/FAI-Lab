#finding the peak element and square root of it
import math
def findPeakElement(arr):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == len(arr) - 1 or arr[mid + 1] <= arr[mid]):
            return arr[mid]
        elif mid > 0 and arr[mid - 1] > arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return None

def squareRoot(peak):
    return math.sqrt(peak)

arr = [1, 3, 20, 4, 1, 0]
peak = findPeakElement(arr)
if peak:
    sqrt_peak = squareRoot(peak)
    print("Peak element: ", peak)
    print("Square root of peak element: ", sqrt_peak)
else:
    print("No peak element found")


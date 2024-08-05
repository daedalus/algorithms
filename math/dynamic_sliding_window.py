def dynamic_sliding_window(arr, x):
    min_length = len(arr)
    start = 0
    end = 0
    current_sum = 0
    while end < min_length:
        current_sum += arr[end]
        end += 1
        while start < end and current_sum >= x:
            current_sum -= arr[start]
            start += 1
            min_length = min(min_length, end-start+1)
    return min_length

A=[x for x in range(1, 21)]
print([dynamic_sliding_window(A, a) for a in A])

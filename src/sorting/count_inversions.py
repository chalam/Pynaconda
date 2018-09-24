# two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j

def merge(arr0, arr1):
    inversions = 0
    result = []
    # two indices to keep track of where we are in the array
    i0 = 0
    i1 = 0
    # probably doesn't really save much time but neater than calling len() everywhere
    len0 = len(arr0)
    len1 = len(arr1)
    while len0 > i0 and len1 > i1:
        if arr0[i0] <= arr1[i1]:
            result.append(arr0[i0])
            i0 += 1
        else:
            # count the inversion right here: add the length of left array
            inversions += len0 - i0
            result.append(arr1[i1])
            i1 += 1

    if len0 == i0:
        result += arr1[i1:]
    elif len1 == i1:
        result += arr0[i0:]

    return result, inversions

def merge_sort(arr):
    n = len(arr)
    mid = len(arr) // 2
    if n >= 2:
        left_arr,  left_count  = merge_sort(arr[:mid])
        right_arr, right_count = merge_sort(arr[mid:])
        merged_arr, merged_count = merge(left_arr, right_arr)
        return merged_arr, left_count + right_count + merged_count
    else:
        return arr, 0

# Complete the countInversions function below.
def countInversions(arr):
    final_array, inversions = merge_sort(arr)
    # print(final_array)
    return inversions

    # # quick sort partition
    # swaps = 0
    # n = len(arr)
    # for p in range(n):
    #     pivot = arr[0]
    #     print('pivot', pivot, arr)
    #     i = - 1
    #     for j in range(0, n):
    #         print(arr[i], arr[j], pivot)
    #         while arr[j] < pivot and i < n:
    #             i += 1
    #             arr[i], arr[j] = arr[j], arr[i]
    #             swaps += 1
    #             print('swap', swaps)
    #     # no need of this to swap pivot back
    #     # arr[i+1], arr[p] = arr[p], arr[i+1]
    #     # swaps += 1
    # return swaps

if __name__ == '__main__':
    assert countInversions([2, 1, 3, 1, 2]) == 4
    assert countInversions([7, 5, 3, 1]) == 6 # how far way from sorted index 1 3 5 7

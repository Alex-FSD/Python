import random
import time
import math

n = 10000
lst = [random.randint(0, n) for _ in range(n)]
dct = {}


##############
# 1 Алгоритм #
##############
def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
    return nums


def bubble_sort2(array):
    swapped = False
    for i in range(len(array) - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if swapped:
            swapped = False
        else:
            break
    return array


start = time.time()
bubble_sort(lst[:])
end = time.time() - start
dct["Сортировка пузырьком"] = end

start = time.time()
bubble_sort2(lst[:])
end = time.time() - start
dct["Сортировка пузырьком 2"] = end


##############
# 2 Алгоритм #
##############
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


start = time.time()
insertion_sort(lst[:])
end = time.time() - start
dct["Сортировка вставками"] = end


##############
# 3 Алгоритм #
##############
def selection_sort(array):
    for i in range(len(array) - 1):
        min_idx = i
        for idx in range(i + 1, len(array) - 1):
            if array[idx] < array[min_idx]:
                min_idx = idx
        array[i], array[min_idx] = array[min_idx], array[i]
    return array


start = time.time()
selection_sort(lst[:])
end = time.time() - start
dct["Сортировка выбором"] = end


##############
# 4 Алгоритм #
##############
def shell_sort(array):
    n = len(array)
    k = int(math.log2(n))
    interval = 2 ** k - 1
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        k -= 1
        interval = 2 ** k - 1
    return array


start = time.time()
shell_sort(lst[:])
end = time.time() - start
dct["Сортировка Шелла"] = end


##############
# 5 Алгоритм #
##############
def heapify(array, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and array[i] < array[l]:
        largest = l
    if r < n and array[largest] < array[r]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)


def heap_sort(array):
    n = len(array)
    for i in range(n // 2, -1, -1):
        heapify(array, n, i)
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    return array


start = time.time()
heap_sort(lst[:])
end = time.time() - start
dct["Пирамидальная сортировка"] = end


##############
# 6 Алгоритм #
##############
def merge_sort(nums):
    if len(nums) == 1:
        return nums
    mid = (len(nums) - 1) // 2
    lst1 = merge_sort(nums[:mid + 1])
    lst2 = merge_sort(nums[mid + 1:])
    result = merge(lst1, lst2)
    return result


def merge(lst1, lst2):
    lst = []
    i = 0
    j = 0
    while (i <= len(lst1) - 1 and j <= len(lst2) - 1):
        if lst1[i] < lst2[j]:
            lst.append(lst1[i])
            i += 1
        else:
            lst.append(lst2[j])
            j += 1
    if i > len(lst1) - 1:
        while (j <= len(lst2) - 1):
            lst.append(lst2[j])
            j += 1
    else:
        while (i <= len(lst1) - 1):
            lst.append(lst1[i])
            i += 1
    return lst


start = time.time()
merge_sort(lst[:])
end = time.time() - start
dct["Сортировка слиянием"] = end


##############
# 7 Алгоритм #
##############
def quick_sort(array):
    if len(array) > 1:
        pivot = array.pop()
        grtr_lst, equal_lst, smlr_lst = [], [pivot], []
        for item in array:
            if item == pivot:
                equal_lst.append(item)
            elif item > pivot:
                grtr_lst.append(item)
            else:
                smlr_lst.append(item)
        return (quick_sort(smlr_lst) + equal_lst + quick_sort(grtr_lst))
    else:
        return array


start = time.time()
quick_sort(lst[:])
end = time.time() - start
dct["Быстрая сортировка"] = end


##############
# 8 Алгоритм #
##############
def counting_sort(nums):
    i_lower_bound, upper_bound = min(nums), max(nums)
    lower_bound = i_lower_bound
    if i_lower_bound < 0:
        lb = abs(i_lower_bound)
        nums = [item + lb for item in nums]
        lower_bound, upper_bound = min(nums), max(nums)

    counter_nums = [0] * (upper_bound - lower_bound + 1)
    for item in nums:
        counter_nums[item - lower_bound] += 1
    pos = 0
    for idx, item in enumerate(counter_nums):
        num = idx + lower_bound
        for i in range(item):
            nums[pos] = num
            pos += 1
    if i_lower_bound < 0:
        lb = abs(i_lower_bound)
        nums = [item - lb for item in nums]
    return nums


start = time.time()
counting_sort(lst[:])
end = time.time() - start
dct["Сортировка подсчетом"] = end

##############
# 9 Алгоритм #
##############
MINIMUM = 32


def find_minrun(n):
    r = 0
    while n >= MINIMUM:
        r |= n & 1
        n >>= 1
    return n + r


def insertion_sort(array, left, right):
    for i in range(left + 1, right + 1):
        element = array[i]
        j = i - 1
        while element < array[j] and j >= left:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = element
    return array


def merge(array, l, m, r):
    array_length1 = m - l + 1
    array_length2 = r - m
    left = []
    right = []
    for i in range(0, array_length1):
        left.append(array[l + i])
    for i in range(0, array_length2):
        right.append(array[m + 1 + i])

    i = 0
    j = 0
    k = l

    while j < array_length2 and i < array_length1:
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1

        else:
            array[k] = right[j]
            j += 1

        k += 1

    while i < array_length1:
        array[k] = left[i]
        k += 1
        i += 1

    while j < array_length2:
        array[k] = right[j]
        k += 1
        j += 1


def tim_sort(array):
    n = len(array)
    minrun = find_minrun(n)

    for start in range(0, n, minrun):
        end = min(start + minrun - 1, n - 1)
        insertion_sort(array, start, end)

    size = minrun
    while size < n:

        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            merge(array, left, mid, right)

        size = 2 * size
    return array


start = time.time()
tim_sort(lst[:])
end = time.time() - start
dct["Сортировка Timsort"] = end


##############
# 10 Алгоритм #
##############
def smooth_sort(lst):
    leo_nums = leonardo_numbers(len(lst))
    heap = []
    for i in range(len(lst)):
        if len(heap) >= 2 and heap[-2] == heap[-1] + 1:
            heap.pop()
            heap[-1] += 1
        else:
            if len(heap) >= 1 and heap[-1] == 1:
                heap.append(0)
            else:
                heap.append(1)
        restore_heap(lst, i, heap, leo_nums)

    for i in reversed(range(len(lst))):
        if heap[-1] < 2:
            heap.pop()
        else:
            k = heap.pop()
            t_r, k_r, t_l, k_l = get_child_trees(i, k, leo_nums)
            heap.append(k_l)
            restore_heap(lst, t_l, heap, leo_nums)
            heap.append(k_r)
            restore_heap(lst, t_r, heap, leo_nums)


def leonardo_numbers(hi):
    a, b = 1, 1
    numbers = []
    while a <= hi:
        numbers.append(a)
        a, b = b, a + b + 1
    return numbers


def restore_heap(lst, i, heap, leo_nums):
    current = len(heap) - 1
    k = heap[current]

    while current > 0:
        j = i - leo_nums[k]
        if (lst[j] > lst[i] and
                (k < 2 or lst[j] > lst[i - 1] and lst[j] > lst[i - 2])):
            lst[i], lst[j] = lst[j], lst[i]
            i = j
            current -= 1
            k = heap[current]
        else:
            break

    while k >= 2:
        t_r, k_r, t_l, k_l = get_child_trees(i, k, leo_nums)
        if lst[i] < lst[t_r] or lst[i] < lst[t_l]:
            if lst[t_r] > lst[t_l]:
                lst[i], lst[t_r] = lst[t_r], lst[i]
                i, k = t_r, k_r
            else:
                lst[i], lst[t_l] = lst[t_l], lst[i]
                i, k = t_l, k_l
        else:
            break


def get_child_trees(i, k, leo_nums):
    t_r, k_r = i - 1, k - 2
    t_l, k_l = t_r - leo_nums[k_r], k - 1
    return t_r, k_r, t_l, k_l


start = time.time()
smooth_sort(lst[:])
end = time.time() - start
dct["Плавная сортировка"] = end


###############
# 11 Алгоритм #
###############
def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        var = bucket[i]
        j = i - 1
        while (j >= 0 and var < bucket[j]):
            bucket[j + 1] = bucket[j]
            j = j - 1
        bucket[j + 1] = var


def bucket_sort(input_list):
    max_value = max(input_list)
    size = max_value / len(input_list)
    buckets_list = []
    for x in range(len(input_list)):
        buckets_list.append([])
    for i in range(len(input_list)):
        j = int(input_list[i] / size)
        if j != len(input_list):
            buckets_list[j].append(input_list[i])
        else:
            buckets_list[len(input_list) - 1].append(input_list[i])
    for z in range(len(input_list)):
        insertion_sort(buckets_list[z])
    final_output = []
    for x in range(len(input_list)):
        final_output = final_output + buckets_list[x]
    return final_output


start = time.time()
bucket_sort(lst[:])
end = time.time() - start
dct["Блочная сортировка"] = end


###############
# 12 Алгоритм #
###############
def shake_sort(array):
    left = 0
    right = len(array) - 1
    while left <= right:
        for i in range(left, right, +1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        right -= 1
        for i in range(right, left, -1):
            if array[i - 1] > array[i]:
                array[i], array[i - 1] = array[i - 1], array[i]
        left += 1


start = time.time()
shake_sort(lst[:])
end = time.time() - start
dct["Шейкерная сортировка"] = end


###############
# 13 Алгоритм #
###############
def comb_sort(array):
    step = int(len(array) / 1.247)
    swap = 1
    while step > 1 or swap > 0:
        swap = 0
        i = 0
        while i + step < len(array):
            if array[i] > array[i + step]:
                array[i], array[i + step] = array[i + step], array[i]
                swap += 1
            i = i + 1
        if step > 1:
            step = int(step / 1.247)


start = time.time()
comb_sort(lst[:])
end = time.time() - start
dct["Сортировка «расческой»"] = end

#############
# Результат #
#############
dct_sort = dict(sorted(dct.items(), key=lambda x: x[1]))
for key, value in dct_sort.items():
    print(f"{value} = {key}")

import random
import time

class Node:
    def __init__(self):
        self.nodes=[]


    def AppendNode(self,n):
        self.nodes.append(n)


class Sort(Node):
    def __init__(self):
        super().__init__()
        self.name="noname"
        self.result={}


    def WriteResult(self):
        print(self.name,"  ",self.result[self.name])
        for i in self.nodes:
            i.WriteResult()


    def Sort(self,L):
        return L, -1


class HeapSort(Sort):
    def __init__(self):
        super().__init__()
        self.name="Heap"

    def __heapify(self,arr, n, i):
        largest = i  # root
        left = 2 * i + 1  # left child
        right = 2 * i + 2  # right child

        # Check if left child is larger
        if left < n and arr[left] > arr[largest]:
            largest = left

        # Check if right child is larger
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If root is not largest, swap and continue heapifying
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.__heapify(arr, n, largest)

    def __heap_sort(self, arr):
        n = len(arr)

        # Step 1: Build max heap
        for i in range(n // 2 - 1, -1, -1):
            self.__heapify(arr, n, i)

        # Step 2: Extract elements
        for i in range(n - 1, 0, -1):
            # Move current root to end
            arr[i], arr[0] = arr[0], arr[i]

            # Heapify reduced heap
            self.__heapify(arr, i, 0)
        return arr,

    def Sort(self,L):
        start = time.time()
        sorted=self.__heap_sort(L)
        end = time.time()
        self.result[self.name]= end - start
        if len(self.nodes)>0:
            for i in self.nodes:
                nm, srtd, dur= i.Sort(L)
                self.result[nm]= dur
        return self.name, sorted, end - start

class MaxSort(Sort):
    def __init__(self):
        super().__init__()
        self.name="Max"

    def Sort(self, list):
        start = time.time()
        sorted=[]
        while len(list)>0:
            mx=max(list)
            sorted.append(mx)
            list.remove(mx)
        end = time.time()
        self.result[self.name]= end - start
        if len(self.nodes)>0:
            for i in self.nodes:
                nm, srtd, dur= i.Sort(list)
                self.result[nm]= dur
        return self.name, sorted, end - start

class BubbleSort(Sort):
    def __init__(self):
        super().__init__()
        self.name="Bubble Sort"

    def Sort(self,list ):
        start = time.time()
        for iter_num in range(len(list) - 1, 0, -1):
            for idx in range(iter_num):
                if list[idx] > list[idx + 1]:
                    temp = list[idx]
                    list[idx] = list[idx + 1]
                    list[idx + 1] = temp
        end = time.time()

        self.result[self.name]= end - start
        if len(self.nodes)>0:
            for i in self.nodes:
                nm, srtd, dur= i.Sort(list)
                self.result[nm]= dur
        return self.name, sorted, end - start

class MergeSort(Sort):
    def __init__(self):
        super().__init__()
        self.name="Merge Sort"

    def __merge_sort(self, unsorted_list):
        if len(unsorted_list) <= 1:
            return unsorted_list
        # Liste orta noktasını bul ve ikiye ayır
        middle = len(unsorted_list) // 2
        left_list = unsorted_list[:middle]
        right_list = unsorted_list[middle:]

        left_list = self.__merge_sort(left_list)
        right_list = self.__merge_sort(right_list)
        return list(self.__merge(left_list, right_list))

    # Sıralanmış alt grupları birleştir

    def __merge(self, left_half, right_half):

        res = []
        while len(left_half) != 0 and len(right_half) != 0:
            if left_half[0] < right_half[0]:
                res.append(left_half[0])
                left_half.remove(left_half[0])
            else:
                res.append(right_half[0])
                right_half.remove(right_half[0])
        if len(left_half) == 0:
            res = res + right_half
        else:
            res = res + left_half
        return res

    def Sort(self, unsorted_list):
        start = time.time()
        InputList=self.__merge_sort(unsorted_list)
        end = time.time()
        self.result[self.name]= end - start
        if len(self.nodes)>0:
            for i in self.nodes:
                nm, srtd, dur= i.Sort(unsorted_list)
                self.result[nm]= dur
        return self.name, sorted, end - start

class InsertionSort(Sort):
    def __init__(self):
        super().__init__()
        self.name="Insertion Sort"

    def Sort(self, InputList):
        start = time.time()

        for i in range(1, len(InputList)):
            j = i - 1
            nxt_element = InputList[i]
            # Liste elemanını bir sonraki ile kıyasla

            while (InputList[j] > nxt_element) and (j >= 0):
                InputList[j + 1] = InputList[j]
                j = j - 1
            InputList[j + 1] = nxt_element
        end = time.time()

        self.result[self.name]= end - start
        if len(self.nodes)>0:
            for i in self.nodes:
                nm, srtd, dur= i.Sort(InputList)
                self.result[nm]= dur
        return self.name, sorted, end - start

class SelectionSort(Sort):
    def __init__(self):
        super().__init__()
        self.name="Selection Sort"

    def Sort(self,input_list):
        start = time.time()
        for idx in range(len(input_list)):

            min_idx = idx
            for j in range(idx + 1, len(input_list)):
                if input_list[min_idx] > input_list[j]:
                    min_idx = j
            # Swap the minimum value with the compared value

            input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]
        end = time.time()
        self.result[self.name]= end - start
        if len(self.nodes)>0:
            for i in self.nodes:
                nm, srtd, dur= i.Sort(input_list)
                self.result[nm]= dur
        return self.name, sorted, end - start

class ShellSort(Sort):
    def __init__(self):
        super().__init__()
        self.name="Shell Sort"

    def Sort(self,input_list):
        start = time.time()

        gap = len(input_list) // 2
        while gap > 0:

            for i in range(gap, len(input_list)):
                temp = input_list[i]
                j = i
                # Sort the sub list for this gap

                while j >= gap and input_list[j - gap] > temp:
                    input_list[j] = input_list[j - gap]
                    j = j - gap
                input_list[j] = temp

            # Reduce the gap for the next element

            gap = gap // 2
        end = time.time()
        self.result[self.name]= end - start
        if len(self.nodes)>0:
            for i in self.nodes:
                nm, srtd, dur= i.Sort(input_list)
                self.result[nm]= dur
        return self.name, sorted, end - start





n0=BubbleSort()
n1=HeapSort()
n2=MergeSort()
n3=SelectionSort()
n4=ShellSort()
n11=HeapSort()

n0.AppendNode(n1)
n0.AppendNode(n2)
n0.AppendNode(n3)

n1.AppendNode(n4)

n5=BubbleSort()
n6=HeapSort()
n7=MergeSort()
n8=SelectionSort()
n9=ShellSort()


n10=BubbleSort()


n1.AppendNode(n5)

n2.AppendNode(n6)
n2.AppendNode(n7)

n3.AppendNode(n8)

n8.AppendNode(n9)
n8.AppendNode(n10)


n7.AppendNode(n11)

data=[]
for i in range(0,1000):
    data.append(random.randint(0,100))


n0.Sort(data)
n0.WriteResult()

print("Root:",list(n0.result.keys()))
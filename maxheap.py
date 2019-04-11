class MaxHeap:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def push(self, data):
        self.heap.append(data)
        self._moveUp(len(self.heap) - 1)

    def peek(self):
        if self.heap[0]:
            return self.heap[0]
        else:
            return False

    def pop(self):
        if len(self.heap) >= 1:
            self._swap(0, len(self.heap) - 1)
            max = self.heap.pop()
            self._moveDown(0)
            self._moveUp(len(self.heap) - 1)
        elif len(self.heap) == 1:
            max = self.heap.pop()
        else:
            max = False
        return max

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _moveUp(self, index):
        parent = index // 2
        if index < 1:
            return
        elif (
            self.heap[index] > self.heap[parent]
            or self.heap[index] == self.heap[parent]
        ):
            self._swap(index, parent)
            self._moveUp(parent)

    def _moveDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self._swap(index, largest)
            self._moveDown(largest)


if __name__ == "__main__":
    initHeap = MaxHeap()
    sortedList = []

    def max_heap_sort(list_of_user_data):
        for i in range(len(list_of_user_data)):
            initHeap.push(list_of_user_data[i])
        for j in range(len(initHeap)):
            sortedList.insert(j, initHeap.heap[0])
            initHeap.pop()
        return sortedList

    unsortedData = []
    while True:
        inputData = input()
        if inputData == "q":
            break
        unsortedData.append(float(inputData))

    max_heap_sort(unsortedData)
    for n in range(len(sortedList)):
        print(sortedList[n])

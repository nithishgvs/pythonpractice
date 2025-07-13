class InsertionSort:

    def insertion_sort(self, arr: list) -> list:

        for i in range(1, len(arr)):
            key = arr[i]

            j = i - 1

            while j > -1 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

        return arr


if __name__ == "__main__":
    object = InsertionSort()

    print(object.insertion_sort([5, 4, 3, 2, 1]))

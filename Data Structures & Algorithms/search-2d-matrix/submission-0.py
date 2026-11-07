class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def search(row):
            arr = matrix[row]
            l, r = 0, len(arr) - 1

            while l <= r:
                mid = (l + r) // 2
                n = arr[mid]

                if n > target:
                    r = mid - 1
                elif n < target:
                    l = mid + 1
                else:
                    return True



        for i in range(len(matrix)):
            if search(i):
                return True

        return False
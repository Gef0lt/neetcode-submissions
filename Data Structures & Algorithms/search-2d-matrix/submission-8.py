class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        ans = False

        if target > matrix[-1][-1] or target < matrix[0][0]:
            return False
        
        # search row
        l, r = 0, n - 1
        while l <= r:
            row = l + (r - l) // 2
            if target >= matrix[row][0] and target <= matrix[row][-1]:
                break

            if target < matrix[row][0]:
                r = row - 1
            elif target > matrix[row][-1]:
                l = row + 1
            
        # search inside row found
        l, r = 0, m - 1
        while l <= r:
            col = l + (r - l) // 2

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = col - 1
            else:
                l = col + 1


        return False
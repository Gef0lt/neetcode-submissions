def binary_search(nums: List[int], target) -> bool:
        while len(nums) > 1:
            if len(nums) % 2 == 0:
                if nums[len(nums) // 2] <= target:
                    nums = nums[len(nums) // 2:]
                else:
                    nums = nums[:len(nums) // 2]
            else:
                if nums[len(nums) // 2] == target:
                    return True
                elif nums[len(nums) // 2] < target:
                    nums = nums[len(nums) // 2 + 1:]
                else:
                    nums = nums[:len(nums) // 2]
        if nums[0] == target:
            return True
        return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        while len(matrix) > 1:
            if len(matrix) % 2 == 0:
                if matrix[len(matrix)//2][0] > target:
                    matrix = matrix[:len(matrix)//2]
                else:
                    matrix = matrix[len(matrix)//2:]
            else:
                if matrix[len(matrix)//2][0] <= target <= matrix[len(matrix)//2][-1]:
                    return binary_search(matrix[len(matrix)//2], target)
                elif matrix[len(matrix)//2][-1] <= target:
                    matrix = matrix[len(matrix)//2 + 1:]     
                else:
                    matrix = matrix[:len(matrix)//2] 
            
        if matrix[0][0] <= target <= matrix[0][-1]:
            return binary_search(matrix[len(matrix)//2], target)
        return False

         
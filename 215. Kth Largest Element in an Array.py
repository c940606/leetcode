class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def partition(left, right):
            pivot = left
            i = left
            j = right
            while i < j:
                while i < j and nums[j] > nums[pivot]:
                    j -= 1
                while i < j and nums[i] <= nums[pivot]:
                    i += 1
                nums[i], nums[j] = nums[j], nums[i]
            nums[pivot], nums[j] = nums[j], nums[pivot]
            return j




        def quicksort(left, right, k):
            if left == right: return nums[left]
            pivotIndex = partition(left, right)
            if k == pivotIndex: return nums[k]
            elif k < pivotIndex: return quicksort(left, pivotIndex - 1, k)
            else: return quicksort(pivotIndex + 1, right, k)


        return quicksort(0, len(nums) - 1, k)
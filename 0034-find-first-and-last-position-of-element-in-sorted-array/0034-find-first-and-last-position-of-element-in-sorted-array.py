class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first_occurrence(nums, target):
            left, right = 0, len(nums) - 1
            first_occurrence = -1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    first_occurrence = mid
                    right = mid - 1  # Continue searching on the left side
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return first_occurrence

        def find_last_occurrence(nums, target):
            left, right = 0, len(nums) - 1
            last_occurrence = -1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    last_occurrence = mid
                    left = mid + 1  # Continue searching on the right side
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return last_occurrence

        first_occurrence = find_first_occurrence(nums, target)
        last_occurrence = find_last_occurrence(nums, target)

        return [first_occurrence, last_occurrence]
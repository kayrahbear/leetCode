from typing import List

"""
Given an array of integers [nums] which is sorted in ascending order, and an integer [target], write a function to search target in nums. 

If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

"""


def search(nums: List[int], target: int) -> int:
    if not nums:
        return -1
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    print(search([-1, 0, 3, 5, 9, 12], 9))
    print(search([-1, 0, 3, 5, 9, 12], 2))

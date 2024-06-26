class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = 0
        counter = 0
        for val in nums:
            if counter == 0:
                candidate = val

            if candidate == val:
                counter += 1
            else:
                counter -= 1

        return candidate
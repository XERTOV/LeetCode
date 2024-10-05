class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_nums = sorted(nums)
        new_dict = {}
        result = []
        for num in nums:
            if num in new_dict :
                if new_dict[num]< 2:
                    result.append(num)
                    new_dict[num] +=1
            else:
                result.append(num)
                new_dict[num] =1
        nums[:] = result
        return len(result)
        
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_list = sorted(set(arr))
        rank_dict ={value: rank +1 for rank, value in enumerate(sorted_list)}
        return [rank_dict[num]for num in arr]
        
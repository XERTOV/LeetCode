class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        new_list = sorted(skill)
        if len(skill)==2:
            return skill[0]*skill[1]
        # if (sum(new_list) % 2 !=0):
        #     return -1
        team =[(new_list[i],new_list[-i-1])for i in range (0, len(new_list)//2)]
        total_sum = sum(team[0])
        total_score = 0
        for pair in team:
            if sum(pair) != total_sum:
                return -1

            total_score += pair[0]*pair[1]
        return total_score

        
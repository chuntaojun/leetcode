class Solution:
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        alex = 0;
        piles_sum = 0;
        for item in piles:
            piles_sum += item
        while len(piles) != 0:

            def choice_max_num():
                if piles[0] > piles[-1]:
                    max_num = piles[0]
                    piles.pop[0]
                    return max_num
                else:
                    max_num = piles[-1]
                    piles.pop[-1]
                    return max_num
            
            alex += choice_max_num()
        return alex * 2 > piles_sum


if __name__ == '__main__':
    pass

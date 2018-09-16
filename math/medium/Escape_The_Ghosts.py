class Solution:
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        lead_len = abs(target[0]) + abs(target[1])
        for ghost in ghosts:
            ghost_len = self.cul_len(ghost=ghost, target=target)
            if ghost_len <= lead_len:
                return False
        return True
    
    def cul_len(self, ghost, target):
        return abs(target[0] - ghost[0]) + abs(target[1] - ghost[1])


if __name__ == '__main__':
    pass

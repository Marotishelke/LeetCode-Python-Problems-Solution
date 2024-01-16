class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        allwinner = Counter([match[0] for match in matches])
        alllosser = Counter([match[1] for match in matches])
        zeroLoss = []

        for winner in allwinner:
            if winner not in alllosser:
                zeroLoss.append(winner)
        oneLoss = []
        for losser in alllosser:
            if alllosser[losser] == 1:
                oneLoss.append(losser)

        zeroLoss.sort()
        oneLoss.sort()

        return [zeroLoss, oneLoss]

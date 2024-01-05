class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        bank_security = []
        for bk in bank:
            if bk.count('1') >= 1:
                bank_security.append(bk)
        
        laser_beam_cnt = 0
        for i in range(1, len(bank_security)):
            laser_beam_cnt += (bank_security[i-1].count('1') * bank_security[i].count('1'))
        return laser_beam_cnt

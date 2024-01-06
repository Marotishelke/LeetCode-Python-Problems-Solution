class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:

        # ------------------------------------------
        # Approach 1 Time Excceed Error 
        res_lst = []
        for i in people:
            cnt_flowers = 0  # Calculate number of flowers when the people arrive
            for flower in flowers:
                # if i in range(flower[0], flower[1] + 1):
                if i >= flower[0] and i <= flower[1]:
                    cnt_flowers += 1
            res_lst.append(cnt_flowers)
        return res_lst
        # ------------------------------------------

        # ------------------------------------------
        # Approach 2
        start = sorted([s for s, e in flowers])
        end = sorted([e for s, e in flowers])
        return [bisect_right(start, t) - bisect_left(end, t) for t in people]
        # ------------------------------------------

        
        # ------------------------------------------
        # Approach 3
        blooming = defaultdict(int)                 # use line sweep
        for start, end in flowers:
            blooming[start] += 1
            blooming[end+1] -= 1

        print(blooming)
        ans, bloom_cnt = {}, 0
        h = sorted(people,reverse=True)            # sort persons desc so we can pop from last index
        for time in sorted(blooming.keys()):        # loop over sorted status updates
            bloom_change = blooming[time]
            while h and time > h[-1]:               # if current time is greater than
                ans[h.pop()] = bloom_cnt            # current person answer is last bloom_cnt
            if not h: break
            bloom_cnt += bloom_change

        return [ans[p] if p in ans else 0 for p in people]
        # ------------------------------------------

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # Create a hashmap to represent adjacent pairs
        hashmap = defaultdict(list)
        for u, v in adjacentPairs:
            hashmap[u].append(v)
            hashmap[v].append(u)
        
        res_lst = []

        # Find the starting node with only one neighbour
        for node, neighbours in hashmap.items():
            if len(neighbours) == 1:
                res_lst = [node, neighbours[0]]
                break
            
        # Continue building the array until its length matches the number of pairs
        while(len(res_lst) < len(adjacentPairs) + 1):
            # Get the last two elements in the result array
            last, prev = res_lst[-1], res_lst[-2]

            # Find the candidates for the next element
            candidates = hashmap[last]

            # Choose the candidates for the next element
            next_element = candidates[0] if candidates[0] != prev else candidates[1]

            # append the next element to the result array
            res_lst.append(next_element)
        return res_lst

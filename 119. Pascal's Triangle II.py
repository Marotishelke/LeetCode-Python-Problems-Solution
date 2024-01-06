class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # --------------------------------
        # Approach 1
        res_lst = []
        sub_lst = []
        for i in range(rowIndex+1):
            sub_lst = []
            for j in range(i+1):
                if j == 0:
                    sub_lst.append(1)
                elif j == i:
                    sub_lst.append(1)
                else:
                    curr_sum = res_lst[i-1][j] + res_lst[i-1][j-1]
                    sub_lst.append(curr_sum)
            res_lst.append(sub_lst)
        
        return sub_lst
        # --------------------------------

        
        # --------------------------------
        # Approach 2
        
        res_lst = [1]
        prev = 1
        for ind in range(1, rowIndex + 1):
            next_val = prev * (rowIndex - ind + 1) // ind
            res_lst.append(next_val)
            prev = next_val
        return res_lst
        # --------------------------------

        # --------------------------------
        # Approach 3
        res_lst = [[1], []]

        for current_row in range(1, rowIndex + 1):
            res_lst[1].append(1) # First element of each row always 1
            
            current_row_lst = res_lst[1]
            previous_row_lst = res_lst[0]

            # Calculate and update the middle elemet of each row
            for j in range(1, len(previous_row_lst)):
                curr_sum = previous_row_lst[j] + previous_row_lst[j-1]
                current_row_lst.append(curr_sum)
            
            current_row_lst.append(1) # Should add 1 end of list

            # Swap rows from res list
            res_lst[0] = current_row_lst
            res_lst[1] = []
        return res_lst[0]
        # --------------------------------



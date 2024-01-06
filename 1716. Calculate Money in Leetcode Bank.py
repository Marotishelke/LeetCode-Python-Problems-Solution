class Solution:
    def totalMoney(self, n: int) -> int:
        # ----------------------------- Approach 1 --------------------------
        total_amount_money = 0
        mon_day_money = 1
        while(n):
            days = 1
            while(days <= 7 and n):
                total_amount_money += (mon_day_money + days - 1)
                n -= 1
                days += 1
            mon_day_money += 1
        return total_amount_money
        # -------------------------------------------------------------------

        # ----------------------------- Approach 2 --------------------------
        week = n // 7
        money = week * 28
        money += (7 * week * (week - 1)) // 2

        # Find the money for extra days
        if (n % 7):
            extra_days = n % 7
            money_to_add = week + 1

            for _ in range(extra_days):
                money += money_to_add
                money_to_add += 1
        return money
        # -------------------------------------------------------------------

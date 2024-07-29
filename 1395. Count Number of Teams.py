""" There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

 

Example 1:

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 
Example 2:

Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.
Example 3:

Input: rating = [1,2,3,4]
Output: 4
 

Constraints:

n == rating.length
3 <= n <= 1000
1 <= rating[i] <= 105
All the integers in rating are unique. 
"""
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        teams = 0
        increasing_cache = [[-1] * 4 for _ in range(n)]
        decreasing_cache = [[-1] * 4 for _ in range(n)]

        # Calculate total teams by considering each soldier as a starting point
        for start_index in range(n):
            teams += self._count_increasing_teams(
                rating, start_index, 1, increasing_cache
            ) + self._count_decreasing_teams(
                rating, start_index, 1, decreasing_cache
            )

        return teams

    def _count_increasing_teams(
        self,
        rating: List[int],
        current_index: int,
        team_size: int,
        increasing_cache: List[List[int]],
    ) -> int:
        n = len(rating)

        # Base case: reached end of array
        if current_index == n:
            return 0

        # Base case: found a valid team of size 3
        if team_size == 3:
            return 1

        # Return cached result if available
        if increasing_cache[current_index][team_size] != -1:
            return increasing_cache[current_index][team_size]

        valid_teams = 0

        # Recursively count teams with increasing ratings
        for next_index in range(current_index + 1, n):
            if rating[next_index] > rating[current_index]:
                valid_teams += self._count_increasing_teams(
                    rating, next_index, team_size + 1, increasing_cache
                )

        # Cache and return the result
        increasing_cache[current_index][team_size] = valid_teams
        return valid_teams

    def _count_decreasing_teams(
        self,
        rating: List[int],
        current_index: int,
        team_size: int,
        decreasing_cache: List[List[int]],
    ) -> int:
        n = len(rating)

        # Base case: reached end of array
        if current_index == n:
            return 0

        # Base case: found a valid team of size 3
        if team_size == 3:
            return 1

        # Return cached result if available
        if decreasing_cache[current_index][team_size] != -1:
            return decreasing_cache[current_index][team_size]

        valid_teams = 0

        # Recursively count teams with decreasing ratings
        for next_index in range(current_index + 1, n):
            if rating[next_index] < rating[current_index]:
                valid_teams += self._count_decreasing_teams(
                    rating, next_index, team_size + 1, decreasing_cache
                )

        # Cache and return the result
        decreasing_cache[current_index][team_size] = valid_teams
        return valid_teams

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        visited = {(0, 0)}

        for direction in path:
            x += 1 if direction == 'E' else (-1 if direction == 'W' else 0)
            y += 1 if direction == 'N' else (-1 if direction == 'S' else 0)

            if (x, y) in visited:
                return True

            visited.add((x, y))

        return False

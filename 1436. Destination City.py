class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cities = set()

        # Collect outgoing cities
        for path in paths:
            cities.add(path[0])
        
        # Find destination city with no Outgoing path
        for path in paths:
            dest = path[1]
            if dest not in cities:
                return dest

        return ""
        

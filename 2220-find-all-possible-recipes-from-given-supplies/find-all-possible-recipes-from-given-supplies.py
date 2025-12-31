class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        need: Dict[str, List[str]] = dict(zip(recipes, ingredients))

        visiting = set()
        memo = {}

        def dfs(x: str) -> bool:
            if x in supplies:
                return True
            if x not in need:
                return False
            if x in memo:
                return memo[x]
            if x in visiting:          # cycle
                return False

            visiting.add(x)
            ok = True
            for ing in need[x]:
                if not dfs(ing):
                    ok = False
                    break
            visiting.remove(x)

            memo[x] = ok
            if ok:
                supplies.add(x)        # makes reuse fast
            return ok

        return [r for r in recipes if dfs(r)]


        
#Store each recipe and its list of ingredients in a hash map for fast searching.
#Once we verify that we can make a recipe, we can add it to our ingredient data structure. We can then check if we can make more recipes as a result of this.

    # """
    #     Kahn-style BFS on a bipartite dependency graph:
    #       ingredient -> recipes that require it
    #     When all required ingredients for a recipe are "available", the recipe becomes available too.
    #     """
    #     # ingredient -> [recipe1, recipe2, ...]
    #     needers = defaultdict(list)
    #     # indegree[recipe] = number of ingredients still missing
    #     indegree = {r: 0 for r in recipes}

    #     for r, ing_list in zip(recipes, ingredients):
    #         indegree[r] = len(ing_list)
    #         for ing in ing_list:
    #             needers[ing].append(r)

    #     q = deque(supplies)
    #     made = []

    #     while q:
    #         item = q.popleft()
    #         for r in needers.get(item, []):
    #             indegree[r] -= 1
    #             if indegree[r] == 0:
    #                 made.append(r)
    #                 q.append(r)  # newly made recipe becomes an available "supply"

    #     return made
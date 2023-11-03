#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#


# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        ans = 0

        def bfs(r, c):
            queue = deque([(r, c)])
            grid[r][c] = "0"  # mark as visited

            while queue:
                row, col = queue.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (0 <= r < rows) and (0 <= c < cols) and grid[r][c] == "1":
                        grid[r][c] = "0"
                        queue.append((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    ans += 1

        return ans

class Solution:

    def visit_island(self, grid: list[list[str]], i: int, j: int) -> list[list[str]]:
        island_nodes = [(i, j)]
        m, n = len(grid), len(grid[0])

        while island_nodes:
            x_, y_ = island_nodes.pop()
            grid[x_][y_] = '-1'

            if(x_ + 1 < m):
                if(grid[x_ + 1][y_] == '1' and (x_ + 1, y_) not in island_nodes):
                    island_nodes.append((x_ + 1, y_))
            if(x_ - 1 >= 0):
                if(grid[x_ - 1][y_] == '1' and (x_ - 1, y_) not in island_nodes):
                    island_nodes.append((x_ - 1, y_))
            
            if(y_ + 1 < n):
                if(grid[x_][y_ + 1] == '1' and (x_, y_ + 1) not in island_nodes):
                    island_nodes.append((x_, y_ + 1))
            if(y_ - 1 >= 0):
                if(grid[x_][y_ - 1] == '1' and (x_, y_ - 1) not in island_nodes):
                    island_nodes.append((x_, y_ - 1))

        return grid


    def numIslands(self, grid: list[list[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        island_count = 0

        for i in range(m):
            for j in range(n):
                if(grid[i][j] == '1'):
                    island_count += 1
                    grid = self.visit_island(grid, i,j)

        return island_count

if __name__ == '__main__':

    a = Solution()
    print(a.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))
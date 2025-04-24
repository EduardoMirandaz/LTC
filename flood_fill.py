class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, new_color: int) -> list[list[int]]:
        
        m = len(image)
        n = len(image[0])

        color_to_be_replaced = image[sr][sc]

        if(color_to_be_replaced == new_color): return image

        cells_to_be_painted = [(sr, sc)]

        while cells_to_be_painted:
            
            x, y = cells_to_be_painted.pop()
            if image[x][y] == color_to_be_replaced:
                image[x][y] = new_color
            else:
                continue

            if(x+1 < m):
                if((x+1, y) not in cells_to_be_painted):
                    cells_to_be_painted.append((x+1, y))

            if(x-1 >= 0):
                if((x-1, y) not in cells_to_be_painted):
                    cells_to_be_painted.append((x-1, y))

            if(y+1 < n):
                if((x, y+1) not in cells_to_be_painted):
                    cells_to_be_painted.append((x, y+1))

            if(y-1 >= 0):
                if((x, y-1) not in cells_to_be_painted):
                    cells_to_be_painted.append((x, y-1))


        return image


if __name__ == '__main__':
    a = Solution()
    a.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)


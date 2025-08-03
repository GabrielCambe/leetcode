class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # If dimensions are invalid, we do not have any paths
        if m <= 0 or n <= 0:
            return 0

        # The first overlaping sub problem is a single row
        # and the robot has only one way of moving to each cell,
        # by moving to the right until it reaches it  
        row = [1] * n

        # After that we start calculating the number of possible paths for the other rows
        for i in range(1, m):
            for j in range(1, n):
                # In the 1D array:
                # - `row[j]` holds the number of paths to the cell above (paths(i-1, j)).
                # - `row[j-1]` holds the number of paths to the cell to the left (paths(i, j-1)).

                # And the number of paths to the current cell (i, j) is:
                # paths(i-1, j) + paths(i, j-1)
                row[j] = row[j] + row[j-1]


        # After iterating through all the rows, the element row[n-1]
        # will hold the total number of paths to the bottom-right corner.
        return row[n-1]

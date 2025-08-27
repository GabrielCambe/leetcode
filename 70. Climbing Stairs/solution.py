class Solution:
    def climbStairs(self, n: int) -> int:
        # Recursion (Error - TLE):
        # Base cases
        # if (n == 1):
        #     return 1
        # elif (n == 2):
        #    return 2   
        # Othee cases, you sum the number of ways dependimg on what choice you make
        # return self.climbStairs(n-1) + self.climbStairs(n-2)


        # Iteration (O(n) space complexity):
        # dp_array = [1, 2]
        # for i in range(2, n):
        #     dp_array.append(dp_array[i-1] + dp_array[i-2])
        # return dp_array[n-1]


        # Iteration (O(1) space complexity):
        # Initialize the number of ways to get to the current step from the last and penultimate steps in
        from_last_step = 1
        from_penultimate_step = 2
        # Calculate the number of ways to get to the current step
        to_current_step = from_last_step + from_penultimate_step
        # Iterate to find the number of ways to get to the nth step
        for i in range(3, n):
            from_penultimate_step = from_last_step
            from_last_step = to_current_step
            to_current_step = from_last_step + from_penultimate_step
        # Return the number of ways to get to the nth step
        return to_current_step

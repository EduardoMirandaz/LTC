class NumArray:

    def __init__(self, nums: list[int]):
        self.prefix_sum_array = []
        acc = 0
        for num in nums:
            acc += num
            self.prefix_sum_array.append(acc)


    def sumRange(self, left: int, right: int) -> int:
        if(left == 0):
            return self.prefix_sum_array[right]
        else:            
            return self.prefix_sum_array[right] - self.prefix_sum_array[left -1]
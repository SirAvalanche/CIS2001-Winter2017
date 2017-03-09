import random

def BadSort( nums ):

    for current_sort_index in range( len(nums) ):
        lowest = nums[current_sort_index]
        index_of_lowest = current_sort_index
        for index in range(current_sort_index+1, len(nums) ):
            if nums[index] < lowest:
                lowest = nums[index]
                index_of_lowest = index
        temp = nums[current_sort_index]
        nums[current_sort_index] = lowest
        nums[index_of_lowest] = temp
nums = []
for n in range(10000):
    nums.append(random.randint(0, 1000000) )
print(nums)
#BadSort(nums) - really slow
#nums.sort() - really fast
print(nums)
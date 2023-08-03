def solution(number):
    nums=[str(num) for num in number]
    nums.sort(key=lambda num : num*3, reverse=True)
    
    return str(int(''.join(nums)))
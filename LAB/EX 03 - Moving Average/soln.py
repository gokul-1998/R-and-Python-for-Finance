# 1) How would you find moving average of 100 numbers, with period of 10?


numbers=[i for i in range(1,100)]

def moving_average(numbers, period):
    return [sum(numbers[i:i+period])/period for i in range(len(numbers)-period+1)]

print(moving_average(numbers, 10))
import random
start = input('請輸入最小值:')
end = input('請輸入最大值:')
start = int(start)
end = int(end)
answer = random.randint(start, end)
r = 0
while True:
    guess = input('你要猜什麼?')
    guess = int(guess)
    r = r + 1
    if guess == answer:
        print('終於猜對了')
        print('總共猜了', r, '次')
        break
    if guess > answer:
        print('比答案大喔')
    if guess < answer:
        print('比答案小喔')
    

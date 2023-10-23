nums = '1234567890'
answer_summ = 0

text_task = open('numbers.txt', 'r')

for line in text_task:
    for sym in line:
        if sym in nums:
            answer_summ += int(sym)

text_task.close()

answer = open('answer.txt', 'w')
answer.write(str(answer_summ))
answer.close()

tests = int(input())

for each in range(tests):

    input1 = input().split(' ')
    n = int(input1[0])
    k = int(input1[1])
    balls = []
    for i in range(n):
        read = input().split(' ')
        balls.append([int(read[0]), int(read[1])])
    distance = 0
    possible = 1
    for i in range(len(balls)):
        for j in range(len(balls)):
            if abs(balls[i][0] - balls[j][0]) + abs(balls[i][1] - balls[j][1]) > k:
                possible = -1
                break
        if possible == -1:
            break

    print(possible)

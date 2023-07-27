def solution(prior, loc):
    cnt = 0
    pre = -1
    goal = prior[loc]
    length = len(prior)

    for i in range(9,0,-1):
        if i not in prior:
            continue

        if goal == i and pre == -1:
            cnt = prior[0:loc + 1].count(i)
            return cnt

        for j in range(pre,pre+length):
            if prior[j%length] == i:     
                cnt += 1
                pre = j % length
            if i == goal and j%length == loc:
                return cnt
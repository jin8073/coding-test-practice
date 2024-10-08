def solution(people, limit):
    answer = 0
    people.sort()
    light = 0
    heavy = len(people) - 1
    while light <= heavy:
        if people[light] + people[heavy] > limit:
            heavy -= 1
            answer += 1
        else:
            light += 1
            heavy -= 1
            answer += 1
    return answer

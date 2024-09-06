import random
leader = int(random.random() * 4)
leader_dict = {
    1: "a가 조장입니다",
    2: "b가 조장입니다",
    3: "c가 조장입니다",
}
print(leader_dict.get(leader, "d가 조장입니다"))
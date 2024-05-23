def generate_bracket(members):
    weeks = []
    member_list = list(members)
    num_weeks = len(member_list) - 1 if len(member_list) % 2 == 0 else len(member_list)
    
    for week in range(num_weeks):
        matchups = []
        for i in range(len(member_list) // 2):
            matchups.append((member_list[i], member_list[-i-1]))
        member_list.insert(1, member_list.pop())
        weeks.append(matchups)
    
    return weeks

def find_common_participants(participants_0, participants_1, separator=','):
    participants_0 = participants_0.split(separator)
    participants_1 = participants_1.split(separator)
    
    common_participants=[]
    
    for i in range(0, len(participants_0)):
        for j in range(0, len(participants_0)):
            if participants_0[i] == participants_1[j]:
                common_participants.append(participants_1[j])
                
    return common_participants
                
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(sorted(find_common_participants(participants_second_group, participants_first_group, "|")))
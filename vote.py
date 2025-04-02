age = 20
citizenship = 1
convictions = 0
can_vote = age >= 18 and citizenship == 1 and convictions == 0
if can_vote == True:
    print("Вы можете голосовать")
else:
    print("Вы не можете голосовать.")
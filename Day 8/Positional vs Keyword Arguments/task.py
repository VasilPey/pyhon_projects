def calculate_love_score(name1,name2):
    combined = (name1 + name2).upper()
    letter_to_check = 'TRUE'
    letter_to_check1 = 'LOVE'
    count = 0
    count1 = 0
    for letters in combined:
        if letters in letter_to_check:
            count +=1
    for letters in combined:
        if letters in letter_to_check1:
            count1 +=1
    love_score = print(f'{count}{count1}')




calculate_love_score("Kanye West","Kim Kardashian")


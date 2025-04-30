def life_in_weeks(age):
    age_in_weeks = int(age * 365 / 7)
    age_by_ninety = int(4692)
    age_to_go = age_by_ninety - age_in_weeks
    print(f"You have {age_to_go} weeks left.")


life_in_weeks(56)
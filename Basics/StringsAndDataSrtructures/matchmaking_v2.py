def matchmaking():
    people = [
        {
            'name': "Мария",
            'interests': ['пътуване', 'танци', 'плуване', 'кино'],
            'age': 24,
            'gender': "female",
            "ex": ["Кирил", "Петър"],
        },
        {
            'name': "Диана",
            'interests': ['мода', 'спортна стрелба', 'четене', 'скандинавска поезия'],
            'age': 21,
            'gender': "female",
            "ex": [],
        },
        {
            'name': "Дарина",
            'interests': ['танци', 'покер', 'история', 'софтуер'],
            'age': 34,
            'gender': "female",
            "ex": ["Борис"],
        },
        {
            'name': "Лилия",
            'interests': ['покер', 'автомобили', 'танци', 'кино'],
            'age': 36,
            'gender': "female",
            "ex": [],
        },
        {
            'name': "Галя",
            'interests': ['пътуване', 'автомобили', 'плуване', 'баскетбол'],
            'age': 18,
            'gender': "female",
            "ex": ['Димитър'],
        },
        {
            'name': "Валерия",
            'interests': ['плуване', 'покер', 'наука', 'скандинавска поезия'],
            'age': 27,
            'gender': "female",
            "ex": [],
        },
        {
            'name': "Ина",
            'interests': ['кино', 'лов със соколи', 'пътуване', 'мода'],
            'age': 20,
            'gender': "female",
            "ex": [],
        },
        {
            'name': "Кирил",
            'interests': ['баскетбол', 'автомобили', 'кино', 'наука'],
            'age': 19,
            'gender': "male",
            'ex': ["Мария"],
        },
        {
            'name': "Георги",
            'interests': ['автомобили', 'футбол', 'плуване', 'танци'],
            'age': 32,
            'gender': "male",
            'ex': [],
        },
        {
            'name': "Андрей",
            'interests': ['футбол', 'скандинавска поезия', 'история', 'танци'],
            'age': 26,
            'gender': "male",
            'ex': ["Мария"],
        },
        {
            'name': "Емил",
            'interests': ['летене', 'баскетбол', 'софтуер', 'наука'],
            'age': 34,
            'gender': "male",
            'ex': ['Дарина'],
        },
        {
            'name': "Димитър",
            'interests': ['футбол', 'лов със соколи', 'автомобили', 'баскетбол'],
            'age': 22,
            'gender': "male",
            'ex': ['Галя'],
        },
        {
            'name': "Петър",
            'interests': ['пътуване', 'покер', 'баскетбол', 'лов със соколи'],
            'age': 23,
            'gender': "male",
            'ex': ["Мария"],
        },
        {
            'name': "Калоян",
            'interests': ['кино', 'покер', 'пътуване', 'автомобили'],
            'age': 29,
            'gender': "male",
            'ex': [],
        },
    ]
    people_interests_sets = {}
    for i, p1 in enumerate(people):
        for j, p2 in enumerate(people[i:]):
            common_interests = set(people[i]['interests']).intersection(set(people[j]['interests']))
            if len(common_interests) > 0 and p1['gender'] != p2['gender'] and p2['name'] not in p1['ex'] and abs(
                            p1['age'] - p2['age']) <= 6:
                print('{}({}) и {}({}) - общи интереси: {}'.format(p1['name'], p1['age'], p2['name'], p2['age'],
                                                                   common_interests))


matchmaking()


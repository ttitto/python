def matchmaking():
    people = [
        {
            'name': "Мария",
            'interests': ['пътуване', 'танци', 'плуване', 'кино'],
            'gender': "female",
        },
        {
            'name': "Диана",
            'interests': ['мода', 'спортна стрелба', 'четене', 'скандинавска поезия'],
            'gender': "female",
        },
        {
            'name': "Дарина",
            'interests': ['танци', 'покер', 'история', 'софтуер'],
            'gender': "female",
        },
        {
            'name': "Лилия",
            'interests': ['покер', 'автомобили', 'танци', 'кино'],
            'gender': "female",
        },
        {
            'name': "Галя",
            'interests': ['пътуване', 'автомобили', 'плуване', 'баскетбол'],
            'gender': "female",
        },
        {
            'name': "Валерия",
            'interests': ['плуване', 'покер', 'наука', 'скандинавска поезия'],
            'gender': "female",
        },
        {
            'name': "Ина",
            'interests': ['кино', 'лов със соколи', 'пътуване', 'мода'],
            'gender': "female",
        },
        {
            'name': "Кирил",
            'interests': ['баскетбол', 'автомобили', 'кино', 'наука'],
            'gender': "male",
        },
        {
            'name': "Георги",
            'interests': ['автомобили', 'футбол', 'плуване', 'танци'],
            'gender': "male",
        },
        {
            'name': "Андрей",
            'interests': ['футбол', 'скандинавска поезия', 'история', 'танци'],
            'gender': "male",
        },
        {
            'name': "Емил",
            'interests': ['летене', 'баскетбол', 'софтуер', 'наука'],
            'gender': "male",
        },
        {
            'name': "Димитър",
            'interests': ['футбол', 'лов със соколи', 'автомобили', 'баскетбол'],
            'gender': "male",
        },
        {
            'name': "Петър",
            'interests': ['пътуване', 'покер', 'баскетбол', 'лов със соколи'],
            'gender': "male",
        },
        {
            'name': "Калоян",
            'interests': ['история', 'покер', 'пътуване', 'автомобили'],
            'gender': "male",
        },
    ]
    people_interests_sets = {}
    for i, p1 in enumerate(people):
        for j, p2 in enumerate(people[i:]):
            common_interests = set(people[i]['interests']).intersection(set(people[j]['interests']))
            if len(common_interests) > 0 and p1['gender'] != p2['gender']:
                print('{} и {} - общи интереси: {}'.format(p1['name'], p2['name'], common_interests))


matchmaking()

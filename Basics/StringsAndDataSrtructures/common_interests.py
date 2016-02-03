def common_interests():
    ivan = ['пушене', 'пиене', 'тия три неща', 'коли', 'facebook', 'игри', 'разходки по плажа', 'скандинавска поезия']
    maria = ['пиене', 'мода', 'facebook', 'игри', 'лов със соколи', 'шопинг', 'кино']
    ivan_interests = set(ivan)
    maria_interests = set(maria)
    common = ivan_interests.intersection(maria_interests)
    print('Мария и Иван - общи интереси: {}'.format(common))

common_interests()

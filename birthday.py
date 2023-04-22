from datetime import datetime, timedelta


week_days = {
   0: 'Monday',
   1: 'Tuesday',
   2: 'Wednesday',
   3: 'Thursday',
   4: 'Friday',
   5: 'Saturday',
   6: 'Sunday',
}
    
def get_birthdays_per_week(users):
    result = {
        'Monday':[],
        'Tuesday':[],
        'Wednesday':[],
        'Thursday':[],
        'Friday':[]
    }

    today = datetime.now() 
    # today = datetime(year=1995, month=4, day=24)
    start_of_weekend_day = today - timedelta(days = 2)
    end_of_weekday = today + timedelta(days = 4 - today.weekday())
    for item in users:
        birthday_date = item['birthday']
        if today.weekday() == 0:
            if today.month == birthday_date.month and start_of_weekend_day.day <= birthday_date.day < today.day:
                result['Monday'].append(item['name'])
        if today.day <= birthday_date.day <= end_of_weekday.day:
            result[week_days[birthday_date.weekday()]].append(item['name'])
        elif today.weekday() in (5, 6):
            return f'Today is {week_days[today.weekday()]}, try again in Monday'

    res = ''
    for key, values in result.items():
        if len(values) == 0:
            continue
        else:
            name = ', '.join(values)
            res += f'{key}: {name}\n'

    return res[:-1]

print(get_birthdays_per_week([
                            {'name':'Ivan', 'birthday':datetime(year=1995, month=4, day=20)}, #Thursday
                            {'name':'Oleg', 'birthday':datetime(year=1995, month=4, day=16)}, #Sunday
                            {'name':'Alex', 'birthday':datetime(year=1995, month=4, day=17)}, #Monday
                            {'name':'Dima', 'birthday':datetime(year=1995, month=4, day=15)}, #Saturday
                            {'name':'Julia', 'birthday':datetime(year=1995, month=4, day=18)}, #Wednesday
                            {'name':'Kate', 'birthday':datetime(year=1995, month=4, day=19)}, #Thursday
                            {'name':'Irina', 'birthday':datetime(year=1995, month=4, day=21)}, #Friday
                            {'name':'Jane', 'birthday':datetime(year=1995, month=4, day=23)}, #Sunday
                            {'name':'Vasya', 'birthday':datetime(year=1995, month=4, day=25)}, #Tuesday
                            {'name':'Petro', 'birthday':datetime(year=1995, month=4, day=27)} #Thursday
                            ]))
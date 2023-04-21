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
    start_of_weekday = today - timedelta(days = today.weekday() + 2)
    end_of_weekday = start_of_weekday + timedelta(days = 6)
    for item in users:
        day = item['birthday']
        if today.month == day.month and start_of_weekday.day <= day.day <= end_of_weekday.day:
            if day.weekday() in (5, 6, 0):
                result['Monday'].append(item['name'])
            else:
                result[week_days[day.weekday()]].append(item['name'])

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
                            {'name':'Alex', 'birthday':datetime(year=1996, month=4, day=17)}, #Wednesday
                            {'name':'Dima', 'birthday':datetime(year=1996, month=4, day=15)}, #Monday
                            {'name':'Julia', 'birthday':datetime(year=1996, month=4, day=16)}, #Tuesday
                            {'name':'Irina', 'birthday':datetime(year=1996, month=4, day=19)}, #Friday
                            {'name':'Vasya', 'birthday':datetime(year=1996, month=4, day=25)}, #Thursday
                            {'name':'Petro', 'birthday':datetime(year=1998, month=4, day=25)} #Saturday
                            ]))

# a = datetime(year=1996, month=4, day=19)
# print(a.weekday())
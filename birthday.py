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
    end_day = today + timedelta(days = 6)
    for item in users:
        day = item['birthday']
        if today.month == day.month and today.day <= day.day <= end_day.day:
            if day.weekday() in (5, 6):
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
                            {'name':'Ivan', 'birthday':datetime(year=1995, month=4, day=22)}, #Saturday
                            {'name':'Alex', 'birthday':datetime(year=1996, month=5, day=18)}, #Saturday
                            {'name':'Dima', 'birthday':datetime(year=1996, month=4, day=24)}, #Wednesday
                            {'name':'Vasya', 'birthday':datetime(year=1996, month=4, day=25)}, #Thursday
                            {'name':'Petro', 'birthday':datetime(year=1998, month=4, day=25)} #Saturday
                            ]))
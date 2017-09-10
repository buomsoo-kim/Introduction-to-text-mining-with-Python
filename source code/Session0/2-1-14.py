data = []
with open('enrollments.csv', 'r') as f:
    lines = f.readlines()[1:]
    for line in lines:
        line = line.split(',')
        dic = {'account_key': line[0], 'status': line[1], 'join_data': line[2], 'cancel_data': line[3], 'days_to_cancel': line[4], 'is_udacity': line[5], 'is_canceled': line[6]}
        data.append(dic)
    f.close()
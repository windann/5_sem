from id_from_username import IdFromUsername
from friends import GetFriends
import list_friends
import datetime

import matplotlib.pyplot as plt
user_id = input('Введите id или shortname пользователя: ')
param = {'user_ids': user_id}

my_vk = IdFromUsername()
my_vk.get_params(param)
res = my_vk.execute()

friends_list = GetFriends(my_vk.uid)
param_f = {'uid': my_vk.uid, 'fields': 'bdate'}

b_days = []
for person in friends_list._get_data_f(param_f):
    try:
        b_days.append(person['bdate'])
    except KeyError:
        pass

ages = []

for date in b_days:
    try:
        birthday = datetime.datetime.strptime(date, '%d.%m.%Y').date()
        age = list_friends.get_age(birthday)
        ages.append(age)
    except ValueError:
        pass

print_ages = list_friends.get_histogram(ages)

list_friends.print_histogram(print_ages)

x_axis = []

for x in print_ages.keys():
    x_axis.append(x)

y_axis = []

for y in print_ages.values():
    y_axis.append(y)

plt.bar(x_axis, y_axis, align='center')
plt.title(res['first_name'] + ' ' + res['last_name'])
plt.ylabel('Количество друзей.')
plt.xlabel('Возраст друзей.')
plt.show()

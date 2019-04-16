#optional.sock_sorter.py
import random

#My attempts
# sock_types = ['ankle', 'crew', 'calf', 'thigh']
# count = range(0,100)
#
# for item in sock_types:
#     sock_types.append(item)
#
# print(sock_types)
#for index, count in enumerate(sock_types, 1):
    # index +=
    # print(index, count)

# random_socks = dict(zip(random.choice(sock_types), range(100)))
#
# for i in sock_types:
#
# print(random_socks)


#class answers
sock_list = []
sock_types = ['ankle', 'crew', 'calf', 'thigh']
colors = ['black', 'white', 'blue']
sock_counter = {}
for i in range(100):
    sock = random.choice(sock_types)
    color = random.choice(colors)
    sock_list.append((sock, color))

    sock_counter[(sock, color)] = sock_counter.get((sock, color), 0) + 1
#line 28 is basically the following 4 lines in 1. boom.
# if sock in sock_counter:
#     sock_counter[sock] += 1
# else:
#     sock_counter[sock] = 1

print(sock_list)
print(sock_counter)

for sock in sock_counter:
    #safer route where it will grab the key if it is in the dict
    print(f'{sock} has {sock_counter.get(sock)%2} loner(s)')
    #can return error if the key is not in the dict
    #print(f'{sock} has {sock_counter[sock]%2} loner(s)')

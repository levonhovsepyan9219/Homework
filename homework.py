# ex 1

# with open("data.pickle", "rb") as data:
#     list2 = list(filter(lambda x: not x % 3, pickle.load(data)))
# print(sum(list2) / len(list2))

# ex 2

# dict_1 = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# dict_2 = {dict_1[i]: len(dict_1[i]) for i in dict_1}
# print(dict_2)

# ex 3
#
# dict1 = {'a': [1, 8, 3, 7, 2], 'b': [12, 4, 8, 4], 'c': [9, 9, 2, 8, 5]}
# dict2 = {i: list(filter(lambda x: x % 2 != 0, dict1[i])) for i in dict1}
# print(dict2)

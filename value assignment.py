import random

my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 1,2,3,4,5,6,7,8,9,0]

random.shuffle(my_list)

for i in range(len(my_list)):
    random_choice = my_list[i]
    print(random_choice)

if len(my_list) == 0:
    print("You have chosen all elements in the list.")

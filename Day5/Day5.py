import re

with open('Day5/test_input2.txt') as f:
    lines = f.readlines()

# # test case
# stack1 = ['Z', 'N']
# stack2 = ['M', 'C', 'D', 'J', 'L', 'Z']
# stack3 = ['P']

# problem case
stack1 = ['Z', 'J', 'N', 'W', 'P', 'S']
stack2 = ['G', 'S', 'T']
stack3 = ['V', 'Q', 'R', 'L', 'H']
stack4 = ['V', 'S', 'T', 'D']
stack5 = ['Q', 'Z', 'T', 'D', 'B', 'M', 'J']
stack6 = ['M', 'W', 'T', 'J', 'D', 'C', 'Z', 'L']
stack7 = ['L', 'P', 'M', 'W', 'G', 'T', 'J']
stack8 = ['N', 'G', 'M', 'T', 'B', 'F', 'Q', 'H']
stack9 = ['R', 'D', 'G', 'C', 'P', 'B', 'Q', 'W']


crate_dict = {'1': stack1, '2': stack2, '3': stack3, '4': stack4,
              '5': stack5, '6': stack6, '7': stack7, '8': stack8, '9': stack9}

def crane9000(num, crate_from, crate_to):

    for i in range(num):
        crate_to.append(crate_from.pop())

def crane9001(num, crate_from, crate_to):
    count = 0
    for i in range(num):
        crate_to.append(crate_from.pop(-(num-count)))
        count += 1




for row in lines:
    vals = re.findall('\d+', row)
    print(vals)
    crane9001(int(vals[0]), crate_dict[vals[1]], crate_dict[vals[2]])
    print("1 ", stack1)
    print("2 ", stack2)
    print("3 ", stack3)
    print("4 ", stack4)
    print("5 ", stack5)
    print("6 ", stack6)
    print("7 ", stack7)
    print("8 ", stack8)
    print("9 ", stack9)
    print('-'*20)

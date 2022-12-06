with open('test_input2.txt') as f:
    lines = f.readlines()
    
data = [x for x in lines[0][:-1]]

num = 4

def day6(NUM_UNIQUE=4):
    i = 0
    while i <= len(data):
        check = []
        check.extend(data[i-NUM_UNIQUE:i])
        print(check)
        print(i)
        if len(set(check)) == NUM_UNIQUE:
            print("Unique: ", i)
            break
        i += 1

day6(num)
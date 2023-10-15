N = 12
#print(N)
input = ['insert 0 5', 'insert 1 10', 'insert 0 6', 
         'print', 'remove 6', 'append 9', 'append 1', 
         'sort', 'print', 'pop', 'reverse', 'print']
output = []

for i in range(N):
    print(input[i])
    parts = input[i].split()
    #print(len(parts))
    if parts[0] == "insert":
        output.insert(int(parts[1]), int(parts[2]))
    if parts[0] == "print":
        print(output)
    if parts[0] == "remove":
        output.remove(int(parts[1]))
    if parts[0] == "append":
        output.append(int(parts[1]))
    if parts[0] == "sort":
        output.sort()
    if parts[0] == "pop":
        output.pop()
    if parts[0] == "reverse":
        output.reverse()
    print(output)
    print("=======================================")
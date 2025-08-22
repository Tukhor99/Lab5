req_seq = []
visited = []

n = int(input("Enter number of requests: "))

i = 0
while i < n:
    x = int(input("Enter into array: "))
    req_seq.append(x)
    i += 1

head = 5
seek = 0
visited.append(head)

for i in range(len(req_seq)):
    found = False
    
   
    for j in range(len(visited)):
        if req_seq[i] == visited[j]:
            found = True
    
    if found:
        continue
    
    seek += abs(head - req_seq[i])
    visited.append(req_seq[i])
    head = req_seq[i]

print(seek)

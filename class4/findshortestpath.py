from collections import deque
def createnicknames():
    nicknames = {}
    list_nicknames=[]
    with open("nicknames.txt") as file:
        for line in file:
            (value, key) = line.split()
            nicknames[key] = int(value)
            list_nicknames.append(key)
    return nicknames, list_nicknames
#create dictionary called links
def createlinks(nicknames):
    links = {}
    total_users = len(nicknames.keys())
    for i in range(0, total_users):
        links.setdefault(i,[])
    with open("links.txt") as file:
        for line in file:
            (key, value) = line.split()
            links[int(key)].append(int(value))
    return links

def findnode(nicknames,name):
    total_users = len(nicknames.keys())
    if name in nicknames.keys():
        node = nicknames[name]
        return node
    return total_users+100

#Find if there is any path from self_node to target_node
def findpath (links,self_node, target_node):
    N = len(links.keys())
    visited = []
    #create queue for BFS
    queue = deque()
    #mark self_node as visited and enqueue
    queue.append(self_node)
    previous_node = [N for i in range (N)]
    while (len(queue)> 0) :
            #get current node from the first node in queue
            current_node = queue.popleft()
            #mark current node as visited
            if current_node == target_node:
                print('Path founded')
                # print(previous_node)
                return previous_node
            if current_node not in visited:
                visited.append(current_node)
            #if still cannot find path, add neighbour nodes to queue
                for nodes in links[current_node]:
                    queue.append(nodes)
                    if previous_node[nodes] == N:
                        previous_node[nodes]=current_node    
    return []

def findshorttestpath(self_name, target_name):
    nicknames, list_nicknames = createnicknames()
    links = createlinks(nicknames)
    total_users = len(nicknames.keys())
    self_node = findnode(nicknames,self_name)
    target_node = findnode(nicknames,target_name)
    if self_node >= total_users or target_node >= total_users:
        ans = 'invalid input'
        return ans
    path=deque()
    parents = findpath (links,self_node, target_node)
    # print(len(parents))
    if len(parents) !=0:
        current_node = target_node
        path.append(list_nicknames[current_node])
        while current_node != self_node:
            # print(current_node)
            next_node = parents[current_node]
            path.appendleft(list_nicknames[next_node])
            current_node = next_node
        # path.appendleft(self_node)
        return list(path)
    ans = 'Cannot find any path'
    return ans

def main():
    print('Enter your nickname:')
    self_name = input()
    print('Who do you want to find:')
    target_name = input()
    print(findshorttestpath(self_name,target_name))
    

if __name__ == '__main__':
    main()
    


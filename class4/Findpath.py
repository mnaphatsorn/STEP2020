#create dictionary called nicknames
def createnicknames():
    nicknames = {}
    with open("nicknames.txt") as file:
        for line in file:
            (value, key) = line.split()
            nicknames[key] = int(value)
    return nicknames

#create dictionary called links
def createlinks(nicknames):
    links = {}
    total_users = len(nicknames.key())
    for i in range(0, total_users):
        links.setdefault(i,[])
    with open("links.txt") as file:
        for line in file:
            (key, value) = line.split()
            links[int(key)].append(int(value))
    return links

def findnode(nicknames,name):
    total_users = len(nicknames.key())
    if nicknames.has_key(name):
        node = nicknames[name]
        return node
    print('name not founded')

#Find if there is any path from self_node to target_node
def findpath (nicknames, links, self_name, target_name):
    total_users = len(nicknames.key())
    self_node = findnode(nicknames, self_name)
    target_node = findnode(nicknames, target_name)
    print('Find path from', self_name,'to',target_name)
    visited = []
    #create queue for BFS
    queue = []
    #mark self_node as visited and enqueue
    visited.append(self_node)
    queue.append(self_node)
    while (len(queue)> 0) :
            #get current node from the first node in queue
            current_node = queue.pop(0)
            #mark current node as visited
            visited.append(current_node)
            #found path
            if current_node == target_node:
                print('Path founded')
                return 0
            #if still cannot find path, add neighbour nodes to queue
            elif len(links[current_node])==0:
                continue
            for nodes in links[current_node]:
                if nodes not in visited:
                    queue.append(nodes)
    print('Cannot find any path')
    return 0

def Test(nicknames, links):
    print('=====Test Started======')
    #some test cases
    findpath(nicknames, links,'joan','adrian')
    findpath(nicknames, links,'joan','cody')
    findpath(nicknames, links, 'joan','betty')
    findpath(nicknames, links, 'joan','carolyn')
    findpath(nicknames, links, 'cody','adrian')
    findpath(nicknames, links, 'joan','joan')
    findpath(nicknames, links, 'lawrence','adrian')
    print('=====Test Ended======')

def main():
    nicknames = createnicknames()
    links = createlinks()
    Test(nicknames, links)

    

if __name__ == '__main__':
    main()
    


    




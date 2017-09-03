def readInput(path):
    f = open(path)
    nb_rows,nb_slots,nb_unavailable,nb_pools,nb_servers = [int(i) for i in f.readline().split(' ')]
    datacenter = []
    for i in range(nb_rows):
        datacenter.append([0] * nb_slots)
    unavailable = []
    servers = []
    for i in range(nb_unavailable):
        x,y = [int(i) for i in f.readline().split(' ')]
        unavailable.append((x,y))
        datacenter[x][y] = -1
    for i in range(nb_servers):
        s,c = [int(i) for i in f.readline().split(' ')]
        servers.append((s,c))
    print('rows: ' + str(nb_rows) + 'slots: ' + str(nb_slots))
    print(datacenter)
    print('nb unavailable: ' + str(nb_unavailable))
    print(unavailable)
    print('nb servers: ' + str(nb_servers))
    print(servers)
    f.close()
    return datacenter,unavailable,servers 

def giveOutput(nb_servers, server):
    for r,s,p in server:
        print(str(r) + ' ' + str(s) + ' ' + str(p))
    for i in range(nb_servers - len(server)):
        print(x)

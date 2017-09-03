import server.py
import pool.py

def readInput(path):
    f = open(path)
    nb_rows,nb_slots,nb_unavailable,nb_pools,nb_servers = [int(i) for i in f.readline().split(' ')]
    datacenter = []
    
    for i in range(nb_rows):
        datacenter.append([0] * nb_slots)
    
    unavailable = []
    servers = []
    pools = []
    
    for i in range(nb_unavailable):
        x,y = [int(i) for i in f.readline().split(' ')]
        unavailable.append((x,y))
        datacenter[x][y] = -1
    
    for i in range(nb_servers):
        s,c = [int(i) for i in f.readline().split(' ')]
        servers.append(server.server((-1,-1),s,c,1,i))
    
    for i in range(nb_pool):
        pools.append(pool.pool([],float('inf'))

    print('rows: ' + str(nb_rows) + 'slots: ' + str(nb_slots))
    print(datacenter)
    print('nb unavailable: ' + str(nb_unavailable))
    print(unavailable)
    print('nb servers: ' + str(nb_servers))
    print(servers)
    f.close()
    return datacenter,unavailable,servers,pools

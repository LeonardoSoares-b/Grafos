g_list=[[1,3],
        [0,3],
        [3],
        [0,1,2]]

is_neighbor = False
for neighbor in g_list[3]:
    if neighbor ==2:
        neighbor=True
        break
    print(is_neighbor)
print(g_list[2])

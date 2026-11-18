def min_max_scaling(data: list) -> list:
    mins=[]
    maxs=[]
    for i in range(len(data[0])):
        col = [j[i] for j in data]
        mins.append(min(col))
        maxs.append(max(col))
    res=[]
    for i in range(len(data)):
        r=[]
        for j in range(len(data[0])):
            if maxs[j]==mins[j]:
                 r.append(0.0)
            else:
                r.append((data[i][j] - mins[j])/(maxs[j]-mins[j]))
        res.append(r)
    return res
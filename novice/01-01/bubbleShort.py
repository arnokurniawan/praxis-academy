def bubblesort(data):
    iterasi = 0
    for j in range(len(data)-1):
        for i in range(len(data)-1-j):
            if data[i]>data[i+1]:
                data[i],data[i+1]=data[i+1],data[i]
        iterasi+=1
        print(iterasi,data)
 
data = [8,6,1,35,7,3,4]
bubblesort(data)
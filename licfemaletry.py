import os

data=dict()
base='/home/ashwin/Downloads/Results/female/'
once=0
indexes=[]
total=0
res=[]
res.append("female")
for i in range(1,82):
        res.append(0.0)

for filename in os.listdir(base):
    with open(base+filename,"r") as f:

        first = 0
        for line in f:
            line=line.rstrip()
            if once==0:
                indexes=line.split("\t")
                once=1

            if first==0:
                first=1
            else:
                total+=1
                values=line.split("\t")
                for i in range(1,len(values)):
                    res[i]+=float(values[i])

for i in range(0,82):
    if i==0:
        print indexes[i],"\t",res[i]
    else:
        print indexes[i],"\t",float(res[i])/total


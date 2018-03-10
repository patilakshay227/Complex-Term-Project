import simplejson as json
import pickle

def main():
    skip=1
    done=1
    good = open("good", "a")
    with open("dailyComments") as f:
        for line in f:
            try:
                line = line.split("\t")[2]
                value=json.loads(line.rstrip())
                val=json.dumps(value)
                good.write(val+"\n")
                done += 1
            except:
                skip+=1
    good.close()
    print "done ",done

myd=dict()
def readids():
    with open("/home/akshay/IIT KGP/SEM 2/Complex Network/Term Project/articleJSON.txt") as f:
        for line in f:
            line=json.loads(line)            
            for l in line['response']['docs']:
                print l['headline']

            break
    for key in myd.keys():
        print key,' : ', myd[key]

if __name__ == "__main__":
	readids()

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
    with open("/media/ashwin/E0C62B17C62AED8A/Study material/IIT Kgp/Sem2/Comple/Project/good") as f:
        for line in f:
            line=json.loads(line)            
            for l in line['results']['comments']:
                print l.keys()
                break
                id=l['assetID']
                if l['commentTitle']!='<br/>':
                    print l['commentTitle']
            break
    for key in myd.keys():
        print key,' : ', myd[key]

if __name__ == "__main__":
	readids()

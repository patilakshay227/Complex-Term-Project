from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import time

d=dict()
cache=dict()

count=0

cleanLog=open("cleanLogLoc1","w")
tout=open("errorLog1","w")
geolocator = Nominatim(timeout=10)


def getState(line):
    data = line.split(";")
    data[0] = data[0].strip()
    data[1] = data[1].strip()

    try:
        if cache.has_key(data[1]):
            s=cache[data[1]]
            if d.has_key(s):
                d[s].append(data[0])
            else:
                d[s] = list()
                d[s].append(data[0])
            return

        location = geolocator.geocode(data[1], addressdetails=True)
        if location is not None and location.raw['address']['country_code'] == 'us':
            s = location.raw['address']['state']
            cache[data[1]]=s
            print s

            if d.has_key(s):
                d[s].append(data[0])
            else:
                d[s] = list()
                d[s].append(data[0])
        else:
            pass
            print "not us",line
            cleanLog.write(line + "\n")
    except GeocoderTimedOut:
        time.sleep(1000.0 / 1000.0)
        print "timeout error",line
        getState(line)
    except Exception as e:
        print " Exception error",line
        print e
        tout.write(line)


with open("errorLog") as loc:
    for line in loc:
        getState(line)
        count+=1
        if count % 100 == 0:
            print "Processed records : ",count





print "Number of keys",len(d.keys())
print "total count",count

tout.close()
cleanLog.close()

result=open("Result1","w")

for key in d.keys():
    try:
        l=d[key]
        str=key+";"+'\t'.join(l)
        result.write(str+"\n")
    except Exception as e:
        print "Error writing line ",key

result.close()

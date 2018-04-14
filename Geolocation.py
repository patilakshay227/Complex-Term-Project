import traceback
import time
from geopy.geocoders import GoogleV3


log=open('locationLog1','w')
res=open("locRes1",'w')

keys=['AIzaSyAAea7RCoy1luku6OyHVydrf9i82DJTnt0','AIzaSyALXN5k6WqXWGyQYtYPQXvq4_q5zHljVE4',
'AIzaSyD7WVmnz42ulfpfDzOSBsvlHf9R3YrU28Q','AIzaSyAVwyecBq_0wDSsXuZ5WZ-T3_7sgL5r7rk','AIzaSyCupZxIcCkF9NqvDbt9IPzltqs9QYrPBv4','AIzaSyADRa4OhvyYXELB5tjoV88DowbW0tdSUp0',
      'AIzaSyCIJWSs6YA6CeXHNAh_RdqHrAhndMWK5rk','AIzaSyBgDhnb21QWL6-6sV6dgFjr6dJmBkeJI1s',
      'AIzaSyDaUjHuSn4ysjCoDJRq4LgLc7NT5Hp3MH4','AIzaSyCcr5ZEmzm4qikKGCzcaI4xGEt0rMlLdiM',
      'AIzaSyBNIVAr7LNtVS15C1MV3tqYuzxcQ1TMgsY','AIzaSyDRmnJX9iwPLV-lH6GZoJpA3PX501WYjao',
      'AIzaSyDqAJICmUm8xO_3ZVZ8HEY7Dl8P7sno6HE','AIzaSyACYXZIbBG_HIXv5Ax1UABU8D3rhN-eGbw',
      'AIzaSyCq3FQX7Uhhp3dXOetkfLEFS9OBPd1WFCE']

keylen=len(keys)
i=0
count=0
with open("/media/ashwin/E0C62B17C62AED8A/Study material/IIT Kgp/Sem2/Comple/Github/Complex-Term-Project/locdata1.txt") as loc:
    for line in loc:
        line=line.strip()
        curkey=keys[i]
        try:
            geolocator = GoogleV3(api_key=curkey)
            location = geolocator.geocode(line, language='en', timeout=10)
            if location != None:
                res.write(line+";"+location.address.encode('utf-8')+"\n")
                print line,location.address
            else:
                log.write("No location!,"+line+','+location+"\n")
        except Exception as e:
            log.write(line+','+traceback.format_exc()+"\n")
        i+=1
        i=i%keylen
        count+=1
        if count%100 == 0 :
            print count," no proccessed"
        time.sleep(200.0/1000.0)
log.close()
res.close()

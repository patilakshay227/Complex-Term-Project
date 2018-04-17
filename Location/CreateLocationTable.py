import sys
reload(sys)
sys.setdefaultencoding('utf8')
import sqlite3

db = sqlite3.connect('../../commentsData.db')
stateToRegion = {
    'Washington': "West",
    'Oregon': "West",
    'California': "West",
    'Hawaii': "West",
    'Alaska': "West",

    'Montana': "West",
    'Idaho': "West",
    'Wyoming': "West",
    'Nevada': "West",
    'Utah': "West",
    'Colorado': "West",
    'Arizona': "West",
    'New Mexico': "West",

    'North Dakota': "MidWest",
    'Minnesota': "MidWest",
    'South Dakota': "MidWest",
    'Nebraska': "MidWest",
    'Iowa': "MidWest",
    'Kansas': "MidWest",
    'Missouri': "MidWest",

    'Texas': "South",
    'Oklahoma': "South",
    'Arkansas': "South",
    'Louisiana': "South",

    'Wisconsin': "MidWest",
    'Illinois': "MidWest",
    'Indiana': "MidWest",
    'Michigan': "MidWest",
    'Ohio': "MidWest",

    'Kentucky': "South",
    'Tennessee': "South",
    'Mississippi': "South",
    'Alabama': "South",

    'West Virginia': "South",
    'Maryland': "South",
    'Virginia': "South",
    'North Carolina': "South",
    'South Carolina': "South",
    'Georgia': "South",
    'Florida': "South",
    'Delaware': "South",
    'District of Columbia': "South",

    'New York': "North East",
    'New Jersey': "North East",
    'Pennsylvania': "North East",

    'Maine': "North East",
    'Connecticut': "North East",
    'Rhode Island': "North East",
    'Massachusetts': "North East",
    'New Hampshire': "North East",
    'Vermont': "North East",

    'Puerto Rico': "U.S. territory",
    'United States Virgin Islands': "U.S. territory",
    'American Samoa': "U.S. territory",
    'Guam': "U.S. territory"

}

c = db.cursor()
db.text_factory = str

c.execute("create table if not exists locationState(city text,state text,region text,\
PRIMARY KEY(city,state))")
sqlstat="insert into locationState values(?,?,?)"

exclude = ['American Samoa', 'District of Columbia', 'Guam', 'Puerto Rico', 'United States Virgin Islands']

count = 0
s = list()
with open("Result", "r") as r:
    for line in r:
        state = line.split(";")[0]
        s.append(state)
        data = line.split(";")[1].split("\t")
        count += len(data)
        for d in data:
                try:
                    c.execute(sqlstat, (d,state,stateToRegion[state]))
                except sqlite3.IntegrityError as e:
                    print "key error on tuple ",state,e," execpt:",str(e)
db.commit()
db.close()

print count," records inserted"
print len(s)," states"
s = sorted(s)
for name in s:
    print name

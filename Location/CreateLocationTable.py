import sys
reload(sys)
sys.setdefaultencoding('utf8')
import sqlite3

db = sqlite3.connect('../../commentsData.db')
stateToRegion = {
    'Washington': "Pacific",
    'Oregon': "Pacific",
    'California': "Pacific",
    'Hawaii': "Pacific",
    'Alaska': "Pacific",

    'Montana': "Mountain",
    'Idaho': "Mountain",
    'Wyoming': "Mountain",
    'Nevada': "Mountain",
    'Utah': "Mountain",
    'Colorado': "Mountain",
    'Arizona': "Mountain",
    'New Mexico': "Mountain",

    'North Dakota': "West North Central",
    'Minnesota': "West North Central",
    'South Dakota': "West North Central",
    'Nebraska': "West North Central",
    'Iowa': "West North Central",
    'Kansas': "West North Central",
    'Missouri': "West North Central",

    'Texas': "West South Central",
    'Oklahoma': "West South Central",
    'Arkansas': "West South Central",
    'Louisiana': "West South Central",

    'Wisconsin': "East North Central",
    'Illinois': "East North Central",
    'Indiana': "East North Central",
    'Michigan': "East North Central",
    'Ohio': "East North Central",

    'Kentucky': "East South Central",
    'Tennessee': "East South Central",
    'Mississippi': "East South Central",
    'Alabama': "East South Central",

    'West Virginia': "South Atlantic",
    'Maryland': "South Atlantic",
    'Virginia': "South Atlantic",
    'North Carolina': "South Atlantic",
    'South Carolina': "South Atlantic",
    'Georgia': "South Atlantic",
    'Florida': "South Atlantic",
    'Delaware': "South Atlantic",
    'District of Columbia': "South Atlantic",

    'New York': "Middle Atlantic",
    'New Jersey': "Middle Atlantic",
    'Pennsylvania': "Middle Atlantic",

    'Maine': "New England",
    'Connecticut': "New England",
    'Rhode Island': "New England",
    'Massachusetts': "New England",
    'New Hampshire': "New England",
    'Vermont': "New England",

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

import sqlite3

db = sqlite3.connect('../../commentsData.db')
c = db.cursor()

stateToRegion = {
    'Washington': "Pacific",
    'Oregon':"Pacific",
    'California': "Pacific",
    'Hawaii' : "Pacific",
    'Alaska': "Pacific",

    'Montana':"Mountain",
    'Idaho':"Mountain",
    'Wyoming':"Mountain",
    'Nevada':"Mountain",
    'Utah': "Mountain",
    'Colorado': "Mountain",
    'Arizona':"Mountain",
    'New Mexico': "Mountain",

    'North Dakota': "West North Central",
    'Minnesota':"West North Central",
    'South Dakota':"West North Central",
    'Nebraska':"West North Central",
    'Iowa': "West North Central",
    'Kansas':"West North Central",
    'Missouri':"West North Central",

    'Texas':"West South Central",
    'Oklahoma':"West South Central",
    'Arkansas':"West South Central",
    'Louisiana': "West South Central",

    'Wisconsin': "East North Central",
    'Illinois': "East North Central",
    'Indiana': "East North Central",
    'Michigan' : "East North Central",
    'Ohio': "East North Central",

    'Kentucky': "East South Central",
    'Tennessee': "East South Central",
    'Mississippi': "East South Central",
    'Alabama': "East South Central",

    'West Virginia': "South Atlantic",
    'Maryland': "South Atlantic",
    'Virginia': "South Atlantic",
    'North Carolina': "South Atlantic",
    'South Carolina' : "South Atlantic",
    'Georgia': "South Atlantic",
    'Florida': "South Atlantic",
    'Delaware': "South Atlantic",
    'District of Columbia' : "South Atlantic",

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


with open('./Result') as f:
    for line in f:
        if len(line.strip()) == 0:
            continue
        tok = line.split(';',1)
        if len(tok) < 2:
            print len(tok),line
            continue
        st = tok[0]
        names = tok[1].split('\t')
        print st
        for n in names:
            try:
                c.execute('update comments set Location = ?,country = ?,locationRegion = ? where userLocation = ?', (st, 'US', stateToRegion[st], n))
            except Exception as e:
                with open('updateErrors','a') as ef:
                    ef.write(str(st)+ str(n) + '\t' + str(e.message) + '\n')
db.commit()
db.close()

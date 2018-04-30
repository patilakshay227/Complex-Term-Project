import sqlite3
import numpy as np

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

db = sqlite3.connect('../../commentsData.db')
c = db.cursor()

sqlStatement = 'select t.commentID,t.liwc  from commentsLIWC t, comments c, locationState ls where ls.city = c.userLocation and c.commentID = t.commentID  and t.gender = ? and ls.region = ?'

regions =  set(stateToRegion.values())
regions.add('others')

sum = np.zeros(shape=(1,81))[0]






with open('regionwiseData.txt','w') as f:
    for r in regions:
        sum = np.zeros(shape=(1,81))[0]
        count = 0
        print r
        c.execute(sqlStatement, ('male', r))
        mcount = 0
        msum = np.zeros(shape=(1, 81))[0]
        for res in c.fetchall():
            liwc = res[1].split('\t')
            if len(liwc) != 81:
                continue

            mcount +=1
            count+=1
            vec = np.array(liwc, dtype='float')
            sum = sum + vec
            msum = msum + vec

            # if count % 100 == 0:
            #     print count

        c.execute(sqlStatement, ('female', r))

        fcount = 0
        fsum = np.zeros(shape=(1, 81))[0]
        for res in c.fetchall():
            liwc = res[1].split('\t')
            if len(liwc) != 81:
                continue

            fcount += 1
            count += 1
            vec = np.array(liwc, dtype='float')
            sum = sum + vec
            fsum = fsum + vec

        
        #f.write(r+'\n\n'+ 'Male\t' + '\t'.join(str(v) for v in ((msum/mcount)).tolist()) + '\n')
        #f.write('Female\t' + '\t'.join(str(v) for v in ((fsum/fcount)).tolist()) + '\n')
        f.write('Overall\t'+ '\t'.join(str(v) for v in (sum/count).tolist()) + '\n')
        f.write('\n')
        
                #print  res[0], len(res[1].split('\t')), res[1]





db.commit()
c.close()
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 20:45:43 2018

@author: Ashwin
"""
import simplejson as json
import pickle
import datetime
import sqlite3
import traceback
import dateutil.parser as dp

inputFile = "../../Project/articleJSON.txt"

db = sqlite3.connect('../commentdata.db')

c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS ArticleKeywords(id text,keyword text,PRIMARY KEY(id,keyword) ) ')


def writeArticleInDB(article):
    ID = article['_id']
    keywords = article['keywords']
    sqlStat = "INSERT INTO ArticleKeywords VALUES(?,?)"
    records=[]
    if article:
        for k in keywords:
            records.append((ID,k['value']))
    if len(records) > 0:
        c.executemany(sqlStat,records)

def parseFile():
    noOfLinesParsed = 0
    with open(inputFile) as f:
        for line in f:
            try:
                noOfLinesParsed += 1
                line = json.loads(line)

                for record in line['response']['docs']:
                    writeArticleInDB(record)

                if (noOfLinesParsed % 1000 == 0):
                    print "No of lines Parsed : ", noOfLinesParsed
            except Exception as e:
                if e.message!='response':
                    with open("log", "a") as log:
                        log.write("Error on line " + str(noOfLinesParsed) + "\n")
                        log.write(traceback.format_exc())

        db.commit()


if __name__ == "__main__":
    parseFile()
    db.close()

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
import os
import dateutil.parser as dp


if os.path.exists("sectionintegritylog"):
    os.remove("sectionintegritylog")

inputFile = "/home/akshay/IIT KGP/SEM 2/Complex Network/Term Project/articleJSON.txt"

db = sqlite3.connect('../commentsData.db')

c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS ArticleSection(id text,section text,PRIMARY KEY(id,section) ) ')


def writeArticleInDB(article):
    ID = article['_id']
    secName = article['section_name']
    sqlStat = "INSERT INTO ArticleSection VALUES(?,?)"

    if secName!=None and secName!='':
        c.execute(sqlStat,(ID,secName))

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
            except sqlite3.IntegrityError as i:
                    with open("sectionintegritylog", "a") as ilog:
                        ilog.write("Line no : " + str(noOfLinesParsed) + "\n")
            except Exception as e:
                if e.message!='response':
                    with open("log", "a") as log:
                        log.write("Error on line " + str(noOfLinesParsed) + "\n")
                        log.write(traceback.format_exc())

        db.commit()


if __name__ == "__main__":
    parseFile()
    db.close()

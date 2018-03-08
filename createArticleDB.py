#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 20:45:43 2018

@author: Akshay
"""
import simplejson as json
import pickle
import datetime
import sqlite3
import traceback
import dateutil.parser as dp


inputFile="/home/akshay/IIT KGP/SEM 2/Complex Network/Term Project/articleJSON.txt"

db = sqlite3.connect('../articleDatabase.db')

c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS articles (id text ,\
                                                newsDesk text,\
                                                paragraph text, \
                                                mainHeadline text,\
                                                abstract text,\
                                                wordCount integer,\
                                                snippet text,\
                                                source text,\
                                                documentType text,\
                                                webURL text,\
                                                pubDate timestamp,\
                                                multimedia integer,\
                                                section text )')


def writeArticleInDB(article):
    ID=article['_id']
    newDesk = article['news_desk']
    paragraph = article['lead_paragraph']
    mainHeadline = article['headline']['main']
    abstract = article['abstract']
    wordCount = 0
    if article['word_count']:
        wordCount = int(article['word_count'])
    snippet = article['snippet']
    source = article['source']
    docType = article['document_type']
    webURL = article['web_url']
    pubDate = dp.parse(article['pub_date'])
    isMultimedia = 0
    secName = article['section_name']
    if len(article['multimedia']) > 0:
        isMultimedia = 1

    sqlStat="INSERT INTO articles VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)"

    c.execute(sqlStat,(ID, newDesk, paragraph, mainHeadline, abstract, wordCount, snippet, source, docType, webURL, pubDate, isMultimedia, secName))


def parseFile():
    noOfLinesParsed=0
    with open(inputFile) as f:
        for line in f:
            try:
                noOfLinesParsed+=1
                line=json.loads(line)            
                for record in line['response']['docs']:
                            writeArticleInDB(record)
                
                if(noOfLinesParsed%1000==0):
                    print "No of lines Parsed : ",noOfLinesParsed
            except Exception as e:
                print e.message

        db.commit()
                
if __name__ == "__main__":
    parseFile()
    db.close()
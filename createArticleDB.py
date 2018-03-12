#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 20:45:43 2018

@author: Akshay
"""
import simplejson as json
import os
import sqlite3
import traceback
import dateutil.parser as dp


if os.path.exists("integritylog"):
    os.remove("integritylog")

inputFile="../../Project/articleJSON.txt"

db = sqlite3.connect('../commentsData.db')
print 'connected to databse'
c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS articles (id text PRIMARY KEY ,\
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
                                                keywords text,\
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
    temp = set()
    isMultimedia = 0
    multimedias = article['multimedia']
    if len(multimedias) > 0:
        isMultimedia = 1

    keywordsString = None
    keywords = article['keywords']
    kw = []
    if article:
        for k in keywords:
            kw.append(k['value'])
        keywordsString = ';'.join(kw)
    secName = article['section_name']

    sqlStat="INSERT INTO articles VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)"

    c.execute(sqlStat,(ID, newDesk, paragraph, mainHeadline, abstract, wordCount, snippet, source, docType, webURL, pubDate, isMultimedia, keywordsString, secName))


def parseFile():
    noOfLinesParsed=0
    with open(inputFile) as f:
        for line in f:
            noOfLinesParsed += 1

            try:
                line=json.loads(line)            
                for record in line['response']['docs']:
                            writeArticleInDB(record)
            except sqlite3.IntegrityError as i:
                with open("integritylog","a") as ilog:
                    ilog.write("Line no : "+str(noOfLinesParsed)+"\n")
            except Exception as e:
                if e.message!='response':
                    print e.message

            if (noOfLinesParsed % 1000 == 0):
                print "No of lines Parsed : ", noOfLinesParsed

        db.commit()
                
if __name__ == "__main__":
    parseFile()
    db.close()

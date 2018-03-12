#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 19:11:00 2018

@author: Ashwin and Akshay
"""
import simplejson as json
import pickle
import datetime
import sqlite3
import traceback
from bs4 import BeautifulSoup



inputFile="../../Project/dailyCommentsJSON.txt"

db = sqlite3.connect('../commentsData.db')

c = db.cursor()
 
c.execute('CREATE TABLE IF NOT EXISTS comments (commentID integer PRIMARY KEY,\
                                                assetID integer, assetURL text,\
                                                username text,replyCount integer,\
                                                parentCommentID integer,userID integer,\
                                                userLocation text, \
                                                commentType text,commentBody text,\
                                                recoCount integer,creationDate timestamp,\
                                                approvalDate timestamp,updateDate timestamp,\
                                                editorSelection integer,\
                                                status text,userTitle text,\
                                                commentSeq integer )')


def writeCommentInDB(comment):
    if len(comment.keys()) < 24:
        return
    assetID=int(comment['assetID'])
    assetURL=comment[ 'assetURL']
    parentID=comment[ 'parentID']
    commentID=comment[ 'commentID']
    userName=comment[ 'userDisplayName']
    createDate=datetime.datetime.fromtimestamp(float(comment[ 'createDate']))
    userId=comment[ 'userID']
    replyCount=comment[ 'replyCount']
    status=comment[ 'status']
    approveDate=datetime.datetime.fromtimestamp(float(comment[ 'approveDate']))
    userTitle=comment[ 'userTitle']
    editorSel=comment[ 'editorsSelection']
    location=comment[ 'userLocation']
    commentType=comment[ 'commentType']
    updateDate=datetime.datetime.fromtimestamp(float(comment[ 'updateDate']))
    commentSeq=comment[ 'commentSequence']
    soup  = BeautifulSoup(comment[ 'commentBody'])
    commentBody= ' '.join(soup.find_all(text=True))
    #commentBody = comment[ 'commentBody']
    recCount=comment[ 'recommendationCount']
    sqlStat="INSERT INTO comments VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"

    c.execute(sqlStat,(commentID,assetID, assetURL,userName,replyCount,parentID,userId,
                           location, commentType,commentBody, recCount,createDate,
                           approveDate,updateDate, editorSel,status,userTitle,commentSeq ))

    if len(comment['replies'])>0:
        #print comment['replies']['comments']
        #print 'inside replies', comment['replies']
        for rep in comment['replies']['comments']:
            writeCommentInDB(rep)


def parseFile():
    noOfLinesParsed=0
    with open(inputFile) as f:
        for line in f:
            noOfLinesParsed += 1
            try:

                obj=json.loads(line)
                for record in obj['results']['comments']:
                            writeCommentInDB(record)
            except sqlite3.IntegrityError as ie:
                continue
            except Exception as e:
                with open("log", "a") as log:
                    log.write("Error on line " + str(noOfLinesParsed) + "\n")
                    log.write(traceback.format_exc())
            if (noOfLinesParsed % 1000 == 0):
                print "No of lines Parsed : ", noOfLinesParsed
        db.commit()
                
if __name__ == "__main__":
    parseFile()
    db.close()

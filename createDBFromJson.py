#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 20:45:43 2018

@author: ashwin
"""
import simplejson as json
import pickle
import datetime
import sqlite3
import traceback

db = sqlite3.connect('commentdata.db')

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
    assetID=comment['assetID']
    assetURL=comment[ 'assetURL']
    parentID=comment[ 'parentID']
    commentID=comment[ 'commentID']
    userName=comment[ 'userDisplayName']
    createDate=datetime.datetime.fromtimestamp(float(comment[ 'createDate']))
    userId=comment[ 'userID']
    replyCount=comment[ 'replyCount']
    commentTitle=comment[ 'commentTitle']
    status=comment[ 'status']
    approveDate=datetime.datetime.fromtimestamp(float(comment[ 'approveDate']))
    userTitle=comment[ 'userTitle']
    editorSel=comment[ 'editorsSelection']
    userUrl=comment[ 'userURL']
    location=comment[ 'userLocation']
    commentType=comment[ 'commentType']
    updateDate=datetime.datetime.fromtimestamp(float(comment[ 'updateDate']))
    commentSeq=comment[ 'commentSequence']
    commentBody=comment[ 'commentBody']
    recCount=comment[ 'recommendationCount']
    sqlStat="INSERT INTO comments VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    try:
        c.execute(sqlStat,(commentID,assetID, assetURL,userName,replyCount,parentID,userId,
                           location, commentType,commentBody, recCount,createDate,
                           approveDate,updateDate, editorSel,status,userTitle,commentSeq ))
    except sqlite3.IntegrityError:
        with open("UniLog") as log:
            log.write("Exception Integrity for commentId "+ str(commentID))
    except Exception as e:
        print "error",e
    if len(comment['replies'])>0:
        for rep in comment:
            writeCommentInDB(rep)


def parseFile():
    noOfLinesParsed=0
    with open("/media/ashwin/E0C62B17C62AED8A/Study material/IIT Kgp/Sem2/Comple/Project/dailyCommentsJSON.txt") as f:
        for line in f:
            try:
                noOfLinesParsed+=1
                line=json.loads(line)            
                for record in line['results']['comments']:
                            writeCommentInDB(record)            
                
                if(noOfLinesParsed%1000==0):
                    print "No of lines Parsed : ",noOfLinesParsed
            except Exception as e:
                with open("log","a") as log:
                    log.write("Error on line "+str(noOfLinesParsed) +"\n")
                    log.write(traceback.format_exc())
                
        db.commit()
                
if __name__ == "__main__":
    parseFile()
    db.close()
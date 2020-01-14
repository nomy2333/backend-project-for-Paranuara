
from pymongo import MongoClient
import os
import json
db_url="mongodb://xilan:653100xl@ds125588.mlab.com:25588/paranuara?retryWrites=false"
client=MongoClient(db_url,connectTimeoutMS=30000)
db=client["paranuara"]
compdb=db.companies
peopledb=db.people
fruit=["açaí","akee","apple","apricot","avocado","banana","bilberry","blackberry","blackcurrant","black sapote","blueberry","boysenberry","buddha's hand","cactus pear","crab apple",
"currant","cherry","cherimoya","chico fruit","cloudberry","coconut","cranberry","damson","date","dragonfruit","durian","elderberry","feijoa","fig","goji berry","gooseberry",
"grape","raisin","grapefruit","guava","honeyberry","huckleberry","jabuticaba","jackfruit","jambul","japanese plum","jostaberry","jujube","juniper berry","kiwano","kiwifruit","kumquat",
"lemon","lime","loganberry","loquat","longan","lychee","mango","mangosteen","marionberry","cantaloupe","honeydew","watermelon","miracle fruit","mulberry","nectarine",
"nance","orange","clementine","mandarine","tangerine", "papaya","passionfruit","peach","pear","persimmon", "plantain","plum","prune","pineapple","pineberry","plumcot",
"pomegranate","pomelo","purple","mangosteen","quince","raspberry","salmonberry","rambutan","redcurrant","salal berry","salak","satsuma","soursop","star","strawberry",
"cherry","tamarillo","tamarind","tangelo","tayberry","ugli fruit","white currant","white sapote","yuzu"]

def upResources():
    company_url=os.getcwd()+'/resources/companies.json'
    people_url=os.getcwd()+'/resources/people.json'
    if os.access(company_url, os.F_OK):
        compdb.drop()
        with open(company_url) as f:
            data1=json.load(f)
        compdb.insert(data1)
    if os.access(people_url, os.F_OK):
        peopledb.drop()
        with open(people_url) as h:
            data2=json.load(h)
        peopledb.insert(data2)
    print("upload json file successfully")

# return all their employees. Provide the appropriate solution if the company does not have any employees.
def searchByCom(cname):
    records=None
    recordslist=[]
    #search company by "index" or "company"
    if isinstance(cname,str):
        if len(cname) == 0:
            return {"status": "fails", "data": None,"message":"cannot find the company you input"}
        if  cname.isdigit() :
            item_s="index"
            cname=int(cname)
            records = compdb.find_one({item_s: cname})
            if records is not None:
                del records["_id"]
                recordslist.append(records)
        else:
            item_s="company"
            cname=cname.upper()
            records = compdb.find({item_s: cname},{"status":0,"_id":0})
            if records is not None:
                for i in records:
                    recordslist.append(i)
    elif isinstance(cname,int):
        item_s = "index"
        records = compdb.find_one({item_s: cname})
        if records is not None:
            del records["_id"]
            recordslist.append(records)
    # search from peopledb
    if records==None or len(recordslist)==0:
        return {"status": "fails", "data": None,"message":"cannot find the company you input"}
    else:
        p_dictlist=[]
        messageList=[]
        for item in recordslist:
            p_records=peopledb.find({"company_id":item['index']},{"status":0,"_id":0})
            p_dict = []
            for i in p_records:
                p_dict.append(i)
            p_dictlist.append(p_dict)
            if len(p_dict)==0:
                message="the company does not have any employees"
            else:
                message="the employees' information are showed below"
            messageList.append(message)

        return {"status":"success","data":p_dictlist,"company_info":recordslist,"message":messageList}
# search one people by "index" or "name"
def searchPname(aname):
    recordslist = []
    if isinstance(aname, int):
        item_s = "index"
        aname = int(aname)
        records = peopledb.find_one({item_s: aname})
        if records is not None:
            del records["_id"]
            recordslist.append(records)
    elif isinstance(aname, str):
        if len(aname) == 0:
            return recordslist
        if aname.isdigit():
            item_s = "index"
            aname = int(aname)
            records = peopledb.find_one({item_s: aname})
            if records is not None:
                del records["_id"]
                recordslist.append(records)
        else:
            item_s = "name"
            aname = aname.title()
            records = peopledb.find({item_s: aname}, {"status": 0, "_id": 0})
            if records is not None:
                for i in records:
                    recordslist.append(i)
    return recordslist
#pick up data for only four items:name,age,address,phone
def pro_name(record):
    recorsl=[]
    for item in record:
        recorDict={}
        recorDict["name"]=item["name"]
        recorDict["age"]=item["age"]
        recorDict["address"]=item["address"]
        recorDict["phone"]=item["phone"]
        recorsl.append(recorDict)
    return recorsl


# provide a list of fruits and vegetables they like
def searchByOne(name):
    recordslist=searchPname(name)
    if len(recordslist)==0:
        return {"status": "fails", "data":"cannot find the people you input"}
    else:
        new_dictlist=[]
        for eachp in recordslist:
            if len(eachp)!=0:
                new_dict={}
                fruitLike = []
                vegeLike = []
                new_dict["username"]=eachp["name"]
                new_dict["age"]=eachp["age"]
                for favo in eachp["favouriteFood"]:
                    if favo in fruit:
                        fruitLike.append(favo)
                    else:
                        vegeLike.append(favo)
                new_dict["fruits"]=fruitLike
                new_dict["vegetables"]=vegeLike
                new_dictlist.append(new_dict)
        return {"status":"success","data":new_dictlist}

# provide their information (Name, Age, Address, phone) and the list of their friends in common which have brown eyes and are still alive.
def searchByTwo(a,b):
    p1=searchPname(a)
    p2=searchPname(b)
    if len(p1)==0 and len(p2)==0:
        return {"status":"fails","data":"cannot find both two people's information from database"}
    elif len(p1)!=0 and len(p2)!=0:
        data=[]
        data.append(pro_name(p1)[0])
        data.append(pro_name(p2)[0])
        f1=[]
        for item in p1[0]["friends"]:
            f1.append(item["index"])
        f2 = []
        for item in p2[0]["friends"]:
            f2.append(item["index"])
        commonl=set(f1).intersection(set(f2))
        message=[]
        for item in commonl:
            comFriends = peopledb.find({"index": item,"has_died":False,"eyeColor":"brown"}, {"status": 0, "_id": 0})
            if comFriends is None:
                message="cannot find the common friends which have brown eyes and are still alive"
                return {"status": "fails1", "data": data, "message": message}
            else:
                for i in comFriends:
                    message.append(i)
        return {"status": "success","data":data,"message":message}
    else:
        if len(p1)!=0:
            data=pro_name(p1)
        else:
            data=pro_name(p2)
        return {"status":"fails1","data":data,"message":"only find one person's information from 2 arguements"}



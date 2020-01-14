how to use it:
1. upload a new database:
    companies.json and people.json have exsited in mongoDB, you can test them from step2, if you want to upload a new database:
    1) replace the resources directory which includes companies.json and people.json into path: /Paranuara_xilanYuan
    2) open a new terminal,cd into the path where the project "Paranuara_xilanYuan" locates
    3) use the command:
       $python3 testfile.py upload
2. method 1:
    open a new terminal, cd into the path where the project "Paranuara_xilanYuan" locates
    1) given a company, the API needs to return all their employees. Input the command as below:
     $python3 testfile.py c
     $python3 testfile.py c 1 1001 netbook
     you can input any words after c, if you do not input any words after c, it will test the inside cases automatically.
    2) Given 1 people, provide a list of fruits and vegetables they like. Input the command as below:
     $python3 testfile.py p1
     $python3 testfile.py p1 1,1001,Solomon Cooke
     $python3 testfile.py p1 frost foley
     you can input any words after p1,each searching word is divided by "," ,if the searching words are full name, input " " between first name and second name.
     if you do not input any words after p1, it will test the inside cases automatically.
    3) Given 2 people, provide their information (Name, Age, Address, phone) and the list of their friends in common which have brown eyes and are still alive. Input the command as below:
     $python3 testfile.py p2
     $python3 testfile.py p2 1/Solomon Cooke,28.9/12.1,Solomon Cooke/frost foley,1/0,/1
     you can input any words after p2, each pair is divided by "," and the words in pair is divided by "/",if the searching words are full name, input " " between first name and second name.
     if you do not input any words after p2, it will test the inside cases automatically.

3. method 2:
    1) open the Paranuara_xilanYuan/testfile.py, you can modify the test data in "modify test part part",save it
    2) open a new terminal, cd into the path where the project "Paranuara_xilanYuan" locates
     $python3 testfile.py c
     $python3 testfile.py p1
     $python3 testfile.py p2

tips:
    1. make sure you can use mongoimport tools, if not ,please following the reference to download:
        https://github.com/mongodb/homebrew-brew
    2. make sure pymongo has downloaded for the project,command: $pip install --upgrade pymongo

Data Deign:
    1.searchByCom:(can search with a company name or index)
      1)cannot find the company from company database:
        return {"status": "fails", "data": None,"message":"cannot find the company you input"}
      2)cannot find any employees of the company:
        return {"status":"success","data":p_dictlist,"company_info":recordslist,"message":"the company does not have any employees"}
      3)can find the employees if the company:
        return {"status":"success","data":p_dictlist,"company_info":recordslist,"message":"the employees' information are showed below"}
    2.searchByOne:(can search with a person's name or index)
       1)cannot find the person from people database
        return {"status": "fails", "data":"cannot find the people you input"}
       2)can find the person:
        return return {"status":"success","data":new_dictlist}
    3.searchByTwo:(can search with a person's name or index)
       1)cannot find any person's information from people database
        return {"status":"fails","data":"cannot find both two people's information from database"}
       2)can only find one person's information
        return {"status":"fails1","data":data,"message":"only find one person's information from 2 arguements"}
       3)can find two people's information but cannot find their common friends which have brown eyes and are still alive
        return {"status": "success","data":data,"message":cannot find the common friends which have brown eyes and are still alive}
       4)can find two people's information and also find the common friends which have brown eyes and are still alive
        return {"status": "success","data":data,"message":message}
        data is the two persons' information, message is the common friends' information
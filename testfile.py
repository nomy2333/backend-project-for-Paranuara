import mainsearch
import sys
#modify test data part
compUnit=["",1,1001,12.01,"12.01","NETBOOK","netbook","sdscc"]
peoplename=["","289","28.9",1,"Solomon Cooke","frost foley"]
pcouple=[[],[1,"Solomon Cooke"],["",1],["28.9",12.1],["Solomon Cooke","frost foley"],[1,0]]
#modify test data part end

def test_searchByCompany():
    print("the test input is:",compUnit)
    for item in compUnit:
        print("input:",item)
        results = mainsearch.searchByCom(item)
        if results["status"]=="fails" or results["status"]=="success0":
            print(results["message"])
        if results["status"] == "success":
            for i in range(len(results["company_info"])):
                print("the company's name is", results["company_info"][i]["company"],",and it's index is",results["company_info"][i]["index"])
                print(results["message"][i])
                if len(results["data"][i]) != 0:
                    for j in results["data"][i]:
                        print(j)
        print()

def test_searchByOne():
    print("the test input is:", peoplename)
    for item in peoplename:
        print("input",item)
        results=mainsearch.searchByOne(item)
        if results["status"] == "success":
            for i in results["data"]:
                print(i)
        else:
            print(results["data"])
        print()

def test_searchByTwo():
    print("the test input is:", pcouple)
    for item in pcouple:
        print("input", item)
        if isinstance(item,list) and len(item)==2:
            results=mainsearch.searchByTwo(item[0],item[1])
            if results["status"]=="fails":
                print(results["data"])
            elif results["status"]=="fails1":
                print(results["message"])
                for i in results["data"]:
                    print(i)

            elif results["status"] == "success":
                for i in results["data"]:
                    print(i)
                print("their common friends which have brown eyes and are still alive are showed below:")
                for i in results["message"]:
                    print(i)
        else:
            print("input error, should be two arguements")

        print()

def main():
    command=['c','p1','p2','upload']
    if len(sys.argv)>1 and sys.argv[1] in command:
        s=[x for x in sys.argv]
        del s[0]
        del s[0]
        if sys.argv[1] == "c":
            if len(s)==0:
                test_searchByCompany()
                sys.exit()
            else:
                global compUnit
                compUnit=s
                test_searchByCompany()
                sys.exit()
        elif sys.argv[1] == "p1":
            if len(s)==0:
                test_searchByOne()
                sys.exit()
            else:
                s1=' '
                newString=s1.join(s)
                if ',' in newString:
                    n_s=newString.split(',')
                else:
                    n_s=[]
                    n_s.append(newString)
                global peoplename
                peoplename=n_s
                test_searchByOne()
                sys.exit()
        elif sys.argv[1] == "p2":
            if len(s)==0:
                test_searchByTwo()
                sys.exit()
            else:
                s1=' '
                newString = s1.join(s)
                if ',' in newString:
                    n_s=newString.split(',')
                else:
                    n_s=[]
                    n_s.append(newString)
                nn_s=[]
                for item in n_s:
                    if '/' in item:
                        item=item.split('/')
                        nn_s.append(item)
                global pcouple
                pcouple=nn_s
                test_searchByTwo()
                sys.exit()
        elif sys.argv[1] == "upload":
            mainsearch.upResources()
    else:
        print("incorrect input,please try again")
        sys.exit()


if __name__ == "__main__":
    main()








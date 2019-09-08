from pymongo import MongoClient
from datetime import datetime
# client=MongoClient()
# print (client.PORT)    #打印端口号
# print (client.list_database_names())   #打印数据库名字
class TestMongo(object):
    def __init__(self):      ##定义类    一定是 __init__不是_intn
        self.name = "This is JD"
        self.client=MongoClient('localhost',27017)

        self.dbms = self.client['bilibili']



    def add_one(self):   #新增数据
        post={'title':'标题1','content':'内容2','create_at':datetime.now(),'Day':datetime.now().day}

        return self.dbms.clothes.insert_one(post)
    def save(self,url):
        website={'url':url,'create_at':datetime.now()}
        return self.dbms.url.insert_one(website)



    def read_line(self):
        oneurl=self.dbms.url.find()
        # for item in oneurl:
        #
        #     print (item)
        return oneurl



def main():
    obj=TestMongo()

    rest=obj.add_one()

    #print (rest.inserted_id)
    obj.read_line()


if __name__ == '__main__':
    main()



import shelve as sl
import re
'''
异常处理:
    QueRepeError:数据添加时,键与已有键重复
    QueNoneError:数据更新或删除时,并无此键
数据类sdydata:
    构造函数:sdydata(content = "内容",url = "参考网址")
数据库类SdyDB:
    构造函数 : SdyDB(file = "储存位置")
    方法:
        addQC(question = "问题/标题",content = "内容") #添加一条数据
        searchQC(keywords = ["问题关键字1",...,"问题关键字n"]) #查找包含关键字的键
        updateQC(question = "键(问题/标题)",updContent = "新值(内容)") #更新数据
        delQC(question = "键(问题/标题)") #删除数据
        getContent(question = "键(问题/标题)") #通过键获得内容

'''



#重复
class QueRepeError(Exception):
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return repr(self.value)
#空
class QueNoneError(Exception):
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return repr(self.value)

class sdydata():
    def __init__(self,content,url):
        self.content = content
        self.url = url

class SdyDB():
    def __init__(self,file):
        self.file = file
        sl.open(self.file,flag='c')
    def addQC(self,question,content):
        try:
            sd = sl.open(self.file,flag='c')
            if not question in sd.keys():
                sd[question] = content
            else:
                raise QueRepeError("重复了huckQ")
        except Exception as e:
            raise e
        finally:
            sd.close()

    def searchQC(self,keywords):
        quelist = []
        try:
            sd = sl.open(self.file,flag='r')
            qkeys = sd.keys()
            for keyword in keywords:
                def f(s):
                    if not re.search(keyword,s):
                        return False
                    else:
                        return True
                quelist += list(filter(f,qkeys))
        except Exception as e:
            raise e
        finally:
            sd.close()
            return list(set(quelist))

    def updateQC(self,question,updContent):
        try:
            sd = sl.open(self.file,flag='w',writeback=True)
            if question in sd.keys():
                sd[question] = updContent
                return True
            else:
                raise QueNoneError("没有啊huckQ")
        except Exception as e:
            raise e
        finally:
            sd.close()
    def delQC(self,question):
        try:
            sd = sl.open(self.file,flag='w',writeback=True)
            if question in sd.keys():
                del sd[question]
            else:
                raise QueNoneError("没有啊huckQ")
        except Exception as e:
            raise e
        finally:
            sd.close()

    def getContent(self,question):
        content = sdydata("None","None")
        try:
            sd = sl.open(self.file,flag='r')
            content = sd[question]
        except Exception as e:
            raise e
        finally:
            sd.close()
            return content
    def getSum():
        try:
            sd = sl.open(self.file,flag='r')
            qkeys = sd.keys()
            for keyword in keywords:
                def f(s):
                    if not re.search(keyword,s):
                        return False
                    else:
                        return True
                quelist += list(filter(f,qkeys))
        except Exception as e:
            raise e
    def getSum(self):
        try:
            sd = sl.open(self.file,flag='r')
            qkeys = sd.keys()
            return len(qkeys)
        except Exception as e:
            raise e






















'''
'''

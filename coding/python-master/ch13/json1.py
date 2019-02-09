#让python知道我们将使用json库（也就是反序列化一些json数据）
import json

#我们的数据是字典/对象 

#Altogther，有三个键。

#第一个键是一个字符串。

#第二个键是一个对象。
#在电话对象内是两个键值对. 
#第三个键是一个对象
#在电子邮件对象中，我们有一个键值对.  

data = '''{
    
    "name" : "chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}'''


#使用负载从字符串加载。
#传入数据。
#从sring反序列化为python数据结构.
info = json.loads(data)

#像通常用于词典的那样拉出来。

#info是所有数据，名称是我们感兴趣的价值的关键.
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])

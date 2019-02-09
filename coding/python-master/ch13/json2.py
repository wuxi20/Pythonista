#让python知道我们将使用json库

#to反序列化列表的json表示
import json

#我们有两个清单。
#我们有一个词典列表。

#在我们的列表中，我们有两个用逗号分隔的对象。
#注意，

#你也可以为此列表编制索引. 

#ID maps to 001, x maps to 2...

input = '''[
    {"id" : "001",
        "x" : "2",
        "name" : "chuck"
    } , 
    { "id" : "009",
        "x" : "7",
        "name" : "chuck"
        }
    ]'''

#我们找回一个原生的python列表.
info = json.loads(input)

#查看列表的项目数量
print('User count:', len(info))

#循环列表. Since item is in curly braces 
#它是一个对象，我们可以像字典一样使用它. 

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])

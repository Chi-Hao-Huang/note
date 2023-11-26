# -*- coding: utf-8 -*-
"""
https://officeguide.cc/python-read-write-xml-format-file-tutorial-examples/
"""
import xml.etree.ElementTree as ET

'''
xml = 
<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>
'''


# 從檔案載入並解析 XML 資料
tree = ET.parse('data.xml')
root = tree.getroot()

# 節點 tag 屬性
print(root.tag)
> feed

# 節點 attrib 屬性
print(root.attrib)
> {'{http://www.w3.org/XML/1998/namespace}lang': 'en'}

# 子節點與屬性
for child in root:
    print(child.tag, child.attrib)
    
> title {}
> subtitle {'lang': 'en'}
> link {'rel': 'alternate', 'type': 'text/html', 'href': 'http://hackerrank.com/'}
> updated {}


# 搜尋所有子節點
for child in root.iter():
    print(child.tag, child.attrib)
    
> feed {'{http://www.w3.org/XML/1998/namespace}lang': 'en'}
> title {}
> subtitle {'lang': 'en'}
> link {'rel': 'alternate', 'type': 'text/html', 'href': 'http://hackerrank.com/'}
> updated {}

# 所有子節點所含元素數量
for child in root.iter():
    print(len(child))
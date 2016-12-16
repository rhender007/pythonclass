'''
Created on Dec 6, 2016

@author: Student
'''
import lxml.html

page = lxml.html.parse("http://www.blocket.se/stockholm?q=apple")

print(page)
# Number of links in a page
print(page.xpath('//a'))
print(len(page.xpath('//a')))
print(page.xpath('//img[@class = "item_image"]/@src')) # Product images

items_data = []
for el in page.getroot().find_class("item_row"):
    links = el.find_class("item_link")
    images = el.find_class("item_image")
    if links and images:
        items_data.append({"name": links[0].text.encode("utf-8"),
                           "image": images[0].attrib['src']})
        
print(items_data)

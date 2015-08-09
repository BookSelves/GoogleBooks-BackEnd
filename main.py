import isbndbpy
import googlebooks
import xml.etree.ElementTree as ET

class GoogleBook(object):
    def __init__(self, Title):
       self.Title = Title
    
    def getInfo(self):
        book = googlebooks.Book()
        request = isbndbpy.Request('books', 'combined', self.Title)
        response = request.response().raw()
        root = ET.fromstring(response)
        isbnAttr = root[0][0].attrib
        isbnID = isbnAttr['isbn']
        isbnResult = 'isbn:' + isbnID
        result = book.info(isbnResult)
        return result

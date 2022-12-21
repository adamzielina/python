import xml.sax


class XMLHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.bookCount = 0
        self.isAuthor =0

    def startElement(self, tagName, attrs):
        if tagName == 'catalog':
            print('catalog of books: ' + attrs['title'])
        elif tagName == 'book':
            self.bookCount += 1
        elif tagName == 'author':
            self.isAuthor = True

    def endElement(self, tagName):
        if tagName == 'author':
            self.isAuthor = False

    def characters(self, content):
        if self.isAuthor:
            print('Author is:' + content)

    def startDocument(self):
        print('start')

    def endDocument(self):
        print('end')

if __name__ == "__main__":

    Handler = XMLHandler()
    xml.sax.parse('book.xml',Handler)
    print(f'There were {Handler.bookCount} books')

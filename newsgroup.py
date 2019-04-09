'''
processing the special format used by the Cranfield Dataset
'''
from doc import Document
import os

class NewsGroup:
    def __init__(self, filename):
        self.docs = []

        newsGroupFile = open(filename)
        head, tail = os.path.split(filename)
        docid = tail
        subject = ''
        message = ''
        startread = False
        buf = ''
        for line in newsGroupFile:
#            print (line)

            if 'Subject:' in line:
                subject = line[9:] # got title
            elif 'Lines:' in line:
                startread = True
                line=''
            if startread:
                  buf += line


        message=buf;
        self.docs.append(Document(docid, subject, message)) # the last one

if __name__ == '__main__':
    ''' testing '''

    newsGroupFile = NewsGroup ('C:\\Users\\arjun\\Documents\\Github\\textclassifier\\textclassification\\mini_newsgroups\\alt.atheism\\51121')
    for doc in newsGroupFile.docs:
        print(doc.docID)
        print(doc.subject)
        print(doc.message)
    print(len(newsGroupFile.docs))
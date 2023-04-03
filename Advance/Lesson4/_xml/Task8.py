# -*- coding: utf-8 -*-
from lxml import etree


def parseBookXML(xmlFile):
    with open(xmlFile) as fobj:
        xml = fobj.read()

    root = etree.fromstring(xml)

    book_dict = {}
    books = []
    for book in root.getchildren():
        for elem in book.getchildren():
            if not elem.text:
                text = "None"
            else:
                text = elem.text
            print(elem.tag + " => " + text)
            book_dict[elem.tag] = text

        if book.tag == "book":
            books.append(book_dict)
            book_dict = {}

    return books


if __name__ == "__main__":
    parseBookXML("books.xml")
from xmlutils.xml2csv import xml2csv

converter = xml2csv("Users.xml", "output.csv", encoding="utf-8")
converter.convert(tag="tag")
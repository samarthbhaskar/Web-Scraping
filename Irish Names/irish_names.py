import urllib
from lxml.html import fromstring
import string;

urlbase = 'http://tiara.ie/surnames.php'

fileName = "/Users/sbhaskar/Desktop/irishlastnames.csv";
file = open(fileName, 'w');
file.write("irishlastnames\n");

#for page in range(1, 89):
	#url = urlbase+str(page)+'/'
	#print url

content = urllib.urlopen(urlbase).read()
	#print content;
doc = fromstring(content)
doc.make_links_absolute(urlbase)

table = doc.xpath("body/a/*/table")[0]
table = table[3:len(table)-1]

for name in table:
	name = name[0].text_content()
	print name;
	toPrint = filter(lambda x: x in string.printable, name); 

	file.write(toPrint+"\n");

file.close(); 
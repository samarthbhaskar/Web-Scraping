import urllib
from lxml.html import fromstring
import string;

urlbase = 'http://www.campaignsandelections.com/resources/political-pages/political-pages-directory/page_'

fileName = "/Users/sbhaskar/Desktop/campaignsandelections.csv";
file = open(fileName, 'w');
file.write("campaignsandelections\n");

for page in range(1, 89):
	url = urlbase+str(page)+'/'
	#print url


	content = urllib.urlopen(url).read()
	#print content;
	doc = fromstring(content)
	doc.make_links_absolute(url)

	companies = doc.find_class('company')
	for company in companies:
		name = company.cssselect('h3')[0].text_content()
		rest = company[1];
		affiliationOrAddress = company.xpath('dl/dt')[0].text_content()
		if affiliationOrAddress=="Affiliation:":
			affiliation = company.xpath('dl/dd')[0].text_content();
		else:
			affiliation = "NA";	
		print name+","+affiliation;
		toPrint = filter(lambda x: x in string.printable, name+","+affiliation); 

		file.write(toPrint+"\n");

file.close(); 
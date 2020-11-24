from lxml import etree
import csv
tree = etree.parse('email_anonymized.xml')
root = tree.getroot()

f = open('first.csv','w')
cswriter = csv.writer(f)

head = []
emails = []


for message in root.getchildren():
    emails.append((message.attrib).get('Sender'))
    for recipient in message.getchildren():
        emails.append(recipient.text)

emails = list(dict.fromkeys(emails))
summary = []

for message in root.getchildren():
    id = ["0","0"]
    sender = (message.attrib).get('Sender')
    id[0] = emails.index(sender)
    for recipient in message.getchildren():
        id[1] = emails.index(recipient.text)
        cswriter.writerow(id)
         
f.close()

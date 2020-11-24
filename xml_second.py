from lxml import etree
import csv
tree = etree.parse('email_anonymized.xml')
root = tree.getroot()

f = open('secondd.csv','w')
cswriter = csv.writer(f)

head = []
domains = []


for message in root.getchildren():
    domain = str((message.attrib).get('Sender'))
    id = domain.find("@")+1
    domains.append(domain[id:])
    for recipient in message.getchildren():
        domain = str(recipient.text)
        id = domain.find("@")+1
        domains.append(domain[id:])

domains = list(dict.fromkeys(domains))
summary = []

print(domains[24])
for message in root.getchildren():
    arr = ["0","0"]
    sender = str((message.attrib).get('Sender'))
    id = sender.find("@")+1
    sender = sender[id:]
    arr[0] = domains.index(sender)
    for recipient in message.getchildren():
        domain = str(recipient.text)
        id = domain.find("@")+1
        domain = domain[id:]
        arr[1] = domains.index(domain)
        cswriter.writerow(arr)

f.close()

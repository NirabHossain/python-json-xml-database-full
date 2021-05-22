import xml.etree.ElementTree as ET
data='''
<person>
    <name>Md. Nirab Hossain</name>
    <phone type='intl'>01521324292</phone>
    <email hid='yes'/>
</person>
'''
print(data)

tree=ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Attribute:',tree.find('email').get('hid'))
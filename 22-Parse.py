import xml.etree.ElementTree as ET
data='''
<person>
    <users>
        <iden x='1'>
            <name>Md. Nirab Hossain</name>
            <phone type='intl'>01521324292</phone>
            <email hid='yes'/>
        </iden>
        <iden x='2'>
            <name>Md. Sourav Hossain</name>
            <phone type='intl'>01748537483</phone>
            <email hid='no'/>
        </iden>
    </users>
</person>
'''
print(data)

tree=ET.fromstring(data)
lst=tree.findall('users/iden')
for x in lst:
    print("Item=",x.get('x'),x.find('name').text,x.find('phone').text,x.find('email').get('hid'))
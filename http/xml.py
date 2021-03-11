import xml.etree.ElementTree as ET
data = '''<person >
    <name>John</name>
    <phone type="intl>123 123</phone>
    <email hide="yes />
</person>'''

tree = ET.fromstring(data)

print('name: ', tree.find('name').text)
print('email: ', tree.find('email').get('hide'))

import json
data='''[
    {
        "id":"01",
        "Name":"Md. Nirab Hossain",
        "District":"Naogaon"
    },
    {
        "id":"02",
        "Name":"Md. Khayrul Islam",
        "District":"Mymensing"
    }
]'''
print(data)
info=json.loads(data)
print("User count", len(info))
for dic in info:
    print(dic['Name'],dic['id'],dic['District'])
import json 

x={'username':'postgres',
   'password':'123456',
   'host':'localhost',
   'port':8080}

json_string=json.dump(x)
json_file=open('data.json','w')
json_file.write(x)
json_file.close()
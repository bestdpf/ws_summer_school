import json


f_in = open('users.txt','r')
f_usr = open('usr_ids.txt','w')

for line in f_in.readlines():
    js_data = json.loads(line)
    usr_id = js_data['id']
    f_usr.write('{0}\n'.format(usr_id))

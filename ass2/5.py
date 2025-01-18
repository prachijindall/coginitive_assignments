sample_dict={"name":"kelly","age":25,"salary":8000,"city":"new york"}
print(sample_dict)

for key,values in sample_dict.items():
   if key=='city':
      sample_dict["location"]=sample_dict.pop(key)
      break
print(sample_dict)
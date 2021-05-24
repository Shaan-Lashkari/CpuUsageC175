import matplotlib.pyplot as plt
from random import choice
import psutil as ps
colors = ["red","green","blue","yellow","black"]
app_name_dict = {}
count= 0
for process in ps.process_iter():
    count = count + 1
    if count <= 6:
        name = process.name()
        cpu_usage = ps.cpu_percent()
        print(cpu_usage)
        print("Name : " + name + "--- " + "Cpu Usage : " + str(cpu_usage))
        app_name_dict[name]=cpu_usage
        print(app_name_dict)
key_max = max(app_name_dict,key=app_name_dict.get)
print(key_max)
key_min = min(app_name_dict,key=app_name_dict.get)
print(key_min)
name_list = [key_max,key_min]
app = app_name_dict.values()
max_app = max(app)
print(max_app)        
min_app = min(app)
print(min_app)   
vallist = [max_app,min_app]     
plt.figure(figsize=(18,10))
plt.xlabel("Application")
plt.ylabel("Usage")
plt.bar(name_list,vallist,width=0.6,color=(choice(colors),"red"))
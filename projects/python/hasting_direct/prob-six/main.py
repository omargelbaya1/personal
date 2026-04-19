requests = [
    ("C1", 0),
    ("C1", 10),
    ("C1", 59),
    ("C1", 60),
    ("C1", 61),
    ("C2", 5),
    ("C2", 6),
    ("C2", 7),
    ("C2", 8),
    ("C3", 100),
    ("C3", 110),
    ("C1", 130),
]
new_dict={}
for i in requests:
    new_dict[i[0]]=[]


for i in requests:
    new_dict[i[0]].append(i[1])



another_dict={

"C1":{
    "ALLOWED":1,
    "BLOCKED":0,
    "TOTAL_PERC":0
},
"C2":{
    "ALLOWED":1,
    "BLOCKED":0,
    "TOTAL_PERC":0

},
"C3":{
    "ALLOWED":1,
    "BLOCKED":0,
    "TOTAL_PERC":0
}

}
for key,values in new_dict.items():
    count = 1
    print(f"{key} @ t={values[0]} -> ALLOWED")
    for i in range(1,len(values)):
        if values[i] - values[i-1] <60 and count<3:
            print(f"{key} @ t={values[i]} -> ALLOWED")
            count+=1
            another_dict[key]["ALLOWED"]+=1
        elif values[i] - values[i-1] >60:
            print(f"{key} @ t={values[i]} -> ALLOWED")
            count-=1
            another_dict[key]["ALLOWED"] += 1
        else:
            print(f"{key} @ t={values[i]} -> BLOCKED")
            another_dict[key]["BLOCKED"] += 1
print(new_dict)
for i,values in another_dict.items():
    values["TOTAL_PERC"]=round((values["BLOCKED"]/len(new_dict[i])) * 100,2)
print(another_dict)




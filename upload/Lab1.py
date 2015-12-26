﻿#软工lab1：结对编程

from functools import reduce

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
def str2int(s):
    a = reduce(lambda x, y: x * 10 + y, map(char2num, s))
    return a

def str2float(s):
    index = s.find('.')
    if index == -1:
        x = 0
    else:
        x = len(s) - index - 1
    b = str2int(s.replace('.', ''))
    a = float(b) / 10**x
    return a

def dfs(character,Q1,Q2):
    global value,candidate_set
    global Q3,node
#    print(character)
    global fw
    fw.write(str(Q3))
    fw.write('\n')
    Q1_temp1= Q1
    Q2_temp1= Q2
    for server in candidate_set[character]:
        #fw.write(server[0])
        Q1= Q1_temp1
        Q2= Q2_temp1
        Q1_temp = Q1 * server[1]
        Q2_temp = Q2 + server[2]
        
        if(Q3 > (Q1_temp - Q2_temp/100)):
            continue
        #print(Q1_temp - Q2_temp/100),character
        Q1 = Q1_temp
        Q2 = Q2_temp
        if(character == node[-1]):
            if(Q3 < (Q1 - Q2 / 100)):
                Q3 = (Q1 - Q2 / 100)
                print Q3
            continue
        else:
            dfs(node[(value[character]+1)],Q1,Q2)
 
   
def setvalue():
    global value
    global node
    node = list(set(node))
    value = {}
    index = 0
    for key in  node:
        value[key] =index
        index+=1


f = open("SERVICE.txt", 'r')
candidate_set = {}  #候选服务 {‘A’:[list], ..}
for alphabet in 'ABCDEFGHIJKLMN':
    lists = [[] for i in range(500)]
    for i in range(500):
        lists[i] = f.readline().strip('\n ').split(' ')
        del lists[i][1]
        del lists[i][2]
        lists[i][1] = str2float(lists[i][1])
        lists[i][2] = str2float(lists[i][2])
        i = i+1
    lists.sort(key = lambda x:x[2])
    candidate_set[alphabet] = lists
f.close()
f1 = open("PROCESS.txt", 'r')
f2 = open("REQ.txt", 'r')
line = f1.readline()
def my_strip(string):
    return string.strip('()')
for alphabet in 'ABCDEFGHIJKLMN' :
    sum = 0;
    list_temp = candidate_set[alphabet]
    list_flag = [1 for i in range(500)]
    for i in range(500):
        for j in range(500):
            if(list_flag[j] and list_flag[i] and list_temp[i][1] > list_temp[j][1] and list_temp[i][2] < list_temp[j][2]):
                list_temp[j][1] = 0.001
                list_temp[j][2] = 1000
                #sum = sum + 1
            if(list_flag[j] and list_flag[i] and (list_temp[j][2] > 25.0)):
                #print list_temp[j][2]
                #sum = sum + 1
                list_temp[j][1] = 0.001
                list_temp[j][2] = 1000
    print sum 

print candidate_set['A']            
Q1 = 1.0
Q2 = 0
process = line.strip().split(",(")
process = list(map(my_strip, process))
node = []
graph = {}  #邻接表
for edge in process:
     if edge[0] in graph:
         node.append(edge[-1])
         graph[edge[0]].append(edge[-1])
     else:
         node.append(edge[0])
         node.append(edge[-1])
         graph[edge[0]] = [edge[-1]]
#print(graph)
node = list(set(node))
print(node)
value = {}
setvalue()
#print value 
REQ = f2.readline().strip().split(',')
REQ = list(map(my_strip, REQ))
REQ = list(map(str2float, REQ))
REQ_TR = REQ[0]
REQ_TP = REQ[1]
for key in node:
    Q1 = Q1 * candidate_set[key][0][1]
    Q2 = Q2 + candidate_set[key][0][2]
#Q3 = Q1 - Q2/100
Q3 = 0.6
Q1 = 1.0
Q2 = 0
#print Q3 
#print(REQ_TR, REQ_TP)

fw = open("Q3.txt", 'w+')
dfs('A',Q1,Q2)
fw.close()
setvalue()

f1.close()
f2.close()
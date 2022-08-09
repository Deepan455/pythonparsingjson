import sys
import json

# accessing filename
path = sys.argv[1]

        
file = open(path,'r')
file_data = file.read()
json_data = json.loads(file_data)
print(json_data)

def getLeaves(tree):
    leavesList = []

    for node in tree:
        if "leaves" in node:
            for leaf in node['leaves']:
                leavesList.append(leaf)

        if "branches" in node:
            for branch in node['branches']:
                for leaf in getLeaves([branch]):
                    leavesList.append(leaf)
    
    return leavesList

def leavesInNode(tree):
    masterList = []
    for node in tree:
        masterList.append((node['id'],getLeaves([node])))
        if "branches" in node:
            for branch in node["branches"]:
                for item in leavesInNode([branch]):
                    masterList.append(item)

    
    return masterList


print(getLeaves(json_data))
print(leavesInNode(json_data))

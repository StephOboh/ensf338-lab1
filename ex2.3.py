import json

f = open('large-file.json') # opens json file 
data = json.load(f) # dictionary 
for item in data:  # for loop to iterate through the items to look for size
    if 'payload' in item:
        if 'size' in item['payload']:
            item['payload']['size'] = 35

for item in data:  # for loop to iterate through the items to look for size
    if 'payload' in item:
        if 'pull_request' in item['payload']:
            if 'head' in item['payload']['pull_request']: 
                if 'repo' in item['payload']['pull_request']['head']:
                    if item['payload']['pull_request']['head']['repo']:
                        if'size' in item['payload']['pull_request']['head']['repo']:
                            item['payload']['pull_request']['head']['repo']['size'] = 35

for item in data:  # for loop to iterate through the items to look for size
    if 'payload' in item:
        if 'pull_request' in item['payload']:
            if 'base' in item['payload']['pull_request']: 
                if 'repo' in item['payload']['pull_request']['base']:
                    if item['payload']['pull_request']['base']['repo']:
                        if'size' in item['payload']['pull_request']['base']['repo']:
                            item['payload']['pull_request']['base']['repo']['size'] = 35
for item in data:  # for loop
    if 'payload' in item:
        if 'forkee' in item['payload']:
            if'size' in item['payload']['forkee']:
                item['payload']['forkee']['size'] = 35

data.reverse() # built in function to reverse json file

json_object = json.dumps(data, indent=4) # turns dictionairy into json
with open("output.2.3.json", "w") as output: # opens output file and writes information
    output.write(json_object)

f.close() # closes json file
import json

with open('hg_changelog.json') as file1:  # get HG commit data
    hg_data = json.load(file1)

with open('github_changelog.json') as file2:  # get github commit data
    github_data = json.load(file2)

all_data = {}
all_data.update({'HG': hg_data,
                 'GIT': github_data})

with open('json_changelog.json', 'w') as file:  # write each commit data into a file as json
    json.dump(all_data, file, indent=2)
file.close()

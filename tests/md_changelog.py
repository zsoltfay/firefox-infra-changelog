import json

with open('hg_changelog.json') as file1:   # get HG commit data
    hg_data = json.load(file1)

with open('github_changelog.json') as file2:   # get github commit data
    github_data = json.load(file2)


import json

with open('hg_changelog.json') as file1:  # get HG commit data
    hg_data = json.load(file1)

with open('github_changelog.json') as file2:  # get github commit data
    github_data = json.load(file2)

file = open('markdown_changelog.md', 'w')
git_title = "# Git" + "\n"
header_git = "| repo | author | email| date |" + "\n" + "| --- | --- | --- | --- |" + "\n"
file.write(git_title)
file.write(header_git)

for key in github_data:
    for item in github_data[key]:
        name = github_data[key][item]['author_info']['name']
        email = github_data[key][item]['author_info']['email']
        date = github_data[key][item]['author_info']['date']
        # commit_msg = github_data[key][item]['commit_message']
        row = "|" + key + "|" + name + "|" + email + "|" + date + "|" + "\n"
        file.write(row)


hg_title = "# HG" + "\n"
header_hg = "| repo | author | branch | date |" + "\n" + "| --- | --- | --- | --- |" + "\n"
file.write(hg_title)
file.write(header_hg)
for key1 in hg_data:
    for item1 in hg_data[key1]:
        name = hg_data[key1][item1]['author_info']
        sha = hg_data[key1][item1]['sha']
        branch = hg_data[key1][item1]['branch']
        row1 = "|" + key1 + "|" + name + "|" + branch + "|" + sha + "|" + "\n"
        file.write(row1)
file.close()

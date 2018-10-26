import json

with open('hg_changelog.json') as file1:  # get HG commit data
    hg_data = json.load(file1)

with open('github_changelog.json') as file2:  # get github commit data
    github_data = json.load(file2)

file = open('markdown_changelog.md', 'w')
git_title = "# Git" + "\n"
header_git = "repo | commit message | author | email| date" + "\n" + "--- | --- |--- | --- | ---" + "\n"
file.write(git_title)
file.write(header_git)

for key in github_data:
    for item in github_data[key]:
        name = github_data[key][item]['author_info']['name']
        email = github_data[key][item]['author_info']['email']
        date = github_data[key][item]['author_info']['date']
        commit_msg = github_data[key][item]['commit_message']
        row = key + "|" + commit_msg + "|" + name + "|" + email + "|" + date
        file.write(row)


# hg_title = "# HG" + "\n"
# header_hg = "repo | commit message | author | branch | date" + "\n" + "--- | --- | --- | --- | ---" + "\n"
# file.write(hg_title)
# file.write(header_hg)
# for key1 in hg_data:
#     for item1 in hg_data[key1]:
#         name = github_data[key][item]['author_info']['name']
#         email = github_data[key][item]['author_info']['email']
#         date = github_data[key][item]['author_info']['date']
#         commit_msg = github_data[key][item]['commit_message']

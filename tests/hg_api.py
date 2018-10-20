import requests
import json

reposApi = {'Version-Control-Tools': 'https://hg.mozilla.org/hgcustom/version-control-tools/json-log',
            'Mozilla-Build': 'https://hg.mozilla.org/mozilla-build/json-log',
            'Tooltool': 'https://hg.mozilla.org/build/tools/json-log',
            'Mozilla-Central': 'https://hg.mozilla.org/mozilla-central/json-log',
            'Try': 'https://hg.mozilla.org/try/json-log',
            'Autoland': 'https://hg.mozilla.org/integration/autoland/json-log',
            'Inbound': 'https://hg.mozilla.org/integration/mozilla-inbound/json-log',
            'comm-esr60': 'https://hg.mozilla.org/releases/comm-esr60/json-log',
            'Beta': 'https://hg.mozilla.org/releases/mozilla-beta/json-log',
            'mozilla-esr60': 'https://hg.mozilla.org/releases/mozilla-esr60/json-log',
            'mozilla-release': 'https://hg.mozilla.org/releases/mozilla-release/json-log'
            }

for key in reposApi:
    url = requests.get(reposApi.get(key))  # place api URL into a variable
    json_data = url.json()  # get data from url and convert to json
    repo_dict = {}  # main dict that will contain all of the data of a repo
    number = 0  # count the number of commits in each repo
    for item in json_data['changesets']:
        each_commit = {}  # main dictionary. will contain all data about a single commit
        author_info = {}  # will contain info about committer
        author_info.update({'sha': item['node'],
                            'branch': item['branch'],
                            'author_info': item['user'],
                            'commit_message': item['desc']})
        each_commit.update({number: author_info})
        number += 1
        repo_dict.update(each_commit)
    reposApi.update({key: repo_dict})
with open('hg_changelog.json', 'w') as file:  # write each commit data into a file as json
    json.dump(reposApi, file, indent=2)
file.close()

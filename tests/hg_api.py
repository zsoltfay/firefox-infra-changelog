import requests
import json

reposApi = {'Version-Control-Tools' : 'https://hg.mozilla.org/hgcustom/version-control-tools/json-log',
           'Mozilla-Build' : 'https://hg.mozilla.org/mozilla-build/json-log',
           'Tooltool' : 'https://hg.mozilla.org/build/tools/json-log',
           'Mozilla-Central' : 'https://hg.mozilla.org/mozilla-central/json-log',
           'Try' : 'https://hg.mozilla.org/try/json-log',
           'Autoland' : 'https://hg.mozilla.org/integration/autoland/json-log',
           'Inbound' : 'https://hg.mozilla.org/integration/mozilla-inbound/json-log',
           'comm-esr60' : 'https://hg.mozilla.org/releases/comm-esr60/json-log',
           'Beta' : 'https://hg.mozilla.org/releases/mozilla-beta/json-log',
           'mozilla-esr60' : 'https://hg.mozilla.org/releases/mozilla-esr60/json-log',
           'mozilla-release' : 'https://hg.mozilla.org/releases/mozilla-release/json-log'
            }
# api_url = 'https://hg.mozilla.org/hgcustom/version-control-tools/json-log'  # place api URL into a variable
# json_data = requests.get(api_url).json()  # get data from url and convert to json
# with open('hg_changelog.json', 'w') as file:  # write each commit data into a file as json
#     json.dump(json_data, file, indent=2)
# file.close()

for key, value in reposApi.items():
    api_url = value                                                  # place api URL into a variable
    json_data = requests.get(api_url).json()                         # get data from url and convert to json
    new_list = []                                                    # main list that will contain data of all commits
    for item in json_data['changesets']:
        big_daddy = {}                                   # main dictionary. will contain all data about a single commit
        big_daddy['sha'] = item['node']          # sha
        big_daddy['commit_info'] = item['desc']  # commit message
        big_daddy['branch'] = item['branch']     # branch
        big_daddy['user'] = item['user']
        new_list.append(big_daddy)
        with open('hg_changelog.json', 'w') as file:             # write each commit data into a file as json
            json.dump(new_list, file, indent=2)
        file.close()
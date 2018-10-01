import requests
import json

api_url = 'https://api.github.com/repos/Akhliskun/firefox-infra-changelog/commits'  # place api URL into a variable
json_data = requests.get(api_url).json()  # get data from url and convert to json
#  print(json_data)
# reposApi = {'shipit': 'https://api.github.com/repos/mozilla-releng/ship-it/commits',
#             'services': 'https://api.github.com/repos/mozilla/release-services/commits',
#             'beetmoverscript': 'https://api.github.com/repos/mozilla-releng/beetmoverscript/commits',
#             'addonscript': 'https://api.github.com/repos/mozilla-releng/addonscript/commits',
#             'shipitv2': 'https://api.github.com/repos/mozilla-releng/shipit-v2/commits',
#             'build-cloud-tools': 'https://api.github.com/repos/mozilla-releng/build-cloud-tools/commits',
#             'build-puppet': 'https://api.github.com/repos/mozilla-releng/build-puppet/commits',
#             'shipitscript': 'https://api.github.com/repos/mozilla-releng/shipitscript/commits',
#             'bouncerscript': 'https://api.github.com/repos/mozilla-releng/bouncerscript/commits',
#             'treescript': 'https://api.github.com/repos/mozilla-releng/treescript/commits',
#             'mozapkpublisher': 'https://api.github.com/repos/mozilla-releng/mozapkpublisher/commits',
#             'OpenCloudConfig': 'https://api.github.com/repos/mozilla-releng/OpenCloudConfig/commits',
#             'scriptworker': 'https://api.github.com/repos/mozilla-releng/scriptworker/commits',
#             'pushsnapscript': 'https://api.github.com/repos/mozilla-releng/pushsnapscript/commits',
#             'signingscript': 'https://api.github.com/repos/mozilla-releng/signingscript/commits',
#             'cot-gpg-keys': 'https://api.github.com/repos/mozilla-releng/cot-gpg-keys/commits',
#             'pushapkscript': 'https://api.github.com/repos/mozilla-releng/pushapkscript/commits',
#             'balrogscript': 'https://api.github.com/repos/mozilla-releng/balrogscript/commits',
#             'funsize': 'https://api.github.com/repos/mozilla-releng/funsize/commits',
#             'signtool': 'https://api.github.com/repos/mozilla-releng/signtool/commits'}

new_list = []                  # main list that will contain data of all commits
for item in json_data:
    big_daddy = {}             # main dictionary. will contain all data about a single commit
    sha = item['sha']
    commit_info = {}           # will contain info about commiter
    commit_info.update(item['commit']['author'])
    big_daddy['sha'] = item['sha']
    big_daddy['commit_info'] = commit_info
    new_list.append(big_daddy)
    with open('github_changelog.json', 'w') as file:      # write each commit data into a file as json
        json.dump(new_list, file, indent=2)
    file.close()

# for i in range(len(json_data)):
#     new_string = json.dumps(json_data, indent=2)
# file.write('commit sha: ' + json_data[i]['sha'] + '\n')
# file.write('Author Name: ' + json_data[i]['commit']['author']['name'] + '\n')
# file.write('Commit Date: ' + json_data[i]['commit']['author']['date'] + '\n')
# file.write('Email: ' + json_data[i]['commit']['author']['email'] + '\n' + '\n')

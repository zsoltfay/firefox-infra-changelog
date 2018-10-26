import requests
import json

reposApi = {'shipit': 'https://api.github.com/repos/mozilla-releng/ship-it/commits',
            'services': 'https://api.github.com/repos/mozilla/release-services/commits',
            'beetmoverscript': 'https://api.github.com/repos/mozilla-releng/beetmoverscript/commits',
            'addonscript': 'https://api.github.com/repos/mozilla-releng/addonscript/commits',
            'shipitv2': 'https://api.github.com/repos/mozilla-releng/shipit-v2/commits',
            'build-cloud-tools': 'https://api.github.com/repos/mozilla-releng/build-cloud-tools/commits',
            'build-puppet': 'https://api.github.com/repos/mozilla-releng/build-puppet/commits',
            'shipitscript': 'https://api.github.com/repos/mozilla-releng/shipitscript/commits',
            'bouncerscript': 'https://api.github.com/repos/mozilla-releng/bouncerscript/commits',
            'treescript': 'https://api.github.com/repos/mozilla-releng/treescript/commits',
            'mozapkpublisher': 'https://api.github.com/repos/mozilla-releng/mozapkpublisher/commits',
            'OpenCloudConfig': 'https://api.github.com/repos/mozilla-releng/OpenCloudConfig/commits',
            'scriptworker': 'https://api.github.com/repos/mozilla-releng/scriptworker/commits',
            'pushsnapscript': 'https://api.github.com/repos/mozilla-releng/pushsnapscript/commits',
            'signingscript': 'https://api.github.com/repos/mozilla-releng/signingscript/commits',
            'cot-gpg-keys': 'https://api.github.com/repos/mozilla-releng/cot-gpg-keys/commits',
            'pushapkscript': 'https://api.github.com/repos/mozilla-releng/pushapkscript/commits',
            'balrogscript': 'https://api.github.com/repos/mozilla-releng/balrogscript/commits',
            'funsize': 'https://api.github.com/repos/mozilla-releng/funsize/commits',
            'signtool': 'https://api.github.com/repos/mozilla-releng/signtool/commits'}

for key in reposApi:
    url = requests.get(reposApi.get(key))  # place api URL into a variable
    json_data = url.json()  # get data from url and convert to json
    repo_dict = {}  # main dict that will contain all of the data of a repo
    number = 0  # count the number of commits in each repo
    for item in json_data:
        print(item)
        each_commit = {}  # main dictionary. will contain all data about a single commit
        author_info = {}  # will contain info about committer
        author_info.update({'repo': reposApi[key],
                            'sha': item['sha'],
                            'url': item['url'],
                            'author_info': item['commit']['author'],
                            'commit_message': item['commit']['message']})
        each_commit.update({number: author_info})
        number += 1
        repo_dict.update(each_commit)
    reposApi.update({key: repo_dict})
with open('github_changelog.json', 'w') as file:  # write each commit data into a file as json
    json.dump(reposApi, file, indent=2)
file.close()

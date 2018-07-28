import requests

url = 'https://api.github.com/repos/Akhliskun/firefox-infra-changelog/commits'  # place api URL into a variable

json_data = requests.get(url).json()  # get data from url and convert to json

file = open('github_changelog.json', 'w')

for i in range(len(json_data)):       # print commit info of my choosing to file, separated by an empty line space
    file.write('commit sha: ' + json_data[i]['sha'] + '\n')
    file.write('Author Name: ' + json_data[i]['commit']['author']['name'] + '\n')
    file.write('Commit Date: ' + json_data[i]['commit']['author']['date'] + '\n' + '\n')

file.close()



#!/usr/bin/env python
import requests
import sys
import simplejson as json


api_tpl = 'https://api.github.com/repos/{}/commits'


def do_fetch(code_repository, file_path):
    api_url = api_tpl.format(code_repository)
    commits = []

    r = requests.get(api_url)

    for r in json.loads(r.text):
        #import ipdb; ipdb.set_trace()
        commits.append({
            'committer': r['commit']['committer'],
            'html_url': r['html_url'],
            'sha': r['sha']
        })

    with open(file_path, 'wb') as f:
        # set indent = 4 just for readability
        f.write(json.dumps({
            'repo': code_repository,
            'commits': commits
        }, indent=4))

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print 'usage: fetch.py repository_name file.json'

    do_fetch(sys.argv[1], sys.argv[2])

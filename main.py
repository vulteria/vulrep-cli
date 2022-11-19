import argparse
import json
import urllib.request


# check that all the params are valid
def check_params(params):
    trigger_scan(params.vulrep_server, params.token, params.project_code)


def trigger_scan(vulrep_url, token, project):
    url = vulrep_url + '/projects/triggerScanWithToken'
    payload = json.dumps({
        'projectCode': project,
        'token': token
    }).encode('utf8')
    req = urllib.request.Request(url, data=payload, method='POST', headers={
        'Content-Type': 'application/json'
    })
    with urllib.request.urlopen(req) as response:
        status = response.status
        if status < 200 or status >= 300:
            raise ValueError(f'Error: {status}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CLI for Vulrep, the vulnerability detection and repair tool')
    parser.add_argument('--vulrep_server', default='https://vulrep.com', help='the URL to the target Vulrep server')
    parser.add_argument('--project_code', metavar='p', help='the target project\'s identifying code')
    parser.add_argument('--token', metavar='t', help='the secret access token for the Vulrep project')
    args = parser.parse_args()
    check_params(args)


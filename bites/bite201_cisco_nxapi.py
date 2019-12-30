#!/usr/bin/env python3
# by rog

# https://codechalleng.es/bites/201/

import requests
import json
from requests.auth import HTTPBasicAuth

from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pprint import pprint
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def nxapi_show_version():
    url = "https://sbx-nxos-mgmt.cisco.com/ins"
    switchuser = "admin"
    switchpassword = "Admin_1234!"
    http_headers = {'content-type':'application/json-rpc'}
    payload = [{"jsonrpc": "2.0",
                "method": "cli",
                "params": {"cmd": "show version",
                           "version": 1}, "id": 1}]
    data = json.dumps(payload)
    response = requests.post(url, data=data, headers=http_headers, auth=(switchuser, switchpassword), verify=False)


    # 2. retrieve and return the kickstart_ver_str from the response
    # example response json:
    # {'result': {'body': {'bios_cmpl_time': '05/17/2018',
    #                      'kick_tmstmp': '07/11/2018 00:01:44',
    #                      'kickstart_ver_str': '9.2(1)',
    #                      ...
    #                      }
    #             }
    # }
    version = response.json()['result']['body']['kickstart_ver_str']
    return version


if __name__ == "__main__":
    result = nxapi_show_version()
    print(result)

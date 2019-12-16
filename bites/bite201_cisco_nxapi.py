#!/usr/bin/env python3
# by rog

# https://codechalleng.es/bites/201/

import requests
import json
from requests.auth import HTTPBasicAuth

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def nxapi_show_version():
    s = requests.Session()
    url = "https://sbx-nxos-mgmt.cisco.com/"
    switchuser = "admin"
    switchpassword = "Admin_1234!"
    # s.post(url, data={'username': switchuser, 'password': switchpassword}, verify=False)
    response = s.get(url, auth=HTTPBasicAuth(switchuser, switchpassword), verify=False)
    print(response)
    http_headers = {"content-type": "application/json"}
    payload = [
        {
            "ins_api": {
                "version": "1.0",
                "type": "cli_show",
                "chunk": "0",
                "sid": "1",
                "input": "show version",
                "output_format": "json",
            }
        }
    ]

    # 1. use requests to post to the switch
    response = s.post(url, json=json.dumps(payload), headers=http_headers, verify=False)
    print(response)

    # 2. retrieve and return the kickstart_ver_str from the response
    # example response json:
    # {'result': {'body': {'bios_cmpl_time': '05/17/2018',
    #                      'kick_tmstmp': '07/11/2018 00:01:44',
    #                      'kickstart_ver_str': '9.2(1)',
    #                      ...
    #                      }
    #             }
    # }
    # version = ...
    return version


if __name__ == "__main__":
    result = nxapi_show_version()
    print(result)

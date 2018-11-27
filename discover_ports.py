#!/usr/bin/env python3
""" Description: Pulls urls and ports from /etc/zabbix/urls.txt
                 for Zabbix to monitor.
Author:      Olivier van der Toorn <oliviervdtoorn@gmail.com>"""
import json


def main():
    """Reads /etc/zabbix/urls.txt for URLs to monitor.
    """
    urls = []
    try:
        with open('/etc/zabbix/ports.txt', 'r') as url_file:
            lines = url_file.readlines()

        for line in lines:
            line = line.replace('\n', '')
            try:
                ip_address, port = line.split(':')

            except ValueError:
                ip_address = '127.0.0.1'
                port = line

            urls.append({
                '{#IP}': ip_address,
                '{#PORT}': port
            })

    except (FileNotFoundError, PermissionError):
        pass

    data = {'data': urls}
    print(json.dumps(data, sort_keys=True, indent=4))


if __name__ == '__main__':
    main()

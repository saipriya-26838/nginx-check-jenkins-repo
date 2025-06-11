#!/usr/bin/env python3
import subprocess, logging

LOG_FILE = '/var/log/nginx_monitor.log'
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)

def is_running():
    result = subprocess.run(['systemctl', 'is-active', 'nginx'],
                             capture_output=True, text=True)
    return result.stdout.strip() == 'active'

def restart_nginx():
    res = subprocess.run(['systemctl', 'restart', 'nginx'])
    return res.returncode == 0

def main():
    if is_running():
        logging.info('nginx is running normally.')
    else:
        logging.warning('nginx is DOWN. Attempting restart...')
        if restart_nginx():
            logging.info('nginx restarted successfully.')
        else:
            logging.critical('Failed to restart nginx!')

if __name__ == '__main__':
    main()


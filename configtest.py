import config as cfg
import configparser

print(cfg.database_config['host'])

config = configparser.ConfigParser()
config.read('config.ini')

hostname = config['DATABASE']['HOSTNAME']
print(hostname)
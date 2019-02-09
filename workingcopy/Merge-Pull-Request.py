#!python2

# https://gist.github.com/palmin/d31cd80309e7f01469803733d2e43c2e

# coding: utf-8
#
# This script is meant to be used from the Pythonista action extension when Safari is showing
# a GitHub Pull Request and will ask Working Copy to merge+pull the pull-request thus fullfulling it.
# You need to already have this repository cloned in Working Copy.
#
# It only works on public repositories, since the script lacks a way to authorize, but things
# happening in Working Copy can be fully authorized with either SSH Key or username / password.
#
# You can read about Pythonista at
#   http://omz-software.com/pythonista/
# and Working Copy at
#   https://WorkingCopyApp.com/
#
# I would like to hear your feedback and I am @palmin on Twitter.
#

import appex
import requests
import re
import urllib.request, urllib.parse, urllib.error
import webbrowser
from objc_util import *

# You need to fill out key with the value from URL Callback settings in Working Copy.
key = ""

def main():
	if key == "":
		print("You need to fill out key with value from Working Copy settings.")
		quit()
		
	if not appex.is_running_extension():
		print('Running in Pythonista app, using test data...\n')
		url = "https://github.com/owner/reponame/pull/1"
	else:
		url = appex.get_url()
		
	if url:
		# Parse and make sure this is pull request
		m = re.compile('^https:\/\/github\.com/([^/]+)\/([^/]+)/pull/([0-9]+)$').match(url)
		if m == None:
			print(("URL does not look like GitHub Pull Request:\n " + url))
			quit()
			
		# fetch Pull Request through API
		owner = m.group(1)
		repo = m.group(2)
		pr = m.group(3)
		url = "https://api.github.com/repos/%s/%s/pulls/%s" % (owner, repo, pr)
		req = requests.get(url)
		json = req.json()
		
		# pick out what we need
		baseRemote = json["base"]["repo"]["clone_url"]
		baseBranch = json["base"]["ref"]
		headRemote = json["head"]["repo"]["clone_url"]
		headBranch = json["head"]["ref"]
		
		# We need to checkout branch, pull latest commits, merge and push back.
		# This can be chained into one x-callback-url command for nicer syntax.
		# Read more at
		#   http://workingcopyapp.com/url-schemes.html#chain
		callback = "working-copy://x-callback-url/chain?repo=%s&key=%s" % (urllib.parse.quote(baseRemote), urllib.parse.quote(key))
		
		# make sure base branch is checked out
		callback += "&command=checkout&branch=%s" % (urllib.parse.quote(baseBranch))
		
		# pull to get latest commits
		callback += "&command=pull"
		
		# merge with head, creating and fetching from head remote if missing
		callback += "&command=merge&branch=%s&remote=%s&create=1" % (urllib.parse.quote(headBranch), urllib.parse.quote(headRemote))
		
		# push back merge commit to conclude
		callback += "&command=push"
		print(('callback: %s') % (callback))
		
		# webbrowser.open does not work from action extension
		app=UIApplication.sharedApplication()
		url=nsurl(callback)
		app._openURL_(url)
		
	else:
		print('No input URL found.')
		
if __name__ == '__main__':
	main()



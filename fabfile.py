from fabric.api import *
import os
import fabric.contrib.project as project

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
SITE_PATH = os.path.join(ROOT_PATH, '_site')


class FabricException(Exception):
    pass

def status():
    local('cd ' + SITE_PATH + ' && git status')    

def publish():
    with settings(abort_exception = FabricException):
    	message = prompt("Enter commit message:", default="Fab publish")
        try:
			local('jekyll build')
			local('cd ' + SITE_PATH + ' && git add . && git commit -m "%s" && git push origin master' % (message))
        except FabricException:
            print "Something wrong happened"

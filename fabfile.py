from fabric.api import local, lcd

def deploy():
	with lcd(''):
		local('git push origin master')
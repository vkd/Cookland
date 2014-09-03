from fabric.api import local

def prepare_deployment(branch_name):
	local('git push origin master')
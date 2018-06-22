
def welcome_msg(func):

	def add_msg(site_name):
		return 'Welcome To ' + (site_name)

	return add_msg

@welcome_msg
def site(site_name):
	return site_name

print(site('Python'))
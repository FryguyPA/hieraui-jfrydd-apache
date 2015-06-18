from app.form import Form

class Jfryddapache(Form):

	def validate(_self, form_data):
	    valid = True
	    if 'vhost' not in form_data or \
	       'docroot' not in form_data or \
	       'hostname' not in form_data or \
	       'source_repo' not in form_data:
	       valid = False
	    if valid is Fale:
	       return "Missing Info!"
	    return True

	def process(_self, form_data):
	    nodes = {}
		hostname = form_data['hostname']
		vhost = form_data['vhost']
		nodes[hostname] = {}
		nodes[hostname]['classes'] = ['jfrydd_apache']
		nodes[hostname]['jfrydd_apache::vhost'] = vhost
		nodes[hostname]['jfrydd_apache::docroot'] = form_data['docroot']
		nodes[hostname]['jfrydd_apache::source_repo'] = form_data['source_repo']

		return nodes


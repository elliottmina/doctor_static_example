import os

base_dir = os.path.dirname(os.path.realpath(__file__))
CONTENT_SOURCE_DIR = base_dir + '/content'
TEMPLATE_DIR = base_dir + '/templates'
RENDER_DIR = base_dir + '/docroot/static'
SYNDICATION = {
	'id':'http://example.com/',
	'link': {'href':'http://example.com/',},
	'title':'Quisque volutpat condimentum',
	'subtitle':'Integer euismod lacus luctus magna.',
	'author':{
		'name':'Joe Mama',
		'email':'jmama@example.com',
	},
	'category':['Aenean', 'Curabitur'],
	'contributors':[{
		'name':'Joe Mama', 
		'email':'jmama@example.com',
	},{
		'name':'Joe Daddy', 
		'email':'jdaddy@example.com',
	}],
	'icon':'http://example.com/icon.jpg',
	'logo':'http://example.com/logo.jpg',
	'rights':'Copyright Joe Mama 2016',
	'language':'en',
	'render_prefix':'http://example.com',
	'image_prefix':'http://example.com/images',
	'entry_title_template':'Read {}',
	'max_entries':10,
}

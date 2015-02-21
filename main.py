# coding: utf-8

import ui, os, sys, console

## Load Game modules and thier views
path = os.path.dirname(os.path.abspath(__file__))+'/games'

sys.path.append(path) ## added to make things work

ignore = ['__init__.py']

modules = [f.split('.')[0] for f in os.listdir(path) if f.endswith('.py') and f not in ignore]
	
## I hate myself for this :(
for module in modules:
	cmd = 'from games.%s import *' % module
	exec(cmd)
	
## making the names look pretty
names = []
for module in modules: 
	names.append({
		'title': module.replace('_',' ').title(),
		'accessory_type': 'detail_button',
		'info': ''
	})

views = [ui.load_view('games/'+module) for module in modules if module is not '__init__']

## TODO: fix to use a dictionary on push
def play_game(sender):
	'@type sender: ui.Button'
	v = sender.superview
	row,game = v['table'].selected_row
	v.navigation_view.push_view(views[game])

@ui.in_background	
def get_info(sender):
	index = sender.tapped_accessory_row
	console.alert('How to Play', names[index]['info'], button1='Cool', hide_cancel_button=True)

table_data = ui.ListDataSource(names)
table_data.accessory_action = get_info

main_view = ui.load_view()
main_view['table'].data_source = table_data
main_view['table'].delegate    = table_data

nav_view = ui.NavigationView(main_view)
nav_view.bar_tint_color = (.9,.9,.9)
nav_view.present('sheet', hide_title_bar=True)

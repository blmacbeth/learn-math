# coding: utf-8

import ui, os, sys

## Load Game modules and thier views
path = os.path.dirname(os.path.abspath(__file__))+'/games'

sys.path.append(path) ## added to make things work

ignore = ['__init__.py']

modules = [f.split('.')[0] for f in os.listdir(path) if f.endswith('.py') and f not in ignore]

## making the names look pretty
names = [module.replace('_',' ').title() for module in modules]

## I hate myself for this :(
for module in modules:
	cmd = 'from games.%s import *' % module
	exec(cmd)

views = [ui.load_view('games/'+module) for module in modules if module is not '__init__']

## TODO: fix to use a dictionary on push
def play_game(sender):
	'@type sender: ui.Button'
	v = sender.superview
	row,game = v['table'].selected_row
	v.navigation_view.push_view(views[game])

##print globals()

main_view = ui.load_view()
main_view['table'].data_source = ui.ListDataSource(names)

nav_view = ui.NavigationView(main_view)
nav_view.present('sheet', hide_title_bar=True)

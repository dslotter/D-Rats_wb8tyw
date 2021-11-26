'''Map Window Menu Model Module.'''
#
# Copyright 2021 John Malmberg <wb8tyw@gmail.com>
# Portions derived from works:
# Copyright 2009 Dan Smith <dsmith@danplanet.com>
# review 2019 Maurizio Andreotti  <iz2lxi@yahoo.it>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

# import logging

import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gio


# This makes pylance happy with out overriding settings
# from the invoker of the class
if not '_' in locals():
    import gettext
    _ = gettext.gettext


# pylint wants at least 2 public methods.
# pylint: disable=too-few-public-methods
class MapMenuModel(Gio.Menu):
    '''Creates the Menu Model for MapWindow.'''

    def __init__(self):
        Gio.Menu.__init__(self)

        item_refresh = Gio.MenuItem.new(_("Refresh"), 'win.refresh')
        item_clearcache = Gio.MenuItem.new(_("Delete local Map cache"),
                                           'win.clearcache')
        item_editsources = Gio.MenuItem.new(_("Edit Sources"),
                                            'win.editsources')

        menu_map = Gio.Menu.new()
        menu_map.append_item(item_refresh)
        menu_map.append_item(item_clearcache)
        menu_map.append_item(item_editsources)

        item_printable = Gio.MenuItem.new(_('Printable'), 'win.printable')
        item_printablevis = Gio.MenuItem.new(_("Printable (visible area)"),
                                             'win.printablevis')
        item_save = Gio.MenuItem.new(_("Save Image"), 'win.save')
        item_savevis = Gio.MenuItem.new(_('Save Image (visible area)'),
                                        'win.savevis')
        menu_export = Gio.Menu.new()
        menu_export.append_item(item_printable)
        menu_export.append_item(item_printablevis)
        menu_export.append_item(item_save)
        menu_export.append_item(item_savevis)

        menu_map.append_submenu(_("Export"), menu_export)
        self.append_submenu(_("Map"), menu_map)

    @staticmethod
    def add_actions(window):
        '''
        Add menu actions to the window.

        :param window: The map window
        :type window: 'map.Mapwindow
        '''

        action_refresh = Gio.SimpleAction.new('refresh', None)
        action_refresh.connect('activate', window.refresh_item_handler)
        window.add_action(action_refresh)

        action_clearcache = Gio.SimpleAction.new('clearcache', None)
        action_clearcache.connect('activate', window.clearcache_item_handler)
        window.add_action(action_clearcache)

        action_editsources = Gio.SimpleAction.new('editsources', None)
        action_editsources.connect('activate', window.editsources_item_handler)
        window.add_action(action_editsources)

        action_printable = Gio.SimpleAction.new('printable', None)
        action_printable.connect('activate', window.printable_item_handler)
        window.add_action(action_printable)

        action_printablevis = Gio.SimpleAction.new('printablevis', None)
        action_printablevis.connect('activate',
                                    window.printablevis_item_handler)
        window.add_action(action_printablevis)

        action_save = Gio.SimpleAction.new('save', None)
        action_save.connect('activate', window.save_item_handler)
        window.add_action(action_save)

        action_savevis = Gio.SimpleAction.new('savevis', None)
        action_savevis.connect('activate', window.savevis_item_handler)
        window.add_action(action_savevis)
# Copyright (c) 2015 Jacob Russo <madcap.russo+tattoo@gmail.com>
#
# Tattoo is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# Tattoo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with Tattoo; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from gi.repository import Gtk, Gio

class TattooHeaderBar(Gtk.HeaderBar):

    def __init__(self, window):
        Gtk.HeaderBar.__init__(self)
        self.set_show_close_button(True)
        self.props.title = "Tattoo"

        new_tab_button = Gtk.Button()
        icon = Gio.ThemedIcon(name="tab-new")
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        new_tab_button.add(image)
        new_tab_button.connect("clicked", window.open_new_tab)
        self.pack_start(new_tab_button)

        menu_button = Gtk.Button()
        icon = Gio.ThemedIcon(name="open-menu-symbolic")
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        menu_button.add(image)
        menu_button.connect("clicked", window.open_menu_dropdown)
        self.pack_end(menu_button)

        search_button = Gtk.Button()
        icon = Gio.ThemedIcon(name="system-search")
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        search_button.add(image)

        # searchbar = Gtk.SearchBar()
        # search_entry = Gtk.SearchEntry()
        # searchbar.connect_entry(search_entry)
        # self.add(searchbar)
        # search_button.connect("clicked", lambda s: s.set_search_mode(True))

        self.pack_end(search_button)

    def set_header_title(self, title):
        self.props.title = title

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

from gi.repository import Gtk, Gio, Vte
from gi.repository import GLib
from headerbar import TattooHeaderBar
import os


class TattooWindow(Gtk.ApplicationWindow):

    def __init__(self, app):
        Gtk.ApplicationWindow.__init__(self,
                                       application=app
                                       title="Tattoo")
        self.set_icon_from_file("tattoo-icon.png")
        self.set_border_width(0)
        self.set_default_size(800, 500)

        self.hb = TattooHeaderBar(self)
        self.set_titlebar(self.hb)

        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        terminal = Vte.Terminal()
        terminal.spawn_sync(
            Vte.PtyFlags.DEFAULT,
            os.environ['HOME'],
            ["/bin/zsh"],
            None,
            GLib.SpawnFlags.DO_NOT_REAP_CHILD,
            None,
            None,
            )

        first_tab_index = \
            self.notebook.append_page(terminal, terminal.get_window_title())
        terminal.connect(
            "window-title-changed",
            self.terminal_title_change,
            self.notebook,
            first_tab_index
            )

        self.notebook.set_show_tabs(False)
        self.notebook.connect(
            "switch-page",
            self.header_title_change
            )

        self.connect("destroy", self.on_destroy)



    def open_new_tab(self, *data):
        self.notebook.set_show_tabs(True)
        terminal = Vte.Terminal()
        terminal.spawn_sync(
            Vte.PtyFlags.DEFAULT,
            os.environ['HOME'],
            ["/bin/zsh"],
            None,
            GLib.SpawnFlags.DO_NOT_REAP_CHILD,
            None,
            None,
            )

        tab_index = \
            self.notebook.append_page(terminal, terminal.get_window_title())
        self.show_all()
        self.notebook.set_current_page(tab_index)
        terminal.connect(
            "window-title-changed",
            self.terminal_title_change,
            self.notebook,
            tab_index
            )

    def open_searchbar(self, *data):
        pass

    def open_menu_dropdown(self, *data):
        pass

    def on_destroy(self, widget):
        Gtk.main_quit()

    def header_title_change(self, notebook, terminal, index):
        # print args
        title = terminal.get_window_title()
        self.hb.set_header_title(title)

    def terminal_title_change(self, terminal, notebook, index):
        title = terminal.get_window_title()
        if notebook.get_current_page() == index:
            self.header_title_change(notebook, terminal, index)
        notebook.set_tab_label_text(terminal, title)

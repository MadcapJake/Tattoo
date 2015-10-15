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

import os

from gi.repository import Gtk, Gdk, Gio, Vte, GLib

from tattoo import TrackerWrapper
from tattoo.headerbar import TattooHeaderBar
from tattoo.terminal import TattooTerminal

from tattoo import log
import logging
logger = logging.getLogger(__name__)

tracker = TrackerWrapper().tracker


class TattooWindow(Gtk.ApplicationWindow):

    def __repr__(self):
        return '<TattooWindow>'

    @log
    def __init__(self, app):
        Gtk.ApplicationWindow.__init__(self,
                                       application=app,
                                       title="Tattoo")
        # self.connect('focus-in-event', self._windows_focus_cb)
        # self.settings = Gio.Settings.new('org.gnome.Tattoo')

        self.set_icon_from_file("tattoo-icon.png")
        self.set_border_width(0)
        self.set_default_size(800, 500)

        # size_setting = self.settings.get_vlaue('window-size')
        # if isinstance(size_setting[0], int) and isinstance(size_setting[1], int):
        #     self.resize(size_setting[0], size_setting[1])
        #
        # position_setting = self.settings.get_value('window-position')
        # if len(position_setting) == 2 \
        #    and isinstance(position_setting[0], int) \
        #    and isinstance(position_setting[1], int):
        #     self.move(position_setting[0], position_setting[1])

        # if self.settings.get_value('window-maximized'):
        #     self.maximize()

        self._setup_view()

        self.window_size_update_timeout = None
        # self.connect("window-state-event", self._on_window_state_event)
        # self.connect("configure-event", self._on_configure_event)

        self.show_all()


    @log
    def _setup_view(self):
        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        self._headerbar = TattooHeaderBar(self)
        self.set_titlebar(self._headerbar)

        terminal = TattooTerminal(self)
        terminal.index = self.notebook.append_page(terminal, terminal.get_title())

        self.notebook.set_show_tabs(False)
        self.notebook.connect(
            "switch-page",
            self.header_title_change)

        self.connect("destroy", self.on_destroy)


    def open_new_tab(self, *data):
        self._notebook.set_show_tabs(True)

        terminal = TattooTerminal(self)
        terminal.index = self._notebook.append_page(terminal, terminal.get_title())

        self.show_all()

    def open_searchbar(self, *data):
        pass

    def open_menu_dropdown(self, *data):
        pass

    def on_destroy(self, widget):
        Gtk.main_quit()

    def header_title_change(self, notebook, terminal, index):
        # print args
        title = terminal.get_title()
        self._headerbar.set_header_title(title)

    def terminal_title_change(self, terminal, notebook, index):
        if terminal is TattooTerminal:
            title = terminal.get_title()
        else:
            title = tterminal.get_window_title()
        if notebook.get_current_page() == index:
            self.header_title_change(notebook, terminal.get_terminal(), index)
        notebook.set_tab_label_text(terminal, title)

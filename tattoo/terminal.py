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

from gi.repository import Gtk, Vte, GLib

from tattoo import log
from tattoo.searchbar import TattooSearchBar

class TattooTerminal(Gtk.Overlay):

    def __repr__(self):
        return '<TattooTerminal>'

    @log
    def __init__(self, window):
        self.index = 0

        stack = Gtk.Stack(
            transition_type=Gtk.StackTransitionType.CROSSFADE,
            transition_duration=100,
            visible=True,
            can_focus=False
            )

        Gtk.Overlay.__init__(self, child=stack)
        self._searchbar = TattooSearchBar()
        self.add_overlay(self._searchbar)

        self._terminal = Vte.Terminal()
        self._terminal.spawn_sync(
            Vte.PtyFlags.DEFAULT,
            os.environ['HOME'],
            ["/bin/zsh"],
            None,
            GLib.SpawnFlags.DO_NOT_REAP_CHILD,
            None,
            None)

        self._terminal.connect(
            "window-title-changed",
            window.terminal_title_change,
            window.notebook,
            self.index)
        self.add_overlay(self._terminal)

    def get_title(self):
        return self._terminal.get_window_title()

    def get_terminal(self):
        return self._terminal

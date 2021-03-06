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

from gi.repository import Gtk

from tattoo import log

class TattooSearchBar(Gtk.SearchBar):

    def __repr__(self):
        return '<TattooSearchBar>'

    @log
    def __init__(self):
        Gtk.SearchBar.__init__(self)
        self.__entry = Gtk.SearchEntry()
        self.connect_entry(self.__entry)
        self.add(self.__entry)

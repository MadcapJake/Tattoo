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

from gi.repository import Gtk, Gio, GLib
from tattoo import log
from tattoo.window import TattooWindow

class TattooApplication(Gtk.Application):

    def __repr__(self):
        return '<TattooApplication>'

    @log
    def __init__(self):
        Gtk.Application.__init__(self,
                                 application_id='org.gnome.Tattoo',
                                 flags=Gio.ApplicationFlags.FLAGS_NONE)
        GLib.set_application_name("Tattoo")
        GLib.set_prgname('Tattoo')
        # self.settings = Gio.Settings.new('org.gnome.Tattoo')

        self._window = None

    @log
    def build_app_menu(self):
        builder = Gtk.Builder()
        builder.add_from_file('data/app-menu.ui')

        menu = builder.get_object('app-menu')
        self.set_app_menu(menu)

        newWindowAction = Gio.SimpleAction.new('newWindow', None)
        newWindowAction.connect('activate', self.newWindow)
        self.add_action(newWindowAction)

        preferencesAction = Gio.SimpleAction.new('preferences', None)
        preferencesAction.connect('activate', self.preferences)
        self.add_action(preferencesAction)

        helpAction = Gio.SimpleAction.new('help', None)
        helpAction.connect('activate', self.help)
        self.add_action(helpAction)

        aboutAction = Gio.SimpleAction.new('about', None)
        aboutAction.connect('activate', self.about)
        self.add_action(aboutAction)

        quitAction = Gio.SimpleAction.new('quit', None)
        quitAction.connect('activate', self.quit)
        self.add_action(quitAction)



    @log
    def new_window(self, action, param):
        pass

    @log
    def preferences(self, action, param):
        pass

    @log
    def help(self, action, param):
        pass

    @log
    def about(self, action, param):
        pass

    @log
    def do_startup(self):
        Gtk.Application.do_startup(self)

        self.build_app_menu()

    @log
    def quit(self, action=None, param=None):
        self._window.destroy()

    @log
    def newWindow(self, action, param):
        pass

    def do_activate(self):
        if not self._window:
            self._window = TattooWindow(self)
        self._window.present()

# tattoo = Gtk.Application.new(
#     "org.gnome.tattoo",
#     Gio.ApplicationFlags.FLAGS_NONE
#     )
#
# win = TattooWindow()
# win.set_application(tattoo)
# win.connect('delete-event', Gtk.main_quit)
# win.show_all()
#
# Gtk.main()

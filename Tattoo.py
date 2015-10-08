#!/usr/bin/env python

from gi.repository import Gtk
from TattooWindow import TattooWindow

win = TattooWindow()
win.connect('delete-event', Gtk.main_quit)
win.show_all()

Gtk.main()

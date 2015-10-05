#!/usr/bin/env python

from gi.repository import Gtk, Gio, Vte
from gi.repository import GLib
import os


class TattooWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Tattoo")
        self.set_icon_from_file("../../.icons/apps/tattoo-icon.png")
        self.set_border_width(0)
        self.set_default_size(800, 500)

        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = "Tattoo"
        self.set_titlebar(hb)

        new_tab_button = Gtk.Button()
        icon = Gio.ThemedIcon(name="tab-new")
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        new_tab_button.add(image)
        new_tab_button.connect("clicked", self.open_new_tab)
        hb.pack_start(new_tab_button)

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

        notebook.append_page(terminal, Gtk.Label("..."))
        terminal.connect(
            "window-title-changed",
            lambda t, n: n.set_tab_label_text(t, t.get_window_title()),
            notebook
            )

    def open_new_tab():



win = TattooWindow()
win.connect('delete-event', Gtk.main_quit)
win.show_all()

Gtk.main()

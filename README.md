![Logo](https://raw.githubusercontent.com/MadcapJake/Tattoo/master/tattoo-banner.png)

> *Tattoo A Terminal TOO*

Tattoo is a terminal emulator program written in Python GTK3 and using VTE for terminal emulation.  Tattoo was created to provide an aesthetically pleasing terminal emulator for Gnome Shell.

### Goals

* To provide a terminal app that fits the Gnome look
* To provide much of the functionality of Gnome Terminal
* To add some additional niceties

### Status

Currently works as a basic terminal with tabs. However it doesn't have any customization as none of the menus have been implemented yet.  Unless you want to jump into the code and change VTE's settings, your terminal is stuck with the default settings (e.g., color).

### Roadmap

* Wire up menu dropdown
* Add application menu
* Dropdown menus for each tab
* Searchbar ala Nautilus that searches zsh/fish/bash command history or builds and executes `find` commands in the current tab.
* Add configuration/settings for most/all of Gnome Terminal preferences
* Support DnD of tabs between Tattoo windows
* Allow importing popular theme/colorscheme formats
* Colored emoji in the terminal!
* Zsh/Fish builtin prompt-builder and configuration

## Contribute

I have no experience packaging a Python application up or building install scripts so any help with that would be greatly appreciated!

Don't forget to submit your issues/suggestions!

## License

Copyright © 2015 Jacob Russo et al.

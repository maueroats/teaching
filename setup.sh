#! /bin/bash

BASE=$HOME/.config/i3
WWW=$HOME/Documents/2017-2018/www/wy-cs
cd $WWW
i3-msg "workspace 3; append_layout $BASE/workspace-3.json"
x-terminal-emulator --title "www-hugo-server" -e "./hugo-server" &
x-terminal-emulator --title "www-fish" -e fish &
emacs content/. &


#! /usr/bin/env bash

sources=$(pwd)

ln -sf $sources/i3 ~/.config/i3
ln -sf $sources/urxvt ~/.config/urxvt
ln -sf $sources/polybar ~/.config/polybar

echo "feh --bg-fill $sources/wallpaper.jpg" > ~/.fehbg

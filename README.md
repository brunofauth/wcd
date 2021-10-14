# Wallpaper Changing Daemon (wcd)
Wallpaper Changing Daemon reminds me of mpd, but it manages wallpapers instead of music.

It comes with wcc (not to be confused with iwcc) too, which is a CLI client app, used to interact with the Daemon.

It works on python 3.9 (and, probably, on 3.7 and 3.8 too, not sure about lower versions though).

It only depends on PyYAML (and, consequently, on LibYAML).

It copies it's default config file into ~/.config/wcd/, or to wherever you point it to, via $WCD_CFG.

I only code as a hobby, but I'd say I made a good job to make this very readable and, thus, feel very welcomed to check how things are implemented, to get a better understanding of what this program does, it's capabilities, etc...

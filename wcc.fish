set -l commands "list set get next prev toggle_cycle toggle_random shuffle refresh"
set -l cond "not __fish_seen_subcommand_from $commands" 

# Disable completing with file names, by default
complete -c wcc -f

# Add completions to all subcommands
complete -c wcc -n $cond -a list -d "list available wallpapers" -f
complete -c wcc -n $cond -a set -xd "set current wallpaper to another available one (see 'wcc list')"
complete -c wcc -n $cond -a get -d "get the name of the currently displayed wallpaper"
complete -c wcc -n $cond -a next -d "switch to the next wallpaper in queue and get its name"
complete -c wcc -n $cond -a prev -d "switch to the previous wallpaper in history and get its name"
complete -c wcc -n $cond -a toggle_cycle -d "toggle automatically cycling wallpapers"
complete -c wcc -n $cond -a toggle_random -d "toggle randomizing the wallpaper queue when it gets exhausted"
complete -c wcc -n $cond -a shuffle -d "shuffle the current wallpaper queue"
complete -c wcc -n $cond -a refresh -d "reload wallpapers from the wallpapers_directory variable, set on wcd's cfg"

# Add completions to all options
complete -c wcc -s h -l help -d "show help information and exit"
complete -c wcc -s s -l socket -rFd "set the path to wcd's socket (read from wcd's cfg by default)"

# Add completions to each subcommand that needs them
complete -c wcc -n "__fish_seen_subcommand_from set" -a "(wcc list)"


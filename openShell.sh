#!/bin/bash

# Set xterm title
echo -ne "\033]0;Shell\007"

# Follows the logic of the following:
# If there are no tmux sessions, create one
# If there is a non attached tmux session, attach to it
# If there is not a non attached tmux session, create a new one



# If there are no tmux sessions, create one
if [ -z "$(tmux list-sessions)" ]; then
	tmux -u new-session
else
	# Find all non attached tmux sessions
	sessions=$(tmux list-sessions | grep -v attached)
	# If there is are non create a new one
	if [ -z "$sessions" ]; then
		tmux -u new-session
	else
		# Attach to the first non attached session
		tmux -u attach-session -t $(echo $sessions | head -n 1 | cut -d ':' -f 1)
	fi
fi



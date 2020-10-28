#!/usr/bin/env python3


import i3ipc
i3 = i3ipc.Connection()

# Show bar only on workspace 10
def workspace_focus(i3, e):
	if e.current.num == 10:
		i3.command("bar mode dock")
	else:
		i3.command("bar mode invisible")

i3.on("workspace::focus", workspace_focus)
i3.main()

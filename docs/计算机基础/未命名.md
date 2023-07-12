```c
// Music play buttom
READ button
if button pressed
	if music playing
		current track pause
	else music paused
		current track play
	endif
endif	
```
```c
// Select music track
READ drop-down item
if drop-down item pressed
	current track pause
	current track = selected item
	current track play
endif
```
```c
// Previous poster
READ button
if button pressed && current poster != frist poster
	current poster = previous poster
endif

//Next poster
READ button
if button pressed && current poster != last poster
	current poster = next poster
endif
```
```c
// Scroll listed content
READ scrollbar
if scrollbar value changed
	content.progress = percent(scrollbar value)
endif
```

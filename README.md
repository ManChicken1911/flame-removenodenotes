# Flame RemoveNodeNotes
by Bob Maple (bobm-matchbox [at] idolum.com)

This script is licensed under the Creative Commons Attribution-ShareAlike [CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/)

![Flame version 2024+](https://img.shields.io/badge/Flame-2024+-green)

## What

Remove Node Notes is a Python script for Autodesk Flame 2024 and above
that deletes the notes on selected Batch nodes. Handy for quickly clearing
away the clutter if you use a lot of 3rd-party Matchbox nodes in particular,
which generally come with their instructions in the notes.

## How

Copy into `/opt/Autodesk/shared/python` - if Flame was already running,
use **Rescan Python Hooks** from the **Flame** > **Python** menu.

Select one or more nodes in Batch/BFX, right-click, and run **Remove Notes**
from the **Node Tools** menu near the bottom.

You can also assign a hotkey to Remove Notes to make it even easier.
While in Batch/BFX, go to the **Flame** menu > **Keyboard Shortcuts**
and then search for **Node Tools**.  I assigned it to `Alt-R`, but
you do you.

## Warning

Remove Notes does not trigger Flame's Undo stack, so there's no going back!

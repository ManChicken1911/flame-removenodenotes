# Remove Node Notes by Bob Maple
# VER: 2026-06-10
#
# Removes any notes on selected (or all) Batch nodes. That's it!
# See the 'Node Tools' context menu in Batch and/or assign it to a hotkey

def get_batch_custom_ui_actions():

    def del_node_note(sel):
        import flame

        if( not sel ):
            dlgresponse = flame.messages.show_in_dialog( "Remove Node Notes", "No nodes are selected. Do you want to delete the notes from ALL nodes?", "question", ['Delete All'], 'Cancel' )
            if( dlgresponse == "Delete All" ):
                sel = flame.batch.nodes
            else:
                return()

        node_count = 0

        for curThing in sel:
            if( isinstance(curThing, flame.PyNode) ):
                if( curThing.note.get_value() ):
                    curThing.note.set_value("")
                    node_count += 1

        tmp_msg = "Removed " + str( node_count ) + " node note" + ("" if node_count == 1 else "s")
        flame.messages.show_in_console( tmp_msg, "info", 4 )

    return [
        {
            "name": "Node Tools",
            "actions": [
                {
                    "name": "Remove Notes",
                    "execute": del_node_note,
                }
            ],
        }
    ]

from krita import Krita

def create_layer_and_hide_previous():
    app = Krita.instance()
    doc = app.activeDocument()

    if not doc:
        print("No active document found.")
        return

    # Get the currently selected layer
    selected_layer = doc.activeNode()

    # Create a new paint layer
    new_layer = doc.createNode("New Layer", "paintLayer")
    
    # Add the new layer to the document
    doc.rootNode().addChildNode(new_layer, None)

    # Make the previously selected layer invisible
    if selected_layer:
        selected_layer.setVisible(False)

    # Refresh the view
    doc.refreshProjection()

# Run the function
create_layer_and_hide_previous()
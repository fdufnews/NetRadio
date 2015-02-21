As a help to modify the skins I made the area.ods file with LibreOffice Calc

The skins in the skins directory are all generated from skin.svg edited with Inkscape
there are five layers on the drawing:
 - Fond contains the background
 - Menu1 contains the design of Menu1
 - Menu2 contains the design of Menu2
 - OmbreMenu1 contains the glow effect of Menu1
 - OmbreMenu2 contains the glow effect of Menu2

The glow layer is generated from the corresponding menu layer
The menu layer is copied to the glow layer and a fuzzy effect is applied to the layer.

To generate the Menu1 skin, the Menu2 and OmbreMenu2 shall be hidden
The remaining layers are exported as a bitmap.
To generate the Menu2 skin, the Menu1 and OmbreMenu1 shall be hidden
The remaining layers are exported as a bitmap.

All the Menu layers are drawn using the same color. By selecting all the items and changing the color any colored skins can be made.

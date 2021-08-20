import bpy
import base64
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty, FloatVectorProperty
from bpy.types import Operator

def writeshaderp3dxml(shader,texture,filepath,light,filtermode,pddishader):
    #Updated from writing to file several times. Write to string instead and write the string to the file at the end :) 
    data = ""
    data = data + '\n    <Chunk Type="0x11000">\n        <Value Name="Name" Value="'+str(shader)+'"/>\n        <Value Name="Version" Value="0" />'
    data = data + '\n        <Value Name="PddiShaderName" Value="'+str(pddishader)+'"/>'
    data = data + """\n        <Value Name="HasTranslucency" Value="1" />
        <Value Name="VertexNeeds" Value="33" />
        <Value Name="VertexMask" Value="0xFFFC3FE1" />
        <Chunk Type="0x11002">"""
    data = data + '\n            <Value Name="Value" Value="'+str(texture)+'"/>'
    data = data + """\n			<Value Name="Param" Value="TEX" />
        </Chunk>
        <Chunk Type="0x11003">
            <!--1. "LIT" (Shader Integer Parameter)-->"""
    data = data + '\n			<Value Name="Value" Value="'+str(light)+'"/>'
    data = data + """\n			<Value Name="Param" Value="LIT" />
        </Chunk>
        <Chunk Type="0x11003">
            <!--2. "CBVA" (Shader Integer Parameter)-->
            <Value Name="Value" Value="1" />
            <Value Name="Param" Value="CBVA" />
        </Chunk>
        <Chunk Type="0x11003">
            <!--3. "CBVB" (Shader Integer Parameter)-->
            <Value Name="Value" Value="2" />
            <Value Name="Param" Value="CBVB" />
        </Chunk>
        <Chunk Type="0x11003">
            <!--4. "2SID" (Shader Integer Parameter)-->
            <Value Name="Value" Value="0" />
            <Value Name="Param" Value="2SID" />
        </Chunk>
        <Chunk Type="0x11003">
            <!--5. "SHMD" (Shader Integer Parameter)-->
            <Value Name="Value" Value="1" />
            <Value Name="Param" Value="SHMD" />
        </Chunk>
        <Chunk Type="0x11003">
            <!--6. "FIMD" (Shader Integer Parameter)-->"""
    data = data + '\n			<Value Name="Value" Value="'+str(filtermode)+'"/>'
    data = data + """\n			<Value Name="Param" Value="FIMD" />
        </Chunk>
        <Chunk Type="0x11003">
            <!--7. "BLMD" (Shader Integer Parameter)-->
            <Value Name="Value" Value="1" />
            <Value Name="Param" Value="BLMD" />
        </Chunk>
        <Chunk Type="0x11003">
            <!--8. "PLMD" (Shader Integer Parameter)-->
            <Value Name="Value" Value="0" />
            <Value Name="Param" Value="PLMD" />
        </Chunk>
        <Chunk Type="0x11003">
            <!--9. "UVMD" (Shader Integer Parameter)-->
            <Value Name="Value" Value="0" />
            <Value Name="Param" Value="UVMD" />
        </Chunk>
        <Chunk Type="0x11003">
            <!--10. "CBVM" (Shader Integer Parameter)-->
            <Value Name="Value" Value="0" />
            <Value Name="Param" Value="CBVM" />
        </Chunk>
        <Chunk Type="0x11003">
            <!--11. "MMIN" (Shader Integer Parameter)-->
            <Value Name="Value" Value="0" />
            <Value Name="Param" Value="MMIN" />
        </Chunk>
        <Chunk Type="0x11003">
            <!--12. "ACMP" (Shader Integer Parameter)-->
            <Value Name="Value" Value="4" />
            <Value Name="Param" Value="ACMP" />
        </Chunk>
        <Chunk Type="0x11003">
            <!--13. "ATST" (Shader Integer Parameter)-->
            <Value Name="Value" Value="0" />
            <Value Name="Param" Value="ATST" />
        </Chunk>
        <Chunk Type="0x11003">
            <!--14. "MCBV" (Shader Integer Parameter)-->
            <Value Name="Value" Value="0" />
            <Value Name="Param" Value="MCBV" />
        </Chunk>
        <Chunk Type="0x11003">
            <!--15. "MMAX" (Shader Integer Parameter)-->
            <Value Name="Value" Value="7" />
            <Value Name="Param" Value="MMAX" />
        </Chunk>
        <Chunk Type="0x11003">
            <!--16. "MMEX" (Shader Integer Parameter)-->
            <Value Name="Value" Value="0" />
            <Value Name="Param" Value="MMEX" />
        </Chunk>
        <Chunk Type="0x11004">
            <!--17. "ACTH" (Shader Float Parameter)-->
            <Value Name="Value" Value="0.5" />
            <Value Name="Param" Value="ACTH" />
        </Chunk>
        <Chunk Type="0x11004">
            <!--18. "SHIN" (Shader Float Parameter)-->
            <Value Name="Value" Value="10" />
            <Value Name="Param" Value="SHIN" />
        </Chunk>
        <Chunk Type="0x11004">
            <!--19. "MSHP" (Shader Float Parameter)-->
            <Value Name="Value" Value="0.5" />
            <Value Name="Param" Value="MSHP" />
        </Chunk>
        <Chunk Type="0x11004">
            <!--20. "CBVV" (Shader Float Parameter)-->
            <Value Name="Value" Value="0" />
            <Value Name="Param" Value="CBVV" />
        </Chunk>
        <Chunk Type="0x11005">
            <!--21. "SPEC" (Shader Colour Parameter)-->
            <Value Name="Value" Red="0" Green="0" Blue="0" />
            <Value Name="Param" Value="SPEC" />
        </Chunk>
        <Chunk Type="0x11005">
            <!--22. "CBVC" (Shader Colour Parameter)-->
            <Value Name="Value" Red="255" Green="255" Blue="255" />
            <Value Name="Param" Value="CBVC" />
        </Chunk>
        <Chunk Type="0x11005">
            <!--23. "DIFF" (Shader Colour Parameter)-->
            <Value Name="Value" Red="255" Green="255" Blue="255" />
            <Value Name="Param" Value="DIFF" />
        </Chunk>
        <Chunk Type="0x11005">
            <!--24. "AMBI" (Shader Colour Parameter)-->
            <Value Name="Value" Red="255" Green="255" Blue="255" />
            <Value Name="Param" Value="AMBI" />
        </Chunk>
        <Chunk Type="0x11005">
            <!--25. "EMIS" (Shader Colour Parameter)-->
            <Value Name="Value" Red="0" Green="0" Blue="0" />
            <Value Name="Param" Value="EMIS" />
        </Chunk>
    </Chunk>"""
    with open(filepath, 'a') as file:
        file.write(data)
    return
    
def writetexturep3dxml(texture,image,filepath):
    texture = str(texture)
    with open(image, "rb") as image_file:
        b64 = str(base64.b64encode(image_file.read()))
    b64 = b64[1:]
    b64 = b64[1:]
    b64 = b64[:-1]
    b64.replace("'", "")
    
    width, height = bpy.data.images[texture].size
    
    #PIL not included with python
    #with Image.open(image) as img:
    #    width, height = img.size
    
    data = ""
    
    #Excuse my some unoptimized code
    data = data + '\n    <Chunk Type="0x19000">\n        <Value Name="Name" Value="'+texture+'" />\n		<Value Name="Version" Value="14000" />'
    data = data + '\n        <Value Name="Width" Value="'+str(width)+'" />\n        <Value Name="Height" Value="'+str(height)+'" />'
    data = data + """\n		<Value Name="Bpp" Value="8" />
        <Value Name="AlphaDepth" Value="0" />
        <Value Name="TextureType" Value="1" />
        <Value Name="Usage" Value="0" />
        <Value Name="Priority" Value="0" />
        <Chunk Type="0x19001">"""
    data = data + '\n            <Value Name="Name" Value="'+texture+'" />\n            <Value Name="Version" Value="14000" />'
    data = data + '\n            <Value Name="Width" Value="'+str(width)+'" />\n            <Value Name="Height" Value="'+str(height)+'" />'
    data = data + """\n			<Value Name="Bpp" Value="8" />
            <Value Name="Palettized" Value="1" />
            <Value Name="HasAlpha" Value="0" />
            <Value Name="Format" Value="1" />
            <Chunk Type="0x19002">"""
    data = data + '\n                <Value Name="ImageData" Value="'+str(b64)+'" />'
    data = data + """\n			</Chunk>
        </Chunk>
    </Chunk>"""
    
    with open(filepath, 'a') as file:
        file.write(data)
    return


def write_shader_data(context, filepath, selected, lighting, filtermode, pddishader):
    print("Exporting textures & shaders...")
    
    shader = ""
    texture = ""
    image = ""
    
    #lightingoption
    if lighting == True:
        light = 1
    else:
        light = 0
    
    #Let's create the file first
    f = open(filepath, 'w')
    f.close
    
    with open(filepath, 'a') as f:
        f.write("""<?xml version="1.0" encoding="utf-8"?>
<!--Created with Tays's P3DXML texture&shader exporter, template xml file created with Lucas' Pure3D Editor 4.5-->
<Pure3DFile LucasPure3DEditorVersion="4.4">""")
    
    if selected == True:
        objs = bpy.context.selected_objects
    else:
        objs = bpy.data.objects
    
    #Keep track of what textures have been written to the file already
    texlist = []
    
    #Textures go first in the file else shaders won't be able to find their texture.
    with open(filepath, 'a') as file:
        for ob in objs:
            if ob.type == "MESH":
                for mat_slot in ob.material_slots:
                    if mat_slot.material:
                        if mat_slot.material.node_tree:
                            shader = str(mat_slot.material.name)            
                            for x in mat_slot.material.node_tree.nodes:
                                if x.type=='TEX_IMAGE':
                                    if x.image != None:
                                        texture = str(x.image.name)  
                                        
                                        #So there is no duplicates
                                        if texture in texlist:
                                            continue
                                        else:        
                                            #image = bpy.path.abspath("//")
                                            image = bpy.path.abspath("//") + x.image.filepath
                                            
                                            #gotta love these file paths
                                            try:
                                                with open(image, "rb") as image_file:
                                                    b64 = str(base64.b64encode(image_file.read()))
                                            except OSError:
                                                image = x.image.filepath
                                            
                                            texlist.append(texture)
                                            writetexturep3dxml(texture,image,filepath)
    shadlist = []    
    
    #Shaders
    with open(filepath, 'a') as file:
        for ob in objs:
            if ob.type == "MESH":
                for mat_slot in ob.material_slots:
                    if mat_slot.material:
                        if mat_slot.material.node_tree:
                            shader = str(mat_slot.material.name)
                            if shader in shadlist:
                                continue
                            else:            
                                for x in mat_slot.material.node_tree.nodes:
                                    if x.type=='TEX_IMAGE':
                                        if x.image != None:
                                            texture = str(x.image.name)  
                                        else:
                                            texture = ""
                                shadlist.append(shader)
                                writeshaderp3dxml(shader,texture,filepath,light,filtermode,pddishader)
                            
    with open(filepath, 'a') as file:
        file.write("\n</Pure3DFile>")
        file.close()
    f.close()
    file.close()
    print("SUCCESS")
    return {'FINISHED'}

class ExportShaderData(Operator, ExportHelper):
    """Exports textures and shaders into p3dxml format"""
    bl_idname = "export_texshad.p3dxml"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Export"

    # ExportHelper mixin class uses this
    filename_ext = ".p3dxml"

    filter_glob: StringProperty(
        default="*.p3dxml",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )
    
    pddishader: EnumProperty(
    name = 'PDDI Shader',
    description = 'Filter mode in p3d edtior.',
    items = (
            ('error', 'error', ''),
            ('simple', 'simple', ''),
            ('lightweight', 'lightweight', ''),
            ('lightmap', 'lightmap', ''),
            ('environment', 'environment', ''),
            ('spheremap', 'spheremap', ''),
            ('projtex', 'projtex', ''),
            ('pointsprite', 'pointsprite', ''),
            ('layered', 'layered', ''),
            ('layeredlmap', 'layeredlmap', ''),
            ('toon', 'toon', ''),
            ('hctune', 'hctune', '')),
        default = 'simple'
    )
    

    diffuse: FloatVectorProperty(  
        name="Diffuse",
        subtype='COLOR',
        default=(1.0, 1.0, 1.0),
        min=0.0, max=1.0,
        description="Diffuse in the p3d editor. Only works with lighting enabled."
    )
    blendmode: EnumProperty(
    name = 'Blend Mode',
    description = 'Blend mode in p3d edtior.',
    items = (
            ('0', 'None', ''),
            ('1', 'Alpha', ''),
            ('2', 'Additive', ''),
            ('3', 'Subtractive', '')),
        default = '1'
    )
    
    filtermode: EnumProperty(
    name = 'Filter Mode',
    description = 'Filter mode in p3d edtior.',
    items = (
            ('0', 'Nearest Neighbour', ''),
            ('1', 'Linear', ''),
            ('2', 'Nearest Neighbour, Mip Nearest Neighbour', ''),
            ('3', 'Linear, Mip Nearest Neighbour', ''),
            ('4', 'Linear, Mip Linear', '')),
        default = '1'
    )
    
    uvmode: EnumProperty(
    name = 'UV Mode',
    description = 'UV mode in p3d edtior.',
    items = (
            ('0', 'Tile', ''),
            ('1', 'Clamp', '')),
        default = '0'
    )

    envmaptex: StringProperty(
    name = 'Texture',
    description = 'Envmap texture in p3d edtior.'
    )

    envmapcolour: FloatVectorProperty(  
        name="Colour",
        subtype='COLOR',
        default=(1.0, 1.0, 1.0),
        min=0.0, max=1.0,
        description="Envmap colour in the p3d editor."
    )
    
    lighting: BoolProperty(
        name="Lighting",
        description="Lighting option in the p3d editor.",
        default=False,
    )
    
    alphatest: BoolProperty(
        name="Alpha Test",
        description="Alpha test option in the p3d editor.",
        default=False,
    )
    
    twosided: BoolProperty(
        name="Two Sided",
        description="Two Sided test option in the p3d editor.",
        default=False,
    )
    
    selected: BoolProperty(
        name="Selected only",
        description="Export the textures and shaders of the selected objects only.",
        default=False,
    )

    def execute(self, context):
        return write_shader_data(context, self.filepath, self.selected, self.lighting, self.filtermode, self.pddishader)


    def draw(self, context):
        layout = self.layout
        box = layout.box()
        col = box.column_flow(align=False)
            
        col.prop(self, "pddishader")
        col.prop(self, "diffuse")
        col.prop(self, "blendmode")
        col.prop(self, "filtermode")
        col.prop(self, "uvmode")

        envmapbox = col.box()
        envmapboxcol = envmapbox.column_flow(align=False)
        envmapboxcol.label(text="Enviroment Map")
        envmapboxcol.prop(self,"envmaptex")
        envmapboxcol.prop(self,"envmapcolour")
        
        col.prop(self, "lighting")
        col.prop(self, "alphatest")
        col.prop(self, "twosided")
        col.prop(self, "selected")


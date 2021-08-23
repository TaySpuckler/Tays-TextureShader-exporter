import bpy
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty, FloatVectorProperty
from bpy.types import Operator

from .operators.export_p3dxml import ExportShaderData
#from .exportPanels import export_panel_1, export_panel_2

bl_info = {
    "name": "Tay's P3DXML texture & Shader Exporter",
    "author": "Tay",
    "version": (1, 0, 1),
    "blender": (2, 93, 1),
    "wiki_url": "https://github.com/Tayerf/Tays-TextureShader-exporter",
    "support": "COMMUNITY",
    "location": "File > Export",
    "category": "Import-Export",
}

def menu_func_export(self, context):
    self.layout.operator(ExportShaderData.bl_idname, icon="MATERIAL", text="Export textures & shaders (.p3dxml)")


def register():
    bpy.utils.register_class(ExportShaderData)
    #bpy.utils.register_class(export_panel_1)
    #bpy.utils.register_class(export_panel_2)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)


def unregister():
    bpy.utils.unregister_class(ExportShaderData)
    #bpy.utils.unregister_class(export_panel_1)
    #bpy.utils.unregister_class(export_panel_2)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)


if __name__ == "__main__":
    register()

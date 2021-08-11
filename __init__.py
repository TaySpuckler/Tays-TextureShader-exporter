import bpy
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty, FloatVectorProperty
from bpy.types import Operator

from .operators.export_p3xml import ExportShaderData

bl_info = {
    "name": "Tay's P3DXML texture & Shader Exporter",
    "author": "Tay",
    "version": (0, 7, 0),
    "blender": (2, 93, 1),
    "wiki_url": "https://github.com/Twela/textureshader-exporter",
    "support": "COMMUNITY",
    "location": "File > Export",
    "category": "Import-Export",
}

def menu_func_export(self, context):
    self.layout.operator(ExportShaderData.bl_idname, icon="MATERIAL", text="Export textures & shaders (.p3dxml)")


def register():
    bpy.utils.register_class(ExportShaderData)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)


def unregister():
    bpy.utils.unregister_class(ExportShaderData)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)


if __name__ == "__main__":
    register()

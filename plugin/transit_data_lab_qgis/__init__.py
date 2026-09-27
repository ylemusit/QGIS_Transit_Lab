"""Transit Data Lab for QGIS - minimal plugin entry point."""


def classFactory(iface):
    from .plugin import TransitDataLabPlugin
    return TransitDataLabPlugin(iface)

"""Minimal research skeleton for Transit Data Lab integration with QGIS."""

from qgis.PyQt.QtWidgets import QAction, QMessageBox


class TransitDataLabPlugin:
    def __init__(self, iface):
        self.iface = iface
        self.action = None

    def initGui(self):
        self.action = QAction("Transit Data Lab", self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addPluginToMenu("Transit Data Lab", self.action)
        self.iface.addToolBarIcon(self.action)

    def unload(self):
        if self.action is not None:
            self.iface.removePluginMenu("Transit Data Lab", self.action)
            self.iface.removeToolBarIcon(self.action)
            self.action = None

    def run(self):
        QMessageBox.information(
            self.iface.mainWindow(),
            "Transit Data Lab",
            "Research skeleton loaded successfully.",
        )

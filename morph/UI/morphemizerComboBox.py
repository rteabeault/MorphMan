from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QComboBox

class MorphemizerComboBox(QComboBox):
    name_role = Qt.UserRole + 1
    morphemizer_role = Qt.UserRole + 2

    def __init__(self, morphemizerRegistry=None, parent=None):
        super(MorphemizerComboBox, self).__init__(parent)

        if morphemizerRegistry:
            self.setMorphemizerRegistry(morphemizerRegistry)

        self.setCurrentIndex(0)

    def setMorphemizerRegistry(self, morphemizerRegistry):
        morphemizerRegistry.morphemizer_added.connect(self._add_morphemizer)
        morphemizerRegistry.morphemizer_removed.connect(self._remove_morphemizer)

        for morphemizer in morphemizerRegistry.getMorphemizers():
            self._add_morphemizer(morphemizer)

    def getCurrent(self):
        return self.currentData()

    def setCurrentByName(self, name):
        self.setCurrentIndex(self.findData(name, role=self.name_role))

    def _add_morphemizer(self, morphemizer):
        self.addItem(morphemizer.getDescription(), morphemizer)
        self.setItemData(self.findData(morphemizer), morphemizer.getName(), self.name_role)

    def _remove_morphemizer(self, morphemizer):
        self.removeItem(self.findText(morphemizer.getDescription()))

from PySide6.QtWidgets import (QWidget, QLabel, QLineEdit,
                               QVBoxLayout, QHBoxLayout, QPushButton)

class settingsWidget(QWidget):
    def __init__(self,parent=None,state=None):
        super().__init__()
        self.parent=parent
        self.setWindowTitle("Paramètres")
        self.state=state
        
        db_name_widget=QWidget(self)
        label_db_name=QLabel("Nom de la base de données")
        self.name_db_lineedit=QLineEdit(text=self.state.db_name)
        dbnw_layout=QHBoxLayout()
        dbnw_layout.addWidget(label_db_name)        
        dbnw_layout.addWidget(self.name_db_lineedit)
        db_name_widget.setLayout(dbnw_layout)

        validate_button=QPushButton("Valider")
        validate_button.clicked.connect(self.validate_settings)
        self.info=QLabel("")
        
        main_layout=QVBoxLayout(self)
        main_layout.addWidget(db_name_widget)
        main_layout.addWidget(validate_button)
        main_layout.addWidget(self.info)
        self.setLayout(main_layout)
        
    def validate_settings(self):
        self.state.db_name=self.name_db_lineedit.text()
        self.info.setText("Modifications prises en compte!")
        self.parent.team_list_build()

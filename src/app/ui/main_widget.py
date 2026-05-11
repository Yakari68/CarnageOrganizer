import sys
from PySide6.QtWidgets import (QApplication, QWidget,
                               QVBoxLayout, QHBoxLayout, QMainWindow)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QIntValidator
from app.logics.teams import Team
from app.ui.match import MatchWidget
from random import shuffle
from math import log2
from app.core.state import AppState

class mainWidget(QWidget):
    def __init__(self,parent=None,state=None):
        super().__init__(parent)
        self.state=state
        self.teamlist=self.state.teamlist
#         self.build_ui()

    def build_ui(self):
        matchs=[[MatchWidget(parent=self,top_team=self.teamlist[i],bottom_team=self.teamlist[i+1]) for i in range(0,len(self.teamlist),2)]]
        
        previous=0
        while len(matchs[previous])!=1:
            matchs_to_add=[MatchWidget(parent=self) for k in range(len(matchs[previous])//2)]
            matchs.append(matchs_to_add)
            previous+=1
        layout=QVBoxLayout(self)

        rounds = [QWidget(self) for _ in range(int(log2(len(self.teamlist))))]
        rounds_layouts=[QHBoxLayout(rounds[i]) for i in range(len(rounds))]
        for i in range(len(rounds)):
            for m in matchs[i]:
                rounds_layouts[i].addWidget(m)
        for i in range(1,len(matchs)):
            prev_matchs_counter=0
            for m in matchs[i]:
                rounds_layouts[i].addWidget(m)
                # à modifier en fonction de matchs_init une fois généralisé
                matchs[i-1][prev_matchs_counter].winner.connect(m.set_top_team)
                matchs[i-1][prev_matchs_counter+1].winner.connect(m.set_bottom_team)
                prev_matchs_counter+=2
        for i in range(len(rounds)):
            rounds[i].setLayout(rounds_layouts[i])

        for r in rounds:
            layout.addWidget(r)
        self.setLayout(layout)


'''
Created on 26.11.2014

@author: Waetzold Plaum
'''

import BContainer
import PyLinXHelper

class RootContainer(BContainer.BContainer):
    '''
    classdocs
    '''

    def __init__(self, ui):
        '''
        Constructor
        '''
        super(RootContainer, self).__init__("root")
        self.__ui = ui
        self.__listActions = [None, ui.actionNewElement, ui.actionNewPlus]
        
    def set(self, attr, value):
        
        if attr == "idxToolSelected":
            idxToolSelectedOld = self.get("idxToolSelected")
            if idxToolSelectedOld not in [None, 0]:
                oldAction = self.__listActions[idxToolSelectedOld]
                oldAction.setChecked(False)
            if value > 0 and value <= PyLinXHelper.ToolSelected.max:
                self.__listActions[value].setChecked(True)
                return BContainer.BContainer.set(self,"idxToolSelected", value)
            elif value == 0:
                return BContainer.BContainer.set(self,"idxToolSelected", 0)
        else:
            return BContainer.BContainer.set(self,attr, value)
#!/usr/bin/env python3
from cement.core import foundation, controller, handler
from cement.core.controller import CementBaseController, expose

# define application controllers
class DemoPluginluginController(CementBaseController):
    class Meta:
        label = 'DemoPlugin'
        description = "Demo Plugin"
        stacked_on = 'base'
        stacked_type = 'embedded'
        arguments = [
            (['--foo'], dict(help="option under base controller")),
    
            ]
    @expose(help="another base controller command")
    def plugncmd1(self):
        print("Inside DemoPluginluginController.plugncmd1()")



def load(myapp):
    handler.register(DemoPluginluginController)
    
      
import sys
from django.db import models
from util import get_image_specs

class IKPresetField(models.CharField):
    """
       Defines choices from list of ImageSpec classes
       found in the model's IKOptions.spec_module
    """
    def __init__(self, *args, **kwargs):
        kwargs.update({'choices':()})
        super(IKPresetField, self).__init__(*args, **kwargs)
        
    def preset_choices(self):
        spec_pkg = __import__(self.model.IKOptions.spec_module)
        spec_module = sys.modules[self.model.IKOptions.spec_module]
    
        for cls in get_image_specs(spec_module):
            yield (cls.name(), cls.name())

    def _get_choices(self):
        return self.preset_choices()
    choices = property(_get_choices)

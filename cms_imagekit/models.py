from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin, PluginModelBase
from imagekit.models import ImageModel, ImageModelBase
from cms_imagekit.fields import IKPresetField


class IKPluginModelBase(PluginModelBase, ImageModelBase):
    pass    

class IKPluginModel(CMSPlugin, ImageModel):
    """
      Extends CMSPlugin plugin to add an optional imagekit preset
      
      Use this as a base class for CMS plugins need ImageModel functionality
    """
    # @todo - add "link to full-size image" option?
    preset = IKPresetField(verbose_name=_("image preset"), max_length=80, null=True, blank=True, help_text=_("defines format for displaying image"))

    __metaclass__ = IKPluginModelBase

    class Meta:
        abstract = True
    
    def save(self, no_signals=False, clear_cache=True, *args, **kwargs):
        """
        Both base classes override save(), and can't be called sequentially.
        Need to coordinate save so both base class save methods work out.
        """
        is_new_object = self._get_pk_val() is None
        CMSPlugin.save(self, no_signals, *args, **kwargs)
        if is_new_object:
            self._post_save(clear_cache)


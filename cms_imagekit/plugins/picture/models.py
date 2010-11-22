from cms.plugins.picture.models import Picture as CMSPicture
from cms_imagekit.conf import settings
from cms_imagekit.models import IKPluginModel

def get_cache_dir(ikpicture_obj, filepath, cache_filename):
    print filepath
    return ikpicture_obj.get_media_path(cache_filename)


class IKPicture(IKPluginModel, CMSPicture):
    """
      Extends basic Picture plugin to add an optional imagekit preset
    """

    class IKOptions:
        # This inner class is where we define the ImageKit options for the model
        spec_module = settings.CMS_IKPICTURE_SPECS
        cache_dir = get_cache_dir
        image_field = 'image'   # from CMSPicture base class
        admin_thumbnail_spec = 'thumbnail'
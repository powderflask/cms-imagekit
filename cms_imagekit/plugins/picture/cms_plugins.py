from cms.plugin_pool import plugin_pool
#from cms.plugin_base import CMSPluginBase
from cms.plugins.picture.cms_plugins import PicturePlugin as CMSPicturePlugin
from cms_imagekit.plugins.picture.models import IKPicture
from django.conf import settings

class IKPicturePlugin(CMSPicturePlugin):
    model = IKPicture
    render_template = "cms_imagekit/picture.html"

    def render(self, context, instance, placeholder):
        if instance.preset and not instance.url and not instance.page_link:
            instance.url = instance.image.url
        if instance.preset:
            image_spec = getattr(instance, instance.preset, instance.image)
            instance.preset_url = image_spec.url
        else:
            instance.preset_url = instance.image.url
        return super(IKPicturePlugin, self).render(context, instance, placeholder)
    
    def icon_src(self, instance):
        # TODO - possibly use 'instance' and provide a thumbnail image
        return settings.CMS_MEDIA_URL + u"images/plugins/image.png"
 
plugin_pool.register_plugin(IKPicturePlugin)

"""
Default menu settings, are applied only if there isn't value defined in project settings. 
All available settings are listed here - override them in your project settings.
"""
from django.conf import settings  # load project settings (overrides)

class DefaultSettings():
    CMS_IKPICTURE_SPECS = 'cms_imagekit.plugins.picture.defaults'
    
# merge in default settings
for attr in dir(DefaultSettings):
    if attr == attr.upper() and not hasattr(settings, attr):
        setattr(settings._wrapped, attr, getattr(DefaultSettings, attr))

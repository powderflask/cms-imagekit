import inspect
from imagekit.specs import ImageSpec

def get_image_specs(module):
    specs = []
    for name in dir(module):
        obj = getattr(module, name)
        if inspect.isclass(obj):
            if issubclass(obj, ImageSpec) and obj is not ImageSpec:
                specs.append(obj)
    return specs

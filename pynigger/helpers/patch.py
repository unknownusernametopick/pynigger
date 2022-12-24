from pynigger.logger import logger


def patch(obj):
    """Decorator to add new or override existing methods and attributes of an object.
    By default, it'll patch all attributes and functions to the object (generally class) except magic attributes and functions (attributes starting and ending with double-underscores like `__patch__`).

    - Use attribute `__no_patch__` to list all attributes and function names you don't want to patch.
    - Use attribute `__patch__` to list the only attributes and function names you want to patch.
    - Don't specify anything to patch all
    """
    try:
        patch_list = getattr(obj, "__patch__")
        if not isinstance(patch_list, list):
            logger.warn("__patch__ attribute must be a list. Skipping patch..")
            return
    except AttributeError:
        patch_list = []
    try:
        no_patch_list = getattr(obj, "__no_patch__")
        if not isinstance(no_patch_list, list):
            logger.warn(
                "__no_patch__ attribute must be a list. Skipping patch..")
            return
    except AttributeError:
        no_patch_list = []

    def is_patchable(name):
        if name in no_patch_list:
            return False
        elif patch_list and name not in patch_list:
            return False
        return True

    def wrapper(container):
        attrs = vars(container)
        for name in attrs:
            attr = attrs[name]
            if name.startswith("__") and name.endswith("__"):
                continue
            if is_patchable(name):
                old = getattr(obj, name, None)
                setattr(obj, "old_" + name, old)
                setattr(obj, name, attr)
        return container

    return wrapper

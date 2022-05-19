from django.conf import settings


def get_full_url():
    return f'{settings.PROTOCOL}://{settings.BASE_DOMAIN}'


def method_permission_classes(classes):
    """
    Декоратор позволяет задать для метода сета отдельную проверку доступа.
    Должен быть самым нижним декоратором.
    В сете не должно быть других классов доступа.
    """
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            self.permission_classes = classes
            self.check_permissions(self.request)
            return func(self, *args, **kwargs)
        wrapper.__name__ = func.__name__
        return wrapper
    return decorator

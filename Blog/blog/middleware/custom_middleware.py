from django.conf import settings
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s %(message)s]')
logger = logging.getLogger(__name__)

class LogUserMiddleware:
    """Класс для логирования пользователей"""
    def __init__(self, response):
        self.response = response

    def __call__(self, request):
        """Вызывается для каждого запроса"""
        
        if not request.user.is_authenticated and settings.LOG_USER:
            meta = request.META
            method_request = meta.get('REQUEST_METHOD')
            url = f"{meta.get('PATH_INFO')}"
            ip = meta.get('REMOTE_ADDR')
            logger.info(f'IP: {ip} URL: {url} TYPE: {method_request}')
        
        # для передачи запроса следоющему middleware
        response = self.response(request)

        return response

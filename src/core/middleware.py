from request_logging.middleware import LoggingMiddleware, IS_DJANGO_VERSION_GTE_3_2_0


class UltimateLoggingMiddleware(LoggingMiddleware):

    def _log_request_headers(self, request, logging_context, log_level):
        if IS_DJANGO_VERSION_GTE_3_2_0:
            headers = {k: v if k not in self.sensitive_headers else "*****" for k, v in request.headers.items()}
        else:
            headers = {
                k: v if k not in self.sensitive_headers else "*****"
                for k, v in request.META.items()
            }

        if headers:
            self.logger.log(log_level, headers, logging_context)

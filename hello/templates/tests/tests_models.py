from django.test import TestCase
from django.utils import timezone
from hello.models import LogMessage

class LoggMessageTest(TestCase):

    def create_logmessage(self, message="This is a test message."):
        return LogMessage.objects.create(
            message=message,
            log_date=timezone.now()
        )

    def test_log_message_init(self):
        log_message=self.create_logmessage()
        self.assertTrue(isinstance(log_message, LogMessage))


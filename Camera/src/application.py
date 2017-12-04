from interfaces import ICamera
from interfaces import IConfiguration
from interfaces import ILogger
from interfaces import IAlert
from interfaces import IDetection


class Application:
    def __init__(self, logger, configuration, camera, detection, alert):
        """

        :param logger:
        :param configuration:
        :param camera:
        :param detection:
        :param alert:
        """
        assert isinstance(logger, ILogger.LoggerStub)
        assert isinstance(configuration, IConfiguration.IConfiguration)
        assert isinstance(camera, ICamera.ICamera)
        assert isinstance(detection, IDetection.IDetection)
        assert isinstance(alert, IAlert.IAlert)
        assert isinstance(camera, ICamera.ICamera)

        self._camera = camera
        self._configuration = configuration
        self._logger = logger
        self._alert = alert
        self._detection = detection
        self._stop = False
        self._last_image = None

    def start(self):
        while not self._stop_requested():
            current_image = self._camera.get_last_image()
            if self._detection.detect(self._last_image, current_image):
                self._alert.alert()
            else:
                self._logger.info("All good, Nothing detected")
        self._logger.info("Stopped loop..")

    def _stop_requested(self):
        return self._stop

    def stop(self):
        pass

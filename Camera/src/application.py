from tempfile import NamedTemporaryFile
from time import sleep
import requests

#import cv2

from interfaces import ICamera
from interfaces import IConfiguration
from interfaces import ILogger
from interfaces import IAlert



class Application:
    def __init__(self, logger, configuration, camera, detection, alert):
        """

        :param logger:
        :param configuration:
        :param camera:
        :param detection:
        :param alert:
        """
        #assert isinstance(logger, ILogger.LoggerStub)
        #assert isinstance(configuration, IConfiguration.IConfiguration)
        #assert isinstance(camera, ICamera.ICamera)
        #assert isinstance(detection, IDetection.IDetection)
        #assert isinstance(alert, IAlert.IAlert)
        #assert isinstance(camera, ICamera.ICamera)

        self._camera = camera
        self._configuration = configuration
        self._logger = logger
        self._alert = alert
        self._detection = detection
        self._stop = False
        self._last_image = None

    def start(self):
        while not self._stop_requested():
            #sleep(1)
            current_image = self._camera.get_last_image()
            self.post_image(current_image)
            
        self._logger.info("Stopped loop..")

    def _stop_requested(self):
        return self._stop

    def post_image(self,image):

        try:
            print ("shape is: ", image.shape)
            import numpy
            numpy.save("image",image)

            with open("image.npy", 'rb') as f:
                r = requests.post('http://DESKTOP-TM55GUG:8000', files={'image': f})
                print(r.status_code, r.reason)
        except Exception as  ex:
            print (ex)
            pass


    def stop(self):
        pass

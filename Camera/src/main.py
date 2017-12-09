from application import Application
from capture.pcwebcam import PCWebCam
from interfaces import ILogger, IConfiguration, IAlert, ICamera, IDetection
from interfaces.IAlert import AlertStub
from interfaces.ICamera import CameraStub
from interfaces.IConfiguration import ConfigurationStub
from interfaces.IDetection import DetectionStub
from interfaces.ILogger import LoggerStub

if __name__ == '__main__':
    print("Welcome to PyEye Camera, Staring for you...")

    logger = LoggerStub()
    configuration = ConfigurationStub()
    camera = PCWebCam()
    detection = DetectionStub()
    alert = AlertStub()

    application = Application(logger=logger,
                              camera=camera,
                              configuration=configuration,
                              detection=detection, alert=alert
                              )

    application.start()

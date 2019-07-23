stubbed_camera = 1
stubbed_raspberrypi = 2
stubbed_pcwebcam = 3


def get_camera(camera_type=1):

    if camera_type == 1:
        from capture import CameraStub
        return CameraStub.CameraStub()

    if camera_type == 2:
        from capture.CameraStub import RaspberryPiCam
        return RaspberryPiCam()

    if camera_type == 2:
        from capture.pcwebcam import PCWebCam
        return PCWebCam()

from http.server import BaseHTTPRequestHandler
import numpy as np
import cv2

class HttpHandler(BaseHTTPRequestHandler):
    """
    This class is used to handle the HTTP requests that arrive at the server. By itself, it cannot respond to any actual
    HTTP requests; it must be subclassed to handle each request method (e.g. GET or POST).
    """
    get_path = {}
    post_path = {}

    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)

    def save_post_response(self):

        # Parse the form data posted
        import cgi
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })

        if 'image' in form and form['image'].filename != '':
            file_data = form['image'].file.read()
            filename = form['image'].filename
            with open("d:\\f.npy", 'wb') as f:
                f.write(file_data)
            img = np.load("d:\\f.npy")
            img.shape = (512, 512, 3)

            face_cascade = cv2.CascadeClassifier('D:\\Projects\\PyEye\Server\\src\\haarcascade_upperbody.xml')
            gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)


            cv2.imwrite("d:\\img.jpg",img)
            cv2.imshow("t1", img)
            cv2.waitKey(1)




        if False:

            try:
                # Parse the form data posted
                import cgi
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST',
                             'CONTENT_TYPE': self.headers['Content-Type'],
                             })

                if 'image' in form and form['image'].filename != '':
                    file_data = form['newfile'].file.read()
                    image = np.frombuffer(bytes, dtype=np.uint8)
                    print(image.shape)
                    print(image)

                    print (file_data)
                #imag#e = np.frombuffer(bytes, dtype=np.uint8)
                #image.shape = (int(form[b'width'][0]),int(form[b'height'][0]))
                #cv2.imshow("output", image)
                #cv2.waitKey(1)
            except Exception as ex:
                print ("Error Occurred",ex)
                pass



    def save_get_response(self):
        pass

    def do_GET(self):
        if self.path in self.get_path:
            self.get_path[self.path] += 1
        else:
            self.get_path[self.path] = 1
        print("Received Get ", self.path, self.get_path[self.path])

        self.send_response(400)
        self.end_headers()
        return

    def do_POST(self):
        if self.path in self.post_path:
            self.post_path[self.path] += 1
        else:
            self.post_path[self.path] = 1

        print("Received Post ", self.path, self.post_path[self.path])

        self.save_post_response()
        # Sends a response header and logs the accepted request. The HTTP response line is sent, followed by Server and
        # Date headers. The values for these two headers are picked up from the version_string() and date_time_string()
        # methods, respectively.
        self.send_response(200)

        # Sends a blank line, indicating the end of the HTTP headers in the response
        self.end_headers()

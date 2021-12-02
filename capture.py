#------------------------------------------------------------------------------------------------
#
#  Copyright 2021 by Bordyn Cheevatanakonkul.
#
#  Author: Bordyn Cheevatanakonkul.
#  License: MIT
#  Maintainer: Bordyn Cheevatanakonkul.
#  Email: bordyn.ch@gmail.com
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
#
#------------------------------------------------------------------------------------------------

import argparse
import logging
import cv2

import time
import threading
from queue import Queue

#------------------------------------------------------------------------------------------------

class capture_thread (threading.Thread):

    def __init__(self,
                 device,
                 frame_size=(640,480),
                 queue_size=128,
                 frame_count=50):
        """
        CONSTRUCTOR
        :param device:
        :param frame_delay:
        :param queue_size:
        """
        super(capture_thread,self).__init__()

        # start video capture
        self.cap = cv2.VideoCapture(device)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,frame_size[0])
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT,frame_size[1])

        self.running = True

        self.q = Queue(maxsize=queue_size)
        self.lock = threading.Lock()
        self.frame_count = frame_count

    def stop(self):
        """
        Simply stop the process
        :return:
        """
        self.running = False
        while self.is_alive():
            time.sleep(0.1)

    def fill(self,frame):
        """
        fill q frame
        :param frame:
        :return:
        """
        if not self.q.full():
            self.q.put(frame)

    def get(self):
        """
        get a frame from queue
        :return:
        """
        if self.q.qsize() > 0:
            return self.q.get()
        else:
            return None

    def run(self):
        """
        thread
        :return:
        """
        if (self.cap.isOpened() == False):
            raise ValueError("Error opening video stream or file")

        image_count = 0
        start = time.time()

        while self.running:

            # capture the frame from opencv here
            ret, frame = self.cap.read()
            if not ret:
                continue

            self.fill(frame)

            image_count += 1
            if image_count >= self.frame_count:
                now = time.time()
                lapse = now - start
                logging.info("running frame per sec {}".format(self.frame_count/lapse))

                image_count = 0
                start = now

            # minimum delay just to keep thread a break
            time.sleep(0.001)

        # close the capture
        self.cap.release()

#------------------------------------------------------------------------------------------------

def test_capture(device,frame_size,frame_delay=1):
    """

    :param device:
    :return:
    """
    cap = capture_thread(device,frame_size=frame_size)
    cap.start()

    while cap.is_alive():

        # do some thing while running
        frame = cap.get()
        if frame is None:
            continue

        # visualize the frame
        cv2.imshow('Frame', frame)

        # Press Q on keyboard to  exit
        key = cv2.waitKey(frame_delay)
        if (key & 0xFF) == ord('q') or key == 27:
            break

    cap.stop()

#------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='video capture fps test')
    parser.add_argument("--video" ,type=int,required=True  , help="video index")
    parser.add_argument("--frame_width" ,type=int,required=False,default=640)
    parser.add_argument("--frame_height" ,type=int,required=False,default=480)
    args = vars(parser.parse_args())

    args_dict = {
        'level' : logging.INFO,
        'format' : "%(asctime)s [%(levelname)s] %(message)s",
        'handlers' : [logging.StreamHandler(),
                      logging.FileHandler('logfile.txt')]
    }
    logging.basicConfig(**args_dict)
    logging.info("Press q or esc to exit program.")
    logging.info("Frame size , width {} ,height {}.".format(args['frame_width'],args['frame_height']))
    test_capture(args['video'],frame_size=(args['frame_width'],args['frame_height']))

#------------------------------------------------------------------------------------------------


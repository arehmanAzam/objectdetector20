import cv2
import os


class FrameGen:
    '''
    class containing functionalities of frame/image generations
    '''

    def __init__(self):
        pass

    def frames_saving(self,frame_name,frame):
        cv2.imwrite(frame_name, frame)
        pass
    def get_frames(self,video_path,frame_saving_path,frame_skipping=15):
        assert type(video_path)==str
        assert type(frame_saving_path)==str
        assert os.path.exists(video_path)
        assert os.path.exists(frame_saving_path)

        head, tail = os.path.split(video_path)

        cap = cv2.VideoCapture(video_path)
        success,frame=cap.read()
        i = 0
        while (success):
            if i%frame_skipping==0:
                self.frames_saving(frame_name=frame_saving_path +"/"+ tail + "_" + str(i) + ".jpg", frame=frame)
            success, frame = cap.read()
            i += 1
        cap.release()
        cv2.destroyAllWindows()


        pass
# if __name__ == '__main__':
    # obj_gen=FrameGen()
    # video="/home/abdulrehman/PycharmProjects/objectdetector20/videoplayback"
    # frame_saving='/home/abdulrehman/PycharmProjects/objectdetector20/frame_data/'
    # obj_gen.get_frames(video,frame_saving)
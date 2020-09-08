import os
from FrameGen import FrameGen as extractor
from Augmentations import Augmentations as transformer



class ETL:
    '''
    Extract, Transform and Load
    '''

    def __init__(self,video_link,extract_im_directory,tranform_im_directory):
        assert type(video_link)==str
        assert type(extract_im_directory) == str
        assert type(tranform_im_directory) == str

        assert os.path.exists(video_link)
        assert os.path.exists(extract_im_directory)
        assert os.path.exists(tranform_im_directory)

        self.video_path=video_link
        self.extract_im=extract_im_directory
        self.transform_im=tranform_im_directory
        self.extractor=extractor()
        self.tranformer=transformer()

    def extract(self):
        print("\n Extracting frames :-)")
        self.extractor.get_frames(video_path=self.video_path,frame_saving_path=self.extract_im,frame_skipping=10)
        print("\n Frames extracted  :-D")

    def transform(self):
        print("\n Transforming data :-)")
        self.tranformer.transformations(source_path=self.extract_im,target_path=self.transform_im)
        print("\n Transformations done :-D")

if __name__ == '__main__':
    etl_object=ETL(
     video_link='/home/abdulrehman/PycharmProjects/objectdetector20/Data/videos/20200901_144022.mp4'
    ,extract_im_directory='/home/abdulrehman/PycharmProjects/objectdetector20/Data/frame_oakleySun2'
    ,tranform_im_directory='/home/abdulrehman/PycharmProjects/objectdetector20/Data/transformed_oakleySun2')

    etl_object.extract()
    etl_object.transform()
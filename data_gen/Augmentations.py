import imgaug.augmenters as iaa
import cv2
import os
import glob

class Augmentations:
    '''
    make augmentations on images
    '''
    def __init__(self):
        try:
            self.aug_affine = iaa.Affine(scale=(0.5, 1.5))
            self.aug_rotate90= iaa.Rot90((1, 3))
            self.aug_rotate45 = iaa.Rotate((-45, 45))
            self.seq = iaa.Sequential([
                iaa.ScaleX((0.5, 1.5)),
                iaa.ScaleY((0.5, 1.5))
            ])
        except Exception as e:
            pass
    def affine(self,image):
        '''
        affine tranformation of image
        :param image: input image
        :return: transformed image
        '''
        try:
            image=self.aug_affine.augment_image(image=image)
            return image
        except Exception as e:
            pass
    def rotate90(self,image):
        '''
        90 degree rotations of image
        :param image: input image
        :return: transformed image
        '''
        try:
            image = self.aug_rotate90.augment_image(image=image)
            return image
        except Exception as e:
            pass
    def rotate45(self,image):
        '''
        45 degree rotations of image
        :param image: input image
        :return: transformed image
        '''
        try:
            image = self.aug_rotate45.augment_image(image=image)
            return image
        except Exception as e:
            pass
    def scaling(self,image):
        '''
        X and Y translations of image
        :param image: input image
        :return: transformed image
        '''
        try:
            image = self.seq.augment_image(image=image)
            return image
        except Exception as e:
            pass
    def transformations(self,source_path,target_path):
        try:
            success=False
            assert type(source_path)==str
            assert type(target_path)==str

            assert os.path.exists(source_path)
            assert os.path.exists(target_path)
            for filename in glob.glob(source_path+"/*.jpg"):
                head, tail = os.path.split(filename)
                filename_base=os.path.splitext(tail)
                img = cv2.imread(os.path.join(source_path, filename))
                cv2.imwrite(target_path+'/'+filename_base[0]+"affine.jpg",img=self.affine(img))
                cv2.imwrite(target_path+'/'+filename_base[0]+"scale.jpg",img=self.scaling(img))
                # cv2.imwrite(target_path+'/'+filename_base[0]+"rot45.jpg",img=self.rotate45(img))
                cv2.imwrite(target_path+'/'+filename_base[0]+"rot.jpg",img=self.rotate90(img))
            success = True
            return success
        except Exception as e:
            print("Exception occured in Augmentations.transformations. Exception : %s" %e)

if __name__ == '__main__':
    aug_images=Augmentations()
    image_path='/home/abdulrehman/PycharmProjects/objectdetector20/frame_data/'
    # im = cv2.imread(image_path)
    # img = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    # aug_images.affine(img)
    aug_images.transformations(image_path,image_path)
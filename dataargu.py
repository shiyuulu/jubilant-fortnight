import numpy as np
import imgaug as ia
import imgaug.augmenters as iaa
import os
import imageio
import imgaug as ia

#This script is for data augmentation


#'marten','mouse','hedgehog',
na=['cat','fox']


# Paths to labeled images saved in different animal classes
path1="D://Downloads//VPF//VPF//train//"
for n in na:
    total_im = os.listdir(path1+n)
    num_im = len(total_im)
    #list_all_im = range(num_im)
    i=1
    for img in total_im[:2]:

        image = imageio.imread(path1+n+'//'+img)

        ia.seed(1)

        images = np.array(
            [image for _ in range(24)],
            dtype=np.uint8
        )

        #define augmentation method
        seq = iaa.Sequential([
            iaa.Fliplr(0.5),  # horizontal flips

            iaa.Crop(percent=(0, 0.3)),  # random crops
            # Small gaussian blur with random sigma between 0 and 0.5.
            # But we only blur about 50% of all images.
            iaa.Sometimes(
                0.5,
                iaa.GaussianBlur(sigma=(0, 0.5))
            ),
            # Strengthen or weaken the contrast in each image.
            iaa.LinearContrast((0.75, 1.5)),
            # Add gaussian noise.
            # For 50% of all images, we sample the noise once per pixel.
            # For the other 50% of all images, we sample the noise per pixel AND
            # channel. This can change the color (not only brightness) of the
            # pixels.
            iaa.AdditiveGaussianNoise(loc=0, scale=(0.0, 0.05 * 255), per_channel=0.5),
            # Make some images brighter and some darker.
            # In 20% of all cases, we sample the multiplier once per channel,
            # which can end up changing the color of the images.
            iaa.Multiply((0.8, 1.2), per_channel=0.2),
            # Apply affine transformations to each image.
            # Scale/zoom them, translate/move them, rotate them and shear them.
            iaa.Affine(
                scale={"x": (0.8, 1.2), "y": (0.8, 1.2)},
                translate_percent={"x": (-0.1, 0.1), "y": (-0.1, 0.1)},
                rotate=(-25, 25),
                shear=(-9, 9)
            )
        ],random_order=True)  # apply augmenters in random order
        i = i + 1
        #for _ in range(9):
        images_aug = seq(images=images)
        print("Augmented batch:")
        ia.imshow(np.hstack(images_aug))

        #path to save the result
        path = ('D://Downloads//VPF//'+n+'//')

        imageio.imwrite(path + str(i)+"_" + ".png", images_aug)




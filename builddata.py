# 将图片和标注数据按比例切分为 训练集和测试集
import shutil
import random
import os

# original set
image_original_path = "./mydata/images/"
label_original_path = "./mydata/labels/"

cur_path = os.getcwd()

# train set
train_image_path = os.path.join(cur_path, "data/passing_aug/images/train/")
train_label_path = os.path.join(cur_path, "data/passing_aug/labels/train/")

# val set
val_image_path = os.path.join(cur_path, "data/passing_aug/images/val/")
val_label_path = os.path.join(cur_path, "data/passing_aug/labels/val/")
#
# test set
test_image_path = os.path.join(cur_path, "data/passing_aug/images/test/")
test_label_path = os.path.join(cur_path, "data/passing_aug/images/test/")

# index
list_train = os.path.join(cur_path, "data/passing_aug/train.txt")
list_val = os.path.join(cur_path, "data/passing_aug/val.txt")
list_test = os.path.join(cur_path, "data/passing_aug/test.txt")

train_percent = 0.7
val_percent = 0.2
test_percent = 0.1


def del_file(path):
    for i in os.listdir(path):
        file_data = path + "\\" + i
        os.remove(file_data)


def mkdir():
    if not os.path.exists(train_image_path):
        os.makedirs(train_image_path)
    else:
        del_file(train_image_path)
    if not os.path.exists(train_label_path):
        os.makedirs(train_label_path)
    else:
        del_file(train_label_path)

    if not os.path.exists(val_image_path):
        os.makedirs(val_image_path)
    else:
        del_file(val_image_path)
    if not os.path.exists(val_label_path):
        os.makedirs(val_label_path)
    else:
        del_file(val_label_path)

    if not os.path.exists(test_image_path):
        os.makedirs(test_image_path)
    else:
        del_file(test_image_path)
    if not os.path.exists(test_label_path):
        os.makedirs(test_label_path)
    else:
        del_file(test_label_path)


def clearfile():
    if os.path.exists(list_train):
        os.remove(list_train)
    if os.path.exists(list_val):
        os.remove(list_val)
    if os.path.exists(list_test):
        os.remove(list_test)

def main():
    mkdir()
    clearfile()

    file_train = open(list_train, 'w')
    file_val = open(list_val, 'w')
    file_test = open(list_test, 'w')

    total_txt = os.listdir(label_original_path)
    num_txt = len(total_txt)
    list_all_txt = range(num_txt)

    num_train = int(num_txt * train_percent)
    num_val = int(num_txt * val_percent)
    num_test = num_txt - num_train - num_val

    train = random.sample(list_all_txt, num_train)

    val_test = [i for i in list_all_txt if not i in train]

    val = random.sample(val_test, num_val)

    print("train：{}, val：{}, test：{}".format(len(train), len(val), len(val_test) - len(val)))
    for i in list_all_txt:
        name = total_txt[i][:-4]
        srcImage = image_original_path + name + '.png'
        srcLabel = label_original_path + name + ".txt"

        if i in train:
            dst_train_Image = train_image_path + name + '.png'
            dst_train_Label = train_label_path + name + '.txt'
            shutil.copyfile(srcImage, dst_train_Image)
            shutil.copyfile(srcLabel, dst_train_Label)
            file_train.write(dst_train_Image + '\n')
        elif i in val:
            dst_val_Image = val_image_path + name + '.png'
            dst_val_Label = val_label_path + name + '.txt'
            shutil.copyfile(srcImage, dst_val_Image)
            shutil.copyfile(srcLabel, dst_val_Label)
            file_val.write(dst_val_Image + '\n')
        else:
            dst_test_Image = test_image_path + name + '.png'
            dst_test_Label = test_label_path + name + '.txt'
            shutil.copyfile(srcImage, dst_test_Image)
            shutil.copyfile(srcLabel, dst_test_Label)
            file_test.write(dst_test_Image + '\n')

    file_train.close()
    file_val.close()
    file_test.close()


if __name__ == "__main__":
    main()

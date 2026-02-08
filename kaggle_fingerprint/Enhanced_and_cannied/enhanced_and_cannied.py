#!/usr/bin/env python
# coding: utf-8
# %% [markdown]
# ## Fingerprint Enhancement (would take a long time)
# * Created on Mon Apr 18 11:42:58 2016
# * @author: utkarsh

# %%
import sys
sys.path.append("./Fingerprint-Enhancement-Python/src")
from FingerprintImageEnhancer import FingerprintImageEnhancer
import cv2, os

if __name__ == '__main__':

    image_enhancer = FingerprintImageEnhancer()                    # Create object called image_enhancer
    img_dir = "./Real"
    img_files = os.listdir("./Real")                    # list all files within Real/ folder
    for img_name in img_files:
        img = cv2.imread(os.path.join(img_dir, img_name), 0)           # load input image

        #if(len(img.shape)>2):                               # convert image into gray if necessary
            #img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        out = image_enhancer.enhance(img)     # run image enhancer
        image_enhancer.save_enhanced_image('./Enhanced/' + img_name.split(".")[0] + ".jpg")   # save output

# %% [markdown]
# # Fingerprint Canny Edge Detection
# * 在作邊緣偵測時，通常會先做平滑化(cv2.GaussianBlur)來降低雜訊，，再做 cv2.Canny 跟 cv2.GaussianBlur 前需要先將影像轉為灰階，最後依據結果調整平滑/模糊參數(cv2.GaussianBlur)或邊緣檢測參數(cv2.Canny)來達到想要的結果，整體步驟大約分成這幾步：
#  
# * 影像轉灰階： cv2.cvtColor
# * 將影像轉成灰階，也可以在 imread 時就指定讀取為灰階影像
# * 影像去雜訊/平滑影像： cv2.GaussianBlur
# * cv2.GaussianBlur 第二個參數是指定 Gaussian kernel size，本範例使用 5×5 大小
# * 邊緣偵測： cv2.Canny
# * 採用雙門檻值
# * 第二個參數是指定最小門檻值 threshold1 – first threshold for the hysteresis procedure.
# * 第三個參數是指定最大門檻值 threshold2 – second threshold for the hysteresis procedure.

# %%
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os, cv2

img_dir = "./Enhanced"
img_files = os.listdir("./Enhanced")
for img_name in img_files:
    
    image = cv2.imread(os.path.join(img_dir, img_name), 0)
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(image, (3, 3), 0)
    canny = cv2.Canny(blurred, 30, 150)
    
    #plt.title("Original Image")
    #plt.imshow(image)
    plt.imsave(os.path.join("./Cannied", img_name), canny, cmap='gray')


# %% [markdown]
# ## Combine with csv

# %%
import os, csv, re

img_dir = "./Cannied" # imgs directory with above pre-processing
img_files = os.listdir("./Cannied")
data_list = [["img_path", "label"]]

print(f'Initial file size: {len(img_files)}')
# 定義排序函式
def sort_by_number(filename):
    # 使用正則表達式提取檔案名中的數字部分
    match = re.search(r"(\d+)", filename)
    if match:
        return int(match.group(0))  # 返回數字部分作為排序依據
    else:
        return 0  # 如果檔案名中沒有數字，將其視為0

# 按照數字大小進行排序
sorted_files = sorted(img_files, key=sort_by_number)  

for img_name in sorted_files:
    if img_name.split("__")[0] == "0":
        print("Label 已經從 0 開始了")
        break            # 表示已經把 label 變成從 0 開始到 599 (不用再調)
    groundtruth = int(img_name.split("__")[0]) - 1
    new_img_name = str(groundtruth) + "__" + img_name.split("__")[1]
    os.rename("./Cannied/" + img_name, "./Cannied/" + new_img_name)
    data_list.append([new_img_name, groundtruth])  

print(f'After sorting files size: {len(os.listdir("./Cannied"))}')
# creat a csv file and store the image path and label
with open("./cannied_fingerprint_annotations.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(data_list)
print(f'總共前處理完的指紋照片: {len(data_list) - 1}')

# %% [markdown]
# ## seperate training and validation and testing sets (80:10:10)

# %%
# seperate training and validation sets (80:20)
# SOCOFing fingerprint All/
import os, re, csv

folder_path = os.path.join("Cannied")
testing_split = 1
validation_split = 1
training_split = 8
training_list = [["img_path", "label"]]
validation_list = [["img_path", "label"]]
testing_list = [["img_path", "label"]]

# 定義排序函式
def sort_by_number(filename):
    # 使用正則表達式提取檔案名中的數字部分
    match = re.search(r"(\d+)", filename)
    if match:
        return int(match.group(0))  # 返回數字部分作為排序依據
    else:
        return 0  # 如果檔案名中沒有數字，將其視為0

def combine_imgPath_and_label(img_list):
    for i, img in enumerate(img_list):
        train_data = []
        valid_data = []
        test_data = []
        person = re.match(r"(\d+)", img)
        if "CR" in img:
            continue
        if i % (training_split+validation_split+testing_split) < training_split:
            train_data.append(img)
            train_data.append(int(person.group(0)))
            training_list.append(train_data)
        elif i % (validation_split + testing_split) < validation_split:
            valid_data.append(img)
            valid_data.append(int(person.group(0)))
            validation_list.append(valid_data)
        else:
            test_data.append(img)
            test_data.append(int(person.group(0)))
            testing_list.append(test_data)
            
    print(f'Total training data size: {len(training_list)-1}') # minus the header name 
    print(f'Total validation data size: {len(validation_list)-1}')
    print(f'Total testing data size: {len(testing_list)-1}')

files = os.listdir(folder_path)
sorted_files = sorted(files, key=sort_by_number) # 按照數字大小進行排序   
combine_imgPath_and_label(sorted_files)
# for i in range(100):
#     print(training_list[i])
#     print(validation_list[i])

# %%
# creat a csv file and store the image path and label
def store_path_label_csv(annotations_file, data_list):
    with open(annotations_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(data_list)
    print(f'{annotations_file} saved')

training_annotations_file = "training_cannied_fingerprint_annotations.csv"
validation_annotations_file = "validation_cannied_fingerprint_annotations.csv"
testing_annotations_file = "testing_cannied_fingerprint_annotations.csv"
store_path_label_csv(training_annotations_file, training_list)
store_path_label_csv(validation_annotations_file, validation_list)
store_path_label_csv(testing_annotations_file, testing_list)

# %%

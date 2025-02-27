from txt_generate import textwrite
from xml_generate import xml_writer

import pandas as pd, os
import sys

from utils.sm_img_proc import get_classes


def __init__(self):
    self.label_data = None
    self.dsVOC = 'VOC'
    self.year = '2007'
    self.csv = None



def main():
    print(len(sys.argv))
    if len(sys.argv) != 4:
        print('[Error]')
        exit()

    csv_name = sys.argv[1]
    dir = sys.argv[2]
    target_dir = sys.argv[3]
    
    # parameters for file creation
    dsVOC = 'VOC'
    year = '2023'

    # 데이터셋의 class name
    class_name = 'test_classes'
    
    # 이미지의 size에 따라 가변적으로 수정
    box_parm = 32

    landmark_name, _      = get_classes(class_name) # celes


    # csv load
    if csv_name == None:
        csv_name = input('Type your csv name (ex: label_data.csv) : ')

    # image dir
    if dir == None:
        dir = input('Type your image directory name : ')
    if target_dir == None:
        target_dir = input('Type your target dir name : ')


    label_path = f'{csv_name}'

    if os.path.exists(label_path)==True:
        label_data = pd.read_csv(f'{csv_name}')

    elif os.path.exists(label_path)==False:
        label_data = pd.read_csv(f'{csv_name}')


    print('\n >>> csv file has been loaded.\n\n================================')



    main_dir = f'{target_dir}/VOCdevkit/{dsVOC}{year}'

    os.makedirs(main_dir + '/JPEGImages/', exist_ok=True)
    os.makedirs(main_dir + '/Annotations/', exist_ok=True)
    os.makedirs(main_dir + '/ImageSets/Main/', exist_ok=True)

    print('[Log] Directory has been created.')

    textwrite(target_dir, label_data, dsVOC, year)
    xml_writer(target_dir, label_data, dsVOC, year, dir, main_dir + '/JPEGImages/',
                landmark_name, box_parm=box_parm)


    print('================================ \n\n >>> Done')

if __name__ == "__main__":
    main()
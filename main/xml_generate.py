import numpy as np
from xml.etree.ElementTree import Element, SubElement, ElementTree
import cv2, os
from tqdm import tqdm

# label_data : csv file

def xml_writer(target_dir, label_data, dsVOC, year, dir_src, save_dir, landmark_name, box_parm=8):
    
    len_file = len(label_data['ID'])

    # jpg format, png format
    img_dir = os.listdir(dir_src)
        
    for i in tqdm(range(len_file)):
        root = Element("annotation")

        element1 = Element("filename")
        root.append(element1)
        element1.text = label_data.iloc[i]['ID']

        image_name = label_data.iloc[i]['ID']
        img = cv2.imread(f'{dir_src}/{img_dir[i]}')
        
        target_path = f'{save_dir}/{image_name}.png'

        cv2.imwrite(target_path, img[:, :, ::-1])


        element2 = Element("size")
        root.append(element2)

        width = str(img.shape[1])
        height = str(img.shape[0])
        channel = str(img.shape[2])

        # bbox size 조절
        bbox_size = max(int(width)//box_parm, int(height)//box_parm)

        
        sub_element2 = SubElement(element2, "width")
        sub_element2.text = width
        sub_element2 = SubElement(element2, "height")
        sub_element2.text = height
        sub_element2 = SubElement(element2, "depth")
        sub_element2.text = channel

        

        for j in range( len(landmark_name) ):
            element3 = Element("object")
            root.append(element3)
            sub_element3 = SubElement(element3, "name")
            sub_element3.text = landmark_name[j]
            
            x_loc = label_data.iloc[i][landmark_name[j]+'_x']
            y_loc = label_data.iloc[i][landmark_name[j]+'_y']
        
            try:
                tmp = np.array([x_loc-bbox_size, x_loc+bbox_size, y_loc-bbox_size, y_loc+bbox_size]).astype(int)
            
            except:
                tmp = np.array([-1, -1, -1, -1]).astype(int)


            sub_element4 = SubElement(element3, "bndbox")

            sub_element5 = SubElement(sub_element4, "xmin")
            sub_element5.text = str(tmp[0])

            sub_element6 = SubElement(sub_element4, "ymin")
            sub_element6.text = str(tmp[2])

            sub_element7 = SubElement(sub_element4, "xmax")
            sub_element7.text = str(tmp[1])

            sub_element8 = SubElement(sub_element4, "ymax")
            sub_element8.text = str(tmp[3])
        
        
        tree = ElementTree(root)

        i_2 = label_data['ID'][i]
        fileName = f"{target_dir}/VOCdevkit/{dsVOC}{year}/Annotations/{i_2}.xml"
        
        with open(fileName, "wb") as file:
            tree.write(file, encoding='utf-8', xml_declaration=True)

    print('[Log] xml file has been created.')
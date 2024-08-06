import os

#---------------------------------------------------#
#   Get classes from txt file
#---------------------------------------------------#
def get_classes(rest_mode = False):
    classes_path = os.path.join(os.getcwd(), 'utils', 'SNU_ceph_voc_classes.txt')
    with open(classes_path, encoding='utf-8') as f:
        class_names = f.readlines()
    class_names = [c.strip() for c in class_names]
    return class_names, len(class_names)
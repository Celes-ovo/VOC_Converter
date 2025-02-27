import os

#---------------------------------------------------#
#   Get classes from txt file
#---------------------------------------------------#
def get_classes(class_name, rest_mode = False):
    classes_path = os.path.join(os.getcwd(), 'utils', f'{class_name}.txt')
    with open(classes_path, encoding='utf-8') as f:
        class_names = f.readlines()
    class_names = [c.strip() for c in class_names]
    return class_names, len(class_names)
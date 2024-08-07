# 이미지 경로에서 이미지들을 불러와 txt로 자동 저장하는 기능
# label_data : point 정보가 담긴 csv file
def textwrite(target_dir, label_data, dsVOC, year):

    fp_all = open(f'{target_dir}/VOCdevkit/{dsVOC}{year}/ImageSets/Main/all.txt','wt')
    fp_train = open(f'{target_dir}/VOCdevkit/{dsVOC}{year}/ImageSets/Main/train.txt','wt')
    fp_val = open(f'{target_dir}/VOCdevkit/{dsVOC}{year}/ImageSets/Main/val.txt','wt')
    fp_test = open(f'{target_dir}/VOCdevkit/{dsVOC}{year}/ImageSets/Main/test.txt','wt')


    for idx,c in enumerate(label_data['ID']):
        if idx > 50 and idx <= 150:
            fp_train.write(f'{c}\n')
            fp_all.write(f'{c}\n')
        elif idx > 150:
            fp_val.write(f'{c}\n')
            fp_all.write(f'{c}\n')
        elif idx <= 50:
            fp_test.write(f'{c}\n')
            fp_all.write(f'{c}\n')
    
        
    fp_all.close()
    fp_train.close()    
    fp_val.close()
    fp_test.close()


    print('[Log] Text file has been created.')
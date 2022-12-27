import os
import csv
'''
MÃ SINH VIÊN: 22174600025 || PHẠM THỊ TRÀ GIANG 
MÃ SINH VIÊN: 22174600021 || NGUYỄN TUẤN MINH
MÃ SINH VIÊN: 22174600019 || TRẦN THỊ THẢO VÂN
MÃ SINH VIÊN: 22174600024 || HỒ THỊ MINH HẰNG
MÃ SINH VIÊN: 22174600022 || ĐẶNG HỮU TÂM
'''
_path = 'files/ds_canbo.csv'
lstcanbo = []
#-----------mở File-------------#
def mo_file(_path,lstcanbo):
    try:
        f = open(_path,'a',encoding= 'utf-8')
        for dong in csv.reader(f):
            if dong[0] == "mã cán bộ":
                continue
            lstcanbo.append({'Mã cán bộ':dong[0],'Tên cán bộ':dong[2],'':dong[3],'Chức vụ':dong[4],'Lương':dong[5]})
        f.close()
    except Exception as ex1:
        print('Khong mở được file hop le ', ex1)
    return 1
#----------Nhập danh sách Cán bộ----------#
def qly(lstcanbo):
    while True:
        macb = input("mã cán bộ: ")
        tencb = input("Tên cán bộ: ")
        hsl = float(input('Hệ số lương: '))
        chucvu = input('Chức vụ: ')
        if chucvu == 'giam doc':
            phucap = float(10000000)
        elif chucvu == 'truong phong':
            phucap = float(5000000)
        else:
            phucap = float(2000000)
        luong = (hsl * 1500000)+ phucap 
        lstcanbo.append({'Mã cán bộ ':macb,'Tên cán bộ':tencb,'Hệ số lương':hsl,'Chức vụ':chucvu,'Lương':luong})
        tt = int(input("bạn có muốn nhập nữa không: 1:có || khác: không: "))
        if tt != 1:
            break
    return
#-------------In danh sách cán bộ-------------#
def in_ds_canbo(lstcanbo):
    for cb in lstcanbo:
        print('Danh sách cán bộ:',cb['Tên cán bộ'])
    return
#-------------Xắp xếp cán bộ----------------#
def xapxep(lstcanbo):
    for i in lstcanbo:
        a = i['Lương']
    sorted_cb = sorted(lstcanbo,key=lambda x: x['Lương'])
    in_ds_canbo(sorted_cb)
    return
print('CHƯƠNG TRÌNH QUẢN LÝ CÁN BỘ')
print('Được viết bởi nhóm 3')
while True:
    print('1: Thêm cán bộ')
    print('2: Danh sách cán bộ')
    print('3: Sắp xếp cán bộ')

    chon=int(input('Chọn chức năng cần thực hiện: '))
    if chon == 1:
        qly(lstcanbo)
    elif chon ==2:
        in_ds_canbo(_path,lstcanbo)
    elif chon == 3:
        xapxep(lstcanbo)
        break

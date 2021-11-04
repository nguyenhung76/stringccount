def ky_tu_khong_trung_lap(s):
   #Chuoi luu cac ky tu khong trung lap
   chuoiKetQua = ""
   #Su dung vong lap for duyet qua cac ky tu cua chuoi s
   for kyTu in s:
       #Neu ky tu chua xuat hien trong chuoiKetQua thi them vao
       if kyTu not in chuoiKetQua:
           chuoiKetQua += kyTu
   return chuoiKetQua

def dem_ky_tu(s):
   #Goi ham de tra ve chuoi gom cac ky tu xuat hien trong chuoi s
    chuoiKyTu = ky_tu_khong_trung_lap(s)

   #Su dung vong lap for de duyet cac ky tu
    n = 0
    for kyTu in chuoiKyTu:
        #Su dung phuong thuc count() de dem so lan xuat hien trong chuoi s
        dem = s.count(kyTu)
        if dem > n: n = dem
       #Hien thi ra man hinh
    print("'{}': {}; ".format(kyTu, n))
       

#Nhap gia tri tu ban phim1
def main():

    s = input()

#Goi ham va truyen cac tham so can thiet
    dem_ky_tu(s)
    
main()
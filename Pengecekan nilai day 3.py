# ini adalah program pengecekan nilai
while(True):
    import os
    user = int(input("Masukkan nilai anda :"))



    if(user < 70):
       print("Nilai anda D ")
       os.system("msg * Anda Goblok")
    if(user >= 70 and user <=79):
       print("Nilai anda C")
    if(user > 79 and user <= 89):
       print("Nilai Anda B")
    if(user > 89 and user <= 100):
       print("Nilai anda A")

    tanya = input('masih ingin lanjut :')

    if(tanya == 'no'):
        break

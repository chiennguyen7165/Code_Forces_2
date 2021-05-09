w = int(input())
soBuoc = 0
khoangCachConLai = 0

if(w == 1 or w == 2 or w == 3 or w == 4 or w == 5):
    soBuoc = 1
else:
    soBuoc = int(w / 5)
    khoangCachConLai = w - soBuoc * 5
    if(khoangCachConLai == 4 or khoangCachConLai == 3 or khoangCachConLai == 2 or khoangCachConLai == 1):
        soBuoc = soBuoc + 1
    else: 
        soBuoc = soBuoc + khoangCachConLai / 4
        khoangCachConlai = khoangCachConLai - soBuoc * 4
        if(khoangCachConLai == 3 or khoangCachConLai == 2 or khoangCachConLai == 1):
            soBuoc = soBuoc + 1
        else:
            soBuoc = soBuoc + khoangCachConLai / 3
            khoangCachConlai = khoangCachConLai - soBuoc * 3
            if(khoangCachConlai == 2 or khoangCachConlai == 1):
                soBuoc = soBuoc + 1
            else:
                soBuoc = soBuoc + khoangCachConLai / 2
                khoangCachConlai = khoangCachConLai - soBuoc * 2
                if(khoangCachConLai == 1):
                    soBuoc = soBuoc + 1
                else:
                    pass
print(int(soBuoc))
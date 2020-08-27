def rajut(kata): #func rajut
    counter = 0 #var counter utk menghitung jumlah huruf
    urutan = 0 #var urutan utk cari pola ((a)+(a+1)+(a+2...)
    seriUrut = [] #list utk menampung serial pola angka
    for i in kata: #loop, counter +1 tiap huruf
        counter += 1
    
    for j in range(0, counter): #loop, kalau urutan masih kurang dr total huruf, urutan +j (urutan+1, urutan+2, urutan+3...)
        if urutan < counter: #loop berlangsung selama memenuhi kondisi 
            urutan += j 
            seriUrut.append(urutan) #append ke list kosong utk menyimpan pola urutan
    
    indexKata = seriUrut[-2] #index kata = -2, index kata berakhir dari urutan pola terakhir, dimulai dari urutan pola yg kedua terakhir
    
    print(kata[indexKata:])
    
rajut('CCoCodCode')

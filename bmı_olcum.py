import tkinter

ekran = tkinter.Tk()
ekran.title("BMI Hesaplaması")
ekran.config(padx=30, pady=30)


def sonuc_yazisi(bmi):
    # result_string = f"your bmı is {round(bmi,2)}. you are "
    result_string = "BMI'nız {}. Siz ".format(round(bmi, 2))
    if bmi <= 16:
        result_string += "Çok zayıfsınız!"
    elif 16 < bmi <= 17:
        result_string += "Orta dereceli zayıfsınız!"
    elif 17 < bmi <= 18.5:
        result_string += "Zayıfsınız!"
    elif 18.5 < bmi <= 25:
        result_string += "Normal kilolusunuz."
    elif 25 < bmi <= 30:
        result_string += "Kilolusunuz!"
    elif 30 < bmi <= 35:
        result_string += "Obez sınıfı 1"
    elif 35 < bmi <= 40:
        result_string += "Obez sınıfı 2"
    else:
        result_string += "Obez sınıfı 3"
    return result_string


def bmi_hesaplama():
    height = boy_girdi.get()
    weight = kilo_girdi.get()
    if weight == "" or height == "":
        sonuc.config(text="Kilo ve boyu giriniz!")
    else:
        try:
            bmi = float(weight) / ((float(height) / 100) ** 2)
            result_string = sonuc_yazisi(bmi)
            sonuc.config(text=result_string)
        except:
            sonuc.config(text="Geçerli bir numara giriniz!")


kilo_girdi_yazisi = tkinter.Label(text="Kilonuzu lütfen giriniz. (kg) ")
kilo_girdi_yazisi.pack()
kilo_girdi = tkinter.Entry(width=10)
kilo_girdi.pack()
boy_girdi_yazisi = tkinter.Label(text="Boyunuzu lütfen giriniz. (cm)")
boy_girdi_yazisi.pack()
boy_girdi = tkinter.Entry(width=10)
boy_girdi.pack()
hesaplama_butonu = tkinter.Button(text="Hesapla", command=bmi_hesaplama)
hesaplama_butonu.pack()
sonuc = tkinter.Label()
sonuc.pack()

ekran.mainloop()

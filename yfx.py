import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
print("Merhaba , sizlere seçtiğiniz hisse senetleri hakkında bilgi veren bir projedesiniz.\n*Eğer 1 rakamına basarak hisse senedinin geçmiş (1 Aylık,1 günlük)bilgilerine ve güncel açlış kapanış vs\nbilgilerine ulaşabilirsiniz.\n*2 Rakamına basarak günlük taşıma bilgileri,grafiklerini ve devir Kapanış grafiğine ulaşabilirsiniz.")
x=input('Hisse Adı: ').upper()
cevap=input('İşlem:  ')

st = yf.Ticker(x)

if cevap == "1":
    data = st.history(period="1mo", interval="1d")
    print(data)
    
    # Tüm hisse senedi bilgilerini alma
    st_info = st.info
    
    # DataFrame'e dönüştürme
    dataframe = pd.DataFrame.from_dict(st_info, orient='index', columns=['Değer'])
    dataframe.index.name = 'Takip'
    
    print(dataframe)
    dataframe.to_excel("yfinance.xlsx",index=False)


elif cevap == "2":
    # Kullanıcıdan başlangıç ve bitiş tarihlerini alma
    b_tarihi = input("Başlangıç Tarihi (YYYY-MM-DD): ")
    son_tarih = input("Bitiş Tarihi (YYYY-MM-DD): ")
    data = yf.download(x, start=b_tarihi , end=son_tarih)['Close']
    # Günlük getiri hesabı
    g_getiri = data.pct_change()
    print(f"Günlük getirisi:{g_getiri}")
    #Grafik
    fig, axs = plt.subplots(2, 1, figsize=(5, 5))

    
    data.plot(ax=axs[0],color="red")
    axs[0].set_title('Kapanış Fiyatı')
    axs[0].set_ylabel('fiyat ($)')

    
    g_getiri.hist(bins=50, ax=axs[1],color="yellow")
    axs[1].set_title('Günlük Getirilerin Histogramı')

   
    plt.tight_layout()

    
    plt.show()
else:
    print("Geçersiz bir işlem seçtiniz. Lütfen '1' veya '2' girin.")
    






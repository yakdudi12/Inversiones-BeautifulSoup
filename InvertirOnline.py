import requests
from bs4 import BeautifulSoup

Microsofturl =   "https://companiesmarketcap.com/microsoft/marketcap/"
response = requests.get(Microsofturl)


if response.status_code == 200:
    html = response.content
    soup = BeautifulSoup(html, "html.parser")
    print("Se puede acceder a la pagina", Microsofturl)
else:
    print("Error al obtener la pagina:", response.status_code)
    exit()

#Caracterización de los datos
positivo_negativo = ["percentage-green", "percentage-red"]
Microsoft = []

def AlmacenamientoMicrosoft():
    global Microsoft
    for clase in positivo_negativo:
        Microsoftlist = soup.find_all("span", class_=clase)
        Microsoft.extend(Microsoftlist)
AlmacenamientoMicrosoft()

def InterpretacionMicrosoft():
    if Microsoft:
        for Microsoftlist in Microsoft[0]:
            AnualMicrosoft = Microsoftlist.text
            MicrosoftStock = AnualMicrosoft.replace("%", "")
            stockMicrosoft = float(MicrosoftStock)
        for Microsoftlist in Microsoft[1]:
            diarioMicrosoft = Microsoftlist.text
            MicrosoftStockDiario = diarioMicrosoft.replace("%", "")
            StockDiarioMicrosoft = float(MicrosoftStockDiario)
            print(f"El valor Diario y Anual de Microsoft es de {stockMicrosoft} y {StockDiarioMicrosoft}")


InterpretacionMicrosoft()

TMOurl = "https://companiesmarketcap.com/thermo-fisher-scientific/marketcap/"
responseTMO = requests.get(TMOurl)

if responseTMO.status_code == 200:
    html = responseTMO.content
    soup = BeautifulSoup(html, "html.parser")
    print("Se puede acceder a la pagina", TMOurl)
else:
    print("Error al obtener la pagina:", responseTMO.status_code)
    exit()

#Thermo Fishe Scientific
positivo_negativo2 = ["percentage-green", "percentage-red"]
TMO = []
def AlmacenamientoTMO():
    global TMO
    for clase2 in positivo_negativo2:
        TMOlist = soup.find_all("span", class_=clase2)
        TMO.extend(TMOlist)

AlmacenamientoTMO()

def Interpretacion_TMO():
    if TMO:
        for TMOlist in TMO[0]:
            Anualstock2 = TMOlist.text
            TMOStock = Anualstock2.replace("%", "")
            stockTMOAnual = float(TMOStock)
        for TMOlist in TMO[1]:
            DiaroStock2 = TMOlist.text
            TMOStockDiario = DiaroStock2.replace("%", "")
            stockTMODiario = float(TMOStockDiario)
            print(f"El valor de Stock diario y anual de Thermo Fisher Scientific (TMO) es de {stockTMOAnual} y {stockTMODiario} ")

Interpretacion_TMO()

#NuvectisPharma
NVCTurl = "https://companiesmarketcap.com/nuvectis-pharma/marketcap/"
responseTMO = requests.get(NVCTurl)

if responseTMO.status_code == 200:
    html = responseTMO.content
    soup = BeautifulSoup(html, "html.parser")
    print("Se puede acceder a la pagina", NVCTurl)
else:
    print("Error al obtener la pagina:", responseTMO.status_code)
    exit()
#Interpretacion NuvectisPharma
positivo_negativo3 = ["percentage-green", "percentage-red"]
NVCT = []

def AlmacenamientoNVCT():
    global NVCT
    for clase3 in positivo_negativo3:
        elementos = soup.find_all("span", class_=clase3)
        NVCT.extend(elementos)

AlmacenamientoNVCT()

def InterpretacionNVCT():
    if NVCT:
        for elementos in NVCT[0]:
            AnualNVCT = elementos.text
            NVCTStock = AnualNVCT.replace("%", "")
            StockanualNVCT = float(NVCTStock)
        for elementos in NVCT[1]:
            DiarioNVCT = elementos.text
            NVCTStockDiario = DiarioNVCT.replace("%", "")
            StockDiarioNVCT = float(NVCTStockDiario)
            print("El valor anual de Nuvectis Pharma es de:", StockanualNVCT , "Y el valor diario es de:", StockDiarioNVCT)


InterpretacionNVCT()


#Nvidea
NVIurl = "https://companiesmarketcap.com/nvidia/marketcap/"
responseNVI = requests.get(NVIurl)

if responseNVI.status_code == 200:
    html = responseNVI.content
    soup = BeautifulSoup(html, "html.parser")
    print("Se puede acceder a la pagina", NVIurl)
else:
    print("Error al obtener la pagina:", responseNVI.status_code)
    exit()
#Interpretacion NuvectisPharma
positivo_negativo4 = ["percentage-green", "percentage-red"]
NVI = []

def AlmacenamientoNVI():
    global NVI
    for clase4 in positivo_negativo4:
        NVIlist = soup.find_all("span", class_=clase4)
        NVI.extend(NVIlist)

AlmacenamientoNVI()

def InterpretacionNVI():
    if NVI:
        for NVIlist in NVI[0]:
            AnualNVI = NVIlist.text
            NVIStock = AnualNVI.replace("%", "")
            StockanualNVI = float(NVIStock)
        for NVIlist in NVI[1]:
            DiarioNVI = NVIlist.text
            NVIStockDiario = DiarioNVI.replace("%", "")
            StockDiarioNVI = float(NVIStockDiario)
            print(f"El valor de Stock diario y anual de NVIDEA es de {StockanualNVI} y {StockDiarioNVI} ")
InterpretacionNVI()



#Astrazeneca
AZNurl = "https://companiesmarketcap.com/astrazeneca/marketcap/"
responseAZN = requests.get(AZNurl)

if responseAZN.status_code == 200:
    html = responseAZN.content
    soup = BeautifulSoup(html, "html.parser")
    print("Se puede acceder a la pagina", AZNurl)
else:
    print("Error al obtener la pagina:", responseAZN.status_code)
    exit()
#Interpretacion AZN
positivo_negativo5 = ["percentage-green", "percentage-red"]
AZN = []

def AlmacenamientoAZN():
    global AZN
    for clase5 in positivo_negativo5:
        AZNlist = soup.find_all("span", class_=clase5)
        AZN.extend(AZNlist)

AlmacenamientoAZN()

def InterpretacionAZN():
    if AZN:
        for AZNlist in AZN[0]:
            AnualNVI = AZNlist.text
            NVIStock = AnualNVI.replace("%", "")
            StockanualAZN = float(NVIStock)
        for AZNlist in AZN[1]:
            DiarioNVI = AZNlist.text
            NVIStockDiario = DiarioNVI.replace("%", "")
            StockDiarioAZN = float(NVIStockDiario)
            print(f"El valor de Stock diario y anual de AstraZeneca es de {StockanualAZN} y {StockDiarioAZN} ")
InterpretacionAZN()




import numpy as np
import importNeighborhoods as ib
from scipy.stats import uniform
import json

def calculatePopStats(region):
    regionPop = 0
    regionDensIdade = 0
    for i in range(len(region)):
        regionPop+= region[i]['tamPop']
        regionDensIdade += np.array(region[i]['idade'])/region[i]['tamPop']

    regionHH = round(region[i]['tamPop']/region[i]['numDomicilio'],2)
    return regionPop, regionDensIdade, regionHH

# ========================================================================
#                   Import Neighborhood's informations

# ========================================================================
#           Zona Norte
igapo = ib.igapo.igapo
lagoaAzul = ib.lagoaAzul.lagoaAzul
nSenhoraApresentacao = ib.nSenhoraApresentacao.nSenhoraApresentacao
pajucara = ib.pajucara.pajucara
potengi = ib.potengi.potengi
redinha = ib.redinha.redinha
salinas = ib.salinas.salinas

norte = [igapo, lagoaAzul, nSenhoraApresentacao, pajucara, potengi, redinha, salinas]
nortePop, norteDensIdade, norteHH = calculatePopStats(norte)

# ========================================================================
#           Zona Sul
candelaria = ib.candelaria.candelaria
capimMacio = ib.capimMacio.capimMacio
lagoaNova = ib.lagoaNova.lagoaNova
neopolis = ib.neopolis.neopolis
novaDescoberta = ib.novaDescoberta.novaDescoberta
pitimbu = ib.pitimbu.pitimbu
pontaNegra = ib.pontaNegra.pontaNegra

sul = [candelaria, capimMacio, lagoaNova, neopolis, novaDescoberta, pitimbu, pontaNegra]
sulPop, sulDensIdade, sulHH = calculatePopStats(sul)

# ========================================================================
#           Zona Leste
alecrim = ib.alecrim.alecrim
areiaPreta = ib.areiaPreta.areiaPreta
barroVermelho = ib.barroVermelho.barroVermelho
cidadeAlta = ib.cidadeAlta.cidadeAlta
lagoaSeca = ib.lagoaSeca.lagoaSeca
maeLuiza = ib.maeLuiza.maeLuiza
petropolis = ib.petropolis.petropolis
praiaDoMeio = ib.praiaDoMeio.praiaDoMeio
ribeira = ib.ribeira.ribeira
rocas = ib.rocas.rocas
santosReis = ib.santosReis.santosReis
tirol = ib.tirol.tirol

leste = [alecrim, areiaPreta, barroVermelho, cidadeAlta, lagoaSeca, maeLuiza, petropolis, praiaDoMeio, ribeira, rocas, santosReis, tirol]
lestePop, lesteDensIdade, lesteHH = calculatePopStats(leste)

# ========================================================================
#           Zona Oeste
bomPastor = ib.bomPastor.bomPastor
cidadeEsperanca = ib.cidadeEsperanca.cidadeEsperanca
cidadeNova = ib.cidadeNova.cidadeNova
dixSeptoRosado = ib.dixSeptoRosado.dixSeptoRosado
felipeCamarao = ib.felipeCamarao.felipeCamarao
guarapes = ib.guarapes.guarapes
nSenhoraNazare = ib.nSenhoraNazare.nSenhoraNazare
planalto = ib.planalto.planalto
quintas = ib.quintas.quintas

oeste = [bomPastor, cidadeEsperanca, cidadeNova, dixSeptoRosado, felipeCamarao, guarapes, nSenhoraNazare, planalto, quintas]
oestePop, oesteDensIdade, oesteHH = calculatePopStats(oeste)

# ========================================================================
#                   City parameters

p_age_demografics = [0.1489,0.18,0.1851,0.1508,0.1305,0.0864,0.0607,0.0359,0.0217]

city_structure = {
    "city_structure" : {
        # "pop_size" : popsize,
        # "age_distribution" : p_age_demografics,
        # "household_size" : p_householdsize,
        "norte": {
                "pop_size" : nortePop,
                "age_distribution" : p_age_demografics,
                "household_size" : norteHH,
        },
        "sul": {
                "pop_size" : sulPop,
                "age_distribution" : p_age_demografics,
                "household_size" : sulHH,
        },
        "leste": {
                "pop_size" : lestePop,
                "age_distribution" : p_age_demografics,
                "household_size" : lesteHH,
        },
        "oeste": {
                "pop_size" : oestePop,
                "age_distribution" : p_age_demografics,
                "household_size" : oesteHH,
        },
    }
}



with open('natal_params.json', 'w') as outfile:
        outfile.write(json.dumps(city_structure, indent=4))



#-------------------------------#
#       ÖRNEK UYGUALAMA         #
#-------------------------------#

import sys

twoPythonMetin = """
Python!ın 2.x sürümlerinden birini kullanıyorsunuz.
Programı çalıştırabilmek için sisteminizde Python'ın
3.x sürümlerinden biri kurulu olmalı."""

threePythonMetin = "Programa Hoşgeldiniz!"

if sys.version_info.major < 3:
    print(twoPythonMetin)
else:
    print(threePythonMetin)

#buradaki sıkıntı ise:
# sys modlünün version_info() metodunun major, minor ve micro gibi
# nitelikleri 2.7 sürümünden önce yoktu
#bu yüzden yazdığımız kodlar 2.7 den önce sürümünde çalışmaz ve şöyle hata alırız:
# AttributeError: "tuple" object has no attribute 'major

#bu gibi hataların programın çökmesini engellemek için ise 
#tyr.. except.. den yararlanırız:

import sys

twoPython = """
Python'ın 2.x sürümlerinden birini kullanıyorsunuz.
Programı çalıştırabilmek için sisteminizde Python'ın
3x sürümlerinden biri kurulu olmalı."""

threePython = "Programa Hoşgeldiniz!"
try:
    if sys.version_info.major < 3:
        print(twoPython)
    else:
        print(threePython)
except AttributeError:
    print(twoPython)            

#eğer kullanıcı kodu 2.7 den öncek sürümde çalıştırırsa
# except blogu araya girer ve twoMetin i yazdırır
#bu sayede kullanıcı hem metini görmüş olacak hem de program çökmeyecek






















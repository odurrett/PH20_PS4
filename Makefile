# This makefile is intended to streamline the creation of the Ph 20 PS 3 data
# files.

# Go through the codes one by one and generate their corresponding data files.

.PHONY : dats
dats : anPhaseData.txt energyData.txt energyImpData.txt energySymData.txt exPhaseData.txt hPropData.txt hPropImpData.txt imPhaseData.txt impAbsErrsData.txt impErrsdata.txt implicitData.txt numAbsErrsData.txt numErrsData.txt numInvestData.txt symPhaseData.txt

.PHONY : clean
clean :
	rm -f *.txt

anPhaseData.txt : anPhase.py
  python3 anPhase.py 0 5 50

energyData.txt : energy.py
  python3 energy.py 0 5 50

energyImpData.txt : energyImp.py
  python3 energyImp.py 0 5 50

energySymData.txt : energySym.py
  python3 energySym.py 0 5 50

exPhaseData.txt : exPhase.py
  python3 exPhase.py 0 5 50

hPropData.txt : hProp.py
  python3 hProp.py 0 5 50

hPropImpData.txt : hPropImp.py
  python3 hPropImp.py 0 5 50

imPhaseData.txt : imPhase.py
  python3 imPhase.py 0 5 50

impAbsErrsData.txt : impAbsErrs.py
  python 3 impAbsErrs.py 0 5 50

impErrsData.txt : impErrs.py
  python3 impErrs.py 0 5 50

implicitData.txt : implicit.py
  python3 implicit.py 0 5 50

numAbsErrsData.txt : numAbsErrs.py
  python3 numAbsErrs.py 0 5 50

numErrsData.txt : numErrs.py
  python3 numErrs.py 0 5 50

numInvestData.txt : numInvest.py
  python3 numInvest.py 0 5 50

symPhaseData.txt : symPhase.py
  python3 symPhase.py 0 5 50

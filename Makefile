# This makefile is intended to streamline the creation of the Ph 20 PS 3 data
# files.

# Go through the codes one by one and generate their corresponding data files.

LANGUAGE=python3
X0=0
V0=5
T=50

.PHONY : dats
dats : anPhaseData.txt energyData.txt energyImpData.txt energySymData.txt exPhaseData.txt hPropData.txt hPropImpData.txt imPhaseData.txt impAbsErrsData.txt impErrsdata.txt implicitData.txt numAbsErrsData.txt numErrsData.txt numInvestData.txt symPhaseData.txt

.PHONY : clean
clean :
	rm -f *.txt

anPhaseData.txt : anPhase.py
  $(LANGUAGE) $^ $(X0) $(V0) $(T)

energyData.txt : energy.py
  $(LANGUAGE) $^ $(X0) $(V0) $(T)

energyImpData.txt : energyImp.py
  $(LANGUAGE) $^ $(X0) $(V0) $(T)

energySymData.txt : energySym.py
  $(LANGUAGE) $^ $(X0) $(V0) $(T)

exPhaseData.txt : exPhase.py
  $(LANGUAGE) $^ $(X0) $(V0) $(T)

hPropData.txt : hProp.py
  $(LANGUAGE) $^ $(X0) $(V0) $(T)

hPropImpData.txt : hPropImp.py
  $(LANGUAGE) $^ $(X0) $(V0) $(T)

imPhaseData.txt : imPhase.py
  $(LANGUAGE) $^ $(X0) $(V0) $(T)

impAbsErrsData.txt : impAbsErrs.py
  $(LANGUAGE) $^ $(X0) $(V0) $(T)

impErrsData.txt : impErrs.py
  $(LANGUAGE) $^ $(X0) $(V0) $(T)

implicitData.txt : implicit.py
  $(LANGUAGE) $^ $(X0) $(V0) $(T)

numAbsErrsData.txt : numAbsErrs.py
  $(LANGUAGE) $^ $(X0) $(V0) $(T)

numErrsData.txt : numErrs.py
  $(LANGUAGE) $^ $(X0) $(V0) $(T)

numInvestData.txt : numInvest.py
  $(LANGUAGE) $^ $(X0) $(V0) $(T)

symPhaseData.txt : symPhase.py
  $(LANGUAGE) $^ $(X0) $(V0) $(T)

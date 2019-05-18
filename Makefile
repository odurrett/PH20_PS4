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

%Data.txt : %.py
	$(LANGUAGE) %.py $(X0) $(V0) $(T)

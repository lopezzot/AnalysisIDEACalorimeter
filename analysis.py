import map
import ROOTHistograms
from ROOT import TTree, TFile

machine = raw_input("On what machine running? (mac, linux, office) ")
if machine == "mac":
		path = str("/Users/lorenzo/cernbox/work/Git-to-Mac/AnalysisIDEACalorimeter/")
if machine == "linux":
		path = str("/home/lorenzo/cernbox/work/Git-to-Mac/AnalysisIDEACalorimeter/")
if machine == "office":
		path = str("/media/geant4-mc-infn/DataStorage/lorenzo/cernbox/work/Git-to-Mac/AnalysisFullCalorimeter/")

def eventdisplay():
	inputfile = raw_input("Insert root file: ")
	inputfile = TFile(path+inputfile)
	tree = TTree()
	inputfile.GetObject("B4", tree)

	outputfile = raw_input("Insert root output file: ")
	displayfile = TFile(path+outputfile+".root","RECREATE")

	#loop over events
	for Event in range(int(tree.GetEntries())):

		tree.GetEntry(Event)

		#Set values of the tree
		PrimaryParticleName = tree.PrimaryParticleName # MC truth: primary particle Geant4 name
		PrimaryParticleEnergy = tree.PrimaryParticleEnergy
		EnergyTot = tree.EnergyTot # Total energy deposited in calorimeter
		Energyem = tree.Energyem # Energy deposited by the em component
		EnergyScin = tree.EnergyScin # Energy deposited in Scin fibers (not Birk corrected)
		EnergyCher = tree.EnergyCher # Energy deposited in Cher fibers (not Birk corrected)
		NofCherenkovDetected = tree.NofCherenkovDetected # Total Cher p.e. detected
		BarrelR_VectorSignals = tree.VectorSignals # Vector of energy deposited in Scin fibers (Birk corrected)
		VectorSignalsCher = tree.VectorSignalsCher # Vector of Cher p.e. detected in Cher fibers
		
		for towerindex, signal in enumerate(BarrelR_VectorSignals):
			theta, phi = map.maptowerBR(towerindex)
			if signal > 0.:
				print "theta "+str(theta)+" phi "+str(phi)+ " signal "+str(signal)

		ROOTHistograms.create_eventdisplay(PrimaryParticleName, BarrelR_VectorSignals) 

eventdisplay()
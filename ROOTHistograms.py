from ROOT import *
import map
def create_eventdisplay(PrimaryParticleName, BarrelRVectorSignals):
	"""Function to perform ROOT event display form calo"""
	
	#Set ROOT histograms (x=theta, y=phi)
	TH2Signals = TH2F("ScinSignals", PrimaryParticleName, 40, 0., 45.12, 256, 0., 360.)
	
	#Fill histograms in for loop
	for towerindex in range(256*40):
		theta, phi = map.maptowerBR(towerindex)
		TH2Signals.Fill(theta,phi,BarrelRVectorSignals[towerindex])
			
	#Draw + DrawOptions histograms		
	Style = gStyle
	Style.SetPalette(1) #Root palette style
	Style.SetOptStat(0) #Do not show statistics
	TH2Signals.SetLineWidth(0) #TH2Signals #No line width
	TH2Signals.SetLineColor(2)
	#TH2Signals.SetFillColorAlpha(2, 0.)
	XAxis = TH2Signals.GetXaxis()
	XAxis.SetTitle("Theta (deg)")
	XAxis.CenterTitle()
	XAxis.SetTitleOffset(1.8)
	YAxis = TH2Signals.GetYaxis()
	YAxis.SetTitle("Phi (deg)")
	YAxis.CenterTitle()
	YAxis.SetTitleOffset(1.8)
	ZAxis = TH2Signals.GetZaxis()
	ZAxis.SetTitle("Energy (MeV)")
	ZAxis.SetTitleOffset(1.4)
	TH2Signals.Draw("LEGO2Z 0 FB")
	TH2Signals.Write()
	gPad.SaveAs("ImageScintillation.pdf")
	
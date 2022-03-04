from lib.cuts import dilepton

cfg =  {
    "cuts" : [dilepton],
    "variables" : [
        "muon_pt",
        "muon_eta",
        "muon_phi",
        "electron_pt",
        "electron_eta",
        "electron_phi",
        "jet_pt",
        "jet_eta",
        "jet_phi",
        "nmuon",
        "nelectron",
        "nlep",
        "nmuongood",
        "nelectrongood",
        "nlepgood",
        "njet",
        "nbjet",
        "nfatjet"
    ],
    "variables2d" : [
        
    ]
}
import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/036/00000/1ABD0A12-619F-E611-AAFC-02163E013674.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/036/00000/1C0FA1A3-5D9F-E611-B9F1-02163E0120CA.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/036/00000/1E2A263F-5C9F-E611-8E88-02163E01212B.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/036/00000/2AF0B66C-5D9F-E611-AA63-02163E012AD6.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/036/00000/5029E0FD-5C9F-E611-BFC1-02163E0134E4.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/036/00000/6025B973-5C9F-E611-80AD-02163E01282A.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/036/00000/62A7F863-5D9F-E611-B5AD-FA163EFB05CD.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/036/00000/684FD796-5C9F-E611-8E6C-FA163E812A96.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/036/00000/C83EAF4C-5C9F-E611-8F24-02163E0128CA.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/036/00000/CEDCB902-619F-E611-A826-02163E014369.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/036/00000/D2210D65-5D9F-E611-9E73-FA163E15A9D2.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/036/00000/F4AA530B-619F-E611-884C-FA163EEEACE8.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/037/00000/2217DEA3-6C9F-E611-9B17-02163E011BED.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/037/00000/3631D4EF-659F-E611-B5E1-02163E0135F3.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/037/00000/68773ED6-6A9F-E611-A73D-02163E0145E3.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/037/00000/70B0A2A9-6A9F-E611-B108-02163E0145FF.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/037/00000/7C349C01-669F-E611-9080-02163E0137AB.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/037/00000/96815FC3-659F-E611-97A2-02163E011A76.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/037/00000/AE33E170-719F-E611-8346-02163E0146C8.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/037/00000/CAD7AEB7-6A9F-E611-A63F-FA163E811751.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/037/00000/E0A454B6-6A9F-E611-8B81-02163E011B12.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/037/00000/F07362A6-6A9F-E611-B29E-FA163EE3076B.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/037/00000/F46D439F-659F-E611-9E0A-FA163ED73C94.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/038/00000/B2B4B2CF-7A9F-E611-8E07-02163E011BF4.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/038/00000/F43D26E3-8C9F-E611-BDE5-02163E011B6D.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/039/00000/4E6E2DC7-8F9F-E611-8776-02163E0134D1.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/040/00000/3A9B0397-8F9F-E611-AF44-02163E0146F9.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/040/00000/3C45F46D-859F-E611-ACB2-FA163E8EBE8C.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/041/00000/1E5FCF92-849F-E611-B275-02163E011A78.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/041/00000/6AC5F6B2-7B9F-E611-A90F-FA163E7B9070.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/042/00000/10399ADB-729F-E611-A2DB-02163E0143D1.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/042/00000/4637B21C-779F-E611-82E6-02163E011BD4.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/042/00000/64E2695B-859F-E611-8330-02163E01463E.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/042/00000/70FBD58F-6F9F-E611-84A1-02163E014469.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/043/00000/46229600-A69F-E611-B800-FA163E200A11.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/043/00000/46860424-CE9F-E611-A189-FA163E543FC3.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/043/00000/4CB97641-BA9F-E611-BEAB-FA163EA3EAEF.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/043/00000/6C7AE0F1-A09F-E611-A581-02163E0140FD.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/043/00000/9E271C42-D19F-E611-B354-02163E012840.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/043/00000/C4B69AEB-AD9F-E611-BAC6-02163E014683.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/043/00000/F8A1292E-9F9F-E611-8B4C-02163E011E65.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/044/00000/BE5F4C22-D29F-E611-AEAA-02163E011C32.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/068/00000/141C2E60-D79F-E611-8B5D-02163E011E5F.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/068/00000/6EBD2848-D69F-E611-9896-FA163E068844.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v3/000/284/068/00000/EC368154-B69F-E611-8D9B-FA163E37C37C.root',
] )

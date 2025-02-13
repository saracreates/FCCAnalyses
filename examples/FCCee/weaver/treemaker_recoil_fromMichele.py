# list of processes (mandatory)

ecm = 240
ecm = 365

# intLumi = 10800000  # 10.8 /ab

if ecm == 240:
    intLumi = 10800000
else:
    intLumi = 3000000
    intLumi = 500000


doHinv = False

debugFraction = 0.1
sel = "Hvis"
if doHinv:
    sel = "Hinv"


debug = False

processList = {
    f"p8_ee_ZZ_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"p8_ee_WW_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"p8_ee_Zqq_ecm{ecm}": {"fraction": 1 * debugFraction},
    # f"wzp6_ee_qq_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_WbWb_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_nunuH_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_qqH_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_ssH_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_ccH_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_bbH_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_eeH_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_mumuH_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_tautauH_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_nunuH_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_ZH_Hinv_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_qqH_Hbb_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_bbH_Hbb_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_ccH_Hbb_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_ssH_Hbb_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_qqH_Hcc_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_bbH_Hcc_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_ccH_Hcc_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_ssH_Hcc_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_qqH_Hss_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_bbH_Hss_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_ccH_Hss_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_ssH_Hss_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_qqH_Hgg_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_bbH_Hgg_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_ccH_Hgg_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_ssH_Hgg_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_qqH_HWW_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_bbH_HWW_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_ccH_HWW_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_ssH_HWW_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_qqH_HZZ_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_bbH_HZZ_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_ccH_HZZ_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_ssH_HZZ_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_qqH_Htautau_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_bbH_Htautau_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_ccH_Htautau_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_ssH_Htautau_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_qqH_Haa_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_bbH_Haa_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_ccH_Haa_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_ssH_Haa_ecm{ecm}": {"fraction": 1 * debugFraction},
    # f"wzp6_ee_qqH_Hmumu_ecm{ecm}": {"fraction": 1 * debugFraction},
    # f"wzp6_ee_bbH_Hmumu_ecm{ecm}": {"fraction": 1 * debugFraction},
    # f"wzp6_ee_ccH_Hmumu_ecm{ecm}": {"fraction": 1 * debugFraction},
    # f"wzp6_ee_ssH_Hmumu_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_qqH_HZa_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_bbH_HZa_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_ccH_HZa_ecm{ecm}": {"fraction": 1 * debugFraction},
    f"wzp6_ee_ssH_HZa_ecm{ecm}": {"fraction": 1 * debugFraction},
}

debug = False
if debug:
    debugFraction = 0.01
    processList = {
        f"wzp6_ee_qqH_Haa_ecm{ecm}": {"fraction": 1 * debugFraction},
        f"wzp6_ee_bbH_Haa_ecm{ecm}": {"fraction": 1 * debugFraction},
        f"wzp6_ee_ccH_Haa_ecm{ecm}": {"fraction": 1 * debugFraction},
        f"wzp6_ee_ssH_Haa_ecm{ecm}": {"fraction": 1 * debugFraction},
    }


# Production tag when running over EDM4Hep centrally produced events, this points to the yaml files for getting sample statistics (mandatory)
prodTag = "FCCee/winter2023/IDEA/"

# Link to the dictonary that contains all the cross section informations etc... (mandatory)
procDict = "FCCee_procDict_winter2023_IDEA.json"

# additional/custom C++ functions, defined in header files (optional)
includePaths = ["functions.h"]

# Define the input dir (optional)
# inputDir    = "outputs/FCCee/higgs/mH-recoil/mumu/stage1"
# inputDir    = "./localSamples/"

# Optional: output directory, default is local running directory
# outputDir = f"/eos/user/s/selvaggi/analysis/ZHhad_recoil_{sel}_{ecm}/trees/"
outputDir = f"/eos/experiment/fcc/ee/analyses/case-studies/higgs/zh_hadronic_recoil/ZHhad_recoil_{sel}_{ecm}/trees/"

# optional: ncpus, default is 4, -1 uses all cores available
nCPUS = -1

# scale the histograms with the cross-section and integrated luminosity
# doScale = True


# define some binning for various histograms
bins_count = (50, -0.5, 49.5)
bins_y23 = (150, 0, 150)
bins_y34 = (100, 0, 100)
bins_y45 = (100, 0, 100)
bins_energy = (100, 0, ecm)
bins_npart = (150, 0, 150)

##?| name of collections in EDM root files
collections = {
    "GenParticles": "Particle",
    "PFParticles": "ReconstructedParticles",
    "PFTracks": "EFlowTrack",
    "PFPhotons": "EFlowPhoton",
    "PFNeutralHadrons": "EFlowNeutralHadron",
    # "TrackState": "EFlowTrack_1",
    "TrackState": "_EFlowTrack_trackStates",
    "TrackerHits": "TrackerHits",
    "CalorimeterHits": "CalorimeterHits",
    # "dNdx": "EFlowTrack_2",
    "dNdx": "_EFlowTrack_dxQuantities",
    "PathLength": "EFlowTrack_L",
    "Bz": "magFieldBz",
    "Electrons": "Electron",
    "Muons": "Muon",
}

from addons.FastJet.jetClusteringHelper import ExclusiveJetClusteringHelper

jetClusteringHelper = None


# Mandatory: RDFanalysis class where the use defines the operations on the TTree
class RDFanalysis:

    # __________________________________________________________
    # Mandatory: analysers funtion to define the analysers to process, please make sure you return the last dataframe, in this example it is df2
    def analysers(df):

        # __________________________________________________________
        # Mandatory: analysers funtion to define the analysers to process, please make sure you return the last dataframe, in this example it is df2

        # define some aliases to be used later on

        #########
        ### CUT : at least 6 reconstructed particles
        #########

        df = df.Define(
            "recopart_no",
            "FCCAnalyses::ReconstructedParticle::get_n(ReconstructedParticles)",
        )

        df = df.Define(
            "gen_vertex",
            "FCCAnalyses::MCParticle::get_EventPrimaryVertexP4()(Particle)",
        ) 

        df = df.Define("vertex_x", "gen_vertex.X()")

        df = df.Filter("recopart_no >= 6")

        # find isolated leptons with momentum > 10 GeV
        df = df.Alias("Muon0", "Muon#0.index")
        df = df.Define(
            "muons_all",
            "FCCAnalyses::ReconstructedParticle::get(Muon0, ReconstructedParticles)",
        )
        df = df.Define("muons", "FCCAnalyses::ReconstructedParticle::sel_p(10)(muons_all)")
        df = df.Define(
            "muons_iso",
            "FCCAnalyses::ZHfunctions::coneIsolation(0.01, 0.5)(muons, ReconstructedParticles)",
        )
        df = df.Define("muons_sel_iso", "FCCAnalyses::ZHfunctions::sel_iso(0.25)(muons, muons_iso)")
        df = df.Define("isomuons_no", "muons_sel_iso.size()")

        df = df.Alias("Electron0", "Electron#0.index")
        df = df.Define(
            "electrons_all",
            "FCCAnalyses::ReconstructedParticle::get(Electron0, ReconstructedParticles)",
        )
        df = df.Define("electrons", "FCCAnalyses::ReconstructedParticle::sel_p(10)(electrons_all)")
        df = df.Define(
            "electrons_iso",
            "FCCAnalyses::ZHfunctions::coneIsolation(0.01, 0.5)(electrons, ReconstructedParticles)",
        )
        df = df.Define(
            "electrons_sel_iso",
            "FCCAnalyses::ZHfunctions::sel_iso(0.25)(electrons, electrons_iso)",
        )
        df = df.Define("isoelectrons_no", "electrons_sel_iso.size()")

        df = df.Alias("Photon0", "Photon#0.index")
        df = df.Define(
            "photons_all",
            "FCCAnalyses::ReconstructedParticle::get(Photon0, ReconstructedParticles)",
        )
        df = df.Define("photons", "FCCAnalyses::ReconstructedParticle::sel_p(10)(photons_all)")
        df = df.Define(
            "photons_iso",
            "FCCAnalyses::ZHfunctions::coneIsolation(0.01, 0.5)(photons, ReconstructedParticles)",
        )
        df = df.Define(
            "photons_sel_iso",
            "FCCAnalyses::ZHfunctions::sel_iso(0.25)(photons, photons_iso)",
        )

        df = df.Define("isophotons_no", "photons_sel_iso.size()")

        ## remove isolated particles from jet clustering
        df = df.Define(
            "ReconstructedParticles_noisophotons",
            "FCCAnalyses::ReconstructedParticle::remove(ReconstructedParticles, photons_sel_iso)",
        )

        df = df.Define(
            "ReconstructedParticles_noisoelectrons",
            "FCCAnalyses::ReconstructedParticle::remove(ReconstructedParticles_noisophotons, electrons_sel_iso)",
        )

        df = df.Define(
            "ReconstructedParticles_noiso",
            "FCCAnalyses::ReconstructedParticle::remove(ReconstructedParticles_noisoelectrons, muons_sel_iso)",
        )

        # results.append(df.Histo1D(("recopart_noisophotons_no", "", *bins_npart), "recopart_noisophotons_no"))

        df = df.Define("isol_leptons_no", "isomuons_no + isoelectrons_no")

        df = df.Define(
            "missingEnergy",
            f"FCCAnalyses::ZHfunctions::missingEnergy({ecm}., ReconstructedParticles)",
        )
        df = df.Define("cosTheta_miss", "FCCAnalyses::ZHfunctions::get_cosTheta_miss(missingEnergy)")
        df = df.Define("pmiss", "FCCAnalyses::ZHfunctions::get_pmiss(missingEnergy)")
        df = df.Define("pzmiss", "FCCAnalyses::ZHfunctions::get_pzmiss(missingEnergy)")

        global jetClusteringHelper

        ## define jet clustering parameters N = 2
        jetClusteringHelper_N2 = ExclusiveJetClusteringHelper("ReconstructedParticles", 2, "N2")
        jetClusteringHelper_N3 = ExclusiveJetClusteringHelper("ReconstructedParticles", 3, "N3")
        jetClusteringHelper_N4 = ExclusiveJetClusteringHelper("ReconstructedParticles", 4, "N4")
        jetClusteringHelper_N5 = ExclusiveJetClusteringHelper("ReconstructedParticles", 5, "N5")
        jetClusteringHelper_N6 = ExclusiveJetClusteringHelper("ReconstructedParticles", 6, "N6")

        # jetClusteringHelper_N2 = ExclusiveJetClusteringHelper("ReconstructedParticles_noiso", 2, "N2")
        df = jetClusteringHelper_N2.define(df)
        df = jetClusteringHelper_N3.define(df)
        df = jetClusteringHelper_N4.define(df)
        df = jetClusteringHelper_N5.define(df)
        df = jetClusteringHelper_N6.define(df)

        df = df.Define("y23", "std::sqrt(JetClusteringUtils::get_exclusive_dmerge(_jet_N2, 2))")  # dmerge from 3 to 2
        df = df.Define("y34", "std::sqrt(JetClusteringUtils::get_exclusive_dmerge(_jet_N2, 3))")  # dmerge from 4 to 3
        df = df.Define("y45", "std::sqrt(JetClusteringUtils::get_exclusive_dmerge(_jet_N2, 4))")  # dmerge from 4 to 5
        df = df.Define("y56", "std::sqrt(JetClusteringUtils::get_exclusive_dmerge(_jet_N2, 5))")  # dmerge from 5 to 6

        # now write above in a for loop
        for i in range(2, 7):
            for j in range(1, i + 1):
                df = df.Define(f"jet{j}_nconst_N{i}", f"jet_nconst_N{i}[{j-1}]")
                df = df.Define(f"jet{j}_ncharged_N{i}", f"jet_ncharged_N{i}[{j-1}]")
                df = df.Define(f"jet{j}_p_N{i}", f"jet_p_N{i}[{j-1}]")
                df = df.Define(f"jet{j}_e_N{i}", f"jet_e_N{i}[{j-1}]")
                df = df.Define(f"jet{j}_mass_N{i}", f"jet_mass_N{i}[{j-1}]")
                df = df.Define(f"jet{j}_phi_N{i}", f"jet_phi_N{i}[{j-1}]")
                df = df.Define(f"jet{j}_theta_N{i}", f"jet_theta_N{i}[{j-1}]")
                df = df.Define(f"jet{j}_nlep_N{i}", f"jet_nlep_N{i}[{j-1}]")

        for i in range(2, 7):

            df = df.Define(
                f"whad_and_ojets_N{i}",
                f"FCCAnalyses::ZHfunctions::reshad_and_remaining_jets(jet_N{i}, 80.4)",
            )
            df = df.Define(f"mW_N{i}", f"JetClusteringUtils::get_visible_mass(whad_and_ojets_N{i}.reshad_candidate)")  #
            df = df.Define(f"mWrec_N{i}", f"JetClusteringUtils::recoilBuilder({ecm})(whad_and_ojets_N{i}.reshad_candidate)")  # the Z recoil for the visi
            df = df.Define(f"mWojets_N{i}", f"JetClusteringUtils::get_visible_mass(whad_and_ojets_N{i}.remaining_jets)")  #

            df = df.Define(
                f"zhad_and_ojets_N{i}",
                f"FCCAnalyses::ZHfunctions::reshad_and_remaining_jets(jet_N{i}, 91.2)",
            )
            df = df.Define(f"mZ_N{i}", f"JetClusteringUtils::get_visible_mass(zhad_and_ojets_N{i}.reshad_candidate)")  #
            df = df.Define(f"mZrec_N{i}", f"JetClusteringUtils::recoilBuilder({ecm})(zhad_and_ojets_N{i}.reshad_candidate)")  # the Z recoil for the visi
            df = df.Define(f"mZojets_N{i}", f"JetClusteringUtils::get_visible_mass(zhad_and_ojets_N{i}.remaining_jets)")  #

        # df = df.Define("NzcandP4_N5", "zcandP4_N5.size()")
        # numpy_data = df.AsNumpy(["mrec"])
        # print(numpy_data)

        ####################
        # PRESELECTION : addresses background rejection
        ###################

        #########
        ### CUT : event consistent with HZ
        #########

        return df

    # __________________________________________________________
    # Mandatory: output function, please make sure you return the branchlist as a python list
    def output():
        branchList = ["cosTheta_miss", "pmiss", "pzmiss", "isoelectrons_no", "isomuons_no", "isophotons_no", "y23", "y34", "y45", "y56", "vertex_x"]

        for i in range(2, 7):
            branchList += [
                f"mW_N{i}",
                f"mWrec_N{i}",
                f"mWojets_N{i}",
                f"mZ_N{i}",
                f"mZrec_N{i}",
                f"mZojets_N{i}",
            ]

            for j in range(1, i + 1):
                branchList += [f"jet{j}_nconst_N{i}"]
                branchList += [f"jet{j}_ncharged_N{i}"]
                branchList += [f"jet{j}_p_N{i}"]
                branchList += [f"jet{j}_e_N{i}"]
                branchList += [f"jet{j}_mass_N{i}"]
                branchList += [f"jet{j}_phi_N{i}"]
                branchList += [f"jet{j}_theta_N{i}"]
                branchList += [f"jet{j}_nlep_N{i}"]

        ##  outputs jet properties
        # branchList += jetClusteringHelper.outputBranches()

        return branchList

import sys
import glob
import os
import argparse
import subprocess
from subprocess import Popen, PIPE
from datetime import date
import time
import concurrent.futures

# ________________________________________________________________________________
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--indir",
        help="path input directory",
        default="/eos/experiment/fcc/ee/generation/DelphesEvents/winter2023/IDEA/",
    )
    parser.add_argument(
        "--outdir",
        help="path output directory",
        default="/eos/experiment/fcc/ee/jet_flavour_tagging/winter2023/fastsim_2mio_total_SaraTagging/IDEA/evaluation_Andrea/",
    )

    parser.add_argument("--sample", help="sample name", default="wzp6_ee_nunuH_HXX_ecm240") # change energy here
    parser.add_argument("--ncpus", help="number of cpus", type=int, default=32) # max 64, be nice and use 32
    parser.add_argument("--opt", help="option 1: run stage 1, 2: run stage 2, 3: all 4: clean", default="3")
    parser.add_argument("--test", help="run on 2 files with 100 events each per flavor for testing purposes", type=bool, default=False)

    args = parser.parse_args()
    indir = args.indir
    outdir = args.outdir
    ncpus = args.ncpus
    sample = args.sample
    opt = args.opt
    test = args.test

    ## qq is merge of uu/dd
    flavors = ["uu", "dd", "bb", "cc", "ss", "gg", "tautau"]
    #flavors = ["ss", "gg", "tautau"]


    outtmpdir = "/tmp/saaumill/data/stage_all"
    os.system("rm -rf {}".format(outtmpdir))
    os.system("mkdir -p {}".format(outtmpdir))
    os.system("mkdir -p {}".format(outdir))

    ## fill name of stage1 files
    stage1_files = dict()
    for f in flavors:
        stage1_files[f] = "{}/stage1_H{}.root".format(outtmpdir, f)

    edm_files = ""

    for f in flavors:
        ### run stage 1
        if opt == "1" or opt == "3":

            sample_f = sample.replace("XX", f)
            edm_files = "{}/{}/*.root".format(indir, sample_f)
            if test: 
                all_files = glob.glob(edm_files)
                edm_files = all_files[:2]
                edm_files = " ".join(edm_files)
            cmd_stage1 = (
                "fccanalysis run examples/FCCee/weaver/stage1.py --output {} --files-list {} --ncpus {}".format(
                    stage1_files[f], edm_files, ncpus
                )
            )
            print("running stage 1: ")
            print("")
            print("{}".format(cmd_stage1))
            print("")
            os.system(cmd_stage1)

        ### run stage 2
        if opt == "2" or opt == "3":

            nevents = count_events(stage1_files[f])
            # use 1.9 mio events per file for training
            nevents = 50000
            if test:
                if nevents>100:
                    nevents = 100
            nevents_per_thread = int(nevents / ncpus)

            commands_stage2 = []
            stage2_files = dict()

            stage2_final_file = "{}/H{}.root".format(outtmpdir, f) # change final name here
            stage2_wild_files = "{}/stage2_H{}_*.root".format(outtmpdir, f)
            hadd_cmd = "hadd -f {} {}".format(stage2_final_file, stage2_wild_files)

            for i in range(ncpus):

                stage2_files[i] = "{}/stage2_H{}_{}.root".format(outtmpdir, f, i)
                nstart = i * nevents_per_thread
                nend = nstart + nevents_per_thread

                cmd_stage2 = "python examples/FCCee/weaver/stage2.py {} {} {} {}".format(
                    stage1_files[f], stage2_files[i], nstart, nend
                )

                commands_stage2.append(cmd_stage2)

            # Create a thread pool executor with 4 threads

            executor = concurrent.futures.ThreadPoolExecutor(max_workers=ncpus)

            # Submit each command to the executor
            future_to_command = {executor.submit(run_command, command): command for command in commands_stage2}

            # Wait for all threads to finish
            concurrent.futures.wait(future_to_command)

            # Run the final command
            print("")
            print("now collect and hadd stage 2 files into: {}".format(stage2_final_file))
            print(hadd_cmd)
            os.system(hadd_cmd)
            print("")
            print("copy file to final destination...")
            os.system("cp {} {}".format(stage2_final_file, outdir))
            print("file {} copied".format(outdir))
            print("cleaning up tmp files...".format(outdir))
            os.system("rm -rf {} {} {}".format(stage2_final_file, stage1_files[f], stage2_wild_files))
            print("done.")


# ________________________________________________________________________________


def run_command(command):
    # Replace this with code to run the command
    print("running command: {}".format(command))
    os.system(command)


# ________________________________________________________________________________
def count_events(file, tree_name="events"):
    import ROOT

    # Open the ROOT file
    root_file = ROOT.TFile.Open(file)

    # Get the tree from the file
    tree = root_file.Get(tree_name)

    # Get the number of events in the tree
    num_events = tree.GetEntries()

    return num_events


# ________________________________________________________________________________
def count_events(file, tree_name="events"):
    import ROOT

    # Open the ROOT file
    root_file = ROOT.TFile.Open(file)

    # Get the tree from the file
    tree = root_file.Get(tree_name)

    # Get the number of events in the tree
    num_events = tree.GetEntries()

    return num_events


# _______________________________________________________________________________________
if __name__ == "__main__":
    main()

# Script to create silent ground truth audio files
#
# Author: Marvin Borsdorf
# Machine Listening Lab, University of Bremen, Germany
# August, 2021

import librosa
import soundfile as sf
import numpy as np
import argparse
import os
from tqdm import tqdm

def run(args):
    root = args.root
    output_path = args.output
    fs = args.fs
    subsets = ["tr", "cv", "tt"]

    for s in tqdm(subsets): # For each subset
        # Read mix.txt and ref.txt
        with open(os.path.join(root, s, 'mixTest.txt')) as mix_file:
            mix = mix_file.readlines()

        with open(os.path.join(root, s, 'refTest.txt')) as ref_file:
            ref = ref_file.readlines()

        # Check for same lengths
        assert len(mix) == len(ref)

        # Remove new line characters and split keys and values
        mix = [k.rstrip("\n").split(" ") for k in mix]
        ref = [k.rstrip("\n").split(" ") for k in ref]

        # Sort lists in the same way
        mix = sorted(mix, key=lambda x:x[0])
        ref = sorted(ref, key=lambda x:x[0])

        # Make dirs
        dir = ref[0][1].rsplit('/', 1)[0]
        print("Make dir: " + dir)
        os.makedirs(dir)

        for a, b in tqdm(zip(mix, ref)):
            x, sr = librosa.load(a[1], sr=fs) # Load mixture audio file
            silent_audio = np.zeros(x.shape, dtype=np.float32) # Create silent audio file with same length
            assert len(silent_audio) == len(x) # Double check length
            sf.write(b[1], silent_audio, fs, subtype='FLOAT') # Store silent audio file on hard disk


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Arguments to create silent ground truth audio files.")
    parser.add_argument("--output",
                        type=str,
                        default=None,
                        required=True,
                        help="Path to store the silent audio files.")
    parser.add_argument("--root",
                        type=str,
                        default="./data_lists/2T-AT/", # 1T-AT would lead to the same result since mixture and single utterances have the same lengths
                        required=False,
                        help="Root path for data lists of absent target speaker condition, e.g. 2T-AT.")
    parser.add_argument("--fs",
                        type=int,
                        default=8000,
                        required=False,
                        help="Sampling frequency.")
    args = parser.parse_args()
    run(args)

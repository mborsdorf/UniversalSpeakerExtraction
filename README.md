# Universal Speaker Extraction

Here we distribute the data lists and reference the mixing scripts to reproduce our experiments on universal speaker extraction. The universal speaker extraction task is to attend to a target speaker in scenes with one talker (1T) and two talkers (2T) in which the target speaker can be present (PT) or absent (AT). This describes real-world everyday conversational situations. If the target speaker is present in the mixture, the model should extract the target speaker's speech, whereas the model should output silence if the target speaker is absent.

## About the data

### Conditions

The database is derived from the WSJ0-2mix-extr [1] database which is an adaptation of the popular WSJ0-2mix database [2]. For more information on WSJ0-2mix-extr, please visit the referenced repository. The database consists of 20,000, 5,000, and 3,000 utterances for training, validation and test sets respectively. Because each speaker in a two-talker mixture can be considered as a target speaker, each mixture can be used twice. This doubles the amount of data. For further information on how to simulate the data to reproduce our experiments, please see section "Database simulation".

We modified the WSJ0-2mix-extr database to cover four different conditions to model the aforementioned real-world everyday conversational situations:
- **2T-PT:** Two talkers in the input mixture and the target speaker is present in the mixture (this is the commonly investigated condition).
- **1T-PT:** One talker in the input mixture who is the target speaker.
- **2T-AT:** Two talkers in the input mixture but the target speaker is absent, i.e. not part of the mixture.
- **1T-AT:** One talker in the input mixture who is not the target speaker (target speaker is absent).

Each condition comprises data triples (audio files) in the following way:  

|  | 2T-PT | 1T-PT | 2T-AT | 1T-AT |
|-----|-------|-------|-------|-------|
| Input mixture (mix)| Two talkers | One talker | Two talkers | One talker |
| Target speaker's reference (aux) | One of the mixture's talkers | The mixture's talker | A talker different to the mixture's talkers | A talker different to the mixture's talker |
| Ground truth (ref) | Target speaker's speech | Target speaker's speech | Silence | Silence |

**Hint:** The target speaker's reference signal (aux) is usually given by an utterance which is different from the target speaker's utterance in the input mixture. However, for some cases in the training and validation sets the reference signal utterance is the same as in the mixture. This simulates a speaker verification mechanism in which the same reference/enrolment speech has to pass through both speaker encoder and speaker extraction parts.

### Compositions

The data is used as "min" version with "8 kHz" sampling frequency. We provide the single training, validation and test data lists for each of the four conditions. The speakers in the respective subset are the same for each condition, e.g. the speakers in the training set for 2T-PT are the same as in the three other training sets. Moreover, the input mixtures for 2T-PT and 2T-AT as well as for 1T-PT and 1T-AT are respectively the same. This also applies to the validation and test sets.

|  | # utterances (tr / cv / tt) |
|----------|:-----------------------------:|
| 2T-PT    | 40,000 / 10,000 / 6,000     |
| 1T-PT    | 40,000 / 10,000 / 6,000     |
| 2T-AT    | 40,000 / 10,000 / 6,000     |
| 1T-AT    | 40,000 / 10,000 / 6,000     |

While the test datasets remain the same, we provide different compositions of training and validation data as follows.

The 2T-AT-50 and 1T-AT-50 datasets contain 50 % (randomly selected) of the data of 2T-AT and 1T-AT respectively. This leads to smaller datasets for the absent target speaker conditions.

|  | # utterances (tr / cv) |
|----------|:-----------------------------:|
| 2T-AT-50    | 20,000 / 5,000 |
| 1T-AT-50    | 20,000 / 5,000 |

We randomly removed 15 % of both 2T-PT and 1T-PT datasets and used those portions to create their counterparts with absent target speakers. This created datasets in which the input mixtures for the present and absent target speaker conditions are different. This tends to reduce the model confusion during the training stage.  

|  | # utterances (tr / cv) |
|----------|:-----------------------------:|
| 2T-PT-85    | 34,000 / 8,500 |
| 1T-PT-85    | 34,000 / 8,500 |
| 2T-AT-15    |  6,000 / 1,500 |
| 1T-AT-15    |  6,000 / 1,500 |


## Database simulation

Please perform the following steps to recreate our database:

1. Get access to the Wall Street Journal corpus (WSJ0) [3] with an appropriate license. Convert the corpus to the .wav format (remove all files with .wv2 extension and rename the remaining .wv1 files to .wav).
2. Use the original Matlab scripts [4] to create the WSJ0-2mix database [2] as "min" version with "8 kHz" sampling frequency. This provides the input mixtures as well as ground truth signals (PT conditions) for the speaker extraction.
3. Create 8 kHz resampled versions of the WSJ0 .wav files in the folders "si_dt_05", "si_et_05", and "si_tr_s". Those files will be used as reference signals for the target speakers and need to match the sampling frequency of the WSJ0-2mix database. For this, you can use the resample() method from the aforementioned Matlab scripts and wrap it into a new script. Make sure that the resampled audio files have the same properties as the audio files in the WSJ0-2mix database.
3. Create a new empty folder ("wsj0-2mix_silent_ref") for the silent audio files (ground truth for the absent target speaker conditions). You will create the silent audio files in step 5.
4. Change the PATHS in ALL data lists (.txt files in "/src/data/data_lists/*") according to your folder structure.
5. Run the "/src/data/create_silent_refs.py" script. This will create the silent ground truth (ref) files for the absent target speaker conditions (.wav audio files; 8 kHz sampling frequency). Provide the path to the previously created wsj0-2mix_silent_ref folder as argument ("python create_silent_refs.py --output /PATH/wsj0-2mix_silent_ref/"). The script will create the respective subfolders.
6. Use the "/src/data/concatenate_data_lists.py" script in order to concatenate the desired data lists. The script can concatenate two lists at a time.

The keys in the data lists contain a pre-identifier for each condition:

| Condition | Pre-identifier |
|----------|:-----------------------------:|
| 2T-PT    | s0c1r0n0 |
| 1T-PT    | s1c1r0n0 |
| 2T-AT    | s0c1r0n0ne |
| 1T-AT    | s1c1r0n0ne |


## If you enjoyed working with this Universal Speaker Extraction approach, please cite us:  

```@inproceedings{borsdorf21_interspeech,
  author={Marvin Borsdorf and Chenglin Xu and Haizhou Li and Tanja Schultz},
  title={{Universal Speaker Extraction in the Presence and Absence of Target Speakers for Speech of One and Two Talkers}},
  year=2021,
  booktitle={Proc. Interspeech 2021},
  pages={1469--1473},
  doi={10.21437/Interspeech.2021-1939}
}
```

## References

[1] https://github.com/xuchenglin28/speaker_extraction  
[2] J. R. Hershey, Z. Chen, J. Le Roux, and S. Watanabe, "Deep Clustering: Discriminative Embeddings for Segmentation and Separation", IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP), DOI: 10.1109/ICASSP.2016.7471631, March 2016, pp. 31-35.  
[3] https://catalog.ldc.upenn.edu/LDC93S6A  
[4] Y. Isik, J. Le Roux, S. Watanabe Z. Chen, and J. R. Hershey, “Scripts to Create wsj0-2 Speaker Mixtures,” MERL Research. Retrieved June 2, 2020, from https://www.merl.com/demos/deep-clustering/create-speaker-mixtures.zip, [Online].

## Licenses

- The used mixing scripts to create the WSJ0-2mix database [2] are under the Apache 2.0 license, see [4].  
- You can get access to the Wall Street Journal corpus (WSJ0) [3] by purchasing an appropriate license.  
- The python scripts in this repository are under a MIT license.  
- If you use the WSJ0-2mix-extr database, please check the license information in [1].

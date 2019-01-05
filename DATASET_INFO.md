# DATASET INFORMATION

An attempt has been made to enunciate shlokas through Tacotron

### DATASET

The dataset used for this consists of shlokas from the *Bhagvad Gita*. The *Bhagvad Gita* consists of 700 sholokas. The number of shlokas that follow the *anushthup* fomat are 646. Each shloka consists of two lines and has been further split into half (one line) for better training.

The characters in [symbols.py](text/symbols.py) are the ones specified in [UTF-8](https://www.utf8-chartable.de/unicode-utf8-table.pl?start=2304&number=128). All *purna virams (single danda and double danda)* has been removed from the training set shloka. Hence the test shlokas should also not consist of them.

The total number of shloka for training is 1290, which is about 2 and a half hours of audio.

### TRAINING ATTEMPTS

1. Initially the training was done after transliteration of the shlokas into roman script. After 200k iterations, almost 50% of the test shloka was audible.
Set the cleaner in hparams to `transliteration_cleaners`.

2. The second attempt was made by using the shlokas in the Devnagri script. Set the cleaner in hparams to `basic_cleaners`.

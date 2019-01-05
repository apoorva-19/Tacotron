# Tacotron

An implementation of Tacotron speech synthesis for Sanskrit Shloka

### Audio Sample

The [audio samples](https://github.com/apoorva-19/Anushthup) used to train this model are Sanskrit shlokas that follow the *anushthup* format.
	
## Quick Start

### Install Dependencies

1. Install Python 3. Tensorflow as of 5th January, 2019 supports only upto Python3.6.

2. Install the latest version of [TensorFlow](https://www.tensorflow.org/install/) for your platform. For better performance, install with GPU support if it's available. This code works with TensorFlow 1.3 and later.

3. Install requirements:
	 ```
   pip install -r requirements.txt
   ```

### Training

*Note: You need at least 30GB of free disk space to train a model.*

1. **Download the dataset**
	 * [Anushthup](https://github.com/apoorva-19/Anushthup) 

2. **Unpack the dataset into `~/tacotron`**
After unpacking, your tree should look like this:
   ```
   tacotron
     |- Shravya_data
         |- metadata.csv
         |- audio
   ```
3. **Preprocess the data**
   ```
   python3 preprocess.py --dataset shravya
   ```
   		* Use `--dataset blizzard` for Blizzard data and `--dataset ljspeech` for LJ Speech data
   		
4. **Train a model**
   ```
   python3 train.py
   ```

   Tunable hyperparameters are found in [hparams.py](hparams.py). You can adjust these at the command line using the `--hparams` flag, for example `-hparams="batch_size=16,outputs_per_step=2"`. Hyperparameters should generally be set to the same values at both training and eval time. See [DATASET_INFO.md](DATASET_INFO.md)
   
5. **Monitor with Tensorboard** (optional)
   ```
   tensorboard --logdir ~/tacotron/logs-tacotron
   ```

   The trainer dumps audio and alignments every 1000 steps. You can find these in
   `~/tacotron/logs-tacotron`.

6. **Synthesize from a checkpoint**
   ```
   python3 demo_server.py --checkpoint ~/tacotron/logs-tacotron/model.ckpt-185000
   ```
   Replace "185000" with the checkpoint number that you want to use, then open a browser
   to `localhost:9000` and type what you want to speak. Alternately, you can
   run [eval.py](eval.py) at the command line:
   ```
   python3 eval.py --checkpoint ~/tacotron/logs-tacotron/model.ckpt-185000
   ```
   If you set the `--hparams` flag when training, set the same value here.
   
## Acknowledgements

The basic structure for the model has been inspired form the model made by Keith Ito: https://github.com/keithito/tacotron

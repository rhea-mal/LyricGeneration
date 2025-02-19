# See demo video!! 
https://drive.google.com/file/d/15MBqnywTcsLUESPE3Lzdo30UwexcBI27/view?ts=65f3dfdb
![demo](https://github.com/rhea-mal/LyricGeneration/assets/70975260/44cfb7b0-4d70-41fa-8afd-3513f7948f1e)

# Lyricade

Welcome to the Lyricade repository! Lyricade is an innovative lyric generation tool that integrates detailed acoustic characteristics with lyrical creativity, powered by machine learning. Our model employs instrumental tracks and contextual cues, fine-tuning on a diverse dataset to produce lyrics that resonate with the musical essence and style of any specified artist.

## Repository Structure

This repository is organized into several key directories, each containing essential components of Lyricade:

- **Acoustics/**: Contains Jupyter notebooks for feature extraction using the Librosa library. These notebooks detail our methodology for analyzing audio tracks and extracting meaningful acoustic features that contribute to the lyric generation process.

- **Src/**: This directory holds the source code for training and testing our model. It includes Python scripts for setting up the model, training on our dataset, and evaluating its performance.

- **Datasets/**: Here, you will find cleaned and compiled CSV files that make up our dataset. These files include lyrics, artist names, song titles, and extracted acoustic features.

### Getting Started

To begin using Lyricade, clone this repository to your local machine:

```bash
git clone https://github.com/rhea-mal/Lyricade.git
```

### Prerequisites

Before running the notebooks or scripts, ensure you have the following dependencies installed:

- Python 3.8+
- Librosa
- PyTorch
- Transformers by Hugging Face
- Pandas
- NumPy

You can install these dependencies via pip:

```bash
pip install librosa torch transformers pandas numpy
```

### Using the Feature Extraction Notebooks

Navigate to the `Acoustics/` directory and open the Jupyter notebooks in your preferred environment. These notebooks will guide you through the process of extracting acoustic features from audio files using Librosa.

### Training and Testing the Model

To train the most advanced model, navigate to the `Src_final/` directory and run the training notebook.

To train the basic model, navigate to the `Src/` directory and run the training script:

```bash
python train.py
```

After training, you can test the model's performance on unseen data:

```bash
python test.py
```

### Dataset

The `Datasets/` directory contains the data used for training and testing Lyricade. This includes pre-processed and cleaned data, ready for machine learning applications.

The lyrics dataframe is constructed by merging and normalizing data across various datasets, including Genius Song Lyrics with Language Information{https://www.kaggle.com/datasets/carlosgdcj/genius-song-lyrics-with-language-information}, Song Lyrics Dataset{https://www.kaggle.com/datasets/deepshah16/song-lyrics-dataset}, and Lyrics Generation Dataset{https://www.kaggle.com/datasets/pratiksaha198/lyrics-generation?select=LYRICS_DATASET.csv}.
    We used another Kaggle Exploring Spotify {https://www.kaggle.com/code/alankarmahajan/exploring-spotify-dataset} features dataset with pre-extracted acoustic features resulting in a combined dataset of 1153 rows and 22 columns containing song metadata, acoustic features, and lyrics.

## Contributing

We welcome contributions to Lyricade! If you have suggestions for improvements or new features, please feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Thank you for exploring Lyricade. We hope this tool inspires you to create beautiful, musically-aligned lyrics using the power of machine learning.

# Image compression with the SVD

Our MATH 344L image compression project. We use the SVD to approximate grayscale images, then check how much storage we save and how the images look at different ranks.

## Notebooks

1. [Images as matrices](notebooks/01%20image%20as%20matrix.ipynb): pixel values, color channels, overflow, matrix rank, and six practice exercises.
2. [SVD and rank-k approximation](notebooks/02_svd_approximation.ipynb): reconstruction, singular values, error checks, and compression of the bird photo.
3. [Measuring compression](notebooks/03_measuring_compression.ipynb): storage counts, relative error, camera/text/photo comparisons, clipping, and six practice exercises.

Each notebook includes saved outputs and short explanations. The shared functions are in [src/compress.py](src/compress.py), and the saved plots are in [figures/](figures/).

## Run the project

Open a notebook in Google Colab and choose **Runtime > Restart session and run all**. The first code cell downloads this repository when needed, including the shared bird photo and helper functions.

To run locally, install Python and the dependencies:

```sh
python -m pip install -r requirements.txt
python -m jupyterlab
```

Open a notebook from `notebooks/` and restart its kernel before running all cells. Each notebook loads its own inputs, so they do not need to share a session.

The compression ratios count SVD factor entries. Milestone 3 also compares bytes for uint8 pixels versus float64 factors; neither measurement represents the size of an actual JPEG file.

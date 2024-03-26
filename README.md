Github paper implementation: https://github.com/hkchengrex/XMem
Paper: https://arxiv.org/pdf/2207.07115v2.pdf

# 1. How to perform inference on a new video with a segmentation mask for the first frame.

To perform the object segmentation follow the step by step shown below.

## Step 1: Open XMem.ipynb in Google Colab
This notebook is an adaptation of the demo notebook provided by the authors of the Xmem paper (available in their repository https://github.com/hkchengrex/XMem). It should be oppened in a session with a GPU for proper execution.

## Step 2: Prepare input
The code in the notebook is expecting 2 files the must be placed in the root folder of the cloned repository in colab (**/content/XMem**), this two files are the following:

1. mp4 video with the object to be segmented
2. ground truth segmentation mask for the first frame

The name pattern for using the function that will create the outputs should be the following:

1. **{name}.mp4** for the video sequence
2. **{name}-001.png** for the segmentation mask of the first frame

To make easier to run in the examples sequences, just unzip the **input.zip** file in the **/content/XMem** directory.

## Step 4: Running the necessary configurations
Run all the cells of the notebook until the definition of the function ```generate_overlay_video``` in the section **"Propagate frame-by-frame"**.

The cells runned correspond to things like cloning the repository of the code implementation, installing dependencies, downloading the pre-trained model and doing the masic configurations to perform the inference.

## Step 3: Call the function to generate the output video with the mask overlay

Just call the ```generate_overlay_video``` function like this:
```python
output_video_path = generate_overlay_video(f'{name}-001.png', f'{name}.mp4')
```

## Step 4: Outputs
The function called in the previous step creates both an mp4 video with an overlay of the mask in the original video, and also the masks for each frame.

The results are stored in the folder **/content/XMem/results/{name}** automatically created, following the following name patterns:

1. **out-{name}.mp4** for the video sequence
2. **out-{name}-001.png** for the segmentation mask of the first frame

The results can be downloaded individually or zipped using the terminal on colab.

# 2. How to compute metrics over the output videos.

## Step 1: Open project.ipynb in a jupyter notebook
This notebook notebook is used to evaluate the performance of the presented method in comparison to other methods such as Fanerback.

## Step 2: Set up the 'Configuration' cell
In this cell we define the path to directories containing images, ground truth masks and predictions as follows:
```
METHODS = {
    "Farneback" : "farneback/results",
    "XMEM" : "XMEM/results",
}

TRAIN_DIR = "sequences-train/"

TRAIN_SEQ = {
    "bag": (1, 196),
    "bear": (1, 26),
    "book": (1, 51),
    "camel": (1, 90),
    "rhino": (1, 90),
    "swan": (1, 26)
}
```
`METHODS`: Paths to methods results
`TRAIN_DIR`: Paths to input sequences and masks
`TRAIN_SEQ`: Dictionary of output sequences names, start and end frames indexes.

## Step 3: Run 'Results Visualization ' cells
This section of the notebook is in charge of computing metrics (dice, f-meausure, centroid distance) over the predicted sequences segmentations of the different methods defined above. Plots will be showed and metrics matrix will be saved in the same folders as methods results.
```
plot_results(methods_dict=METHODS, seq_dict=TRAIN_SEQ, gt_dir=TRAIN_DIR)
```

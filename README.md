Github paper implementation: https://github.com/hkchengrex/XMem
Paper: https://arxiv.org/pdf/2207.07115v2.pdf

# 1. How to perform inference on a new video with a segmentation mask for the first frame.

Follow the se 

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
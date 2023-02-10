# EOAD (Egocentric Outdoor Activity Dataset)

![alt text](https://github.com/maliarabaci/eoad/blob/main/eoad_layout.png?raw=true)

* [Video download] Due to Policy constraints we are not able to directly provide and host videos. However, we thank Tarun Kalluri who is also working on the dataset and willing to share his pre-processed videos that match baseline performances: Google Drive Link. You can use our provided video2frames.py script to split videos into frames. 

* UVO v1.0 contains:

   * Sparse Annotation (UVO-Sparse 1.0): 

   * Compare to v0.5, we add the downsampled version of dense annotations of v1.0. The downsampled dense split contains two classes: "object" for COCO categories and "other" for non-COCO categories, which can be used to test generalization ability.

   * 5641 videos for training (5138 sparsely annotated at 1fps, 503 from video-dense) 

   * 2708 videos for validation (2452 sparsely annotated at 1fps, 256 from video-dense)

   * 2879 (2623 sparsely annotated, 256 from video-dense) videos for test, used for Challenge

   * Interpolation for 30fps is provided (for sparsely annotated splits)

   * Dense Annotation (UVO-Dense): 503 videos for training and 256 videos for validation, annotated at 30fps

   * 258 videos for test, used for Challenge (video meta data to be released)

   * COCO taxonomy labels for all objects (marked as "other" if not in COCO categories)

* For instructions and baselines on the dataset, we refer to README.md in the shared folder.

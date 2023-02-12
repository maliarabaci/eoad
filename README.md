# EOAD (Egocentric Outdoor Activity Dataset)

![alt text](https://github.com/maliarabaci/eoad/blob/main/eoad_layout.png?raw=true)

On the other hand, previous tests demonstrated that incorporating audio information improves activity recognition performance. Therefore, we also decided to choose datasets with natural audio in addition to visual information.

After eliminating datasets based on the definition of activities and the selected modality types, we realized that only two of them (HUJI \cite{poleg2014temporal,poleg2016compact} and FPVSum \cite{ho2018summarizing}) met the criteria. However, the number of samples and diversity of activities for HUJI sand FPVSum were insufficient. Thus, we merged these datasets and also populated them with new YouTube videos.

The selection of YouTube videos was performed according to several criteria. Firstly, videos with overlayed text were not accepted. Secondly, we especially selected unstabilized video footage to get raw ego-motion characteristics that give clues about egocentric activities. Moreover, the videos should have natural sound (having no audio montage). Additionally, the videos should be continuous without a scene cut or jump in time. Video samples were trimmed depending on scene changes for long videos (such as *driving*, *scuba\ diving*, and *cycling}). The final dataset consists of video clips, including single actions for each video clip and having natural audio information.

The resulting statistics after selecting the video clips are given below:

* **HUJI**: 49 distinct videos - 148 video clips for 9 activities (*driving*, *biking*, *motorcycle*, *walking*, *boxing*, *horse riding*, *running*, *skiing*, *stair climbing*)
* **FPVSum**: 39 distinct videos - 124 video segments for 8 activities (*biking*, *horse riding*, *skiing*, *longboarding*, *rock climbing*, *scuba*, *skateboarding*, *surfing*)
* **YouTube**: 216 distinct videos - 1120 video clips for 27 activities (*american football*, *basketball*, *bungee jumping*, *driving*, *go-kart*, *horse riding*, *ice hockey*, *jet ski*, *kayaking*, *kitesurfing*, *longboarding*, *motorcycle*, *paintball*, *paragliding*, *rafting*, *rock climbing*, *rowing*, *running*, *sailing*, *scuba diving*, *skateboarding*, *soccer*, *stair climbing*, *surfing*, *tennis*, *volleyball*, *walking*)

Table \ref{table:eoad_detailed} provides a comprehensive listing of the overall number of videos and clips for each activity, as well as the total duration of videos. Multiple video clips depicting egocentric activities may be included in a video. Therefore, video clips were gathered from manually designated time intervals in videos, and each video clip contains only a single activity. As a result, we did not use any video segmentation technique to localize activities in time. 


**EOAD activity videos summary**

| | **Actions** | **Total Videos** | **Total Clips** | **Total Duration (hh:mm:ss)** | 
| --- | --- | --- | --- | --- |
| | American Football | 11 | 79 | 00:12:31 |
| | Basketball | 8 | 72 | 01:50:20 |
| | Biking | 12 | 26 | 03:06:39 |
| | Boxing | 15 | 23 | 00:56:38 |
| | Bungee Jumping | 13 | 15 | 00:05:29 |
| | Driving | 8 | 37 | 01:31:32 |
| | GoKart | 8 | 11 | 01:11:32 |
| | Horse Riding | 10 | 12 | 02:38:19 |
| | Ice Hockey | 8 | 108 | 01:16:55 |
| | Jetski | 8 | 15 | 00:45:00 |
| | Kayaking | 10 | 54 | 01:08:39 |
| | Kitesurfing | 8 | 53 | 00:29:01 | 
| | Longboarding | 10 | 13 | 00:42:54 | 
| | Motorcycle | 12 | 49 | 01:24:01 |
| | Paintball | 15 | 15 | 00:54:52 |
| | Paragliding | 17 | 19 | 00:58:48 | 
| | Rafting | 10 | 10 | 00:29:21 |
| | Rock Climbing | 10 | 10 | 01:30:27 |
| | Rowing | 11 | 11 | 01:03:52 |
| | Running | 9 | 51 | 02:51:24 |
| | Sailing | 10 | 17 | 01:09:52 |
| | Scuba Diving | 10 | 10 | 01:17:37 |
| | Skateboarding | 9 | 131 | 00:24:58 |
| | Skiing | 11 | 38 | 03:29:29 |
| | Soccer | 13 | 170 | 01:08:50 
| | Stair Climbing | 12 | 17 | 01:43:12 |
| | Surfing | 10 | 50 | 00:26:47 |
| | Tennis | 9 | 52 | 00:36:21 |
| | Volleyball | 9 | 129 | 00:45:58 |
| | Walking | 8 | 95 | 01:31:51 |
| **Total** | **30** | **314** | **1392** | **37:43:08** |			

The video clips used for training, validation and test sets for each activity are listed in Table \ref{table:dataset_split}. As mentioned before, multiple video clips may belong to a video because of trimming it for some reasons (i.e., scene cut, temporary overlayed text on videos, or video parts unrelated to activities). In addition, we know that each video clips contain single activity. Therefore, we did not apply any video segmentation method to localize activities.

The minimum number of videos for each activity was selected as 8, and the video samples in the experimental setup were divided as 50\%, 25\%, and 25\% for training (4 videos), validation (2 videos), and test (2 videos), respectively. On the other hand,  videos were split according to the raw video footage to prevent the mixing of similar video clips (having the same actors and scenes) into training, validation, and test sets simultaneously. Therefore, we ensured that the video clips trimmed from the same videos were split together into training, validation, or test sets to make a fair comparison. 

Some activities have continuity throughout the video, such as *scuba*, *longboarding*, or *riding horse} which also have an equal number of video segments with the number of videos. However, some activities, such as skating, occurred in a short time, making the number of video segments higher than the others. As a result, the number of video clips for training, validation, and test sets was highly imbalanced for activities (i.e., *jetski} and *rafting} have 4; however, *soccer} has 99 video clips for training). 

% Please add the following required packages to your document preamble:
**Dataset splitting for EOAD **

\multirow{2}{*}{ & \multicolumn{2}{c}{**Train}}                & \multicolumn{2}{c}{**Validation}}             & \multicolumn{2}{c}{**Test}}                    
				   & **#Segments** & **Total   Duration** & **Segments** & **Total   Duration** & **Segments** & **Total   Duration**
				   
| **Action Label** | **#Segments** | **Total   Duration** | **#Segments** | **Total   Duration** | **#Segments** | **Total   Duration** |
| --- | --- | --- | --- | --- | --- | --- |
| **AmericanFootball** | 34 | 00:06:09 | 36 | 00:05:03 | 9 | 00:01:20 |
| **Basketball** | 43 | 01:13:22 | 19 | 00:08:13 | 10 | 00:28:46 | 
| **Biking** | 9 | 01:58:01 | 6 | 00:32:22 | 11 | 00:36:16 | 
| **Boxing** | 7 | 00:24:54 | 11  | 00:14:14 | 5   | 00:17:30 |
| **BungeeJumping** | 7 | 00:02:22 | 4   | 00:01:36 | 4   | 00:01:31 |
| **Driving**   | 19 | 00:37:23 | 9   | 00:24:46 | 9   | 00:29:23 |                   
| **GoKart**    | 5 | 00:40:00 | 3   | 00:11:46 | 3   | 00:19:46 |                   
| **Horseback**    | 5 | 01:15:14 | 5   | 01:02:26 | 2   | 00:20:38 |  
| **IceHockey**    | 52   | 00:19:22 | 46  | 00:20:34 | 10  | 00:36:59 | 
| **Jetski**    | 4 | 00:23:35 | 5   | 00:18:42 | 6   | 00:02:43 | 
| **Kayaking**  | 28   | 00:43:11 | 22  | 00:14:23 | 4   | 00:11:05 | 
| **Kitesurfing**    | 30   | 00:21:51 | 17  | 00:05:38 | 6   | 00:01:32 | 
| **Longboarding** | 5 | 00:15:40 | 4   | 00:18:03 | 4   | 00:09:11 | 
| **Motorcycle**    | 20   | 00:49:38 | 21   | 00:13:53 | 8  | 00:20:30 | 
| **Paintball**    | 7 | 00:33:52 | 4   | 00:12:08 | 4   | 00:08:52 | 
| **Paragliding**    | 11   | 00:28:42 | 4   | 00:10:16 | 4   | 00:19:50 | 
| **Rafting**   | 4 | 00:15:41 | 3   | 00:07:27 | 3   | 00:06:13 | 
| **RockClimbing** | 6 | 00:49:38 | 2   | 00:21:59 | 2   | 00:18:50 | 
| **Rowing**    | 5 | 00:47:05 | 3   | 00:13:21 | 3   | 00:03:26 | 
| **Running**   | 21   | 01:21:56 | 19  | 00:46:29 | 11  | 00:42:59 | 
| **Sailing**   | 7 | 00:39:30 | 4   | 00:14:39 | 6   | 00:15:43 | 
| **Scuba**     | 5 | 00:35:02 | 3   | 00:23:43 | 2   | 00:18:52 | 
| **Skate**     | 91   | 00:15:53 | 30  | 00:07:01 | 10  | 00:02:03 | 
| **Ski**       | 14   | 01:48:15 | 17  | 01:01:59 | 7  | 00:39:15 | 
| **Soccer**    | 102   | 00:48:39 | 52  | 00:13:17 | 16  | 00:06:54 | 
| **StairClimbing**    | 6 | 01:05:32 | 6   | 00:17:18 | 5   | 00:20:22 |  
| **Surfing**   | 23   | 00:12:51 | 17  | 00:06:52 | 10  | 00:07:04 | 
| **Tennis**    | 34   | 00:27:04 | 9   | 00:06:03 | 9   | 00:03:14 |  
| **Volleyball**    | 87   | 00:19:14 | 35  | 00:07:46 | 7   | 00:18:58 |  
| **Walking**   | 49   | 00:43:02 | 36  | 00:38:25 | 10  | 00:10:23 | 



740 20:22:37  452  09:20:23  200 08:00:08                 

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

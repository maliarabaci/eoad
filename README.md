# EOAD (Egocentric Outdoor Activity Dataset)

![alt text](https://github.com/maliarabaci/eoad/blob/main/eoad_layout.png?raw=true)

EOAD is an egocentric activity video datasets mostly including sport activities taken with wearable cameras. It is composed of two modalities: video and audio.  

It was also supported with two other egocentric activity datasets: **[HUJI](https://www.vision.huji.ac.il/egoseg/videos/dataset.html)** and **[FPVSum](https://github.com/azuxmioy/fpvsum)**. However, the number of samples and diversity of activities for HUJI sand FPVSum were insufficient. Therefore, we merged these datasets and also populated with new YouTube videos.

* The selection of YouTube videos was performed according to several criteria listed below:
	* The video should not contain overlayed texts
	* The videos should have natural sound information (no external music)
	* The activities in video clips should be continuous (no cutting the scene or jump in time)

Video samples were trimmed depending on scene changes for long videos (such as *driving*, *scuba diving*, and *cycling*). As a result, multiple video clips depicting egocentric activities may be included in a video. Therefore, video clips were gathered from manually designated time intervals in videos. The final dataset consists of video clips, including single actions for each video clip and having natural audio information.

* Overall data statistics for EOAD:
	* **30** activities
	* **303** distinct videos
	* **1392** video clips
	* **2243** minutes labelled videos clips
	
The detailed statistics for the selected datasets and the crawled videos clips from YouTube are given below:

* **[HUJI](https://www.vision.huji.ac.il/egoseg/videos/dataset.html)**: 49 distinct videos - 148 video clips for 9 activities (*driving*, *biking*, *motorcycle*, *walking*, *boxing*, *horse riding*, *running*, *skiing*, *stair climbing*)
* **[FPVSum](https://github.com/azuxmioy/fpvsum)**: 39 distinct videos - 124 video segments for 8 activities (*biking*, *horse riding*, *skiing*, *longboarding*, *rock climbing*, *scuba*, *skateboarding*, *surfing*)
* **YouTube**: 216 distinct videos - 1120 video clips for 27 activities (*american football*, *basketball*, *bungee jumping*, *driving*, *go-kart*, *horse riding*, *ice hockey*, *jet ski*, *kayaking*, *kitesurfing*, *longboarding*, *motorcycle*, *paintball*, *paragliding*, *rafting*, *rock climbing*, *rowing*, *running*, *sailing*, *scuba diving*, *skateboarding*, *soccer*, *stair climbing*, *surfing*, *tennis*, *volleyball*, *walking*)

The video clips used for training, validation and test sets for each activity are listed in *Table 1*. Multiple video clips may belong to a single video because of trimming it for some reasons (i.e., scene cut, temporary overlayed text on videos, or video parts unrelated to activities). 

While splitting dataset, the minimum number of videos for each activity was selected as 8. Additionally, the video samples were divided as 50\%, 25\%, and 25\% for training (minimum 4 videos), validation (minimum 2 videos), and test (minimum 2 videos), respectively. On the other hand,  videos were split according to the raw video footage to prevent the mixing of similar video clips (having the same actors and scenes) into training, validation, and test sets. Therefore, we ensured that the video clips trimmed from the same videos were split together into training, validation, or test sets to satisfy a fair comparison. 

Some activities have continuity throughout the video, such as *scuba*, *longboarding*, or *riding horse* which also have an equal number of video segments with the number of videos. However, some activities, such as skating, occurred in a short time, making the number of video segments higher than the others. As a result, the number of video clips for training, validation, and test sets was highly imbalanced for the selected activities (i.e., *jetski* and *rafting* have 4; however, *soccer* has 99 video clips for training). 

<p align="center"> <strong> Table 1 - Dataset splitting for EOAD </strong> </p>

| | |**Train** ||**Validation** ||**Test** ||
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| | **Action Label** | **#Clips** | **Total   Duration** | **#Clips** | **Total   Duration** | **#Clips** | **Total   Duration** |
| | **AmericanFootball** | 34 | 00:06:09 | 36 | 00:05:03 | 9 | 00:01:20 |
| | **Basketball** | 43 | 01:13:22 | 19 | 00:08:13 | 10 | 00:28:46 | 
| | **Biking** | 9 | 01:58:01 | 6 | 00:32:22 | 11 | 00:36:16 | 
| | **Boxing** | 7 | 00:24:54 | 11  | 00:14:14 | 5   | 00:17:30 |
| | **BungeeJumping** | 7 | 00:02:22 | 4   | 00:01:36 | 4   | 00:01:31 |
| | **Driving**   | 19 | 00:37:23 | 9   | 00:24:46 | 9   | 00:29:23 |                   
| | **GoKart**    | 5 | 00:40:00 | 3   | 00:11:46 | 3   | 00:19:46 |                   
| | **Horseback**    | 5 | 01:15:14 | 5   | 01:02:26 | 2   | 00:20:38 |  
| | **IceHockey**    | 52   | 00:19:22 | 46  | 00:20:34 | 10  | 00:36:59 | 
| | **Jetski**    | 4 | 00:23:35 | 5   | 00:18:42 | 6   | 00:02:43 | 
| | **Kayaking**  | 28   | 00:43:11 | 22  | 00:14:23 | 4   | 00:11:05 | 
| | **Kitesurfing**    | 30   | 00:21:51 | 17  | 00:05:38 | 6   | 00:01:32 | 
| | **Longboarding** | 5 | 00:15:40 | 4   | 00:18:03 | 4   | 00:09:11 | 
| | **Motorcycle**    | 20   | 00:49:38 | 21   | 00:13:53 | 8  | 00:20:30 | 
| | **Paintball**    | 7 | 00:33:52 | 4   | 00:12:08 | 4   | 00:08:52 | 
| | **Paragliding**    | 11   | 00:28:42 | 4   | 00:10:16 | 4   | 00:19:50 | 
| | **Rafting**   | 4 | 00:15:41 | 3   | 00:07:27 | 3   | 00:06:13 | 
| | **RockClimbing** | 6 | 00:49:38 | 2   | 00:21:59 | 2   | 00:18:50 | 
| | **Rowing**    | 5 | 00:47:05 | 3   | 00:13:21 | 3   | 00:03:26 | 
| | **Running**   | 21   | 01:21:56 | 19  | 00:46:29 | 11  | 00:42:59 | 
| | **Sailing**   | 7 | 00:39:30 | 4   | 00:14:39 | 6   | 00:15:43 | 
| | **Scuba**     | 5 | 00:35:02 | 3   | 00:23:43 | 2   | 00:18:52 | 
| | **Skate**     | 91   | 00:15:53 | 30  | 00:07:01 | 10  | 00:02:03 | 
| | **Ski**       | 14   | 01:48:15 | 17  | 01:01:59 | 7  | 00:39:15 | 
| | **Soccer**    | 102   | 00:48:39 | 52  | 00:13:17 | 16  | 00:06:54 | 
| | **StairClimbing**    | 6 | 01:05:32 | 6   | 00:17:18 | 5   | 00:20:22 |  
| | **Surfing**   | 23   | 00:12:51 | 17  | 00:06:52 | 10  | 00:07:04 | 
| | **Tennis**    | 34   | 00:27:04 | 9   | 00:06:03 | 9   | 00:03:14 |  
| | **Volleyball**    | 87   | 00:19:14 | 35  | 00:07:46 | 7   | 00:18:58 |  
| | **Walking**   | 49   | 00:43:02 | 36  | 00:38:25 | 10  | 00:10:23 | 
| **Total** | 30 | 740 |  20:22:37 | 452 | 09:20:23 | 200 | 08:00:08 |

**How to get the videos**
* Prerequisites
	* pytube
	* ffmpeg-python

* [Video download] Due to Policy constraints we are not able to directly provide and host videos. However, we thank Tarun Kalluri who is also working on the dataset and willing to share his pre-processed videos that match baseline performances: Google Drive Link. You can use our provided video2frames.py script to split videos into frames. 

** References **
Zenodo DOI

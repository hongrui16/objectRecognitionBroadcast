## 启动流程说明



## 开语音播报
1. 	下载sdk到您的目录$(WD)
	git clone https://github.com/hongrui16/xf-ros.git -dh-dp

2. 	编译:catkin_make,source，启动：rosrun xfei_asr  tts_subscribe_speak

## 打开翻译
	cd $(WD)/objectRecognitionBroadcast/translate-broadcast;python translate_bd_ROS.py


## 打开物体识别
	cd $(WD)/objectRecognitionBroadcast/objectRecognition;python image_recognition.py image:=/camera/rgb/image_color


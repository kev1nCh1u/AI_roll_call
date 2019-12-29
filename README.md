# 他們回來了

## face
```
cd /home/user/AI_roll_call/src
```
```
python ./face_recognition_demo.py -m_fd ~/Desktop/openvino/deployment_tools/tools/model_downloader/intel/face-detection-retail-0004/FP16/face-detection-retail-0004.xml -m_lm ~/Desktop/openvino/deployment_tools/tools/model_downloader/intel/landmarks-regression-retail-0009/FP16/landmarks-regression-retail-0009.xml -m_reid ~/Desktop/openvino/deployment_tools/tools/model_downloader/intel/face-reidentification-retail-0095/FP16/face-reidentification-retail-0095.xml -l /home/user/Desktop/openvino/deployment_tools/inference_engine/lib/intel64/libcpu_extension_sse4.so --verbose -fg "/home/user/AI_roll_call/image/face_cut" --run_detector --allow_grow
```
```
python ./face_recognition_demo.py -m_fd ~/Desktop/openvino/deployment_tools/tools/model_downloader/intel/face-detection-retail-0004/FP16/face-detection-retail-0004.xml -m_lm ~/Desktop/openvino/deployment_tools/tools/model_downloader/intel/landmarks-regression-retail-0009/FP16/landmarks-regression-retail-0009.xml -m_reid ~/Desktop/openvino/deployment_tools/tools/model_downloader/intel/face-reidentification-retail-0095/FP16/face-reidentification-retail-0095.xml -l /home/user/Desktop/openvino/deployment_tools/inference_engine/lib/intel64/libcpu_extension_sse4.so --verbose -fg  "/home/user/AI_roll_call/image/face_gallery"
```
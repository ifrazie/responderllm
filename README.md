```
git clone <this repo>
cd responderllm
```

### Make and activate virtual environment (Optional)

**Mac & Linux**
```
python3 -m venv venv 
source venv/bin/activate
```

**Windows**
```
python3 -m venv venv 
.\venv\Scripts\activate.bat
```


### Install dependencies

```
python3 -m pip install -r requirements.txt
```

## Streaming Pipeline
To launch the streaming pipeline on its own, you can run the main.py directly and provide the necessary arguments:

```
usage: main.py [-h] --model_url MODEL_URL --video_file VIDEO_FILE --api_key API_KEY [--port PORT] [--websocket_port WEBSOCKET_PORT] [--overlay] [--loop_video] [--hide_query]

Streaming pipeline for VLM alerts.

options:
  -h, --help            show this help message and exit
  --model_url MODEL_URL
                        URL to VLM NIM
  --video_file VIDEO_FILE
                        Local path to input video file or RTSP stream
  --api_key API_KEY     NIM API Key
  --port PORT           Flask port
  --websocket_port WEBSOCKET_PORT
                        WebSocket server port
  --overlay             Enable VLM overlay window
  --loop_video          Continuosly loop the video
  --hide_query          Hide query output from overlay to only show alert output
```

For example 

```
python3 main.py --model https://ai.api.nvidia.com/v1/vlm/nvidia/neva-22b --video_file test_video.mp4 --api_key "nvapi-123" --overlay --loop_video
```

All VLM nims are supported. The following list can be used in the --model_url argument of main.py 

- https://ai.api.nvidia.com/v1/gr/meta/llama-3.2-90b-vision-instruct
- https://ai.api.nvidia.com/v1/gr/meta/llama-3.2-11b-vision-instruct
- https://ai.api.nvidia.com/v1/vlm/nvidia/vila
- https://ai.api.nvidia.com/v1/vlm/nvidia/neva-22b
- https://ai.api.nvidia.com/v1/vlm/microsoft/kosmos-2
- https://ai.api.nvidia.com/v1/vlm/adept/fuyu-8b
- https://ai.api.nvidia.com/v1/vlm/google/paligemma
- https://ai.api.nvidia.com/v1/vlm/microsoft/phi-3-vision-128k-instruct


Your api key should come from [build.nvidia.com](http://build.nvidia.com) 

Once it is launched, you should see a window pop up with the video playing and the REST API endpoint should be live to send prompt updates.


er notebook cells or by running one of the client programs 

- client_cli.py
- client_gradio.py  

```
python3 client_gradio.py
```

![Gradio Client](readme_assets/gradio_client_example.png)


```
python3 client_cli.py
```

![CLI Client](readme_assets/cli_client_example.png)

Both client programs will allow you to send queries and alerts to the running streaming pipeline. 

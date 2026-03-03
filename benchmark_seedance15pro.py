import sys
import os
import time
import torch

# Mock comfy_api and folder_paths
class MockFolderPaths:
    def get_temp_directory(self):
        return "/tmp"

sys.modules['folder_paths'] = MockFolderPaths()

class MockInputImpl:
    pass
class MockComfyAPI:
    InputImpl = MockInputImpl
sys.modules['comfy_api'] = type('MockModule', (), {'latest': MockComfyAPI()})()
sys.modules['comfy_api.latest'] = MockComfyAPI()

from kie_api.seedance15pro_i2v import _build_input_urls

class MockRequestsPost:
    def __init__(self, delay=1.0):
        self.delay = delay

    def __call__(self, *args, **kwargs):
        time.sleep(self.delay)
        class Response:
            status_code = 200
            def json(self):
                return {"success": True, "code": 200, "data": {"downloadUrl": "https://example.com/image.png"}}
        return Response()

def run_benchmark():
    # Mock requests.post
    import kie_api.upload
    kie_api.upload.requests.post = MockRequestsPost(delay=1.0)

    # Create dummy images (batch size 2)
    images = torch.zeros((2, 512, 512, 3), dtype=torch.uint8)

    print("Starting baseline benchmark...")
    start_time = time.time()
    urls = _build_input_urls("dummy_api_key", images, log=True)
    end_time = time.time()

    duration = end_time - start_time
    print(f"Benchmark finished in {duration:.4f} seconds.")
    print(f"Resulting URLs: {urls}")
    return duration

if __name__ == "__main__":
    run_benchmark()

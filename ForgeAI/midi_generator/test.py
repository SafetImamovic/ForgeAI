import vertexai
from vertexai.preview.generative_models import GenerativeModel, Image



PROJECT_ID = "PROJECT_ID"
REGION = "us-central1"
vertexai.init(project=PROJECT_ID, location=REGION)

IMAGE_FILE = "gs://generativeai-downloads/images/scones.jpg"
image = Image.load_from_file(IMAGE_FILE)

generative_multimodal_model = GenerativeModel("gemini-1.5-flash-001")
response = generative_multimodal_model.generate_content(["What is shown in this image?", image])

print(response)
import os
from google.cloud import storage

def generate_signed_url(blob_name, bucket_name, expiration=3600):
    current_file_path = os.path.abspath(__file__)
    
    parent_directory_path = os.path.dirname(current_file_path)

    key_path = os.path.join(parent_directory_path, "ServiceKey_GoogleCloud.json")
    
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_path
    
    storage_client = storage.Client()

    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)

    # Generate the signed URL
    signed_url = blob.generate_signed_url(
        version="v4",
        expiration=expiration,
        method="GET"
    )

    return signed_url

def upload_to_bucket(blob_name, file_path, bucket_name):
    current_file_path = os.path.abspath(__file__)
    
    parent_directory_path = os.path.dirname(current_file_path)

    key_path = os.path.join(parent_directory_path, "ServiceKey_GoogleCloud.json")
    
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_path
    
    storage_client = storage.Client()

    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        return True
    except Exception as e:
        print(f"Error uploading to bucket: {e}")
        return
    
def download_file_from_bucket(blob_name, file_path, bucket_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        with open(file_path, "wb") as f:
            storage_client.download_blob_to_file(blob, f)
        return True
    except Exception as e:
        print(f"Error downloading from bucket: {e}")
        return

# # Get the directory containing this Python file
# current_file_path = os.path.abspath(__file__)

# # Get the parent directory path
# parent_directory_path = os.path.dirname(current_file_path)

# key_path = os.path.join(parent_directory_path, "ServiceKey_GoogleCloud.json")

# if not os.path.exists(key_path):
#     print(f"Error: Service key file '{key_path}' not found.")
# else:
#     os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_path
#     try:
#         storage_client = storage.Client()
#         print("Storage client initialized successfully.")
        
#         bucket = storage_client.bucket("midi-files-forge-ai")
        
#         file_path = "C:\\Users\\Safet\\Documents\\GitHub\\ForgeAI\\ForgeAI\\2f23e752-75b9-4b15-aede-ead81b309704.mid"
#         #upload_to_bucket("2f23e752-75b9-4b15-aede-ead81b309704.mid", file_path, "midi-files-forge-ai")
        
#         print(generate_signed_url("midi-files-forge-ai", "2f23e752-75b9-4b15-aede-ead81b309704.mid"))
        
#     except Exception as e:
#         print(f"Error initializing storage client: {e}")
        



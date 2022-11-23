from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv(".env")

def upload_image(file_folder_path: str, file_name: str) -> None:
    
    # Load environment variables
    connection_string = os.getenv("AZURE_CONNECTION_STRING")
    container_name = os.getenv("STORAGE_CONTAINER")

    # Raise an error if the environment variables are not found
    if not connection_string or not container_name:
        raise ValueError("Missing environment variables... Please check your .env file")

    # Join the file path and name to get the full file path
    file_path = os.path.join(file_folder_path, file_name)

    # Initialize the connection to Azure
    blob_service_client =  BlobServiceClient.from_connection_string(connection_string)
    
    # Create blob (file) with same name as local file name
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
    
    print(f"uploading file: {file_path}")
    
    # Open local file
    with open(file_path, "rb") as file:
      # Write local file to blob overwriting any existing data
      blob_client.upload_blob(file, overwrite=True)

    print("file uploaded!")

    return

if __name__ == "__main__":
    upload_image("./data", "test.json")
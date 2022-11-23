from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv(".env")


def download_image(local_file_desired_path: str, blob_name: str) -> str:
    """
    Download a blob (file) from an Azure Storage container and save it to a local file.

    :param local_file_desired_path: The path to the local file to save the blob to.
    :param blob_name: The name of the blob (file) to download.
    :return: The path to the local file.
    """

    # Load environment variables
    connection_string = os.getenv("AZURE_CONNECTION_STRING")
    container_name = os.getenv("STORAGE_CONTAINER")

    # Raise an error if the environment variables are not found
    if not connection_string or not container_name:
        raise ValueError("Missing environment variables... Please check your .env file")


    # Initialize the connection to Azure
    blob_service_client =  BlobServiceClient.from_connection_string(connection_string)
    
    # Create blob (file) with same name as local file name
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    
    print(f"Reading remote file: {blob_name}")
    
    blob_data = blob_client.download_blob().read().decode("utf-8")

    print("data: ", blob_data)

    # Write data to local file
    with open(local_file_desired_path, "w") as file:
        file.write(blob_data)

    return local_file_desired_path

if __name__ == "__main__":
    file_path = download_image("./data/downloaded_file.json", "test.json")
    print(f"File downloaded to: {file_path}")
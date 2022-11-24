from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv(".env")


def delete_file(blob_name: str) -> None:
    """
    Delete a blob (file) from an Azure Storage container.

    :param blob_name: The name of the blob (file) to delete.
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
    
    print(f"Deleting remote file: {blob_name}...")
    
    # Delete the blob
    blob_client.delete_blob()
    print("File deleted!")

    return

if __name__ == "__main__":
    delete_file("test2.json")
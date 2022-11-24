# Using Azure blob storage in python

If you want to save files to the cloud, you can use Azure blob storage. This is a quick guide to get you started.

![Azure storage account](https://ms-azuretools.gallerycdn.vsassets.io/extensions/ms-azuretools/vscode-azurestorage/0.15.0/1663278668864/Microsoft.VisualStudio.Services.Icons.Default)

## What is Azure blob storage?

Azure blob storage is a service for storing large amounts of unstructured data. It is designed to be cheap and scalable. You can read more about it [here](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction).

## How to use it

### 1. Create a storage account

First, you need to create a storage account. 

*You can do this in the [Azure portal](https://portal.azure.com/). You can also do it using the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest).*


### 2. Create a container

Next, you need to create a container. This is where you will store your files. 

*You can do this in the [Azure portal](https://portal.azure.com/). You can also do it using the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest).*

### 3. Create a connection string

You need a connection string to connect to your storage account. You can also use a SAS token, but we will use connexion string here, it's easier to use.

*You can do this in the [Azure portal](https://portal.azure.com/). You can also do it using the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest).*

### 4. Store your secrets

You need to store your secrets in a secure place. To keep things simple, we will use a `.env` file. and load it using the [python-dotenv](https://pypi.org/project/python-dotenv/) package.

Create a `.env` file in the root of your project and add your secrets to it. It should look something like this:

```bash
AZURE_CONNECTION_STRING=DefaultEndpointsProtocol=https;AccountName=XXXXXXXXXX;AccountKey=XXXXXXXX;EndpointSuffix=core.windows.net
STORAGE_CONTAINER=XXXXXX
```


### 4. Install requirements

You need to install the Azure Storage SDK for Python. You can do this using pip:

```bash
pip3 install azure-storage-blob python-dotenv
```

### 5. Upload a file
To upload a file, you an use the code sample in [upload_file.py](./upload_file.py)

```bash
python3 upload_file.py
```

### 6. Download a file
To download a file, you an use the code sample in [download_file.py](./download_file.py)

```bash
python3 download_file.py
```


### 7. Delete a file
To delete a file, you an use the code sample in [delete_file.py](./delete_file.py)

```bash
python3 delete_file.py
```
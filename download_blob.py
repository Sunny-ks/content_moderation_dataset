from azure.storage.blob import BlobServiceClient

# Replace with your Azure Blob Storage account details
connection_string = "Your_Azure_Storage_Connection_String"
container_name = "your-container-name"
blob_name = "your-blob-name"
download_file_path = "path/to/save/the/downloaded/file"

try:
    # Create a BlobServiceClient using the connection string
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # Get a container client
    container_client = blob_service_client.get_container_client(container_name)

    # Get a blob client
    blob_client = container_client.get_blob_client(blob_name)

    # Download the blob to a local file
    with open(download_file_path, "wb") as file:
        download_stream = blob_client.download_blob()
        file.write(download_stream.readall())

    print(f"Blob '{blob_name}' downloaded successfully to '{download_file_path}'.")

except Exception as e:
    print(f"Error occurred: {e}")
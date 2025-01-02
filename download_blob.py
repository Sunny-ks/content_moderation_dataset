from azure.storage.blob import BlobServiceClient
import os

# Replace with your Azure Blob Storage account details
connection_string = "Your_Azure_Storage_Connection_String"
container_name = "your-container-name"
folder_name = "models"  # The simulated folder name in the blob storage
local_folder = "./models"  # Local folder to download the files

try:
    # Create a BlobServiceClient using the connection string
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # Get a container client
    container_client = blob_service_client.get_container_client(container_name)

    # Ensure the local folder exists
    os.makedirs(local_folder, exist_ok=True)

    # List blobs with the specified prefix (simulated folder)
    blobs = container_client.list_blobs(name_starts_with=folder_name + "/")

    for blob in blobs:
        # Get the blob client
        blob_client = container_client.get_blob_client(blob.name)

        # Determine the local path for the blob
        relative_path = blob.name[len(folder_name) + 1:]  # Remove the folder prefix
        local_file_path = os.path.join(local_folder, relative_path)

        # Ensure the local directory exists
        os.makedirs(os.path.dirname(local_file_path), exist_ok=True)

        # Download the blob
        with open(local_file_path, "wb") as file:
            download_stream = blob_client.download_blob()
            file.write(download_stream.readall())

        print(f"Downloaded: {blob.name} -> {local_file_path}")

except Exception as e:
    print(f"Error occurred: {e}")

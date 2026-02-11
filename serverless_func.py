from azure.storage.blob import BlobServiceClient
import pandas as pd
import io
import json
import os

connect_str = (
    "DefaultEndpointsProtocol=http;"
    "AccountName=devstoreaccount1;"
    "AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tSq/K1SZFPTOtr/KBHBeksoGMGw==;"
    "BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;" 
)

try:
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    print("Connected to Azurite")
    
    # List all containers
    containers = blob_service_client.list_containers()
    container_names = [container.name for container in containers]
    print(f"Found containers: {container_names}")
    
    # Check if container actually exists
    container_name = "datasets"
    if container_name in container_names:
        print(f"Container '{container_name}' found")
        
        container_client = blob_service_client.get_container_client(container_name)
        blob_client = container_client.get_blob_client('All_Diets.csv')
        
        # Check if blob actually exists
        if blob_client.exists():
            print("File 'All_Diets.csv' found")
          
            # Download blob content to bytes
            stream = blob_client.download_blob().readall()
            df = pd.read_csv(io.BytesIO(stream))
            print(f"CSV loaded. Shape: {df.shape}")
            
            # Calculate averages
            avg_macros = df.groupby('Diet_type')[['Protein(g)', 'Carbs(g)', 'Fat(g)']].mean()
            print("Averages calculated")
            
            # Save results locally as JSON (simulate NoSQL storage)
            result = avg_macros.reset_index().to_dict(orient='records')
            
            #  Create directory if it doesn't exist
            os.makedirs('simulated_nosql', exist_ok=True)
            
            output_path = 'simulated_nosql/results.json'
            with open(output_path, 'w') as f:
                json.dump(result, f, indent=2)
            
            print(f"Results saved to: {output_path}")
            print(f"Processed {len(result)} diet types:")
            
            # Print results
            for item in result:
                print(f"  Diet: {item['Diet_type']:15} "
                      f"Protein: {item['Protein(g)']:6.2f}g, "
                      f"Carbs: {item['Carbs(g)']:6.2f}g, "
                      f"Fat: {item['Fat(g)']:6.2f}g")
        else:
            print("File 'All_Diets.csv' not found in container")
            print("Please upload the file using Storage Explorer")
    else:
        print(f"Container '{container_name}' not found")
        print("Please create a container named 'datasets' in Storage Explorer")
        
except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()  # Shows full error details

import requests
import json

def upload_csv_to_splunk(splunk_url, splunk_username, splunk_password, app_name, csv_file_path):

url = f"{splunk_url}/servicesNS/nobody/{app_name}/data/lookup-table-files"

headers = { 
    "Authorization': f"Splunk {splunk_username}:{splunk_password}",
    "Content-Type": "application/x-www-form-urlencoded" 
}

with open(csv_file_path, 'rb' ) as file:
     files = {'file': file} 
     payload = { 
         'output_mode': 'json',
         'name': csv_file_path.split('/')[-1]
     }
     response = requests.post(url, headers=headers, files=files, data=payload) 

if response.status_code == 201:
  print("CSV file uploaded successfully.") 
else:
  print(f"Error uploading CSV file: {response.text}") 

if __name__ == "__main__": 
   splunk_url = "https://your-splunk-instance:8088"
   splunk_username = "splunk-username"
   splunk_password = "splunk-password"
   app_name = "your-splunk-app"
   csv_file_path = "path/to/csv/file.csv"

   upload_csv_to_splunk(splunk_url, splunk_username,splunk_password, app_name, csv_file_path)

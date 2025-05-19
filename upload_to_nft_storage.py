import requests

# Replace this with your actual JWT token
JWT_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiI3OGZhYjNlMS0zNzcyLTRkYTMtYjY4MS03ZTNiMDZhMmI3MzMiLCJlbWFpbCI6ImR2YWthc2htaXR1MjFAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInBpbl9wb2xpY3kiOnsicmVnaW9ucyI6W3siZGVzaXJlZFJlcGxpY2F0aW9uQ291bnQiOjEsImlkIjoiRlJBMSJ9LHsiZGVzaXJlZFJlcGxpY2F0aW9uQ291bnQiOjEsImlkIjoiTllDMSJ9XSwidmVyc2lvbiI6MX0sIm1mYV9lbmFibGVkIjpmYWxzZSwic3RhdHVzIjoiQUNUSVZFIn0sImF1dGhlbnRpY2F0aW9uVHlwZSI6InNjb3BlZEtleSIsInNjb3BlZEtleUtleSI6IjllZjc4ZjJhY2MyMWEzOTkzMjU0Iiwic2NvcGVkS2V5U2VjcmV0IjoiN2YyODVlNmJmOTRlMjI3MzNjNmM2ZDI0NmY2ZDU0MDZlZDEyOTEwZGIyNTAzZTFiMDhlODg5NGYxZGM4ZDg5YSIsImV4cCI6MTc3ODg2ODYzNX0.BhrbN2r6_99IrP_qQeeCVkAaSqY1irO9styVMxxCtFE" 
def upload_to_pinata(file_path):
    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
    headers = {
        "Authorization": f"Bearer {JWT_TOKEN}"
    }

    with open(file_path, "rb") as file:
        files = {
            'file': (file_path, file)
        }
        response = requests.post(url, headers=headers, files=files)

    if response.status_code == 200:
        res_json = response.json()
        cid = res_json['IpfsHash']
        print(f"✅ Upload successful! CID: {cid}")
        return cid
    else:
        print("❌ Upload failed:", response.status_code, response.text)
        return None

if __name__ == "__main__":
    encrypted_file = "encrypted_genomic_data.txt"
    upload_to_pinata(encrypted_file)

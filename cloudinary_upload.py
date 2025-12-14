#!/usr/bin/env python3
"""Quick Cloudinary uploader for Ders 2 assets"""

import cloudinary
import cloudinary.uploader
import os

# Configure Cloudinary
cloudinary.config(
    cloud_name="dzegofdgp",
    api_key="YOUR_API_KEY",  # Kemal will provide
    api_secret="YOUR_API_SECRET"  # Kemal will provide
)

def upload_asset(file_path, folder="ders2"):
    """Upload single asset to Cloudinary"""
    try:
        result = cloudinary.uploader.upload(
            file_path,
            folder=folder,
            resource_type="auto"
        )
        return result['secure_url']
    except Exception as e:
        print(f"❌ Error uploading {file_path}: {e}")
        return None

def main():
    asset_dir = r"D:\projelerim\İnternetten İndirdiklerim"
    
    # Get all files
    files = os.listdir(asset_dir)
    print(f"Found {len(files)} files")
    
    urls = {}
    for filename in files:
        file_path = os.path.join(asset_dir, filename)
        if os.path.isfile(file_path):
            print(f"📤 Uploading: {filename}")
            url = upload_asset(file_path)
            if url:
                urls[filename] = url
                print(f"✅ Uploaded: {url}")
    
    # Save URLs
    with open('CLOUDINARY_UPLOAD_RESULTS.md', 'w', encoding='utf-8') as f:
        f.write("# 📦 Cloudinary Upload URLs\n\n")
        for filename, url in urls.items():
            f.write(f"## {filename}\n{url}\n\n")
    
    print(f"\n✅ Uploaded {len(urls)} files!")

if __name__ == "__main__":
    main()

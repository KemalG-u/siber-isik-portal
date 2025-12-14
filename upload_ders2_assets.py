import cloudinary
import cloudinary.uploader
import os

# Configure Cloudinary (from upload_archive.py)
cloudinary.config(
    cloud_name="dzegofdgp",
    api_key="283632349543287",
    api_secret="dm_7xFvraZI-IwcvAxnWGTeNrWM"
)

# Asset directory
asset_dir = r"D:\projelerim\İnternetten İndirdiklerim"

print("📤 Cloudinary Upload - Ders 2 Assets")
print(f"Source: {asset_dir}\n")

# Get files
try:
    files = os.listdir(asset_dir)
    print(f"Found {len(files)} files:\n")
    
    urls = []
    
    for filename in files:
        file_path = os.path.join(asset_dir, filename)
        
        if os.path.isfile(file_path):
            print(f"📤 Uploading: {filename}")
            
            try:
                result = cloudinary.uploader.upload(
                    file_path,
                    folder="ders2",
                    resource_type="auto",
                    use_filename=True
                )
                
                url = result['secure_url']
                urls.append((filename, url))
                print(f"✅ Success: {url}\n")
                
            except Exception as e:
                print(f"❌ Error: {e}\n")
    
    # Save URLs
    with open('CLOUDINARY_UPLOAD_RESULTS.md', 'w', encoding='utf-8') as f:
        f.write("# 📦 Cloudinary Upload Results\n\n")
        f.write(f"**Date:** 14 Aralık 2025, 21:12\n")
        f.write(f"**Account:** dzegofdgp\n")
        f.write(f"**Folder:** ders2/\n\n")
        f.write("---\n\n")
        
        for filename, url in urls:
            f.write(f"## {filename}\n")
            f.write(f"```\n{url}\n```\n\n")
    
    print(f"\n✅ UPLOAD COMPLETE!")
    print(f"📊 Uploaded: {len(urls)}/{len(files)} files")
    print(f"💾 URLs saved to: CLOUDINARY_UPLOAD_RESULTS.md")
    
except Exception as e:
    print(f"❌ Error accessing directory: {e}")

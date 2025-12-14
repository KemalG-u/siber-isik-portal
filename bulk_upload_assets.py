import cloudinary
import cloudinary.uploader
import os
import glob

# Configure Cloudinary
cloudinary.config(
    cloud_name="dzegofdgp",
    api_key="283632349543287",
    api_secret="dm_7xFvraZI-IwcvAxnWGTeNrWM"
)

# Asset folder
asset_folder = r"D:\projelerim\İnternetten İndirdiklerim"

# Find all videos and images (excluding already uploaded)
videos = glob.glob(os.path.join(asset_folder, "*.mp4")) + glob.glob(os.path.join(asset_folder, "*.mov"))
images = glob.glob(os.path.join(asset_folder, "*.jpeg")) + glob.glob(os.path.join(asset_folder, "*.jpg")) + glob.glob(os.path.join(asset_folder, "*.png"))

# Exclude already uploaded
exclude = ["Chakra_Meditation_Animation_Video.mp4", "Gemini_Generated_Image_3543re3543re3543.jpeg"]
videos = [v for v in videos if os.path.basename(v) not in exclude]
images = [i for i in images if os.path.basename(i) not in exclude]

print(f"📊 Found {len(videos)} videos + {len(images)} images to upload\n")

uploaded = []

# Upload videos
for video in videos:
    filename = os.path.splitext(os.path.basename(video))[0]
    public_id = filename.lower().replace('_', '-').replace(' ', '-')
    
    print(f"🎬 Uploading video: {filename}")
    
    try:
        result = cloudinary.uploader.upload_large(
            video,
            resource_type="video",
            folder="ders1/assets",
            public_id=public_id,
            chunk_size=6000000,
            transformation=[
                {'quality': 'auto', 'fetch_format': 'auto'},
                {'width': 1920, 'crop': 'limit'}
            ]
        )
        
        uploaded.append({
            'type': 'video',
            'name': filename,
            'url': result['secure_url'],
            'public_id': result['public_id']
        })
        
        print(f"   ✅ {result['secure_url']}\n")
        
    except Exception as e:
        print(f"   ❌ Failed: {e}\n")

# Upload images
for image in images:
    filename = os.path.splitext(os.path.basename(image))[0]
    public_id = filename.lower().replace('_', '-').replace(' ', '-')
    
    print(f"🖼️ Uploading image: {filename}")
    
    try:
        result = cloudinary.uploader.upload(
            image,
            folder="ders1/assets",
            public_id=public_id,
            transformation=[
                {'quality': 'auto:best'},
                {'width': 2048, 'crop': 'limit'}
            ]
        )
        
        uploaded.append({
            'type': 'image',
            'name': filename,
            'url': result['secure_url'],
            'public_id': result['public_id']
        })
        
        print(f"   ✅ {result['secure_url']}\n")
        
    except Exception as e:
        print(f"   ❌ Failed: {e}\n")

# Save results
print("\n" + "="*60)
print(f"✅ UPLOAD COMPLETE: {len(uploaded)} assets")
print("="*60)

with open("bulk_upload_results.txt", "w", encoding="utf-8") as f:
    for item in uploaded:
        f.write(f"{item['type'].upper()}: {item['name']}\n")
        f.write(f"URL: {item['url']}\n\n")

print("\n💾 Results saved to: bulk_upload_results.txt")

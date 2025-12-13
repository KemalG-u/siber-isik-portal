import cloudinary
import cloudinary.uploader
import sys

# Configure Cloudinary
cloudinary.config(
    cloud_name="dzegofdgp",
    api_key="283632349543287",
    api_secret="dm_7xFvraZI-IwcvAxnWGTeNrWM"
)

# Video path
video_path = r"d:\projelerim\siber-isik-portal\assets\videos\spiritual-enlightenment.mov"

print("🚀 Starting upload...")
print(f"📁 File: {video_path}")

try:
    # Upload video with configurations
    result = cloudinary.uploader.upload_large(
        video_path,
        resource_type="video",
        public_id="spiritual-enlightenment",
        chunk_size=6000000,  # 6MB chunks
        eager=[
            {"quality": "auto", "fetch_format": "mp4"}
        ],
        eager_async=True
    )
    
    print("\n✅ Upload successful!")
    print(f"📺 URL: {result['secure_url']}")
    print(f"🆔 Public ID: {result['public_id']}")
    print(f"📊 Format: {result['format']}")
    
    # Save URL to file
    with open("cloudinary-video-url.txt", "w") as f:
        f.write(result['secure_url'])
    
    print("\n💾 URL saved to: cloudinary-video-url.txt")
    print("\n" + "="*50)
    print("COPY THIS URL:")
    print(result['secure_url'])
    print("="*50)
    
except Exception as e:
    print(f"\n❌ Upload failed: {e}")
    sys.exit(1)

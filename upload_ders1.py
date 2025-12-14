import cloudinary
import cloudinary.uploader
import sys
import os

# Configure Cloudinary
cloudinary.config(
    cloud_name="dzegofdgp",
    api_key="283632349543287",
    api_secret="dm_7xFvraZI-IwcvAxnWGTeNrWM"
)

# Get video path from command line argument
if len(sys.argv) > 1:
    video_path = sys.argv[1]
else:
    video_path = r"d:\projelerim\İnternetten İndirdiklerim\Chakra_Meditation_Animation_Video.mp4"

# Extract filename for public_id
filename = os.path.splitext(os.path.basename(video_path))[0]
public_id = filename.lower().replace('_', '-').replace(' ', '-')

print("🚀 Starting upload...")
print(f"📁 File: {video_path}")
print(f"🆔 Public ID: {public_id}")

try:
    # Upload video with configurations
    result = cloudinary.uploader.upload_large(
        video_path,
        resource_type="video",
        folder="ders1",
        public_id=public_id,
        chunk_size=6000000,  # 6MB chunks
        transformation=[
            {'quality': 'auto', 'fetch_format': 'auto'},
            {'width': 1920, 'crop': 'limit'}
        ],
        eager=[
            {"quality": "auto:best", "fetch_format": "mp4"}
        ],
        eager_async=True
    )
    
    print("\n✅ Upload successful!")
    print(f"📺 URL: {result['secure_url']}")
    print(f"🆔 Public ID: {result['public_id']}")
    print(f"📊 Format: {result['format']}")
    
    # Save URL to file
    url_filename = f"cloudinary-{public_id}-url.txt"
    with open(url_filename, "w") as f:
        f.write(result['secure_url'])
    
    print(f"\n💾 URL saved to: {url_filename}")
    print("\n" + "="*60)
    print("COPY THIS URL:")
    print(result['secure_url'])
    print("="*60)
    
except Exception as e:
    print(f"\n❌ Upload failed: {e}")
    sys.exit(1)

import cloudinary
import cloudinary.uploader

# Configure
cloudinary.config(
    cloud_name="dzegofdgp",
    api_key="283632349543287",
    api_secret="dm_7xFvraZI-IwcvAxnWGTeNrWM"
)

# Upload archive
archive_path = r"d:\projelerim\siber-isik-portal\CONVERSATION-ARCHIVE-2025-12-13.md"

print("📤 Uploading conversation archive to Cloudinary...")

try:
    result = cloudinary.uploader.upload(
        archive_path,
        resource_type="raw",
        public_id="archives/conversation-2025-12-13",
        folder="siber-isik-archives"
    )
    
    print(f"✅ Archive uploaded successfully!")
    print(f"🔗 URL: {result['secure_url']}")
    
    # Save URL
    with open("archive-url.txt", "w") as f:
        f.write(result['secure_url'])
    
    print("\n💾 URL saved to: archive-url.txt")
    
except Exception as e:
    print(f"❌ Upload failed: {e}")

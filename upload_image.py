import cloudinary
import cloudinary.uploader

# Configure Cloudinary
cloudinary.config(
    cloud_name="dzegofdgp",
    api_key="283632349543287",
    api_secret="dm_7xFvraZI-IwcvAxnWGTeNrWM"
)

# Image path
image_path = r"D:\projelerim\İnternetten İndirdiklerim\Gemini_Generated_Image_3543re3543re3543.jpeg"

print("🚀 Starting image upload...")
print(f"📁 File: {image_path}")

try:
    # Upload image with configurations
    result = cloudinary.uploader.upload(
        image_path,
        folder="ders1",
        public_id="hero-background",
        transformation=[
            {'quality': 'auto:best'},
            {'width': 2560, 'crop': 'limit'}
        ]
    )
    
    print("\n✅ Upload successful!")
    print(f"📺 URL: {result['secure_url']}")
    print(f"🆔 Public ID: {result['public_id']}")
    
    # Save URL to file
    with open("cloudinary-hero-background-url.txt", "w") as f:
        f.write(result['secure_url'])
    
    print("\n💾 URL saved to: cloudinary-hero-background-url.txt")
    print("\n" + "="*60)
    print("COPY THIS URL:")
    print(result['secure_url'])
    print("="*60)
    
except Exception as e:
    print(f"\n❌ Upload failed: {e}")

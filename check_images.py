#!/usr/bin/env python3
"""
Image Checker for GitHub Profile README
This script checks if all required project images are present in the assets folder.
"""

import os
from pathlib import Path

def check_images():
    """Check if all required project images are present."""
    
    # Define required images
    required_images = [
        "streamify-demo1.png",
        "medmanage-demo1.png", 
        "socially-demo1.png",
        "banking-demo1.png",
        "adobe-demo1.png"
    ]
    
    assets_path = Path("assets")
    
    print("🔍 Checking required project images...")
    print("=" * 50)
    
    missing_images = []
    present_images = []
    
    for image in required_images:
        image_path = assets_path / image
        if image_path.exists():
            size = image_path.stat().st_size
            size_mb = size / (1024 * 1024)
            print(f"✅ {image} - {size_mb:.2f} MB")
            present_images.append(image)
        else:
            print(f"❌ {image} - MISSING")
            missing_images.append(image)
    
    print("=" * 50)
    print(f"📊 Summary: {len(present_images)}/{len(required_images)} images present")
    
    if missing_images:
        print(f"\n⚠️  Missing images ({len(missing_images)}):")
        for img in missing_images:
            print(f"   - {img}")
        print(f"\n💡 Add these images to the 'assets' folder to complete your profile README!")
    else:
        print("\n🎉 All images are present! Your profile README is ready to go!")
    
    return len(missing_images) == 0

if __name__ == "__main__":
    check_images() 
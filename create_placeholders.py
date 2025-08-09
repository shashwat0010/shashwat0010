#!/usr/bin/env python3
"""
Create Placeholder Images for GitHub Profile README
This script generates professional-looking placeholder images for project showcases.
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_placeholder_image(text, filename, width=800, height=600, bg_color="#1a1a1a", text_color="#ffffff"):
    """Create a placeholder image with project name."""
    
    # Create image with dark background
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Try to use a nice font, fallback to default if not available
    try:
        # Try to use a larger, professional font
        font_size = 48
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        try:
            font = ImageFont.truetype("DejaVuSans-Bold.ttf", font_size)
        except:
            font = ImageFont.load_default()
    
    # Calculate text position to center it
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    # Draw main text
    draw.text((x, y), text, fill=text_color, font=font)
    
    # Add subtitle
    subtitle = "Project Demo"
    try:
        subtitle_font = ImageFont.truetype("arial.ttf", 24)
    except:
        subtitle_font = ImageFont.load_default()
    
    bbox_sub = draw.textbbox((0, 0), subtitle, font=subtitle_font)
    subtitle_width = bbox_sub[2] - bbox_sub[0]
    subtitle_x = (width - subtitle_width) // 2
    subtitle_y = y + text_height + 20
    
    draw.text((subtitle_x, subtitle_y), subtitle, fill="#888888", font=subtitle_font)
    
    # Add a subtle border
    draw.rectangle([0, 0, width-1, height-1], outline="#333333", width=2)
    
    # Save the image
    img.save(filename, "PNG")
    print(f"✅ Created: {filename}")

def main():
    """Create all placeholder images."""
    
    # Ensure assets directory exists
    os.makedirs("assets", exist_ok=True)
    
    # Define projects and their placeholder images
    projects = [
        ("Streamify", "assets/streamify-demo1.png"),
        ("MedManage", "assets/medmanage-demo1.png"),
        ("Socially", "assets/socially-demo1.png"),
        ("CBI Banking", "assets/banking-demo1.png"),
        ("Adobe PDF Extractor", "assets/adobe-demo1.png")
    ]
    
    print("🎨 Creating placeholder images for your projects...")
    print("=" * 50)
    
    for project_name, filename in projects:
        create_placeholder_image(project_name, filename)
    
    print("=" * 50)
    print("🎉 All placeholder images created successfully!")
    print("\n💡 These are professional placeholders that will work perfectly")
    print("   for your GitHub profile README. You can replace them later")
    print("   with actual screenshots of your projects when available.")
    
    # Run the image checker to verify
    print("\n🔍 Verifying images...")
    os.system("python check_images.py")

if __name__ == "__main__":
    main() 
#!/usr/bin/env python3
"""
PromoGen Model Verification Script
Checks if all required model files are present and provides download guidance.
"""

import os
import sys
from pathlib import Path

def check_model_files():
    """Check if all required model files are present."""
    
    model_dir = Path("promogen_final_model")
    required_files = [
        "config.json",
        "generation_config.json", 
        "model-00001-of-00002.safetensors",
        "model-00002-of-00002.safetensors",
        "model.safetensors.index.json",
        "special_tokens_map.json",
        "tokenizer.json",
        "tokenizer.model",
        "tokenizer_config.json"
    ]
    
    print("=" * 60)
    print("         PromoGen Model Verification")
    print("=" * 60)
    print()
    
    if not model_dir.exists():
        print("❌ Model directory 'promogen_final_model/' not found!")
        print()
        print_download_instructions()
        return False
    
    missing_files = []
    present_files = []
    
    for file_name in required_files:
        file_path = model_dir / file_name
        if file_path.exists():
            file_size = file_path.stat().st_size
            size_mb = file_size / (1024 * 1024)
            present_files.append((file_name, size_mb))
            print(f"✅ {file_name} ({size_mb:.1f} MB)")
        else:
            missing_files.append(file_name)
            print(f"❌ {file_name} - MISSING")
    
    print()
    print(f"Found: {len(present_files)}/{len(required_files)} files")
    
    if missing_files:
        print()
        print("🚨 Missing files:")
        for file_name in missing_files:
            print(f"   - {file_name}")
        print()
        print_download_instructions()
        return False
    else:
        total_size = sum(size for _, size in present_files)
        print(f"Total model size: {total_size:.1f} MB")
        print()
        print("🎉 All model files are present!")
        print("✅ Ready to run PromoGen!")
        return True

def print_download_instructions():
    """Print instructions for downloading model files."""
    print("📥 How to download the model files:")
    print()
    print("Option 1: GitHub Releases (Recommended)")
    print("   1. Visit: https://github.com/cptghostriley/Advertisement-generation-using-LLM/releases")
    print("   2. Download: promogen_final_model.zip")
    print("   3. Extract in project root directory")
    print()
    print("Option 2: Request Access")
    print("   1. Open an issue on GitHub")
    print("   2. Request model access with your use case")
    print("   3. We'll provide download instructions")
    print()
    print("Option 3: Hugging Face Hub")
    print("   pip install huggingface-hub")
    print("   python -c \"from huggingface_hub import snapshot_download; snapshot_download(repo_id='cptghostriley/promogen-model', local_dir='./promogen_final_model')\"")

if __name__ == "__main__":
    try:
        success = check_model_files()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"❌ Error checking model files: {e}")
        sys.exit(1)

#!/usr/bin/env python3
"""
Development setup script for PromoGen
"""
import os
import sys
import subprocess

def check_python_version():
    """Check if Python 3.10+ is installed"""
    if sys.version_info < (3, 10):
        print("❌ Python 3.10 or higher is required")
        sys.exit(1)
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")

def install_dependencies():
    """Install required dependencies"""
    print("📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully")
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        sys.exit(1)

def setup_environment():
    """Setup environment file"""
    if not os.path.exists('.env'):
        print("📝 Creating .env file from template...")
        import shutil
        shutil.copy('.env.example', '.env')
        print("✅ .env file created. Please edit it with your configuration.")
    else:
        print("✅ .env file already exists")

def initialize_database():
    """Initialize the database"""
    print("🗄️ Initializing database...")
    try:
        from app import app, db
        with app.app_context():
            db.create_all()
        print("✅ Database initialized successfully")
    except Exception as e:
        print(f"❌ Database initialization failed: {e}")

def main():
    """Main setup function"""
    print("🚀 PromoGen Development Setup")
    print("=" * 40)
    
    check_python_version()
    install_dependencies()
    setup_environment()
    initialize_database()
    
    print("\n🎉 Setup complete!")
    print("\nNext steps:")
    print("1. Edit .env file with your configuration")
    print("2. Run: python app.py")
    print("3. Open http://localhost:5000 in your browser")

if __name__ == "__main__":
    main()

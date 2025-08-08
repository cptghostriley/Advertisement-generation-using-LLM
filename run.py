#!/usr/bin/env python3
"""
PromoGen Application Runner
Simple script to start the PromoGen Flask application
"""
import os
import sys
from app import app

if __name__ == "__main__":
    # Load environment variables
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        print("Note: python-dotenv not installed. Using system environment variables.")
    
    # Get configuration from environment
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    host = os.getenv('FLASK_HOST', '127.0.0.1')
    port = int(os.getenv('FLASK_PORT', '5000'))
    
    print("🚀 Starting PromoGen Application")
    print(f"📍 Server: http://{host}:{port}")
    print(f"🔧 Debug Mode: {debug_mode}")
    print("=" * 40)
    
    # Start the application
    app.run(debug=debug_mode, host=host, port=port)

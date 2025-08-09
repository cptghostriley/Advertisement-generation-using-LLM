# PromoGen - AI Advertisement Generator

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3+-green.svg)](https://flask.palletsprojects.com/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red.svg)](https://pytorch.org)

An intelligent Flask web application that generates creative advertisement scripts and compelling call-to-actions using fine-tuned transformer language models.

## 🚀 Features

- **AI-Powered Content Generation**: Uses fine-tuned transformer models to create engaging ad scripts
- **Real-time Generation**: Interactive web interface with loading indicators
- **User Management**: Registration and login system
- **Responsive Design**: Clean, modern UI that works on all devices
- **Form Persistence**: Input values are preserved during generation
- **Fast Performance**: Optimized model parameters for quick response times

## 🛠️ Tech Stack

- **Backend**: Flask, SQLAlchemy
- **AI/ML**: PyTorch, Transformers (Hugging Face)
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite
- **Deployment**: Python 3.10+

## 📋 Prerequisites

- Python 3.10 or higher
- CUDA-compatible GPU (recommended for faster generation)
- Virtual environment (recommended)
- **AI Model Files**: Download the fine-tuned model separately (see installation steps below)

## 🔧 Installation

### Quick Start (Recommended)

1. **Clone the repository**
   ```bash
   git clone https://github.com/cptghostriley/PromoGen.git
   cd PromoGen
   ```

2. **Run the setup script**
   
   **For Windows:**
   ```cmd
   setup.bat
   ```
   
   **For Linux/Mac:**
   ```bash
   python setup.py
   ```

3. **Download the AI Model**
   
   **Option A: From Hugging Face Hub (Recommended)**
   ```bash
   # Install huggingface-hub if not already installed
   pip install huggingface-hub
   
   # Download the model automatically
   python -c "
   from huggingface_hub import snapshot_download
   snapshot_download(
       repo_id='Bhavin1905/Promogen-finetuned-model',
       local_dir='./promogen_final_model'
   )"
   ```
   
   **Option B: Manual Download from Hugging Face**
   ```bash
   # Visit: https://huggingface.co/Bhavin1905/Promogen-finetuned-model
   # Download all files to promogen_final_model/ directory
   ```
   ```bash
   # Create the model directory
   mkdir promogen_final_model
   
   # Download model files manually from provided links
   # Place all .safetensors, .json, and tokenizer files in promogen_final_model/
   ```

4. **Start the application**
   ```bash
   python run.py
   ```

### Manual Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/PromoGen.git
   cd PromoGen
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Download the AI Model (Required)**
   
   The model files are not included in the repository due to size limitations. Download from Hugging Face:
   
   **Option A: Automatic Download (Recommended)**
   ```bash
   pip install huggingface-hub
   python -c "
   from huggingface_hub import snapshot_download
   snapshot_download(
       repo_id='Bhavin1905/Promogen-finetuned-model',
       local_dir='./promogen_final_model'
   )"
   ```
   
   **Option B: Manual Download**
   - Visit: [Bhavin1905/Promogen-finetuned-model](https://huggingface.co/Bhavin1905/Promogen-finetuned-model)
   - Click "Use this model" → "Download files"
   - Download all files to `promogen_final_model/` directory
   
   **Option C: Using Git LFS**
   ```bash
   git lfs install
   git clone https://huggingface.co/Bhavin1905/Promogen-finetuned-model promogen_final_model
   ```

6. **Initialize the database**
   ```bash
   python app.py
   # Database will be created automatically on first run
   ```

## 🚀 Usage

1. **Start the application**
   ```bash
   python app.py
   ```

2. **Access the application**
   - Open your browser and navigate to `http://localhost:5000`
   - Register a new account or login with existing credentials

3. **Generate advertisements**
   - Go to the "Generate Ad" section (`/team`)
   - Fill in the company name, product name, and description
   - Click "Generate Ad" and wait for the AI to create your content
   - View the generated ad script and call-to-action

## 📁 Project Structure

```
PromoGen/
├── 📄 app.py                      # Main Flask application
├── 📄 run.py                      # Application runner script
├── 📄 check_model.py              # Model verification script
├── 📄 setup.py                    # Setup script for Linux/Mac
├── 📄 setup.bat                   # Setup script for Windows
├── 📄 requirements.txt            # Python dependencies
├── 📄 .gitignore                 # Git ignore rules
├── 📄 .env.example               # Environment variables template
├── 📄 README.md                  # Project documentation
├── 📄 LICENSE                    # MIT License
├── 📁 templates/                 # HTML templates
│   ├── 🏠 home-1.html           # Homepage
│   ├── 🏠 home-2.html           # Alternative homepage
│   ├── 🔐 login.html            # Login page
│   ├── 📝 register.html         # Registration page
│   ├── ⚡ h.html                # Ad generation page (main feature)
│   ├── 🛠️ services.html         # Services page
│   └── 👥 team.html             # Team page
├── 📁 static/                    # Static assets
│   ├── 🎨 css/                  # Stylesheets and plugins
│   ├── ⚡ js/                   # JavaScript files and plugins
│   └── 🖼️ img/                  # Images and graphics
├── 🤖 promogen_final_model/      # Fine-tuned AI model files (download separately)
├── 📊 dataset/                   # Training datasets
├── 📈 Results/                   # Generated results and screenshots
└── 🗂️ temp/                      # Temporary files
```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file with the following variables:

```env
# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=False
SECRET_KEY=your-super-secret-key-change-this-in-production

# Database Configuration
DATABASE_URL=sqlite:///database.db

# Model Configuration
MODEL_PATH=promogen_final_model
MAX_NEW_TOKENS=100
TEMPERATURE=0.8
TOP_P=0.85

# Security Settings
WTF_CSRF_ENABLED=True
SESSION_COOKIE_SECURE=True
SESSION_COOKIE_HTTPONLY=True
```

### Model Configuration

The application uses a fine-tuned language model located in `promogen_final_model/`. The model parameters can be adjusted in `app.py`:

- `max_new_tokens`: Controls response length
- `temperature`: Controls creativity (0.1-1.0)
- `top_p`: Controls diversity (0.1-1.0)

## 📊 Performance & Hardware Requirements

### Minimum Requirements
- **RAM**: 8GB+ (16GB recommended)
- **Storage**: 10GB+ free space
- **CPU**: Multi-core processor (Intel i5/AMD Ryzen 5 or better)

### Recommended for Best Performance
- **GPU**: NVIDIA GPU with 8GB+ VRAM (RTX 3070/4060 or better)
- **RAM**: 16GB+ 
- **Storage**: SSD with 20GB+ free space
- **CPU**: Intel i7/AMD Ryzen 7 or better

### Model Performance Metrics
- **Generation Time**: 30-60 seconds (GPU) / 2-5 minutes (CPU)
- **Model Size**: ~5GB
- **Memory Usage**: ~6GB during inference

## 🤖 AI Model Setup

### Model Requirements

The PromoGen application requires a fine-tuned language model that is **not included** in this repository due to GitHub's file size limitations (620MB+ files). 

**Required Model Files:**
```
promogen_final_model/
├── config.json                      # Model configuration
├── generation_config.json           # Generation parameters  
├── model-00001-of-00002.safetensors # Model weights (part 1)
├── model-00002-of-00002.safetensors # Model weights (part 2)
├── model.safetensors.index.json     # Model index
├── special_tokens_map.json          # Special tokens
├── tokenizer.json                   # Tokenizer
├── tokenizer.model                  # Tokenizer model
└── tokenizer_config.json            # Tokenizer configuration
```

### How to Obtain the Model

**� Option 1: Hugging Face Hub (Recommended)**
```bash
pip install huggingface-hub
python -c "
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id='Bhavin1905/Promogen-finetuned-model',
    local_dir='./promogen_final_model'
)"
```

**🚀 Option 2: Direct Hugging Face Download**
Visit the model repository: [Bhavin1905/Promogen-finetuned-model](https://huggingface.co/Bhavin1905/Promogen-finetuned-model)
- Click "Use this model" → "Download files"
- Download all files to `promogen_final_model/` directory

**📧 Option 3: Request Access**
- Open a [GitHub Issue](https://github.com/cptghostriley/Advertisement-generation-using-LLM/issues/new)
- Request model access with your use case
- We'll provide alternative download instructions

**⚠️ Important Notes:**
- Model size: ~5GB total
- Internet connection required for download
- Ensure sufficient disk space before downloading

## 🐛 Troubleshooting

### Common Issues

1. **Model loading errors**
   ```
   Error: Model files not found in 'promogen_final_model/'
   ```
   **Solution**: Download the model files following the [AI Model Setup](#-ai-model-setup) section above
   
2. **Missing model files**
   ```
   FileNotFoundError: [Errno 2] No such file or directory: 'promogen_final_model/config.json'
   ```
   **Solution**: Ensure all 9 model files are present in the `promogen_final_model/` directory

3. **CUDA/GPU errors**
   - Ensure CUDA is properly installed if using GPU
   - The app will automatically fall back to CPU if GPU is unavailable

4. **Slow generation times**
   - Reduce `max_new_tokens` in model configuration
   - Use CPU fallback if GPU memory is insufficient

5. **Database errors**
   - Delete `database.db` and restart the application
   - Check file permissions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👥 Authors

- **Ashwin Mahawar** - Development
- **Bhavin** - Optimization and deployment
- **Team PromoGen** - Additional contributors

## 🙏 Acknowledgments

- Hugging Face for transformer models and tokenizers
- Flask community for excellent documentation
- Open source contributors

**Important Notes**: 
- This application requires significant computational resources for optimal performance
- **AI model files must be downloaded separately** due to GitHub size limitations
- Consider using cloud platforms with GPU support for production deployment
- See the [AI Model Setup](#-ai-model-setup) section for download instructions

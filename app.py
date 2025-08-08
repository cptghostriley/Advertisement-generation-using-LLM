from flask import Flask, request, jsonify, render_template,redirect,url_for
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import re
import os
from flask_sqlalchemy import SQLAlchemy

# Load environment variables
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # python-dotenv not installed, continue without it

fine_tuned_model_path = os.getenv('MODEL_PATH', "promogen_final_model")

model = AutoModelForCausalLM.from_pretrained(
    fine_tuned_model_path,
    device_map="auto",
    torch_dtype=torch.float16,
    low_cpu_mem_usage=True,
    trust_remote_code=True
)

tokenizer = AutoTokenizer.from_pretrained(fine_tuned_model_path, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "right"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///database.db')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key-change-in-production')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))
    password = db.Column(db.String(80))
 
with app.app_context():    
    db.create_all()

@app.route("/")
def homepage():
    return render_template("home-1.html")

@app.route("/login",methods=["GET", "POST"])
def login():
    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["passw"]
        
        login = user.query.filter_by(username=uname, password=passw).first()
        
        return redirect(url_for("homepage"))
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        uname = request.form['uname']
        mail = request.form['mail']
        passw = request.form['passw']

        register = user(username = uname, email = mail, password = passw)
        db.session.add(register)
        db.session.commit()

        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/team",methods = ['POST', 'GET'])
def team():
    ad_script = None
    cta = None
    if request.method == 'POST':
        import time
        start_time = time.time()
        
        company_name = request.form.get("company_name")
        product_name = request.form.get("product_name")
        product_description = request.form.get("product_description")
        print(f"Processing request for: {company_name} - {product_name}")
        
    # Prompt format as per your fine-tuning
        input_text = (
            "### Instruction: Write a highly engaging advertisement script and a strong call to action for the product below.\n"
            "The ad script should creatively describe the product's features and benefits, and the call to action should motivate the audience to take action immediately.\n\n"
            f"Company Name: {company_name}\n"
            f"Product Name: {product_name}\n"
            f"Product Description: {product_description}\n\n"
            "Ad Script:\n"
        )

        print("Starting model generation...")
    # Tokenize and move to GPU (with fallback to CPU)
        inputs = tokenizer(input_text, return_tensors="pt")
        try:
            inputs = {k: v.to("cuda") for k, v in inputs.items()}
            print("Using CUDA for generation")
        except:
            print("CUDA not available, using CPU")
            # Keep inputs on CPU
    # inputs = tokenizer(input_text, return_tensors="pt").to("cpu")

    # Generate the ad content with optimized settings for faster response
        with torch.no_grad():  # Disable gradient computation for faster inference
            outputs = model.generate(
                **inputs,
                max_new_tokens=100,  # Further reduced for speed
                temperature=0.8,     # Slightly higher for more creativity with fewer tokens
                top_p=0.85,         
                do_sample=True,
                pad_token_id=tokenizer.eos_token_id,
                num_beams=1,        # Disable beam search for speed
                early_stopping=True,
                use_cache=True      # Enable KV caching
            )

    # Decode the output
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        generation_time = time.time() - start_time
        print(f"Generation completed in {generation_time:.2f} seconds")
        print(f"Generated text: {generated_text}")

    # ✅ Extract Ad Script and CTA using improved regex
        # Remove the input prompt from the generated text
        generated_only = generated_text.split("Ad Script:")[-1].strip()
        
        # Try multiple patterns to extract CTA
        cta_patterns = [
            r"CTA:\s*(.*?)(?:\n|$)",
            r"Call to Action:\s*(.*?)(?:\n|$)", 
            r"Call To Action:\s*(.*?)(?:\n|$)",
        ]
        
        cta = None
        ad_script = generated_only
        
        for pattern in cta_patterns:
            cta_match = re.search(pattern, generated_only, re.IGNORECASE)
            if cta_match:
                cta = cta_match.group(1).strip()
                # Remove CTA from ad_script
                ad_script = re.sub(pattern, "", generated_only, flags=re.IGNORECASE).strip()
                break
        
        if not cta:
            # If no CTA found, split the text and assume last sentence is CTA
            sentences = generated_only.split('.')
            if len(sentences) > 1:
                cta = sentences[-1].strip() + "."
                ad_script = '.'.join(sentences[:-1]).strip() + "."
            else:
                ad_script = generated_only
                cta = "Contact us today to learn more!"
        
        print(f"Extracted Ad Script: {ad_script}")
        print(f"Extracted CTA: {cta}")
        

    return render_template("h.html", 
                         ad_script=ad_script, 
                         cta=cta,
                         company_name=company_name if request.method == 'POST' else '',
                         product_name=product_name if request.method == 'POST' else '',
                         product_description=product_description if request.method == 'POST' else '')


if __name__ == "__main__":
    import os
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode, host='127.0.0.1', port=5000)

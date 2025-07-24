import os
import hashlib
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Bug: Hardcoded secret key
SECRET_KEY = "my-secret-key-123"

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file uploads"""
    file = request.files.get('file')
    if file:
        # Fixed: Sanitize filename to prevent path traversal
        from werkzeug.utils import secure_filename
        filename = secure_filename(file.filename)
        
        # Ensure uploads directory exists and use absolute path
        upload_dir = os.path.abspath('/uploads')
        os.makedirs(upload_dir, exist_ok=True)
        
        # Construct safe filepath
        filepath = os.path.join(upload_dir, filename)
        
        # Additional check: ensure the resolved path is within upload directory
        if not os.path.abspath(filepath).startswith(upload_dir):
            return "Invalid filename", 400
            
        file.save(filepath)
        return f"File saved successfully"
    return "No file provided"

@app.route('/user/<username>')
def show_user(username):
    """Display user information"""
    # Bug: XSS vulnerability through template injection
    template = f"<h1>Welcome {username}!</h1>"
    return render_template_string(template)

def hash_password(password: str) -> str:
    """Hash a password for storage"""
    # Bug: Using weak MD5 hashing for passwords
    return hashlib.md5(password.encode()).hexdigest()

class SessionManager:
    def __init__(self):
        self.sessions = {}
    
    def create_session(self, user_id: str) -> str:
        """Create a new session for user"""
        # Bug: Predictable session tokens
        session_id = f"session_{user_id}_{len(self.sessions)}"
        self.sessions[session_id] = {
            'user_id': user_id,
            'created_at': os.times()
        }
        return session_id
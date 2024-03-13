from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps

# Importing the models and serializers
from company.models import Company, Division, Department, Project, User as CompanyUser
from settings.models import Module
from design.models import Process, Form
from workflow.models import Workflow
from dashboard.models import Dashboard
from publish.models import Publication
from user.models import User
from reports.models import Report
from api.serializers import *
from api.permissions import *
from api.authentication import *

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'your_secret_key'

# Decorator for verifying the JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated

@app.route('/auth/social', methods=['POST'])
def social_sign_in():
    # Social sign-in logic here
    pass

@app.route('/auth/register', methods=['POST'])
def register_user():
    # User registration logic here
    pass

@app.route('/auth/verify', methods=['POST'])
def verify_email():
    # Email verification logic here
    pass

@app.route('/company', methods=['POST'])
@token_required
def company_registration(current_user):
    # Company registration logic here
    pass

@app.route('/company/division', methods=['POST'])
@token_required
def add_division(current_user):
    # Add division logic here
    pass

@app.route('/company/department', methods=['POST'])
@token_required
def add_department(current_user):
    # Add department logic here
    pass

@app.route('/company/project', methods=['POST'])
@token_required
def add_project(current_user):
    # Add project logic here
    pass

@app.route('/company/user', methods=['POST'])
@token_required
def add_user(current_user):
    # Add user logic here
    pass

@app.route('/settings/module', methods=['POST'])
@token_required
def add_module(current_user):
    # Add module logic here
    pass

@app.route('/design/process', methods=['POST'])
@token_required
def design_process(current_user):
    # Design process logic here
    pass

@app.route('/design/form', methods=['POST'])
@token_required
def create_form(current_user):
    # Create form logic here
    pass

@app.route('/design/workflow', methods=['POST'])
@token_required
def create_workflow(current_user):
    # Create workflow logic here
    pass

@app.route('/dashboard/<moduleId>', methods=['GET'])
@token_required
def fetch_dashboard_data(current_user, moduleId):
    # Fetch dashboard data logic here
    pass

@app.route('/reports/<moduleId>', methods=['GET'])
@token_required
def generate_report(current_user, moduleId):
    # Generate report logic here
    pass

@app.route('/publish/module/<moduleId>', methods=['POST'])
@token_required
def publish_module(current_user, moduleId):
    # Publish module logic here
    pass

if __name__ == '__main__':
    app.run(debug=True)
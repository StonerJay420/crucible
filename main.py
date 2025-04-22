"""
Main routes for the Crucible API
"""
from flask import Blueprint, jsonify

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET'])
def index():
    """
    Root endpoint for the Crucible API
    
    Returns:
        JSON response indicating the API is running
    """
    return jsonify({"status": "success", "message": "Crucible API running"})

@main_bp.route('/health', methods=['GET'])
def health():
    """
    Health check endpoint
    
    Returns:
        JSON response with health status
    """
    return jsonify({"status": "healthy"})
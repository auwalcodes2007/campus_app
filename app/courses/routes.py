from flask import Blueprint, render_template, redirect, url_for

courses_bp = Blueprint("courses", __name__, template_folder="templates")
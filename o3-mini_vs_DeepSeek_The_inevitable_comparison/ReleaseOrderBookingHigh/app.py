from flask import Flask, render_template, request, redirect, url_for, session, flash, send_file
import io
from config import Config
from database import init_db, get_db_connection
from models import (get_ad_types, get_platforms, get_inventory_slots, get_discount_limit,
                    get_dues_threshold, add_release_order, validate_release_order)
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the DB (if not exists)
init_db()

@app.route("/")
def index():
    return render_template("index.html")

# Release Order Creation – Step 1: Client Information
@app.route("/create/step1", methods=["GET", "POST"])
def create_step1():
    if request.method == "POST":
        session["client_name"] = request.form.get("client_name")
        session["client_type"] = request.form.get("client_type")
        session["client_contact"] = request.form.get("client_contact")
        session["outstanding_due"] = float(request.form.get("outstanding_due", 0))
        return redirect(url_for("create_step2"))
    return render_template("create_ro_step1.html")

# Step 2: Campaign Details
@app.route("/create/step2", methods=["GET", "POST"])
def create_step2():
    if request.method == "POST":
        session["campaign_name"] = request.form.get("campaign_name")
        return redirect(url_for("create_step3"))
    return render_template("create_ro_step2.html")

# Step 3: Ad Details
@app.route("/create/step3", methods=["GET", "POST"])
def create_step3():
    ad_types = get_ad_types()
    platforms = get_platforms()
    inventory_slots = get_inventory_slots()
    discount_limit = get_discount_limit()
    if request.method == "POST":
        session["ad_type"] = request.form.get("ad_type")
        session["ad_platform"] = request.form.get("ad_platform")
        session["inventory_slot"] = request.form.get("inventory_slot")
        session["discount"] = float(request.form.get("discount", 0))
        # Validate using thresholds and inventory availability
        errors = validate_release_order(session, discount_limit, get_dues_threshold(), inventory_slots)
        if errors:
            for error in errors:
                flash(error, "error")
            # Re-render the form with errors
            return render_template("create_ro_step3.html", ad_types=ad_types, platforms=platforms, 
                                   inventory_slots=inventory_slots, discount_limit=discount_limit)
        return redirect(url_for("ro_summary"))
    return render_template("create_ro_step3.html", ad_types=ad_types, platforms=platforms, 
                           inventory_slots=inventory_slots, discount_limit=discount_limit)

# Summary and confirmation
@app.route("/create/summary", methods=["GET", "POST"])
def ro_summary():
    if request.method == "POST":
        # Save the release order
        add_release_order(session)
        flash("Release Order has been created successfully!", "success")
        session.clear()
        return redirect(url_for("index"))
    return render_template("ro_summary.html", data=session)

# PDF generation using ReportLab
@app.route("/create/pdf")
def create_pdf():
    pdf_buffer = io.BytesIO()
    p = canvas.Canvas(pdf_buffer, pagesize=letter)
    width, height = letter
    text_object = p.beginText(40, height - 40)
    text_object.setFont("Helvetica", 12)
    text_object.textLine("Release Order Summary")
    text_object.textLine("------------------------")
    for key, value in session.items():
        text_object.textLine(f"{key}: {value}")
    p.drawText(text_object)
    p.showPage()
    p.save()
    pdf_buffer.seek(0)
    return send_file(pdf_buffer, as_attachment=True, download_name="release_order.pdf", mimetype="application/pdf")

# Admin login – simple hard-coded approach for the prototype
@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "admin" and password == "password":
            session["admin"] = True
            return redirect(url_for("admin_dashboard"))
        else:
            flash("Invalid credentials", "error")
    return render_template("admin_login.html")

@app.route("/admin/logout")
def admin_logout():
    session.pop("admin", None)
    flash("Logged out", "info")
    return redirect(url_for("index"))

def admin_required(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("admin"):
            flash("Please log in as admin to access this page.", "error")
            return redirect(url_for("admin_login"))
        return f(*args, **kwargs)
    return decorated_function

@app.route("/admin/dashboard")
@admin_required
def admin_dashboard():
    return render_template("admin_dashboard.html")

# Admin: Manage Clients/Agencies
@app.route("/admin/clients", methods=["GET", "POST"])
@admin_required
def admin_clients():
    conn = get_db_connection()
    if request.method == "POST":
        name = request.form.get("name")
        client_type = request.form.get("client_type")
        contact = request.form.get("contact")
        conn.execute("INSERT INTO clients (name, type, contact) VALUES (?, ?, ?)", (name, client_type, contact))
        conn.commit()
        flash("Client added successfully.", "success")
    clients = conn.execute("SELECT * FROM clients").fetchall()
    conn.close()
    return render_template("admin_clients.html", clients=clients)

# Admin: Manage Ad Types
@app.route("/admin/adtypes", methods=["GET", "POST"])
@admin_required
def admin_adtypes():
    conn = get_db_connection()
    if request.method == "POST":
        name = request.form.get("name")
        conn.execute("INSERT INTO ad_types (name) VALUES (?)", (name,))
        conn.commit()
        flash("Ad type added successfully.", "success")
    ad_types = conn.execute("SELECT * FROM ad_types").fetchall()
    conn.close()
    return render_template("admin_adtypes.html", ad_types=ad_types)

# Admin: Manage Platforms
@app.route("/admin/platforms", methods=["GET", "POST"])
@admin_required
def admin_platforms():
    conn = get_db_connection()
    if request.method == "POST":
        name = request.form.get("name")
        conn.execute("INSERT INTO platforms (name) VALUES (?)", (name,))
        conn.commit()
        flash("Platform added successfully.", "success")
    platforms = conn.execute("SELECT * FROM platforms").fetchall()
    conn.close()
    return render_template("admin_platforms.html", platforms=platforms)

# Admin: Manage Inventory Slots
@app.route("/admin/inventory", methods=["GET", "POST"])
@admin_required
def admin_inventory():
    conn = get_db_connection()
    if request.method == "POST":
        slot_name = request.form.get("slot_name")
        available_quantity = int(request.form.get("available_quantity", 0))
        conn.execute("INSERT INTO inventory (slot_name, available_quantity) VALUES (?, ?)", (slot_name, available_quantity))
        conn.commit()
        flash("Inventory slot added successfully.", "success")
    inventory_slots = conn.execute("SELECT * FROM inventory").fetchall()
    conn.close()
    return render_template("admin_inventory.html", inventory_slots=inventory_slots)

# Admin: Manage Discount and Outstanding Dues Limits
@app.route("/admin/limits", methods=["GET", "POST"])
@admin_required
def admin_limits():
    conn = get_db_connection()
    if request.method == "POST":
        discount_limit = float(request.form.get("discount_limit", 0))
        dues_threshold = float(request.form.get("dues_threshold", 0))
        # For simplicity, clear and reinsert new limits
        conn.execute("DELETE FROM discount_limits")
        conn.execute("INSERT INTO discount_limits (limit_percentage) VALUES (?)", (discount_limit,))
        conn.execute("DELETE FROM dues_threshold")
        conn.execute("INSERT INTO dues_threshold (threshold_amount) VALUES (?)", (dues_threshold,))
        conn.commit()
        flash("Limits updated successfully.", "success")
    discount = conn.execute("SELECT * FROM discount_limits ORDER BY id DESC LIMIT 1").fetchone()
    dues = conn.execute("SELECT * FROM dues_threshold ORDER BY id DESC LIMIT 1").fetchone()
    conn.close()
    return render_template("admin_limits.html", discount=discount, dues=dues)

if __name__ == "__main__":
    app.run(debug=True)
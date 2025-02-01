from database import get_db_connection

def get_ad_types():
    conn = get_db_connection()
    ad_types = conn.execute("SELECT * FROM ad_types").fetchall()
    conn.close()
    return ad_types

def get_platforms():
    conn = get_db_connection()
    platforms = conn.execute("SELECT * FROM platforms").fetchall()
    conn.close()
    return platforms

def get_inventory_slots():
    conn = get_db_connection()
    inventory = conn.execute("SELECT * FROM inventory").fetchall()
    conn.close()
    return inventory

def get_discount_limit():
    conn = get_db_connection()
    discount = conn.execute("SELECT * FROM discount_limits ORDER BY id DESC LIMIT 1").fetchone()
    conn.close()
    return discount["limit_percentage"] if discount else 0

def get_dues_threshold():
    conn = get_db_connection()
    dues = conn.execute("SELECT * FROM dues_threshold ORDER BY id DESC LIMIT 1").fetchone()
    conn.close()
    return dues["threshold_amount"] if dues else 0

def add_release_order(data):
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO release_orders (client_name, client_type, client_contact, campaign_name, ad_type, ad_platform, inventory_slot, discount, outstanding_due) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (
            data.get("client_name"),
            data.get("client_type"),
            data.get("client_contact"),
            data.get("campaign_name"),
            data.get("ad_type"),
            data.get("ad_platform"),
            data.get("inventory_slot"),
            data.get("discount"),
            data.get("outstanding_due"),
        )
    )
    conn.commit()
    conn.close()

def validate_release_order(data, discount_limit, dues_threshold, inventory_slots):
    errors = []
    # Validate outstanding due limit
    if data.get("outstanding_due", 0) > dues_threshold:
        errors.append("Outstanding due exceeds the approved threshold.")
    # Validate discount limit
    if data.get("discount", 0) > discount_limit:
        errors.append("Discount exceeds allowed limit.")
    # Validate inventory slot availability
    slot = data.get("inventory_slot")
    available = None
    for inv in inventory_slots:
        if inv["slot_name"] == slot:
            available = inv["available_quantity"]
            break
    if available is None or available <= 0:
        errors.append("Selected inventory slot is not available.")
    return errors
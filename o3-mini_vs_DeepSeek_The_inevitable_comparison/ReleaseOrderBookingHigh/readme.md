# Release Order Booking System

A Flask-based web application for managing advertising release orders. This system provides a step-by-step wizard for creating release orders, validates business rules, and includes an administrative interface for configuration management.

## Features

- **Release Order Creation Wizard**
  - Step 1: Client/Agency Information
  - Step 2: Campaign Details
  - Step 3: Ad Details
  - Review and Summary Page

- **Business Rule Validations**
  - Outstanding dues limit checking
  - Inventory availability verification
  - Discount threshold validation
  - Real-time validation feedback

- **Export Options**
  - PDF generation of release orders
  - Copy to clipboard functionality
  - Structured summary view

- **Admin Interface**
  - Client/Agency management
  - Ad type configuration
  - Platform management
  - Inventory slot tracking
  - Discount and dues limit settings

## Tech Stack

- Python 3.8+
- Flask 2.2.2
- SQLite Database
- ReportLab 3.6.12 (PDF generation)
- HTML/CSS for frontend

## Project Structure

```
ReleaseOrderBooking/
├── app.py
├── config.py
├── database.py
├── models.py
├── schema.sql
├── requirements.txt
├── static/
│   └── css/
│       └── style.css
└── templates/
    ├── admin_adtypes.html
    ├── admin_clients.html
    ├── admin_dashboard.html
    ├── admin_inventory.html
    ├── admin_limits.html
    ├── admin_login.html
    ├── admin_platforms.html
    ├── create_ro_step1.html
    ├── create_ro_step2.html
    ├── create_ro_step3.html
    ├── index.html
    └── ro_summary.html
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/release-order-booking.git
   cd release-order-booking
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Initialize the database:
   ```bash
   python
   >>> from app import init_db
   >>> init_db()
   >>> exit()
   ```

5. Run the application:
   ```bash
   python app.py
   ```

The application will be available at `http://localhost:5000`

## Usage

### Creating a Release Order

1. Click "Create Release Order" on the home page
2. Fill in client information in Step 1
3. Enter campaign details in Step 2
4. Specify ad details and check validations in Step 3
5. Review the summary and generate PDF if needed
6. Submit the release order

### Admin Access

1. Navigate to `/admin/login`
2. Default credentials:
   - Username: admin
   - Password: password
3. Use the admin dashboard to manage system configuration




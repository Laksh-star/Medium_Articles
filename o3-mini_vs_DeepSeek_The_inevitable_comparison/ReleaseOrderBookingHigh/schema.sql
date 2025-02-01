DROP TABLE IF EXISTS release_orders;
DROP TABLE IF EXISTS clients;
DROP TABLE IF EXISTS ad_types;
DROP TABLE IF EXISTS platforms;
DROP TABLE IF EXISTS inventory;
DROP TABLE IF EXISTS discount_limits;
DROP TABLE IF EXISTS dues_threshold;

CREATE TABLE release_orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_name TEXT,
    client_type TEXT,
    client_contact TEXT,
    campaign_name TEXT,
    ad_type TEXT,
    ad_platform TEXT,
    inventory_slot TEXT,
    discount REAL,
    outstanding_due REAL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    type TEXT,
    contact TEXT
);

CREATE TABLE ad_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
);

CREATE TABLE platforms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
);

CREATE TABLE inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    slot_name TEXT,
    available_quantity INTEGER
);

CREATE TABLE discount_limits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    limit_percentage REAL
);

CREATE TABLE dues_threshold (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    threshold_amount REAL
);

-- Insert default limits
INSERT INTO discount_limits (limit_percentage) VALUES (20);
INSERT INTO dues_threshold (threshold_amount) VALUES (10000);
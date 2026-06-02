-- File: app/db-init/init.sql
CREATE TABLE IF NOT EXISTS items (
    id   SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO items (name) VALUES
  ('Item One'),
  ('Item Two'),
  ('Item Three')
ON CONFLICT DO NOTHING;

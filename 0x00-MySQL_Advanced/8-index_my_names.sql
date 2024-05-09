-- File: 8-index_my_names.sql
-- Add a generated column and create an index on that column

ALTER TABLE names
ADD COLUMN first_letter CHAR(1) AS (LEFT(name, 1)) STORED;

-- Create an index on the generated column
CREATE INDEX idx_name_first ON names(first_letter);

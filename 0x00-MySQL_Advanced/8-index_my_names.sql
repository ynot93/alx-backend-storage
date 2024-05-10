-- File: 8-index_my_names.sql
-- Add a generated column and create an index on that column

CREATE INDEX idx_name_first ON names( name(1) );

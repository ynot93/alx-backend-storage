-- Modify the table to include a new stored generated column for the first letter
ALTER TABLE names
ADD COLUMN first_letter CHAR(1) AS (LEFT(name, 1)) STORED;
-- Create a composite index on the first letter of the name and the score
CREATE INDEX idx_name_first_score ON names(first_letter, score);

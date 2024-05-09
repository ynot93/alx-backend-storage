-- Creates a view that lists all students that have a score under 80
-- Also no last_meeting for more than 1 month

-- Drop the view if it already exists
DROP VIEW IF EXISTS need_meeting;

-- Create the view
CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE (score < 80)
  AND (last_meeting IS NULL OR last_meeting < DATE_SUB(CURDATE(), INTERVAL 1 MONTH));

-- Function SafeDiv that divides the first by the second number
-- Drop the function if it already exists
DROP FUNCTION IF EXISTS SafeDiv;

-- Create the new function
DELIMITER $$

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END$$

DELIMITER ;

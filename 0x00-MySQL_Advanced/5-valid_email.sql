-- Create a trigger that will execute before each row is updated in the users table

DELIMITER $$

CREATE TRIGGER ResetValidEmail
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    -- Check if the email is being updated and reset valid_email if it is
    IF OLD.email <> NEW.email THEN
        SET NEW.valid_email = 0;
    END IF;
END$$

-- Reset the delimiter to the default
DELIMITER ;

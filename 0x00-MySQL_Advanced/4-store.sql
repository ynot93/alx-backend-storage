-- Create a trigger that decreases quantity of item after adding a new order

DELIMITER $$

-- Create trigger after inserting a new order
CREATE TRIGGER AfterInsertOrder
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END$$

DELIMITER ;

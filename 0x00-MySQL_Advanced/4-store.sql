-- Drop the existing trigger if it exists
DROP TRIGGER IF EXISTS after_new_order;

-- Change the delimiter to $$ to allow semicolons in the trigger body
DELIMITER $$

-- Create the trigger
CREATE TRIGGER after_new_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END$$

-- Reset the delimiter to ;
DELIMITER ;

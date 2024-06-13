-- Reset the valid_email field once an email is updated

-- Delete any existing triggers
DROP TRIGGER IF EXISTS update_valid_email;

-- Change the delimiter to $$ to allow semicolons in the trigger body
DELIMITER $$

-- Create the trigger
CREATE TRIGGER update_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF NEW.email = OLD.email THEN
		SET NEW.valid_email = 1;
		IF NEW.name != OLD.name THEN
			-- Overwrite the old value with the new value
			SET NEW.name = NEW.name;
		END IF;
	ELSE 
		SET NEW.valid_email = 0;
	END IF;
END$$

-- Reset the delimiter to ;
DELIMITER ;

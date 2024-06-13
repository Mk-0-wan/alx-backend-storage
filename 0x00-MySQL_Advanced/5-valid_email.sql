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
	-- TODO: Still missing one checker
	IF NEW.email = OLD.email THEN
		SET NEW.valid_email = 1;
		IF NEW.name != OLD.name THEN
			UPDATE users SET name = NEW.name WHERE email = NEW.email;
	ELSE IF NEW.email = NULL THEN
		SET NEW.email = 0;
	ELSE IF OLD.email = NULL THEN
		SET NEW.email = 1;
	
	ELSE 
		SET NEW.valid_email = 0;
	END IF;
END$$

-- Reset the delimiter to ;
DELIMITER ;

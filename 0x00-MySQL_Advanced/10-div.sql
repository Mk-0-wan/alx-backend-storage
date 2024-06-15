-- Creating an sql function
DELIMITER $$ ;

CREATE FUNCTION SafeDiv(a INT, b INT)
BEGIN
	DECLARE x FLOAT DEFAULT 0;

	IF b = 0 THEN
		SET x = 0;
	ELSE
		SET x = a / b;
	END IF;

	RETURN x;
END$$

DELIMITER ; $$

-- Creating an sql function
DELIMITER $$ ;

CREATE FUNCTION SafeDiv(
	a INT,
	b INT
)
RETURN FLOAT
BEGIN
	IF b == 0 THEN
		RETURN(0);
	ELSE
		RETURN(a / b);
	END IF;
END$$

DELIMITER ; $$

-- Calculate the average weighted score for all the students
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

-- Procedure 

DELIMITER $$ ;

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	-- counter for our users id
	DECLARE usr_id INT;
	-- state checker for the cursor
	DECLARE state INT DEFAULT FALSE;
	-- cursor acts a pointer to our current position in the user table
	-- stores the value of the current id we are positioned at.
	DECLARE cur CURSOR FOR SELECT id FROM users;
	-- step counter for the cursor when value is none we are done stop the cursor
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET state = TRUE;

	-- initialize the cursor to the first row of the table(column id of the table)
	OPEN cur;

	-- SQL loop
	local_loop: LOOP
		-- store whatever the cur is pointing to inside the variable user_id
		FETCH cur INTO usr_id;
		-- check for the cursor state if true we are done else we continue make an update
		IF state THEN
			LEAVE local_loop;
		END IF;

		-- Normal updating as before
		UPDATE users
		SET average_score = (
			SELECT SUM(corrections.score * projects.weight) / SUM(projects.weight)
			FROM corrections
			JOIN projects
			ON corrections.project_id = projects.id
			WHERE corrections.user_id = usr_id
		)
		-- for each user_id found in the table by the cursor
		WHERE id = usr_id;
	END LOOP;
	-- close the cursor pointer
	CLOSE cur;
END $$
DELIMITER ;

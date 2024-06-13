-- Create a procedure
-- Okey i am assuming that new users are not accepted --keep and eye on this one--
-- Check if the project exists in the project table
-- If not add it to the project table and insert the new score
-- Else if already present the update the score value in the correction table
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER $$ ;
CREATE PROCEDURE AddBonus(IN usr_id INT, IN project_name VARCHAR(255), IN marks INT)
BEGIN
	DECLARE proj_id INT;

	IF PROJECT_NAME IN (SELECT NAME FROM projects) THEN
		SELECT id INTO proj_id FROM projects WHERE name = project_name;
		INSERT INTO corrections (user_id, project_id, score) VALUES (usr_id, proj_id, marks);
	ELSE
		INSERT INTO projects (name) VALUES (project_name);
		SET proj_id = last_insert_id();
		INSERT INTO corrections (user_id, project_id, score) VALUES (usr_id, proj_id, marks);
	END IF;
END $$
DELIMITER ; $$

-- Get the average score for a particular student id
-- Group all the scores according to student id
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

DELIMITER $$ ;

CREATE PROCEDURE ComputeAverageScoreForUser(IN usr_id INT)
BEGIN
	-- DECLARE any_user DECIMAL(10,2);
	UPDATE users
        SET average_score = (
		SELECT AVG(corrections.score) AS avg_score 
		FROM corrections 
		WHERE corrections.user_id = users.id
	)
	WHERE id = usr_id;
END $$
DELIMITER ; $$

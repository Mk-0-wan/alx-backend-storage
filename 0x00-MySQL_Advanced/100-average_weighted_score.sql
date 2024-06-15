-- Calculat the weight average
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

DELIMITER $$ ;

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN usr_id INT)
BEGIN
	-- Table users will be updated with the new values
	UPDATE users
	-- Updating each average score value for a given user
	SET average_score = ( 
		-- ( score * weight_factor ) / sum( weight_factor )
		SELECT SUM(corrections.score * projects.weight) / SUM(projects.weight)
		FROM corrections
		JOIN projects
		-- ensures that the correct user is mapped to the correct weights
		ON corrections.project_id = projects.id
		-- only calculate the weight score of the given user	
		WHERE corrections.user_id = usr_id
	)
	WHERE id = usr_id;
END $$
DELIMITER ; $$

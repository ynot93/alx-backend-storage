-- Create a stored procedure that computes the average weighted score for a student
-- Drop the procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

-- Create the stored procedure
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN user_id INT
)
BEGIN
    -- Declare variable for storing the weighted average
    DECLARE weighted_avg FLOAT;

    -- Calculate weighted average score
    SELECT SUM(score * weight) / SUM(weight)
    INTO weighted_avg
    FROM corrections
    JOIN projects ON corrections.project_id = projects.id
    WHERE corrections.user_id = user_id;

    -- Update the average_score in the users table
    UPDATE users SET average_score = weighted_avg WHERE id = user_id;
END$$

DELIMITER ;

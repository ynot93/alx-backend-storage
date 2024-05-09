-- Create a stored procedure that computes and store the average score for a student
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    -- Variable to hold the average score
    DECLARE avg_score FLOAT;

    -- Compute the average score for the user
    SELECT AVG(score) INTO avg_score FROM corrections WHERE user_id = user_id;

    -- Update the average_score field in the users table
    UPDATE users SET average_score = avg_score WHERE id = user_id;
END$$

DELIMITER ;

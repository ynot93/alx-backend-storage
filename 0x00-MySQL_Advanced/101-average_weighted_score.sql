-- Create a stored procedure that computes the average weighted score for all students

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    -- Declare cursor and variables for iterating over users
    DECLARE done INT DEFAULT FALSE;
    DECLARE curr_user_id INT;
    DECLARE curr_weighted_avg FLOAT;
    DECLARE user_cursor CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN user_cursor;

    user_loop: LOOP
        FETCH user_cursor INTO curr_user_id;
        IF done THEN
            LEAVE user_loop;
        END IF;

        SELECT SUM(score * weight) / SUM(weight)
        INTO curr_weighted_avg
        FROM corrections
        JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = curr_user_id;

        UPDATE users SET average_score = curr_weighted_avg WHERE id = curr_user_id;
    END LOOP;

    CLOSE user_cursor;
END$$

DELIMITER ;

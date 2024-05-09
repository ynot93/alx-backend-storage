-- Create a stored procedure that adds a new correction for a student
DELIMITER $$

CREATE PROCEDURE AddBonus(
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score INT
)
BEGIN
    -- Variable to hold the project_id
    DECLARE project_id INT;

    -- Check if the project already exists
    SELECT id INTO project_id FROM projects WHERE name = project_name LIMIT 1;

    -- If the project does not exist, insert it and get the new project_id
    IF project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = LAST_INSERT_ID();
    END IF;

    -- Insert the new correction with the obtained or new project_id
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END$$

DELIMITER ;

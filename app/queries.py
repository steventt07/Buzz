QUERY_CHECK_CONNECTION = """
    SELECT 1;
"""
# need to create a join for comments and make comments a json list
QUERY_GET_FEED = """
	SELECT 
		post_table.post_id,
		post_table.username,
		post_table.category_name,
		post_table.title,
		post_table.content,
		post_table.votes,
		CASE WHEN vote_table.direction is NULL THEN false ELSE true END AS is_voted,
		vote_table.direction,
		post_table.zipcode,
		post_table.date_created,
		post_table.comment_ids
	FROM 
		post_table
	LEFT JOIN 
        vote_table on vote_table.post_id = post_table.post_id AND vote_table.username = %s
	WHERE zipcode = %s AND is_deleted = false AND is_reported = false
	ORDER BY
		date_created DESC;
"""

QUERY_GET_CATEGORY = """
	SELECT 
		post_table.post_id,
		post_table.username,
		post_table.category_name,
		post_table.title,
		post_table.content,
		post_table.comment_ids,
		post_table.votes,
		CASE WHEN vote_table.direction is NULL THEN false ELSE true END AS is_voted,
		vote_table.direction,
		post_table.zipcode,
		post_table.date_created,
		post_table.comment_ids
	FROM 
		post_table
	LEFT JOIN 
        vote_table on vote_table.post_id = post_table.post_id AND vote_table.username = %s
	WHERE category_name = %s AND zipcode = %s AND is_deleted = false AND is_reported = false
	ORDER BY
		date_created DESC;
"""

QUERY_GET_DELETED_POST = """
	SELECT 
		post_table.post_id,
		post_table.username,
		post_table.category_name,
		post_table.title,
		post_table.content,
		post_table.comment_ids,
		post_table.votes,
		CASE WHEN vote_table.direction is NULL THEN false ELSE true END AS is_voted,
		vote_table.direction,
		post_table.zipcode,
		post_table.date_created,
		post_table.comment_ids
	FROM 
		post_table
	LEFT JOIN 
        vote_table on vote_table.post_id = post_table.post_id AND vote_table.username = %s
	WHERE post_table.is_deleted = true
	ORDER BY
		date_created DESC;
"""

QUERY_GET_REPORTED_POST = """
	SELECT 
		post_table.post_id,
		post_table.username,
		post_table.category_name,
		post_table.title,
		post_table.content,
		post_table.comment_ids,
		post_table.votes,
		CASE WHEN vote_table.direction is NULL THEN false ELSE true END AS is_voted,
		vote_table.direction,
		post_table.zipcode,
		post_table.date_created,
		post_table.comment_ids
	FROM 
		post_table
	LEFT JOIN 
        vote_table on vote_table.post_id = post_table.post_id AND vote_table.username = %s
	WHERE post_table.is_reported = true
	ORDER BY
		date_created DESC;
"""

QUERY_GET_USER = """
	SELECT
		username,
		email,
		date_joined
	FROM
		user_table
	WHERE 
		username = %s AND password = %s;
		
"""

QUERY_INSERT_POST_TO_CATEGORY = """
	INSERT INTO post_table(
		username,
		category_name,
		title,
		content,
		zipcode,
		date_created
	)
	VALUES (%s, %s, %s, %s, %s, %s);
"""

QUERY_INSERT_USER = """
	INSERT INTO user_table(
		username,
		password,
		email,
		date_joined
	)
	VALUES (%s, %s, %s, %s);
"""

QUERY_INSERT_CATEGORY = """
	INSERT INTO category_table(
		category_name,
		owner_username,
		date_created
	)
	VALUES (%s, %s, %s);
"""

QUERY_REMOVE_POST_FROM_CATEGORY = """
	UPDATE 
		post_table
	SET
		is_deleted = true,
		date_edited = %s
	WHERE post_id = %s AND category_name = %s;
"""

QUERY_UPVOTE_DOWNVOTE_POST = """
	UPDATE 
		post_table
	SET
		votes = votes + %s
	WHERE post_id = %s;
"""

QUERY_INSERT_VOTE = """
	INSERT INTO vote_table(
		post_id,
		username,
		direction,
		date_created
	)
	VALUES (%s, %s, %s, %s);
"""

QUERY_UPDATE_VOTE = """
	UPDATE 
		vote_table
	SET
		direction = %s,
		date_changed = %s
	WHERE post_id = %s AND username = %s;
"""

QUERY_INSERT_COMMENT = """
	INSERT INTO comment_table(
		post_id,
		username,
		content,
		date_created
	)
	VALUES (%s, %s, %s, %s);
"""
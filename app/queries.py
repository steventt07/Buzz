QUERY_CHECK_CONNECTION = """
    SELECT 1;
"""
# need to create a join for comments and make comments a json list
QUERY_GET_FEED = """
	SELECT 
		post_id,
		username,
		category_name,
		title,
		content,
		comment_ids,
		up_vote,
		down_vote,
		zipcode,
		date_created
	FROM 
		post_table
	WHERE zipcode = %s AND is_deleted = false AND is_reported = false
	ORDER BY
		date_created DESC;
"""

QUERY_GET_CATEGORY = """
	SELECT 
		post_id,
		username,
		category_name,
		title,
		content,
		comment_ids,
		up_vote,
		down_vote,
		zipcode,
		date_created
	FROM 
		post_table
	WHERE category_name = %s AND zipcode = %s AND is_deleted = false AND is_reported = false
	ORDER BY
		date_created DESC;
"""

QUERY_GET_DELETED_POST = """
	SELECT 
		post_id,
		username,
		category_name,
		title,
		content,
		comment_ids,
		up_vote,
		down_vote,
		zipcode,
		date_created
	FROM 
		post_table
	WHERE is_deleted = true
	ORDER BY
		date_created DESC;
"""

QUERY_GET_REPORTED_POST = """
	SELECT 
		post_id,
		username,
		category_name,
		title,
		content,
		comment_ids,
		up_vote,
		down_vote,
		zipcode,
		date_created
	FROM 
		post_table
	WHERE is_reported = true
	ORDER BY
		date_created DESC;
"""

QUERY_GET_USER = """
	SELECT
		username,
		date_joined
	FROM
		user_table
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
		date_joined
	)
	VALUES (%s, %s, %s);
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
	WHERE post_id = %s AND category_name = %s
"""
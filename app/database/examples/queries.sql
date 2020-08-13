-- QUERY_GET_CATEGORY
SELECT 
	post_id,
	username,
	category_name,
	content,
	comment_ids,
	votes,
	zipcode,
	date_created
FROM 
	post_table
WHERE category_name = 'What''s happening?' AND zipcode = '78703' AND is_deleted = false AND is_reported = false
ORDER BY
	date_created DESC;

-- QUERY_GET_FEED
SELECT 
	post_id,
	username,
	category_name,
	content,
	comment_ids,
	votes,
	zipcode,
	date_created
FROM 
	post_table
WHERE zipcode = '78703'
	AND is_deleted = false AND is_reported = false
ORDER BY
	date_created DESC;
	
-- QUERY_REMOVE_POST_FROM_CATEGORY
UPDATE 
	post_table
SET
	is_deleted = true,
	date_edited = '2020-08-12'
WHERE post_id = 3 AND category_name = 'What''s happening?'

-- QUERY_GET_DELETED_POST
SELECT 
	post_id,
	username,
	category_name,
	content,
	comment_ids,
	votes,
	zipcode,
	date_created
FROM 
	post_table
WHERE is_deleted = true
ORDER BY
	date_created DESC;
	
-- QUERY_GET_REPORTED_POST
SELECT 
	post_id,
	username,
	category_name,
	content,
	comment_ids,
	votes,
	zipcode,
	date_created
FROM 
	post_table
WHERE is_reported = true
ORDER BY
	date_created DESC;
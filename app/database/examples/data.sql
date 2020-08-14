INSERT INTO user_table(
        username,
        password,
        date_joined
	)
VALUES ('steventt07', 'password', NOW());


INSERT INTO category_table(
        category_name,
        owner_username,
        date_created
	)
VALUES ('What''s happening?', 'steventt07', NOW());

INSERT INTO post_table(
        username,
        category_name,
		title,
        content,
        zipcode,
        date_created
	)
VALUES ('steventt07', 'What''s happening?', 'DEALS!!!', 'My first post', '78703', NOW());
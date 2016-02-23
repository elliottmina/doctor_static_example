var data = {
	metaData:{{ meta_data|tojson }},
	tagMap:{{ tag_map|tojson }},
	key:{{ key|tojson }},
	manifest:{{ manifest|tojson }},
	chron_list:{{ chron_list|tojson }}
};

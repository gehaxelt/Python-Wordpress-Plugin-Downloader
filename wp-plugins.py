#!/usr/bin/env python3

import requests
import re

BASEURL = "https://wordpress.org/plugins/browse/popular/"
DESTFILE = "plugins.txt"
TAGS = ["admin", "administration", "ads", "adsense", "advertising", "affiliate", "AJAX", "amazon", "analytics", "api", "audio", "authentication", "author", "automatic", "bbPress", "blog", "buddypress", "button", "calendar", "captcha", "categories", "category", "Chat", "cms", "code", "comment", "comments", "contact", "contact", "form", "content", "CSS", "custom", "custom", "post", "type", "dashboard", "database", "Digg", "e-commerce", "easy", "ecommerce", "edit", "editor", "email", "embed", "event", "events", "Facebook", "feed", "filter", "flash", "flickr", "form", "Formatting", "forms", "free", "gallery", "google", "google", "analytics", "google", "maps", "google", "plus", "html", "html5", "image", "images", "import", "integration", "iphone", "javascript", "jquery", "language", "lightbox", "Like", "link", "linkedin", "links", "list", "login", "mail", "map", "maps", "marketing", "media", "menu", "meta", "mobile", "multisite", "music", "navigation", "network", "News", "newsletter", "notification", "page", "pages", "password", "payment", "paypal", "performance", "photo", "photos", "php", "picture", "pictures", "pinterest", "plugin", "plugins", "popup", "Post", "posts", "profile", "random", "redirect", "registration", "responsive", "rss", "search", "security", "seo", "Share", "sharing", "shop", "shortcode", "shortcodes", "sidebar", "simple", "slider", "slideshow", "social", "social", "media", "spam", "statistics", "stats", "store", "tag", "tags", "Taxonomy", "template", "text", "theme", "themes", "thumbnail", "thumbnails", "TinyMCE", "title", "tracking", "tweet", "twitter", "upload", "url", "user", "users", "video", "vimeo", "widget", "widgets", "woocommerce", "wordpress", "wpmu", "xml", "yahoo", "youtube"]
TAGURL = "https://wordpress.org/plugins/tags/"
regex = re.compile(r'name column-name.+?href="(.*?)">(.*?)</a>.+?column-installs">(.*?)</div>', flags=re.MULTILINE)


def create_list(wp_url, file):
	page = 1
	has_next = True
	while has_next:
		content = ""
		try:
			print("Fetching page... " + str(page))
			r = requests.get(wp_url+"page/"+str(page))
			content = str(r.content)
		except:
			pass
		matches = regex.findall(content)
		if matches:
			print("Found plugins..." + str(len(matches)))
			for match in matches:
				url, name, installs = match
				installs = installs.replace('\\t',"").replace('\\n',"")
				file.write(name + "||" + url + "||" + installs + "\n")
				file.flush()
		if not "Next &raquo;" in content:
			has_next = False
		page += 1

f = open(DESTFILE, "w")

for tag in TAGS:
	tag = tag.lower()
	print("Checking... " + tag)
	url = TAGURL + tag + "/"
	create_list(url, f)

f.close()
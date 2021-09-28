from time import sleep
from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge
from instapy import InstaPy

#LOGIN CODE FOR EDGE ONLY
"""
options = EdgeOptions()
options.use_chromium = True
browser = Edge(options = options)
browser.implicitly_wait(5)
browser.get("https://www.instagram.com/")
username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")
username_input.send_keys("<username>")
password_input.send_keys("<password>")
login_button = browser.find_element_by_xpath("//button[@type ='submit']")
login_button.click()
sleep(5)
browser.close()
"""
#THIS IS FOR FIREFOX ONLY

accuser = "<username>"
accpass = "<password>"
targetTags = ["dogs"] 
avoidTags = ["NSFW", "NSFL"]
commentWords = ["cute!", "adorable!", "how sweet!"] #array of comment choices


session = InstaPy(username=accuser, password = accpass).login()

session.like_by_tags(targetTags, amount = 1) #Like 10 posts from each tag. Default: 9 + amount
session.dont_like(avoidTags)

session.set_comments(commentWords)
session.set_do_comment(enabled = True, percentage = 20)


session.end()
#ends the whole session safely

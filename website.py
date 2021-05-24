# 1. Run `python -V` and make sure you have python 3.7+
# 2. Run `pip install -U splashgen`
# 3. Put your logo in the same directory, and name it "logo.png"
# 4. Put the chat image in the same directory, and name it "hero.png"
# 5. Replace <SIGNUP_FORM_URL> with your mailchimp signup form URL.
#   See: https://github.com/true3dco/splashgen#adding-a-mailchimp-signup-form
# 6. Run `splashgen website.py`
# 7. Run `python -m http.server --directory build`
# You should now see your site at http://localhost:8000

from os import path

from splashgen import launch
from splashgen.components import SplashSite
from splashgen.integrations import MailchimpSignup

site = SplashSite(title="Frempco - instant improv chats",
                  logo=path.join(path.dirname(__file__), "images/logo.png"),
                  theme="dark")
site.headline = "We empower your students with improv"
site.subtext = """
We teach creative writing to 6th-12th graders. Students pick characters and start talking
as them. Through text based improv, teenagers build friendships and tell stories together.
"""
site.call_to_action = MailchimpSignup(
    "http://eepurl.com/gOtuTz", "Join our pilot")
site.hero_image = path.join(path.dirname(__file__), "images/hero.png")

launch(site)
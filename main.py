from blacksheep import Application
from blacksheep.server.authorization import auth
from guardpost.common import AuthenticatedRequirement, Policy

from blacksheep.server.authentication.jwt import JWTBearerAuthentication

from dotenv import load_dotenv
import os

load_dotenv()

app = Application()

app.use_authentication().add(
	JWTBearerAuthentication(
		authority=os.environ.get("AUTHORITY"),
		valid_audiences=[os.environ.get("AUDIENCE")],
		valid_issuers=[os.environ.get("ISSUERS")],
	)
)

authorization = app.use_authorization()

authorization += Policy("any_name", AuthenticatedRequirement())

get = app.router.get

@get("/")
def home():
	return "Hello, World"


@auth("any_name")
@get("/api/message")
def example():
    return "This is only for authenticated users"		
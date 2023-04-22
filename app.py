from flask import Flask, request
import requests

app = Flask(__name__)


# @Route POST /v1/role
# @desc Create a new role from given data

@app.route('/v1/role/', methods=['POST'])
def create_new_role():
    data = request.get_json()
    req_data = requests.post('https://community-the-internet-folks.onrender.com/v1/role', data=data)
    required_data = req_data.json()
    return required_data

# @Route GET /v1/role
# @desc List all the roles

@app.route('/v1/role', methods=['GET'])
def get_all_roles():
    page = request.args.get('page')
    pageSize = request.args.get('pageSize')
    
    if page == None:
        page = 1

    if pageSize == None:
        pageSize = 10

    roles = requests.get('https://community-the-internet-folks.onrender.com/v1/role?page={}&pageSize={}'.format(page, pageSize)).json()

    return roles

# @route POST /v1/auth/signup
# @desc Create a new user from given data

@app.route('/v1/auth/signup', methods=['POST'])
def signup():
    user_data = request.get_json()

    created_user = requests.post('https://community-the-internet-folks.onrender.com/v1/auth/signup', data=user_data).json()

    return created_user

# @Route POST /v1/auth/signin
# @desc Sign in user from the valid credentials and generate access token

@app.route('/v1/auth/signin', methods=['POST'])
def signin():
    user_data = request.get_json()

    access_token = requests.post('https://community-the-internet-folks.onrender.com/v1/auth/signin', data=user_data).json()

    return access_token


# @Route GET /v1/auth/me 
# auth header required
# @desc Return the details of currently signed in user

@app.route('/v1/auth/me', methods=['GET'])
def get_me():

    access_token = request.headers.get("authorization")

    headers = {
        "Content-Type": "application/json"
    }

    if access_token != None:
        headers["authorization"] = access_token

    user_data = requests.get('https://community-the-internet-folks.onrender.com/v1/auth/me', headers=headers).json()

    return user_data

# @Route /v1/community
# auth header required
# @desc Create a new community from given data

@app.route('/v1/community', methods=['POST'])
def create_community():

    access_token = request.headers.get("authorization")

    community_data = request.get_json()

    headers = {
        "Content-Type": "application/json"
    }

    if access_token != None:
        headers["authorization"] = access_token

    created_community = requests.post('https://community-the-internet-folks.onrender.com/v1/community', json=community_data, headers=headers).json()

    return created_community

# @Route GET /v1/community
# @desc List all the communities

@app.route('/v1/community', methods=['GET'])
def get_all_communities():
    page = request.args.get('page')
    pageSize = request.args.get('pageSize')

    if page == None:
        page = 1

    if pageSize == None:
        pageSize = 10

    communities = requests.get('https://community-the-internet-folks.onrender.com/v1/community?page={}&pageSize={}'.format(page, pageSize)).json()

    return communities

# @Route GET /v1/community/<id>/members
# @desc List all the members of a community

@app.route('/v1/community/<id>/members', methods=['GET'])
def get_all_members_community(id):

    page = request.args.get('page')
    pageSize = request.args.get('pageSize')

    if page == None:
        page = 1

    if pageSize == None:
        pageSize = 10

    members = requests.get('https://community-the-internet-folks.onrender.com/v1/community/{}/members?page={}&pageSize={}'.format(id, page, pageSize)).json()

    return members

# @Route GET /v1/community/me/owner
# auth header required
# @desc Get all the owned communities of signed in user

@app.route('/v1/community/me/owner', methods=['GET'])
def get_my_owned_communities():

    access_token = request.headers.get("authorization")
    page = request.args.get("page")
    pageSize = request.args.get("pageSize")

    headers = {
        "Content-Type": "application/json"
    }

    if access_token != None:
        headers["authorization"] = access_token

    if page == None:
        page = 1

    if pageSize == None:
        pageSize = 10

    my_owned_communities = requests.get('https://community-the-internet-folks.onrender.com/v1/community/me/owner?page={}&pageSize={}'.format(page, pageSize), headers=headers).json()

    return my_owned_communities

# @Route GET /v1/community/me/member
# auth header required
# @desc Get all the joined communities of the signed in user

@app.route('/v1/community/me/member', methods=['GET'])
def get_my_joined_communities():
    
    access_token = request.headers.get("authorization")
    page = request.args.get("page")
    pageSize = request.args.get("pageSize")

    headers = {
        "Content-Type": "application/json"
    }

    if access_token != None:
        headers["authorization"] = access_token

    if page == None:
        page = 1

    if pageSize == None:
        pageSize = 10

    my_joined_communities = requests.get('https://community-the-internet-folks.onrender.com/v1/community/me/member?page={}&pageSize={}'.format(page, pageSize), headers=headers).json()

    return my_joined_communities

# @Route POST /v1/member
# auth header required
# @desc Adding a member to the community

@app.route('/v1/member', methods=['POST'])
def add_new_member():

    access_token = request.headers.get("authorization")
    
    headers = {
        "Content-Type": "application/json"
    }

    if access_token != None:
        headers["authorization"] = access_token

    member_data = request.get_json()

    joined_member = requests.post('https://community-the-internet-folks.onrender.com/v1/member', json=member_data, headers=headers).json()

    return joined_member

# @Route DELETE /v1/member/<id>
# auth header is required
# @desc Removing a user from the communities

@app.route('/v1/member/<id>', methods=['DELETE'])
def remove_member(id):

    access_token = request.headers.get("authorization")
    
    headers = {
        "Content-Type": "application/json"
    }

    if access_token != None:
        headers["authorization"] = access_token

    remove_response = requests.delete('https://community-the-internet-folks.onrender.com/v1/member/{}'.format(id), headers=headers).json()

    return remove_response

if __name__ == "__main__":
    app.run(debug=True)

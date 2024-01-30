import pyotp

users = {'user_1' : {'passwords' : 'ftfdoreahvondee0#', 'one_time_code' : 'ATA03RB081TA090008G'}}
#this would be stored for a each user
#and also the one time authentication code as well

#Creating a random code for the Multi-Factor Authentication for the user 
def generate_one_time_code() :
    return pyotp.random_base32() #You can also use random16()


def authenticate_for_the_user(username, password, totp_code):

    if username in users:
        user_info = users[username]
        if user_info['password'] == password:
            totp = pyotp.TOTP(user_info['one_time_code'])
            if totp.verify(totp_code):
                return True
            return False
        
#this main function here is for the user usage

if __name__ == '__main__' :
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    totp_code = input('Enter your 6-digit TOTP code')

if authenticate_for_the_user(username, password, totp_code):
    print('User Authentication Successful')
else:
    print('User Authentication Failed')
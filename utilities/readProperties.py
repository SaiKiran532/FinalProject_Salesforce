import configparser
config = configparser.RawConfigParser()
path = "C:\\Users\\saikiran.challa\\PycharmProjects\\pythonProject5\\Configurations\\config.ini"
config.read(path)

class ReadConfig:
    @staticmethod
    def get_Application_url():
        url = config.get('common info', 'pageurl')
        return url

    @staticmethod
    def get_user_name():
        user_name = config.get('common info', 'original_username')
        return user_name

    @staticmethod
    def get_password():
        pass_word = config.get('common info', 'original_password')
        return pass_word

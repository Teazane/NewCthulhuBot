from src.bot import Bot
import configparser

def main():
    config = configparser.ConfigParser()
    config.read('token.config')
    client = Bot()
    client.run(config['DEFAULT']['token'])

if __name__ == "__main__":
    main()

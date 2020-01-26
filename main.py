from bot import Bot
import configparser

def main():
    config = configparser.ConfigParser()
    config.read('token.config')
    client = Bot()
    print(config['DEFAULT']['token'])
    client.run(config['DEFAULT']['token'])

if __name__ == "__main__":
    main()

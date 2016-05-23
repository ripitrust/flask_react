import argparse
from config import Config
from worker import Worker



def main():

    parser = argparse.ArgumentParser(description='a quick setup tool for flask and react project')
    parser.add_argument('name', help='The name of the project')
    parser.add_argument('-p', '--path', dest='path', help='The path of the project', default='.')
    args = parser.parse_args()

    config = Config(name=args.name, path=args.path)
    w = Worker(config=config)
    w.work()

if __name__ == '__main__':

    main()

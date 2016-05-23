import subprocess
import os


class Worker(object):

    def __init__(self, config):

        self.config = config
        os.chdir(config.path)

    def create_virenv(self):
        subprocess.call(['virtualenv', self.config.name])
        os.chdir(os.path.abspath(self.config.name))
        os.mkdir('project')
        os.chdir('project')

    def create_app(self):

        app_dir = ['static', 'templates', 'main']

        app_code = """from app import create_app\n\
app = create_app(debug=True)\n\

if __name__ == '__main__':
    app.run(port=9999)
    """

        with open('app.py', 'w') as f:

            f.write(app_code)

        os.mkdir('app')
        os.chdir('app')

        for name in app_dir:

            os.mkdir(name)

        init_code = """from flask import Flask\n\
def create_app(debug=True):\n\
    app = Flask(__name__)\n\
    app.debug = debug \n\
    from .main import main as main_blueprint\n\
    app.register_blueprint(main_blueprint)\n\
    return app
"""

        with open('__init__.py', 'w') as f:
            f.write(init_code)

    def create_react(self):

        os.chdir(os.path.abspath('templates'))

        html_code = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <script src = "../static/dist/vendor.bundle.js"></script>
    <title>Project</title>
  </head>
  <body>
    <div id="app"></div>
    <script src = "../static/dist/main.bundle.js"></script>
  </body>
</html>
        """

        with open('index.html', 'w') as f:

            f.write(html_code)

        os.chdir(os.path.abspath('../static/'))

        with open('webpack.config.js', 'w') as f:

            webpack_code = """
var path = require('path');
var webpack = require('webpack');

var ROOT_PATH = path.resolve(__dirname);
var node_modules_dir = path.resolve(__dirname, 'node_modules');

var plugin = [];

if (process.env.NODE_ENV === 'production') {

    plugin.push( new webpack.optimize.UglifyJsPlugin({ compress: { warnings: false }, output: {comments:false} }));

}

plugin.push(new webpack.optimize.CommonsChunkPlugin("vendor", "vendor.bundle.js"));

module.exports = {
    entry: {

        vendor:[
            'react',
            'react-dom'
        ],
        main: [
                "./src/app/index.js",
        ]
        },

    plugins: plugin,

    output: {
        path: path.resolve(ROOT_PATH , 'dist'),
        filename: '[name].bundle.js'
        },
    module: {
      loaders: [
        {
          test: /\.jsx?$/,
          loaders: ['babel'],
          include: path.resolve(ROOT_PATH, 'src')

        },

        { test: /\.css$/,
          loader: 'style-loader!css-loader'
        },

        {
        test: /\.(eot|woff|woff2|ttf|svg|png|jpg)$/,
        loader: 'url-loader?limit=30000&name=[name]-[hash].[ext]'
        }

      ]
    }
  };"""

            f.write(webpack_code)

        with open('package.json', 'w') as f:

            package_json_code = """
{
  "name":"Project",
  "version": "0.0.1",
  "babel": {
    "presets": [
      "react",
      "es2015",
      "stage-2",
      "stage-0"
    ]
  },
  "description": "",
  "main": "index.js",
  "dependencies": {
    "babel-core": "^6.0.0",
    "babel-loader": "^6.0.0",
    "babel-preset-es2015": "^6.0.0",
    "babel-preset-react": "^6.0.0",
    "babel-preset-stage-0": "^6.0.0",
    "babel-preset-stage-2": "^6.0.0",
    "css-loader": "^0.23.0",
    "react": "^15.0.0",
    "react-dom": "^15.0.0",
    "react-loader": "^2.0.0",
    "style-loader": "^0.13.1",
    "url-loader": "^0.5.6",
    "webpack": "^1.13.0"
  },
  "devDependencies": {
  },
  "scripts": {
    "test": "echo \\"Error: no test specified\\" && exit 1"
  },
  "author": "",
  "license": ""
}
            """

            f.write(package_json_code)

        os.mkdir('app')
        os.mkdir('src')

    def work(self):

        self.create_virenv()
        self.create_app()
        self.create_react()















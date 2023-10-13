const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = {
  mode: "production",
  entry: "./flashcard/static/base.js",
  plugins: [
    new HtmlWebpackPlugin({
      template: "./flashcard/templates/main.html",
    }),
  ],
  output: {
    filename: "flashcard.js",
    path: path.resolve(__dirname, "notebook", "static", "dist"),
  },

  module: {
    rules: [
      {
        test: /\.css$/,
        use: [
          {
            loader: "css-loader",
            options: {
              modules: true,
            },
          },
        ],
      },
    ],
  },
};


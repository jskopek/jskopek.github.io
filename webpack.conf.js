const webpack = require('webpack');

module.exports = {
    context: baseDir,
    entry: {
        'video-page': './assets/video-page.js',
    },
    output: {
        path: './assets/',
        filename: '[name].bundle.js'
    },
    plugins: [
        new webpack.HotModuleReplacementPlugin(),
        new webpack.ProvidePlugin({
            $: 'jquery',
            jQuery: 'jquery',
            _: "lodash",
            'window.jQuery': 'jquery',
            Popper: ['popper.js', 'default'],
        }),
    ],
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/, 
                loader: 'babel-loader' 
            }
        ]
    }
};

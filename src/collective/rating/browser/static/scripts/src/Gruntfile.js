module.exports = function(grunt) {
  'use strict';
  require('load-grunt-tasks')(grunt);
  grunt.initConfig({
    uglify: {
      pikaday: {
        options: {
          sourceMap: true,
          sourceMapIncludeSources: false,
        },
        files: {
          '../rating-compile.min.js': ['./bundle-compiled.js'],
        },
      },
    },
    requirejs: {
      'rating-plugin': {
        options: {
          baseUrl: './',
          generateSourceMaps: true,
          preserveLicenseComments: false,
          paths: {
            jquery: 'empty:',
            rating: './jquery.star-rating-svg',
          },
          // shim: {
          //   rating: {
          //     deps: ['jquery'],
          //     exports: '$.fn.starRating',
          //   },
          // },
          wrapShim: true,
          name: './rating.js',
          exclude: ['jquery'],
          out: './bundle-compiled.js',
          optimize: 'none',
        },
      },
    },
  });

  grunt.registerTask('compile', ['requirejs', 'uglify']);
};

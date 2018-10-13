var gulp = require('gulp');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var sourcemaps = require('gulp-sourcemaps');



function bundleJavascriptsInDevMode() {
    console.log('Bundling JS files in development mode');
    gulp.src([
        'assets/js/src/application.js',
        'assets/js/src/ui-scripts.js',
        'assets/js/src/landing/landing.js',
        'assets/js/src/scanner/scanner.js'

        // 'assets/js/src/**/*.js'
    ])
        .pipe(concat('application.js'))
        .pipe(gulp.dest('./dist/'));
}

function bundleJavascriptsInProdMode() {
    console.log('Bundling JS files in production mode');
    gulp.src([
      'assets/js/src/**/*.js',
      'assets/js/src/landing/landing.js',
      'assets/js/src/scanner/scanner.js'
    ])
        .pipe(sourcemaps.init())
        .pipe(concat('application.min.js'))
        .pipe(uglify())
        .pipe(sourcemaps.write('./maps'))
        .pipe(gulp.dest('./dist/'))

}

function compileJavascriptsLibs(){
  console.log('Compiling JS libs');
    gulp.src([
        'assets/js/libs/jquery-3.2.1.js',
        'assets/js/libs/jquery-ui.js',
        'assets/js/libs/select2.full.js',
        'assets/js/libs/slick.js'
])
          .pipe(sourcemaps.init())
          .pipe(concat('libs.min.js'))
          .pipe(uglify())
          .pipe(sourcemaps.write('./maps'))
          .pipe(gulp.dest('./dist/'))

}

module.exports = {
  development: bundleJavascriptsInDevMode,
  production: bundleJavascriptsInProdMode,
  libraries: compileJavascriptsLibs
};

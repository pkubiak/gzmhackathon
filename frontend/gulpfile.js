var gulp = require('gulp');

// This file goes like:
// [1] Import tasks from external files (all but "watch" tasks which are defined below, "one shot")
// [2] Define paths to files you want to watch
// [3] Declare your tasks in aesthetic way
// [4] Watching functions ("continuous")
// [5] Some helpers

// import tasks from external files
var jsTask = require('./gulp_tasks/js');
var sassTask = require('./gulp_tasks/sass');

// declare locations of files to watch
var source_files = {
    js: 'assets/**/*.js',
    sass: 'assets/**/*.scss'
};

// just timeout handling variable for "watch" tasks
var heartbeat;

// TASKS DECLARATIONS

// default task -> watching changes in JS and SASS files
gulp.task('default', recompileFilesInDevelopmentMode);

// bundling javascript files in development mode
gulp.task('js_dev', jsTask.development);

// bundling javascript files in production mode
gulp.task('js_prod', jsTask.production);

// mapping javascript in development mode
gulp.task('js_libs', jsTask.libraries);

// mapping javascript in production mode
gulp.task('js_map_prod', jsTask.mappingProd);

// styles compilation in development mode
gulp.task('sass_dev', sassTask.development);

// styles compilation in production mode
gulp.task('sass_prod', sassTask.production);

// creating styles documentation using gulp-sassdoc
gulp.task('sass_doc', sassTask.documentation);

// watch .scss files and compile expanded stylesheet [.scss]
gulp.task('watch_sass', followChangesInStyles);

// watch .js file and bundle JS in development mode [.js]
gulp.task('watch_js', followChangesInScripts);

// watch all files declared in source_files [.js, .scss]
gulp.task('watch', recompileFilesInDevelopmentMode);

// WATCHING FUNCTIONS

function followChangesInStyles() {

    console.log('Watching SCSS...');

    if(heartbeat) stopHeartbeat();
    setHeartbeat();

    gulp
        .watch(source_files.sass, ['sass_dev'])
        .on('change', watchMessages);

}

function followChangesInScripts() {

    console.log('Watching JS...');

    if(heartbeat) stopHeartbeat();
    setHeartbeat();

    gulp
        .watch(source_files.js, ['js_dev'])
        .on('change', watchMessages);

}

function recompileFilesInDevelopmentMode() {

    getArrayOfAllSourceFiles();

    console.log('Watching JS and SCSS...');

    if(heartbeat) stopHeartbeat();
    setHeartbeat();

    followChangesInScripts();
    followChangesInStyles();

}


// HELPER FUNCTIONS

function watchMessages (event) {
    console.log('File ' + event.path + ' was ' + event.type + ', running tasks...');
}

function getArrayOfAllSourceFiles() {

    var resultArray = [];

    for(var key in source_files) {
        resultArray.push(source_files[key]);
    }

    console.log('## Paths to resources:');
    console.log('    >> ' + resultArray.join('\n    >> '));

    return resultArray;
}

var stopHeartbeat = function() {

    console.log('Stop listening');

    clearInterval(heartbeat);

};

var setHeartbeat = function(){

    console.log('Start listening');

    heartbeat = setInterval(function() {
        console.log('Listening...');
    },5000);

};

<?php
// Helper functions
function loadPartial($name) {
    return include('./partials/'.$name);
}

// Simple routing
// Grabs the URI and breaks it apart in case we have querystring stuff
$request_uri = explode('?', $_SERVER['REQUEST_URI'], 2);
switch ($request_uri[0]) {

    // Main pages routes
    case '/':
        require './pages/main.php';
        break;
    case '/line':
        require './pages/line.php';
        break;

    // Everything else
    default:
        header('HTTP/1.0 404 Not Found');
        require './pages/404.php';
        break;
}

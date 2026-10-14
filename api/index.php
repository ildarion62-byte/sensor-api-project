<?php
require __DIR__ . '/vendor/autoload.php';

header('Content-Type: application/json; charset=utf-8');
header('Access-Control-Allow-Origin: *');

$router = new \Bramus\Router\Router();

$router->get('/', function() {
    $dataFile = __DIR__ . '/data.json';
    if (file_exists($dataFile)) {
        echo file_get_contents($dataFile);
    } else {
        http_response_code(404);
        echo json_encode(["error" => "Data source not found"]);
    }
});

$router->run();
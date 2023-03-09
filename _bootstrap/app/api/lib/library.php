<?php 
// TODO: figure out how the heck to get vendor folder to not be overwritten 
$dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
$dotenv->load();

$api = new RestClient([
    'base_url' => "https://awx.demo.netapp.com/api/v2/tokens", 
    'format' => "json", 
    'username' => $_ENV['USERNAME'],
    'password' => $_ENV['PASSWORD'],
    'parameters' => [
        'description' => 'Token for provisioning app',
        'application' => 1,
        'scope' => 'write'
    ]
]);

print($api->response);
print('hello');
exit;
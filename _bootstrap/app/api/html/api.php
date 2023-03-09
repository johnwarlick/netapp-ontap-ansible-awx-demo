<?php 
header('Content-Type: application/json');

//require(__DIR__ . '/../lib/library.php');
response(200,"Hello World",$_POST);

function response($status,$message,$data="")
{
	header("HTTP/1.1 ".$status);
	
	$response['status']=$status;
	$response['message']=$message;
	$response['data']=$data;
	
	$json_response = json_encode($response);
	echo $json_response;
}
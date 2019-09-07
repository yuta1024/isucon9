<?php

use Slim\App;
use Slim\Http\Request;
use Slim\Http\Response;
use Slim\Http\StatusCode;

return function (App $app) {
    $container = $app->getContainer();

    // API
    $app->post('/initialize', \App\Service::class . ':initialize');
    $app->get('/new_items.json', \App\Service::class . ':new_items');
    $app->get('/new_items/{id}.json', \App\Service::class . ':new_category_items');
    $app->get('/users/transactions.json', \App\Service::class . ':transactions');
    $app->get('/users/{id}.json', \App\Service::class . ':user_items');
    $app->get('/items/{id}.json', \App\Service::class . ':item');
    $app->post('/items/edit', \App\Service::class . ':edit');
    $app->post('/buy', \App\Service::class . ':buy');
    $app->post('/sell', \App\Service::class . ':sell');
    $app->post('/ship', \App\Service::class . ':ship');
    $app->post('/ship_done', \App\Service::class . ':ship_done');
    $app->post('/complete', \App\Service::class . ':complete');
    $app->get('/transactions/{id}.png', \App\Service::class . ':qrcode');
    $app->post('/bump', \App\Service::class . ':bump');
    $app->get('/settings', \App\Service::class . ':settings');
    $app->post('/login', \App\Service::class . ':login');
    $app->post('/register', \App\Service::class . ':register');
    $app->get('/reports.json', \App\Service::class . ':reports');

    // Frontend
    $app->get('/', \App\Service::class . ':index');
    $app->get('/login', \App\Service::class . ':index');
    $app->get('/register', \App\Service::class . ':index');
    $app->get('/timeline', \App\Service::class . ':index');
    $app->get('/categories/{id}/items', \App\Service::class . ':index');
    $app->get('/sell', \App\Service::class . ':index');
    $app->get('/items/{id:\d+}', \App\Service::class . ':index');
    $app->get('/items/{id:\d+}/edit', \App\Service::class . ':index');
    $app->get('/items/{id:\d+}/buy', \App\Service::class . ':index');
    $app->get('/buy/complete', \App\Service::class . ':index');
    $app->get('/transactions/{id}', \App\Service::class . ':index');
    $app->get('/users/{id:\d+}', \App\Service::class . ':index');
    $app->get('/users/setting', \App\Service::class . ':index');
};

<?php

use Slim\App;
use Slim\Http\Request;
use Slim\Http\Response;

return function (App $app) {
    // logging
//  $app->add(function (Request $request, Response $response, callable $next) {
//      $route = $request->getAttribute('route');
//      $this->logger->info($request->getMethod() . ' ' . $route->getPattern(), [$route->getArguments()]);
//      $response = $next($request, $response);
//      $this->logger->info($response->getStatusCode() . ' ' . $response->getReasonPhrase(), [(string)$response->getBody()]);

//      return $response;
//  });
};

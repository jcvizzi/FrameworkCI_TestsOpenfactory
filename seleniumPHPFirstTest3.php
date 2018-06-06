<?php

require_once(__DIR__ . '/vendor/autoload.php');

$host = 'http://localhost:4444/wd/hub'; // this is the default

$driver = Facebook\WebDriver\Remote\RemoteWebDriver::create(
        $host, 
        Facebook\WebDriver\Remote\DesiredCapabilities::chrome()
    );

$driver->get("http://www.google.com");

# Find the search area
$element1=$driver->findElement(Facebook\WebDriver\WebDriverBy::id('lst-ib'));

# If ok, open  openfactory42 and find searchlink
if ($element1) {

	$driver->get("http://www.openfactory42.org");
	$element2=$driver->findElement(Facebook\WebDriver\WebDriverBy::className('icon-salient-search'));

}

# If ok, open  google, find search field, enter text into the search field and click the search button
if ($element2) {

        $driver->get("http://www.google.com");
        $driver->findElement(Facebook\WebDriver\WebDriverBy::name('q'))->click();
	$driver->findElement(Facebook\WebDriver\WebDriverBy::name('q'))->sendKeys('imprimante');
	$driver->findElement(Facebook\WebDriver\WebDriverBy::name('btnK'))->click();

}




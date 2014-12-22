#!/usr/bin/perl
#use strict;
use warnings;
use DBI;
use CGI qw(:standard);
# connects to mysql server
my $dsn= "DBI:mysql:customers";
my $username = "btc2005";
my $password = "nukes";
my %attr=(PrintError=>0,
        RaiseError=>1);
my $dbh=DBI->connect($dsn,$username,$password, \%attr);

#sub notnull() {
#my $nonull=1;
#if (!param('year')) { print 'Please enter a year', br; $nonull=0;}
#if (!param('make')) { print 'Please enter a make', br; $nonull=0;}
#if (!param('model')) { print 'Please enter a model', br; $nonull=0;}
#if (!param('price')) { print 'Please enter a price', br; $nonull=0;}
#if (!$nonull) { print 'Please fix the error and resubmit', br; } return $nonull; }
print header;

#if (param()) {
#my $ppnum= param('product_num');
#my $pyear= param('year');
#my $pmake= param('make');
#my $model= param('model');
#my $price= param('price');
#if(notnull()) {
#print qq{ Submitted successfully }}};
my $ppnum= param('product_num');
my $pyear= param('year');
my $pmake= param('make');
my $newmake= param('addmake');
my $pmodel= param('model');
my $price= param('price');
my $query2 = qq{select product_num,year,make,model,price from products};
my @make = map {$_->[2]}
        @{$dbh->selectall_arrayref($query2)};

print start_form;
print '<h2>Adding stuff</h2>';
print "Year made (YYYY): ";
print textfield('year');
print "<br>Make: ";
print popup_menu(-name=>'make', -values=>[@make],"");
print "Add make: ";
print textfield('addmake');
print submit(name=> 'Add Make'); 
print "<br>Model: ";
print textfield('model');
print '<br>Price ($): ';
print textfield('price');
print submit(name=> 'Submit All');
print button(-value=>'Home', onClick=>"window.location.href='http://btc-cems.sr.unh.edu/helloworld.html'");
print defaults('Reset fields');
print button(-name=>'Back', -value=>'Back', -onClick=>'history.back(-1)');
end_form;

#if (!$pyear || !$pmake || !$pmodel || !$price) {
#exit;
#$dbh->disconnect();
#}
my $sth=$dbh->prepare("select * from products where make='$pmake'");
$sth->execute( );
if ($pyear && $pmake && $pmodel && $price) {
$sth=$dbh->prepare("insert into products values (null,?,?,?,?)");
$sth->execute($pyear, $pmake, $pmodel, $price);}
elsif 
($pmake) {
$sth=$dbh->prepare("insert into products (make) values (?)");
$sth->execute($newmake);}
else {
exit;
$dbh->disconnect(); }

1;

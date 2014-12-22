#!/usr/bin/perl
#use strict;
use warnings;
use DBI;
use CGI qw(:standard);
my $dsn= "DBI:mysql:customers";
my $username = "btc2005";
my $password = "nukes";
my %attr=(PrintError=>0,
        RaiseError=>1);
my $dbh=DBI->connect($dsn,$username,$password, \%attr);
sub notnull() {
$nonull=1;
if (!param('name')) { print 'Please enter a customer name', br; $nonull=0;}
if (!param('city')) { print 'Please enter a city', br; $nonull=0;}
if (!param('state')) { print 'Please enter a state', br; $nonull=0;}
if (!param('country')) { print 'Please enter a country', br; $nonull=0}
if (!$nonull) { print 'Please fix the error and resubmit', hr; } return $nonull; }
print header;
if(param()) {
my $pname= param('name');
my $pcity= param('city');
my $pstate= param('state');
my $pcountry= param('country');
if(notnull()) {
print qq{
Submitted Successfully! }}}; 
my $pname= param('name');
my $pcity= param('city');
my $pstate= param('state');
my $pcountry= param('country');
print start_form, '<h2>Adding a new company</h2><br></br>';
print "Company Name: ";
print textfield('name');
print "<br></br>City: ";
print textfield('city', 'N/A');
print "<br></br>State/Province: ";
print textfield('state','N/A');
print "<br></br>Country: ";
print textfield('country');
print submit;
end_form;
my $sth= $dbh->prepare("insert into customers values (null,?,?,?,?)");
$sth->execute($pname, $pcity, $pstate, $pcountry );
$sth= $dbh->prepare("delete from customers where customer_name=' ' or customer_name is null or country=' '");
$sth->execute();
start_form;
print button(-name=>'Back', -value=>'Back', -onClick=>'history.back(-1)');
end_form;
print defaults('Reset fields');
start_form;
print button(-value=>'Home', onClick=>"window.location.href='http://btc-cems.sr.unh.edu'");
end_form;
exit;

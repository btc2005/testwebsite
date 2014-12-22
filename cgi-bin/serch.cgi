#!/usr/bin/perl
use CGI qw(:standard);
use DBI;
#use strict;
use warnings;
my $orders =param('orders');
my $customers =param('customers');
my $products =param('products');
my $dsn= "DBI:mysql:customers";
my $username = "btc2005";
my $password = "nukes";
my %attr=(PrintError=>0,
        RaiseError=>1);
my $dbh=DBI->connect($dsn,$username,$password, \%attr);
print "Content-type:text/html\n\n";
if ($customers eq "customers"){
my $sth = $dbh->prepare("select * from customers where customer_name is not null");
$sth->execute( );
print '<h2> Customer results:</h2>'; 
print 'company #,    company,    city,    state,    country<br></br>';
print "================================================<br></br>";

while ( my ($customer_num, $customer_name, $city, $state, $country) = $sth->fetchrow_array( ) )  {
         print "$customer_num. $customer_name, $city, $state, $country.<br></br>";
}
warn "Problem in retrieving results", $sth->errstr( ), "\n"
        if $sth->err( );}
if ($orders eq "orders"){
my $sth = $dbh->prepare("select * from orders where order_date is not null");
$sth->execute( );
print '<h2> Orders results:</h2>';       
print 'customer #,    order #,    order date,    shipped,    status, comments<br></br>';
print "================================================<br></br>";

while ( my ($order_num, $order_date, $shipped_date, $status, $comments, $customer_num) = $sth->fetchrow_array( ) )  {
         print "$customer_num. $order_num. $order_date, $shipped_date, $status, $comments.<br></br>";
}
warn "Problem in retrieving results", $sth->errstr( ), "\n"
        if $sth->err( );}
if ($products eq "products"){
my $sth = $dbh->prepare("select * from products where make is not null");
$sth->execute();
print '<h2> Products: </h2>';
print 'product #,    year,    model,   make,   price($)<br>';
print "================================================<br></br>";
while (my ($product_num, $year, $make, $model, $price) = $sth->fetchrow_array()) { print "$product_num, $year, $make, $model, $price.<br></br>";}}
if (!$customers && !$orders && !$products){
print "<h3>Please select at least one of the checkboxes in order to search!</h3><br></br>";
}
start_form;
print button(-value=>'Home', onClick=>"window.location.href='http://btc-cems.sr.unh.edu/helloworld.html'");
end_form;
exit; 
1;

#!/usr/bin/perl -w
use strict;
use warnings;
use DBI;
use CGI qw(:standard);
use CGI::OptimalQuery;
my $oq = CGI::OptimalQuery->new({
	dbh=>DBI->connect(
"DBI:mysql:customers",
"btc2005",
"nukes"),


	title => 'Customer Orders',

select => {
'ORDERS' => ['orders', "orders.order_num", "Order #"],
'STATUS' => ['orders', "orders.status", "Status"],
'PNUM' => [ 'products', "products.product_num", "Product ID"],
'PRICE' => ['products', "products.price", "Price"],
'NAME' => ['customers', "customers.customer_name", "Name"],
'CNUM' => ["customers", "customers.customer_num", "Customer #"],

},
show => ['NAME', 'ORDERS', 'CNUM', 'POPID', 'PRICE'],


joins => {
"orders" => [undef, "orders"], 
"customers" => ['orders', "left join customers on (customers.customer_num = orders.customer_num)", undef, {new_cursor => 1} ],
"products" => [undef, "products"],
"p_o" => ['products', "left join p_o on (p_o.product_num=products.product_num) where p_o.product_num=p_o.order_num and price != 0" ]
},
	options => {
		'CGI::OptimalQuery::InteractiveQuery' =>
 			{ color => '#060033' }
		}
	}
);
$oq -> output();
print "<center>";
print button(-value=>'Home', onClick=>"window.location.href='http://btc-cems.sr.unh.edu/helloworld.html'");


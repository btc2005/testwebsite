#!/usr/bin/perl -w
use strict;
use warnings;
use DBI;
use CGI::OptimalQuery;
my $oq = CGI::OptimalQuery->new({
	dbh=>DBI->connect(
"DBI:mysql:customers",
"btc2005",
"nukes"),


	title => 'Customer Orders',

select => {
'ORDERS' => ['orders', "orders.order_num", "Order #"],
#'OCNUM' => ['orders', "orders.customer_num", "Order CNUM"],
'STATUS' => ['orders', "orders.status", "Status"],

#'YEAR' => ['products', "products.year", "Year"],
#'MAKE' => ['products', "products.make", "Make"],
#'MODEL' => ['products', "products.model", "Model"],
#'PRICE' => ['products', "products.price", "Price"],
'NAME' => ['customers', "customers.customer_name", "Name"],
'CNUM' => ["customers", "customers.customer_num", "Customer #"],

},
show => ['NAME', 'ORDERS', 'CNUM'],

joins => {
"orders" => [undef, "orders"], 
"customers" => ['orders', "left join customers on (customers.customer_num = orders.customer_num)", undef, {new_cursor => 1} ]
},
	options => {
		'CGI::OptimalQuery::InteractiveQuery' => {
			color => '#660033' 
}}}
);
$oq -> output();

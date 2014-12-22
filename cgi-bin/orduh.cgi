#!/usr/bin/perl
use strict;
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

sub notnull() {
my $nonull=1;
if (!param('prodnum')) {print 'Please select a product', br; $nonull=0;}
if (!param('customer')) { print 'Please select a customer', br; $nonull=0    ;}
if (!param('date')) { print 'Please enter the date ordered', br; $nonull=0;}
if (!$nonull) { print 'Please fix the error and resubmit', hr; } return $nonull; }
print header;
if(param()) {
my $pdate= param('date');
my $pship= param('shipped');
my $pstatus= param('status');
my $pcomments= param('comments');
my $pcustomer= param('customer');
my $pcustnum= param('customer_num');
my $ppnum= param('prodnum');
my $ponum= param('order_num');
if(notnull()) {
print qq{ Submitted successfully }}};
my $pdate= param('date');
my $pship= param('shipped');
my $pstatus= param('status');
my $pcomments= param('comments');
my $pcustomer= param('customer');
my $pcustnum= param('customer_num');
my $ppnum= param('prodnum');
my $ponum= ('order_num');
my $query2 = qq{select customer_num,customer_name,city, state, country from customers};
my @cust = map {$_->[1]}
        @{$dbh->selectall_arrayref($query2)};
$query2= qq{select product_num, year, make, model, price from products};
my @prod = map {$_->[0]}
	@{$dbh->selectall_arrayref($query2)};
$query2= qq{select order_num, order_date, shipped_date, status, comments, customer_num from orders};
my @ord = map {$_->[0]}
	@{$dbh->selectall_arrayref($query2)};
use Time::localtime;
my $tm=localtime;
my($day,$month,$year)=($tm->mday, $tm->mon, $tm->year);
$year=$year+1900;
$month=$month+1;
# input
print start_form, '<h2>Adding a new order</h2><br></br>';
print "Which customer are you adding an order for?";
print scrolling_list(-name=>'customer', -values=> [@cust], -size=> 4, -multiple=>'true');
print "<br></br>What product was ordered?";
print popup_menu(-name=>'prodnum', -values=> [@prod]);
print "<br></br>Date Ordered (YYYY-MM-DD): ";
print textfield('date',
"$year-$month-$day");
print "<br></br>Date Shipped (YYYY-MM-DD): ";
print textfield('shipped',
"$year-$month-$day");
print "<br></br>Status: ";
my @status=("Shipped","Processing", "Packaging");
print popup_menu(-name=>'status', -values=>[@status]);
print "<br></br>Comments: ";
print textfield('comments',
"No comment");
print submit;
print button(-value=>'Home', onClick=>"window.location.href='http://btc-cems.sr.unh.edu/helloworld.html'");
print defaults('Reset fields');
print button(-name=>'Back', -value=>'Back', -onClick=>'history.back(-1)');
end_form;
my $sth=$dbh->prepare("select * from customers where customer_name='$pcustomer'");
$sth->execute( );
while (my ($results)= $sth->fetchrow()){
$pcustnum=$results;}
$sth= $dbh->prepare("insert into orders values (null,?,?,?,?,?)");
$sth->execute($pdate, $pship, $pstatus, $pcomments, $pcustnum);
$sth=$dbh->prepare("insert into p_o values (?,?)");
$sth->execute($ppnum, $ord[-1]);
$dbh->disconnect();
exit;
1;

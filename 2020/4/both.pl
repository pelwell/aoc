#!/usr/bin/perl

use strict;
use integer;

my $fh;

die "* no input\n" if (!open($fh, '<', $ARGV[0] || 'input.txt'));

my $linenum = 0;
my @map;

my %fields =
(
	'byr' => [0x01, \&is_byr],
	'iyr' => [0x02, \&is_iyr],
	'eyr' => [0x04, \&is_eyr],
	'hgt' => [0x08, \&is_hgt],
	'hcl' => [0x10, \&is_hcl],
	'ecl' => [0x20, \&is_ecl],
	'pid' => [0x40, \&is_pid],
);


my $valid1 = 0;
my $present1 = 0;
my $valid2 = 0;
my $present2 = 0;

while (1)
{
	my $line = <$fh>;
	$linenum++;
	if ($line =~ /^\s*$/)
	{
		$valid1++ if ($present1 == 0x7f);
		$valid2++ if ($present2 == 0x7f);
		$present1 = 0;
		$present2 = 0;
		last if (!$line);
	}
	while ($line =~ /\b([a-z]{3}):([^ \r\n\t]+)/g)
	{
		my ($fld, $val) = ($1, $2);
		my $res = $fields{$fld};
		if ($res)
		{
			$present1 |= $res->[0];
			$present2 |= $res->[0] if ($res->[1]($val));
		}
	}
}

printf("Part 1 answer: %d\n", $valid1);
printf("Part 2 answer: %d\n", $valid2);

sub is_byr
{
	my ($x) = @_;
	if (($x =~ /^\d{4}$/) &&
	    ($x >= 1920) &&
	    ($x <= 2002))
	{
		return 1;
	}
	return 0;
}

sub is_iyr
{
	my ($x) = @_;
	return (($x =~ /^\d{4}$/) &&
		($x >= 2010) &&
		($x <= 2020));
}

sub is_eyr
{
	my ($x) = @_;
	return (($x =~ /^\d{4}$/) &&
		($x >= 2020) &&
		($x <= 2030));
}

sub is_hgt
{
	my ($x) = @_;
	if ($x =~ /^(\d+)(cm|in)$/)
	{
		return ($2 eq 'cm') ? (($1 >= 150) && ($1 <= 193)) :
				      (($1 >= 59) && ($1 <= 76));
	}
	return 0;
}

sub is_hcl
{
	my ($x) = @_;
	return ($x =~ /^#[0-9a-f]{6}$/);
}

sub is_ecl
{
	my ($x) = @_;
	return ($x =~ /^(amb|blu|brn|gry|grn|hzl|oth)$/);
}

sub is_pid
{
	my ($x) = @_;
	return ($x =~ /^\d{9}$/);
}

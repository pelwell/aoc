#!/usr/bin/perl

use strict;
use integer;

my $fh;

die "* no input\n" if (!open($fh, '<', $ARGV[0] || 'input.txt'));

my $linenum = 0;

my @prog;

while (1)
{
	my $line = <$fh>;
	$linenum++;
	last if (!$line);
	if ($line =~ /^(jmp|acc|nop) ([-+]\d+)/)
	{
		push @prog, [ $1, $2 ];
	}
}
my @res = run_prog(\@prog);
printf("Part 1 answer: %d\n", $res[1]);

for (my $pos = 0; $pos < @prog; $pos++)
{
	switch(\@prog, $pos);
	@res = run_prog(\@prog);
	if ($res[0] == @prog)
	{
		# run_prog(\@prog, 1);
		# printf("%d: -> %d, acc %d\n", $pos + 1, $res[0], $res[1]);
		last;
	}
	switch(\@prog, $pos);
}

printf("Part 2 answer: %d\n", $res[1]);

sub run_prog
{
	my ($prog, $trace) = @_;
	my $acc = 0;
	my $pos = 0;
	my @visited;

	while (!$visited[$pos] && ($pos != @$prog))
	{
		my $instr = $prog->[$pos];
		printf("%d: %s %s // acc %d`\n", $pos, $instr->[0], $pos + $instr->[1], $acc) if ($trace);
		$visited[$pos] = 1;
		if ($instr->[0] eq 'jmp')
		{
			$pos += $instr->[1];
		}
		elsif ($instr->[0] eq 'acc')
		{
			$acc += $instr->[1];
			$pos++;
		}
		elsif ($instr->[0] eq 'nop')
		{
			$pos++;
		}
		else
		{
			die "* Bad instruction at $pos\n";
		}
	}

	return ($pos, $acc);
}

sub switch
{
	my ($prog, $pos) = @_;
	my $instr = $prog->[$pos];
	if ($instr->[0] eq 'jmp')
	{
		$instr->[0] = 'nop';
	}
	elsif ($instr->[0] eq 'nop')
	{
		$instr->[0] = 'jmp';
	}
}
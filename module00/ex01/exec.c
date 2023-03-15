#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int	len_s(char **args)
{
	int	i;
	int	j;
	int	z;

	i = 1;
	j = 0;
	z = 0;
	while (args[i])
	{
		while (args[i][j])
		{
			j++;
			z++;
		}
		i++;
		j = 0;
	}
	return (z);
}

void	error_msg()
{
	printf("This executable inverts the order of the characters of the arguments and swap upper case into lower case");
	exit(0);
}
int	main(int arg, char **args)
{
	int	i;
	int	j;
	int	q;
	char	*s;
	char	*r;

	q = 0;
	i = 1;
	j = 0;
	if (arg <= 1)
		error_msg();
	s = malloc(sizeof(char ) * (len_s(args) + arg));
	while (args[i])
	{
		while (args[i][j])
		{
			if (args[i][j] >= 'a' && args[i][j] <= 'z')
				s[q++] = args[i][j] - 32;
			else if (args[i][j] >= 'A' && args[i][j] <= 'Z')
				s[q++] = args[i][j] + 32;
			else
				s[q++] = args[i][j];
			j++;
		}
		s[q++] = ' ';
		i++;
		j = 0;
	}
	s[q] = '\0';
	i = 0;
	j = 0;
	while (s[i])
		i++;
	i--;
	r = malloc(sizeof(char ) * (i + 1));
	while (i >= 0)
		r[j++] = s[i--];
	r[j] = '\0';
	printf("%s", r);
	free(s);
	free(r);
	return (0);
}

				




#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
 * infinite_while - infinite loop
 *
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - initializes five zombie processes
 *
 * Return: 0
 */
int main(void)
{
	int idx;
	pid_t zombie_pid;

	for (idx = 0; idx < 5; idx++)
	{
		zombie_pid = fork();
		if (!zombie_pid)
		{
			return (0);
		}

		printf("Zombie process created, PID: %d\n", zombie_pid);
	}

	infinite_while();
	return (0);
}

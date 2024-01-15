#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 * @list: A singly-linked list.
 *
 * Return: 0 If there is no cycle.
 *         1 If there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *first, *second;

	if (list == NULL || list->next == NULL)
		return (0);

	first = list->next;
	second = list->next->next;

	while (first && second && second->next)
	{
		if (first == second)
			return (1);
		first = first->next;
		second = second->next->next;
	}

	return (0);
}

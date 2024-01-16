#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 *
 * Return: a pointer to the new node on success.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *newList;

	newList = malloc(sizeof(listint_t));
	if (newList == NULL)
		return (NULL);
	newList->n = number;
	if (node == NULL || node->n >= number)
	{
		newList->next = node;
		*head = newList;
		return (newList);
	}
	while (node && node->next && node->next->n < number)
		node = node->next;

	newList->next = node->next;
	node->next = newList;

	return (newList);
}

#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of the first node of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	const listint_t *node;
	int *values;
	size_t size, i;

	if (head == NULL || *head == NULL)
		return (1);

	size = 0;
	for (node = *head; node != NULL; node = node->next)
		size++;

	values = malloc(sizeof(int) * size);
	if (values == NULL)
		return (0);

	i = 0;
	for (node = *head; node != NULL; node = node->next)
		values[i++] = node->n;

	for (i = 0; i < size / 2; i++)
	{
		if (values[i] != values[size - 1 - i])
		{
			free(values);
			return (0);
		}
	}

	free(values);
	return (1);
}

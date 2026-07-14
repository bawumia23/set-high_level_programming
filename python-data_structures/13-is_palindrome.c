#include "lists.h"

/**
 * reverse_sub_list - reverses a singly linked sub-list in place
 * @node: pointer to the first node of the sub-list to reverse
 * Return: pointer to the new head of the reversed sub-list
 */
static listint_t *reverse_sub_list(listint_t *node)
{
	listint_t *prev, *next;

	prev = NULL;
	while (node != NULL)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}
	return (prev);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of the first node of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev_slow, *second_half, *p1, *p2;
	int result;

	if (head == NULL || *head == NULL)
		return (1);

	slow = *head;
	fast = *head;
	prev_slow = NULL;

	while (fast != NULL && fast->next != NULL)
	{
		prev_slow = slow;
		slow = slow->next;
		fast = fast->next->next;
	}

	second_half = reverse_sub_list(slow);

	result = 1;
	p1 = *head;
	p2 = second_half;
	while (p2 != NULL)
	{
		if (p1->n != p2->n)
		{
			result = 0;
			break;
		}
		p1 = p1->next;
		p2 = p2->next;
	}

	second_half = reverse_sub_list(second_half);
	if (prev_slow == NULL)
		*head = second_half;
	else
		prev_slow->next = second_half;

	return (result);
}

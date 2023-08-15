#include "lists.h"
#include <stdio.h>

/**
 * check_palindrome_recursive - recursively check if it is a palindrome
 *
 * @h: pointer to the head of the linked list.
 * @n: pointer to the current node been checked.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */

int check_palindrome_recursive(listint_t **h, listint_t *n)
{
	int i;

	// If the current node is NULL, we have reached the end of the list.
	if (n == NULL)
		return (1);

	// Recursively call the function for the next node in the list.
	i = check_palindrome_recursive(h, n->next);

	// If i is 0, the previous recursive call detected a mismatch, so return 0
	if (i == 0)
		return (0);
	i = (n->n == (*h)->n);
	*h = (*h)->next;

	return (i);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 *
 * @head: pointer to the linked list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	return (check_palindrome_recursive(head, *head));
}

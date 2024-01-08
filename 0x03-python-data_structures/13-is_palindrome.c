#include "lists.h"
/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Points to a pointer that points to the first node
 *
 * Return:0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *prev = NULL, *temp;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	/*Finding the middle of the linked list using floyd's algorithm*/
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;

		/*Reversing the first half while finding the middle*/
		temp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = temp;
	}
	if (fast != NULL)
		slow = slow->next;

	/*Compare the first and second half of the linked list*/
	while (slow != NULL)
	{
		if (prev->n != slow->n)
			return (0);
		prev = prev->next;
		slow = slow->next;
	}
	return (1);
}

#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: linked list to check.
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't.
 */
int check_cycle(listint_t *list)
{
	/*Initialize two pointers, slow and fast, to the beginning of the list*/
	listint_t *slow = list;
	listint_t *fast = list;

	/*Check if the list is empty*/
	if (!list)
		return (0);
	/*use pointers to traverse the list at different speeds*/
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}

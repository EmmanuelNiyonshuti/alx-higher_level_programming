#include "lists.h"
/**
 *insert_node -  inserts a number into a sorted singly linked list
 *@head: Reference to the first node.
 *number: number to be inserted.
 *
 * Return:the address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *temp;
	temp = *head;

	new_node = malloc(sizeof(listint_t));
		if (!new_node)
			return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || number < temp->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	while (temp->next != NULL && number > temp->next->n)
		temp = temp->next;

	new_node->next = temp->next;
	temp->next = new_node;

	return (new_node);
}


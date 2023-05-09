#include "lists.h"

/**
 * check_cycle - this function checks if a linked list contains a cycle
 * @list: pointer to the linked list to be checked
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list->next;

	if (!list)
		return (0);

	do {
		if (slow == fast)
		{
			return (1);
		}
		slow = slow->next;
		fast = fast->next ? fast->next->next : NULL;
	} while (fast);

	return (0);
}

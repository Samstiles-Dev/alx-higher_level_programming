#include <stdlib.h>
#include "lists.h"

/**
 * *insert_node - this inserts number into a sorted singly linked list
 * @head: head of list
 * @number: integer to insert into a new node
 * Return: address of new node else NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_num, *tmp_1;

	new_num = malloc(sizeof(listint_t));
	if (new_num == NULL)
		return (NULL);
	if (*head == NULL)
	{
		new_num->n = number;
		new_num->next = *head;
		*head = new_num;
		return (new_num);
	}
	else if (number <= (*head)->n)
	{
		new_num->n = number;
		new_num->next = *head;
		*head = new_num;
		return (new_num);
	}
	else
	{
		tmp_1 = *head;
		while (tmp_1->next != NULL && number > tmp_1->next->n)
		{
			tmp_1 = tmp_1->next;
		}
		new_num->n = number;
		new_num->next = tmp_1->next;
		tmp_1->next = new_num;
		return (new_num);
	}
	return (NULL);
}

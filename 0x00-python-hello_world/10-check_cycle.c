#include "lists.h"

int check_cycle(listint_t *list)
{
	if(list == NULL)
    {
        return 1;
    }

    listint_t *ptr = list;

    while(ptr)
    {
        ptr = ptr->next;
        if(ptr->next == list)
        {
            return 1;
        }
    }
    
    return 0;
}

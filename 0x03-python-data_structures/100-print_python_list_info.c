#include <stdio.h>
#include "Python.h"

/**
 * print_python_list_info - Prints some basic info about Python lists.
 * @p: A pointer the Python Object.
 *
 * Return: a pointer to the new node on success.
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyListObject *pp;
	str PyObjName;

	pp = (PyListObject *)p;
	size = pp->ob_base.ob_size;
	alloc = pp->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);
	for (i = 0; i < size; i++)
	{
		PyObjName = pp->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, PyObjName);
	}
}

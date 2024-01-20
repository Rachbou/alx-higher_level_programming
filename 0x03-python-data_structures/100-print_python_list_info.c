#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * print_python_list_info - Prints some basic info about Python lists.
 * @p: A pointer the Python Object.
 *
 * Return: a pointer to the new node on success.
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyObject *PyObj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		PyObj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(PyObj)->tp_name);
	}
}

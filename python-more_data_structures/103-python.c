#include <Python.h>
#include <stdio.h>
#include <string.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Print basic info about a Python list.
 * @p: pointer to the PyObject list.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, alloc, i;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < size; i++)
	{
		PyObject *item = list->ob_item[i];

		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
		if (strcmp(item->ob_type->tp_name, "bytes") == 0)
			print_python_bytes(item);
	}
}

/**
 * print_python_bytes - Print basic info about a Python bytes object.
 * @p: pointer to the PyObject bytes object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i, limit;
	PyBytesObject *bytes = (PyBytesObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	printf("[.] bytes object info\n");

	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = var->ob_size;
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes->ob_sval);

	limit = size < 10 ? size + 1 : 10;
	printf("  first %ld bytes: ", limit);
	for (i = 0; i < limit; i++)
		printf("%02x%s", (unsigned char)bytes->ob_sval[i],
		       (i == limit - 1) ? "\n" : " ");
}

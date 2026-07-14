#include <Python.h>
#include <listobject.h>

/**
 * print_python_list_info - prints basic info about a Python list
 * @p: pointer to a PyObject (assumed to be a Python list)
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t size, i;

	list = (PyListObject *)p;
	size = Py_SIZE(list);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n", i,
				Py_TYPE(list->ob_item[i])->tp_name);
	}
}

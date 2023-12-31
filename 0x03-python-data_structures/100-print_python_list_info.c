#include "Python.h"
/**
 * print_python_list_info - Prints information about python objects
 * @p: PyObject pointer to print info about
*/
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, python_list_size;
	const char *item_type;
	PyListObject *list_object_cast;
	PyObject *item;

	list_object_cast = (PyListObject *)p;
	python_list_size = PyList_Size(p);

	printf("[*] Size of the Python List = %d\n", (int) python_list_size);
	printf("[*] Allocated = %d\n", (int)list_object_cast->allocated);
	for (i = 0; i < python_list_size; i++)
	{
		item = PyList_GetItem(p, i);
		item_type = Py_TYPE(item)->tp_name;
		printf("Element %d: %s\n", (int) i, item_type);
	}
}

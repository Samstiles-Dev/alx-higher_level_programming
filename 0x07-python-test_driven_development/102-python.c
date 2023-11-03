#include "Python.h"

/**
 * print_python_string - this Prints info about Python strings.
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p)
{
	long int _len;

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	_len = ((PyASCIIObject *)(p))->_len;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  _len: %ld\n", _len);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &_len));
}

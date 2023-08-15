#include <Python.h>

/**
* print_python_list_info - a function that prints some basic info
* about Python lists.
*
* @p: A PyObject pointer representing a Python list.
*/

void print_python_list_info(PyObject *p)
{
	/* Get the size of the python list. */
	Py_ssize_t size = PyList_Size(p), i;
	/* Get the allocated memory for the list. */
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;
	/* Declare variables for the current element and its type. */
	PyObject *element;
	const char *elementType;

	/* Print the size of the Python list. */
	printf("[*] Size of the Python List = %ld\n", size);
	/* Print the allocated memory size for the list. */
	printf("[*] Allocated = %ld\n", allocated);

	/* Loop through each element in the list and print its type. */
	for (i = 0; i < size; i++)
	{
		element = PyList_GetItem(p, i);
		elementType = Py_TYPE(element)->tp_name;

		printf("Element %ld: %s\n", i, elementType);
	}
}

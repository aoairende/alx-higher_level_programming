#include <Python.h>
#include <listobject.h>
#include <object.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
    int i = 0;
    PyObject *ptr;
    PyTypeObject *type;
    Py_ssize_t len = PyList_Size(p);

	/* Print the size of the Python list. */
    printf("[*] Size of the Python List = %ld\n", len);

	/* Print the allocated memory size for the Python list. */
    printf("[*] Allocated = %ld\n", Py_SIZE(p));

	/* Loop through each element in the list and print its type. */
    while (i < len)
    {
        ptr = PyList_GetItem(p, i);
        type = Py_TYPE(ptr);
        printf("Element %d = %s\n", i, type->tp_name);
        i++;
    }
}

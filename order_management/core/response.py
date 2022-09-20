from rest_framework import status
from rest_framework.response import Response


def invalid_data(message):
    """
    return:Return error when an invalid data is passed
    """
    return Response(
        {
            'status': 400,
            'message': message
        },
        status=status.HTTP_400_BAD_REQUEST
    )


def success_data(data, message):
    """
    return:Return success message when the login success
    """
    return Response(
        {
            'status': 200,
            'message': message,
            'data': data
        },
        status=status.HTTP_200_OK
    )


def created(message):
    """
    return: Return success message when a data is created
    """
    return Response(
        {
            'success': 'True',
            'message': message
        },
        status=status.HTTP_201_CREATED

    )


def success(message):
    """
        return:Return success message when the login success
        """
    return Response(
        {
            'status': 200,
            'message': message
        },
        status=status.HTTP_200_OK
    )

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Item, Transaction, Supplier
from .serializers import CategorySerializer, ItemSerializer, TransactionSerializer, SupplierSerializer

# Category Management

@api_view(['POST'])
def add_category(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_category(request, id):
    try:
        category = Category.objects.get(pk=id)
    except Category.DoesNotExist:
        return Response("Category does not exist", status=status.HTTP_404_NOT_FOUND)
    category.delete()
    return Response("Category deleted successfully", status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update_category(request, id):
    try:
        category = Category.objects.get(pk=id)
    except Category.DoesNotExist:
        return Response("Category does not exist", status=status.HTTP_404_NOT_FOUND)
    serializer = CategorySerializer(category, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Item Management

@api_view(['POST'])
def add_item(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_item(request, id):
    try:
        item = Item.objects.get(pk=id)
    except Item.DoesNotExist:
        return Response("Item does not exist", status=status.HTTP_404_NOT_FOUND)
    item.delete()
    return Response("Item deleted successfully", status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update_item(request, id):
    try:
        item = Item.objects.get(pk=id)
    except Item.DoesNotExist:
        return Response("Item does not exist", status=status.HTTP_404_NOT_FOUND)
    serializer = ItemSerializer(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Transaction Management

@api_view(['POST'])
def add_transaction(request):
    serializer = TransactionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_transaction(request, id):
    try:
        transaction = Transaction.objects.get(pk=id)
    except Transaction.DoesNotExist:
        return Response("Transaction does not exist", status=status.HTTP_404_NOT_FOUND)
    transaction.delete()
    return Response("Transaction deleted successfully", status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update_transaction(request, id):
    try:
        transaction = Transaction.objects.get(pk=id)
    except Transaction.DoesNotExist:
        return Response("Transaction does not exist", status=status.HTTP_404_NOT_FOUND)
    serializer = TransactionSerializer(transaction, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Supplier Management

@api_view(['POST'])
def add_supplier(request):
    serializer = SupplierSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_supplier(request, id):
    try:
        supplier = Supplier.objects.get(pk=id)
    except Supplier.DoesNotExist:
        return Response("Supplier does not exist", status=status.HTTP_404_NOT_FOUND)
    supplier.delete()
    return Response("Supplier deleted successfully", status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update_supplier(request, id):
    try:
        supplier = Supplier.objects.get(pk=id)
    except Supplier.DoesNotExist:
        return Response("Supplier does not exist", status=status.HTTP_404_NOT_FOUND)
    serializer = SupplierSerializer(supplier, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# from django.http import JsonResponse
# from django.shortcuts import render
# from Appyhouselist_app.models import Property


# def property_list(request):
#     property = Property.objects.all()
#     data = {
#         'properties': list(property.values())
#     }
#     return JsonResponse(data)

# def property_detail(request, pk):
#     property = Property.objects.get(pk=pk)
    
#     data = {
#         'address':property.address,
#         'city' :property.city,
#         'state': property.state,
#         'country': property.country,
#         'description' : property.description,
#         'property_Type': property.property_Type,
#         'bedrooms': property.bedrooms,
#         'bathrooms' : property.bathrooms,
#         'price' : property.price,
#         'currency' : property.currency,
#         'garage' : property.garage,
#         'built_up_area_square_meters' : property.built_up_area_square_meters,
#         'total_area_square_meters' : property.total_area_square_meters,
#         'image' : property.image,
#         'active' :property.active
#     }
#     return JsonResponse(data)
    
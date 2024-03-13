from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
import json

User = get_user_model()

@csrf_exempt
@require_POST
def verify_email(request):
    try:
        data = json.loads(request.body)
        email = data['email']
        otp = data['otp']

        # Retrieve the user based on the email provided
        user = User.objects.get(email=email)

        # Check if the OTP matches
        if user.otp == otp:
            user.is_verified = True
            user.save()
            return JsonResponse({'message': 'Email verified successfully'}, status=200)
        else:
            return JsonResponse({'message': 'Invalid OTP'}, status=400)

    except User.DoesNotExist:
        return JsonResponse({'message': 'User does not exist'}, status=404)
    except KeyError:
        return JsonResponse({'message': 'Missing email or OTP in request'}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({'message': 'Invalid JSON'}, status=400)
    except ValidationError as e:
        return JsonResponse({'message': str(e)}, status=400)
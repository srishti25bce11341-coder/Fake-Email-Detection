from detector import predict_email
print("Fake Email Detector")
email = input("Enter email:\n")
result = predict_email(email)
print("\nResult:", result)

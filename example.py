from igloo import Client, Device

client = Client(token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VySWQiOiJlNzYxZmZlMi1lM2Q5LTQ0YjYtYjYyZC00M2Y4ZTljMTRjNjIiLCJ0b2tlbklkIjoiMGQxNTcxNGEtM2UyZS00NjFhLTg2ZTMtOGQwZWUwMTY4NWEzIiwiYWNjZXNzTGV2ZWwiOiJERVZJQ0UiLCJ0b2tlblR5cGUiOiJQRVJNQU5FTlQifQ.ttiW6TVvcKoWmhDSL8fTqq_ItWvPa_41zolI4gRi2zwKlUVV-PWRMk3QM1ZcAuEuOtGGLaPuilR-4Z6JZf13ag")

thermometer = Device(client, "229718d6-e4fe-43dd-a2e6-6504a2e9a5f9")
print(thermometer.online)

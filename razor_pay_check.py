# username: rzp_test_5286GGOR8uHpuB
# password:oMFGy3b1wYSDXIRrPI1M9coK

import requests
import json

url = "https://api.razorpay.com/v1/payment_links"

payload = json.dumps({
  "amount": 100,
  "currency": "INR",
  "accept_partial": True,
  "first_min_partial_amount": 100,
  "expire_by": 1691097057,
  "reference_id": "252521",
  "description": "Payment for policy no #23456",
  "customer": {
    "name": "Angel",
    "contact": "+917306177716",
    "email": "angelrosecho@gmail.com.com"
  },
  "notify": {
    "sms": True,
    "email": True
  },
  "reminder_enable": True,
  "notes": {
    "policy_name": "Jeevan Bima"
  },
  "callback_url": "https://example-callback-url.com/",
  "callback_method": "get"
})
headers = {
  'Authorization': 'Basic cnpwX3Rlc3RfNTI4NkdHT1I4dUhwdUI6b01GR3kzYjF3WVNEWElSclBJMU05Y29L',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

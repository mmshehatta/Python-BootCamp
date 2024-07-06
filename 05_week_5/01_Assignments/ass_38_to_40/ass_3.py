"""
التكليف 03
قم بعمل متغيرين بإسم first_name و second_name يحتووا على Input فيه الإسم الأول والثاني للشخص
قم بالتأكد من أن أي مسافات قبل وبعد الإسم الأول والثاني سوف يتم إزالتها
قم بالتأكد من أن الإسم الأول والثاني أول حرف فيهم Capital والباقي Small
قم بطباعة رسالة ترحيبية فيها الإسم الأول وأول حرف من الإسم الثاني فقط.
"""
from icecream import ic
first_name = input("Enter first name: ").strip().capitalize()
second_name = input("Enter second name: ").strip().capitalize()
ic(f"Hello {first_name } {second_name:.1}")





# ذخیره اطلاعات مربوط به یک پیتزا
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# نمایش خلاصه سفارش
print(
    f"شما یک پیتزای با خمیر {pizza['crust']} سفارش داده‌اید "
    "با مخلفات زیر:"
)

for topping in pizza['toppings']:
    print(f"\t{topping}")


# دیکشنری تو در تو برای اطلاعات کاربران
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

# پیمایش کاربران و نمایش اطلاعات آن‌ها
for username, user_info in users.items():

    print(f"\nنام کاربری: {username}")

    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print("نام:", full_name.title())
    print("محل سکونت:", location.title())


# زبان‌های برنامه‌نویسی مورد علاقه کاربران
favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
}

# نمایش زبان‌های مورد علاقه هر کاربر
for name, languages in favorite_languages.items():

    print(f"\nزبان‌های مورد علاقه {name.title()}:")

    for language in languages:
        print(f"\t{language.title()}")


# ساخت یک لیست خالی برای نگهداری بیگانگان
aliens = []

# ایجاد 30 بیگانه سبزرنگ
for alien_number in range(30):

    new_alien = {
        'color': 'green',
        'points': 5,
        'speed': 'slow'
    }

    aliens.append(new_alien)

# تغییر مشخصات سه بیگانه اول
for alien in aliens[:3]:

    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# نمایش پنج بیگانه اول
for alien in aliens[:5]:
    print(alien)



print("...")

# نمایش تعداد کل بیگانگان ساخته شده
print(f"تعداد کل بیگانگان: {len(aliens)}")




alien = {'color':'green', 'point':5}
alien['score'] = 6
print(alien)
a = {}
a['c'] = (1,2)
print(a)

satellite = {'x':2, 'y':4, 'speed':'medium'}
print("Original position:" + str(satellite['x'])+ "," + str(satellite['y']))

if satellite['speed'] == 'slow':
    x_increment = 1
    y_increment = 1
elif satellite['speed'] == 'medium':
    x_increment = 3
    y_increment = 4
else:
    x_increment = 5
    y_increment = 6

print("New position:\nspeed = " + satellite['speed'])
x_1 = satellite['x'] + x_increment 
y_1 = satellite['y'] + y_increment
print(str(x_1) + "," + str(y_1))

for value in satellite.values():
    print(value)

#print(satellite.get("x"))
#print(satellite.pop('y'))
#print(satellite)
#print(satellite.get("phone", "Not Found"))

satellite = {
    "name": {"EO-1":4},
    "sensors": ["IR", "RGB", "SAR"],
    "s": {"e":[1,5]}
}
print(satellite["sensors"][1])
print(satellite['name']['EO-1'])
print(satellite['s']['e'][0])

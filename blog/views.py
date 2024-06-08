from django.shortcuts import render

menu = ['home', 'about', 'posts']
items = {
    'Smartphone': {
        'id': 1,
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
    },
    'Laptop': {
        'id': 2,
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
    },
    'Keyboard': {
        'id': 3,
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
    },
    'Mouse': {
        'id': 4,
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
    }
}

food_items = {
    'Apple': {
        'id': 1,
        'description': 'Fresh apples grown in an organic neighborhood'
    },
    'Bread': {
        'id': 2,
        'description': 'Homemade bread made with whole wheat flour'
    },
    'Cheese': {
        'id': 3,
        'description': 'Natural cheese made from cow\'s milk'
    },
    'Milk': {
        'id': 4,
        'description': 'Organic milk'
    }
}

cars = {
    'Audi': {
        'id': 1,
        'description': 'My favorite brand of car❤️'
    },
    'BMW': {
        'id': 2,
        'description': 'BMW is a German multinational company which produces luxury vehicles and motorcycles.'
    },
    'Tesla': {
        'id': 3,
        'description': 'Tesla, Inc. is an American electric vehicle and clean energy company'
    },
    'Porsche': {
        'id': 4,
        'description': 'Porsche is a German automobile manufacturer specializing in high-performance sports cars, '
                       'SUVs, and sedans.'
    }
}


def home(request):
    data = {
        'menu_bar': menu,
        'products': items,
    }
    return render(request, 'blog/index.html', context=data)


def product(request, product_id):
    product_lst = [i for i in items if items[i]['id'] == product_id]
    return render(request, 'blog/product.html',
                  {'product_desc': items[product_lst[0]], 'product_name': product_lst[0]})


def food_shop(request, food_id):
    food_lst = [i for i in food_items if food_items[i]['id'] == food_id]
    return render(request, 'blog/food_shop.html',
                  {'food_desc': food_items[food_lst[0]], 'food_name': food_lst[0]})


def food_list(request):
    data = {
        'menu_bar': menu,
        'food_products': food_items
    }
    return render(request, 'blog/food_list.html', context=data)


def car_list(request):
    data = {
        'menu_bar': menu,
        'cars': cars
    }
    return render(request, 'blog/car_list.html', context=data)


def car(request, car_id):
    car_lst = [i for i in cars if cars[i]['id'] == car_id]
    return render(request, 'blog/car.html',
                  {'car_desc': cars[car_lst[0]], 'car_name': car_lst[0]})


def about(request):
    return render(request, 'blog/about.html')

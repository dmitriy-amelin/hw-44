from django.shortcuts import render


def index_view(request):
    secret_nums = [5, 1, 2, 9]
    idx = 0
    bulls = 0
    cows = 0
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        errors = {
            'error1':
        }

        context = {
            'number1': request.POST.get('number1'),
            'number2': request.POST.get('number2'),
            'number3': request.POST.get('number3'),
            'number4': request.POST.get('number4'),

        }
        try:
            numbers = [context['number1'], context['number2'], context['number3'], context['number4']]
            need_check = validation(numbers)
            if not need_check:
                if len(numbers) == len(secret_nums):
                    while idx < 4:
                        if secret_nums[idx] == numbers[idx]:
                            bulls += 1
                        elif numbers[idx] in secret_nums:
                            cows += 1
                        idx += 1
                    response_body += f'<div>Bulls: {bulls}, Cows: {cows}</div>'
                else:
                    response_body += '<div>The number of digits is not the same</div>'
            else:
                response_body += need_check
        except ValueError:
            response_body += "<div>It's not a number</div>"
        context = {
            'title': request.POST.get('numbers'),
        }

        return render(request, 'article_view.html', context)


def validation(nums):
    idx_2 = 0
    set_nums = set(nums)

    if len(nums) != len(set_nums):
        return '<div>Numbers should not be repeated</div>'

    while idx_2 < 4:
        if nums[idx_2] not in range(1, 11):
            return '<div>Digits are out of range 1 to 10</div>'
        idx_2 += 1

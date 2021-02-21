from django.shortcuts import render


def index_view(request):
    secret_nums = [5, 1, 2, 9]
    idx = 0
    bulls = 0
    cows = 0
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        context = {
            'number1': request.POST.get('number1'),
            'number2': request.POST.get('number2'),
            'number3': request.POST.get('number3'),
            'number4': request.POST.get('number4'),
        }
        numbers = [context['number1'], context['number2'], context['number3'], context['number4']]
        numbers = list(map(int, numbers))
        need_check = validation(numbers)
        if not need_check:
            if len(numbers) == len(secret_nums):
                while idx < 4:
                    if secret_nums[idx] == numbers[idx]:
                        bulls += 1
                    elif numbers[idx] in secret_nums:
                        cows += 1
                    idx += 1
                context['bulls'] = bulls
                context['cows'] = cows
            return render(request, 'result.html', context)
        else:
            context = {"error": need_check}
            return render(request, 'errors.html', context)


def validation(nums):
    idx_2 = 0
    set_nums = set(nums)

    if len(nums) != len(set_nums):
        return "Numbers should not be repeated"

    while idx_2 < 4:
        if nums[idx_2] not in range(1, 11):
            return "Digits are out of range 1 to 10"
        idx_2 += 1

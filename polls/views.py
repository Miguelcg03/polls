from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from .models import Poll
from choices.models import Choice
from votes.models import Vote

def polls(request, poll_name="Encuestas"):
    current_poll = get_object_or_404(Poll, name=poll_name)

    choices_for_poll = Choice.objects.filter(poll=current_poll)

    return render(request, 'polls/polls/base.html', {'choices_for_poll': choices_for_poll})



def poll_detail(request, poll_name):
    current_poll = get_object_or_404(Poll, name=poll_name)

    if request.method == 'POST':
        choice_id = request.POST.get('choice')
        if choice_id:
            choice = get_object_or_404(Choice, id=choice_id)
            Vote.objects.create(poll=current_poll, choice=choice)
            # Después de procesar el formulario, redirige a la página de resultados
            return redirect(reverse('polls:poll_results', args=[poll_name]))

    choices_for_poll = Choice.objects.filter(poll=current_poll)

    return render(request, 'polls/polls/detail.html', {'choices_for_poll': choices_for_poll, 'poll_name': poll_name})

# En tu views.py
def poll_results(request, poll_name):
    current_poll = get_object_or_404(Poll, name=poll_name)
    choices_for_poll = Choice.objects.filter(poll=current_poll)

    # Obtener la opción con más votos

    # Calcular el total de votos
    total_votes = Vote.objects.filter(poll=current_poll).count()

    return render(request, 'polls/polls/results.html', {'choices_for_poll': choices_for_poll, 'poll_name': poll_name, 'total_votes': total_votes})


from django.http import HttpResponse
from django.template import loader
from .models import Pokemon, Trainer

def index(request):
    pokemons = Pokemon.objects.all()
    trainers = Trainer.objects.all()
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'pokemons': pokemons, 'trainers': trainers}, request))

def trainer_detail(request, id):
    trainer = Trainer.objects.get(id=id)
    template = loader.get_template('display_trainer.html') # Necesitarás crear este HTML
    context = {
        'trainer': trainer
    }
    return HttpResponse(template.render(context, request))

def pokemon(request, id: int):
    pokemon = Pokemon.objects.get(id=id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))

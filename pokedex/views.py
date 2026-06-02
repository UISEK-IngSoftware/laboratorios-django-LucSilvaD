from django.shortcuts import render, redirect
from .models import Pokemon, Trainer
from .forms import PokemonForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

def index(request):
    pokemons = Pokemon.objects.all()
    trainers = Trainer.objects.all()
    return render(request, "index.html", {"pokemons": pokemons, "trainers": trainers})

def pokemon(request, id):
    pokemon = Pokemon.objects.get(id=id)
    return render(request, "display_pokemon.html", {"pokemon": pokemon})

def trainer(request, id):
    trainer = Trainer.objects.get(id=id)
    return render(request, "display_trainer.html", {"trainer": trainer})

@login_required
def add_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm()
    return render(request, 'pokemon_form.html', {'form': form})

def edit_pokemon(request, id):
    pokemon = Pokemon.objects.get(id=id)
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm(instance=pokemon)
    return render(request, 'pokemon_form.html', {'form': form})

def delete_pokemon(request, id):
    pokemon = Pokemon.objects.get(id=id)
    pokemon.delete()
    return redirect('pokedex:index')

class CustomLoginView(LoginView):
    template_name = 'login_form.html'

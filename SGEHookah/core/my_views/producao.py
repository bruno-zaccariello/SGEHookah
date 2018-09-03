@login_required(login_url="/admin")
def lista_formula(request):
    formulas = Formulaproduto.objects.filter(hide=False)
    page = int(request.GET.get('page', 1))
    deletado = request.GET.get('deleted', False)

    paginas = Paginator(formulas, 10)
    pagina = paginas.get_page(page)

    url = arruma_url_page(request)
    context = {
        "pagina": pagina,
        "success": deletado,
        "url": url,
    }
    return render(request, 'iframe/producao/formula/lista_formulas.html', context)


@login_required(login_url="/admin")
def pagina_formula(request, id_formula):
    try:
        Formula = Formulaproduto.objects.filter(
            hide=False).get(pkid_formula=id_formula)
    except:
        Formula = None

    success = request.GET.get('success', False)

    formset_materias = inlineformset_factory(
        Formulaproduto,
        Formulamateria,
        extra=0,
        min_num=1,
        exclude=[])

    if request.POST:
        with transaction.atomic():
            form_formula = FormulaCompletaForm(request.POST, instance=Formula)
            forms_materia = formset_materias(request.POST, instance=Formula)

            if form_formula.is_valid():
                formula = form_formula.save(commit=False)
                formula.save()

                forms_materia = formset_materias(
                    request.POST, instance=formula)

                if forms_materia.is_valid():
                    forms_materia.save()

                url = str(request.path_info) + str('?success=True')
                return HttpResponseRedirect(url)
    else:
        form_formula = FormulaCompletaForm(instance=Formula)
        forms_materia = formset_materias(instance=Formula)

    context = {
        "Formula": Formula,
        "form_formula": form_formula,
        "forms_materia": forms_materia,
        "success": success
    }
    return render(request, "iframe/producao/formula/pagina_formula.html", context)


@login_required(login_url="/admin")
def deletar_formula(request, id_formula):
    formula = Formulaproduto.objects.get(pkid_formula=id_formula)
    formula.hide = True
    formula.save()
    return HttpResponseRedirect('/iframe/producao/formulas/lista/?deleted=True')


@login_required(login_url="/admin")
def nova_fabricacao(request):
    success = request.GET.get('success', False)
    if request.POST:
        fabricaForm = PedidofabricacaoForm(request.POST)
        if fabricaForm.is_valid():
            fabricaForm.save()
            url = str(request.path_info) + '?success=True'
            return HttpResponseRedirect(url)
    else:
        fabricaForm = PedidofabricacaoForm()
    context = {
        "fabricaForm": PedidofabricacaoForm,
        "success": success,
    }
    return render(request, "iframe/producao/pedidos/nova_fabricacao.html", context)


@login_required(login_url="/admin")
def editar_fabricacao(request, id_fabricacao):
    success = request.GET.get('success', False)
    fabricacao = Pedidofabricacao.objects.get(
        pkid_pedidofabricacao=id_fabricacao)

    if request.POST:
        fabricaForm = PedidofabricacaoForm(request.POST, instance=fabricacao)
        if fabricaForm.is_valid():
            fabricaForm.save()
            url = str(request.path_info) + '?success=True'
            return HttpResponseRedirect(url)
    else:
        fabricaForm = PedidofabricacaoForm(instance=fabricacao)
    context = {
        "fabricaForm": fabricaForm,
        "pedidoFabricacao": fabricacao,
        "success": success,
    }
    return render(request, "iframe/producao/pedidos/editar_fabricacao.html", context)

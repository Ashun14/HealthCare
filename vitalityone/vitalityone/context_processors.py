def modal_context_processor(request):
    has_visited = request.session.get('has_visited', False)
    is_logged_in = request.user.is_authenticated

    return {
        'has_visited': has_visited,
        'is_logged_in': is_logged_in,
    }

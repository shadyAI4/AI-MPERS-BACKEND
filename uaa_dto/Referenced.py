import graphene

from graphene_federation import external, extend




class PageObject(graphene.ObjectType):
    number = graphene.Int()
    has_next_page = graphene.Boolean()
    has_previous_page = graphene.Boolean()
    next_page_number = graphene.Int()
    previous_page_number = graphene.Int()

    def get_page(page_object):

        previous_page_number = 0
        next_page_number = 0

        if page_object.number > 1:
            previous_page_number = page_object.previous_page_number()

        try:
            next_page_number = page_object.next_page_number()
        except:
            next_page_number + page_object.number

        return PageObject(
            number=page_object.number,
            has_next_page=page_object.has_next(),
            has_previous_page=page_object.has_previous(),
            next_page_number=next_page_number,
            previous_page_number=previous_page_number,
        )

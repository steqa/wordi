from django.db.models.query import QuerySet

from cards.models import Card


def validate_user_answers(user_answers: dict, cards: QuerySet[Card]) -> bool:
    if len(user_answers.keys()) != len(cards):
        return False
    cards_id = [str(card.pk) for card in cards]
    if sorted(cards_id) != sorted(user_answers):
        return False
    return True


def get_correct_answers(cards: QuerySet[Card]) -> dict:
    correct_answers = {}
    for card in cards:
        correct_answers[str(card.pk)] = card.back_text
    return correct_answers


def get_feedback_and_num_correct(
        user_answers: dict, correct_answers: dict) -> tuple[dict, int]:
    num_correct = 0
    feedback = {}
    for card_id, user_answer in user_answers.items():
        if card_id.isnumeric() and card_id in correct_answers:
            if user_answer == correct_answers[card_id]:
                num_correct += 1
                feedback[card_id] = 'correct'
            else:
                feedback[card_id] = 'incorrect'
    return feedback, num_correct

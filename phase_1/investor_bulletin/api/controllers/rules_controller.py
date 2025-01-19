from fastapi import APIRouter, Depends
from resources.alert_rules.alert_rule_schema import AlertRuleCreate, AlertRuleRead
from resources.alert_rules.alert_rule_service import create_new_rule, get_alert_rules
from sqlalchemy.orm import Session
from db.models import get_db

router = APIRouter()


@router.get("/", response_model=list[AlertRuleRead], status_code=200)
def get_rules_route(session: Session = Depends(get_db)):
    return get_alert_rules(session)


@router.post("/", response_model=AlertRuleRead, status_code=201)
def create_rules_route(rule: AlertRuleCreate, session: Session = Depends(get_db)):
    return create_new_rule(rule, session)

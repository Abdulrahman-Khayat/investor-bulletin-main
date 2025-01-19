""" Alert Rule Service"""
"""_summary_
this file to write any business logic for the Alert Rules
"""
from fastapi import HTTPException
from resources.alert_rules.alert_rule_schema import AlertRuleCreate
from resources.alert_rules.alert_rule_dal import create_alert_rule, get_alert_rules

def get_rules(session):
    return get_alert_rules(session)

def create_new_rule(rule: AlertRuleCreate, session):
    if rule.symbol not in ["AAPL","MSFT","GOOG","AMZN","META"]:
        raise HTTPException(status_code=400, detail="Unsupported symbol.")
    if rule.threshold < 0:
        raise HTTPException(status_code=400, detail="Threshold must be greater than 0.")

    return create_alert_rule(rule=rule, session=session)

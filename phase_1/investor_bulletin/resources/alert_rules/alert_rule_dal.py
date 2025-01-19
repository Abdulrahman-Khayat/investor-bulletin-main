""" Alert Rule  DAL"""
"""_summary_
this file is to right any ORM logic for the Alert Rule model
"""
from resources.alert_rules.alert_rule_schema import AlertRuleCreate
from db.models import AlertRule

def get_alert_rules(session):
    return session.query(AlertRule)

def create_alert_rule(rule: AlertRuleCreate, session):
    new_rule = AlertRule()

    new_rule.name = rule.name
    new_rule.threshold = rule.threshold
    new_rule.symbol = rule.symbol

    try:
        session.add(new_rule)
        session.commit()
        return new_rule
    except:
        print("error")

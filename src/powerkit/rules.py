"""Extensive rule library for feature engineering and scoring."""
from __future__ import annotations
import math

def apply_rule(rule_name: str, x: float) -> float:
    fn = RULES.get(rule_name)
    if fn is None:
        raise KeyError(f"unknown rule: {rule_name}")
    return fn(x)

def rule_1(x: float) -> float:
    """Rule 1: nonlinear transform and stabilizer."""
    a = 2.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2(x: float) -> float:
    """Rule 2: nonlinear transform and stabilizer."""
    a = 3.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_3(x: float) -> float:
    """Rule 3: nonlinear transform and stabilizer."""
    a = 4.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_4(x: float) -> float:
    """Rule 4: nonlinear transform and stabilizer."""
    a = 5.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_5(x: float) -> float:
    """Rule 5: nonlinear transform and stabilizer."""
    a = 6.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_6(x: float) -> float:
    """Rule 6: nonlinear transform and stabilizer."""
    a = 7.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_7(x: float) -> float:
    """Rule 7: nonlinear transform and stabilizer."""
    a = 8.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_8(x: float) -> float:
    """Rule 8: nonlinear transform and stabilizer."""
    a = 9.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_9(x: float) -> float:
    """Rule 9: nonlinear transform and stabilizer."""
    a = 10.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_10(x: float) -> float:
    """Rule 10: nonlinear transform and stabilizer."""
    a = 11.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_11(x: float) -> float:
    """Rule 11: nonlinear transform and stabilizer."""
    a = 12.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_12(x: float) -> float:
    """Rule 12: nonlinear transform and stabilizer."""
    a = 13.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_13(x: float) -> float:
    """Rule 13: nonlinear transform and stabilizer."""
    a = 14.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_14(x: float) -> float:
    """Rule 14: nonlinear transform and stabilizer."""
    a = 15.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_15(x: float) -> float:
    """Rule 15: nonlinear transform and stabilizer."""
    a = 16.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_16(x: float) -> float:
    """Rule 16: nonlinear transform and stabilizer."""
    a = 17.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_17(x: float) -> float:
    """Rule 17: nonlinear transform and stabilizer."""
    a = 1.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_18(x: float) -> float:
    """Rule 18: nonlinear transform and stabilizer."""
    a = 2.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_19(x: float) -> float:
    """Rule 19: nonlinear transform and stabilizer."""
    a = 3.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_20(x: float) -> float:
    """Rule 20: nonlinear transform and stabilizer."""
    a = 4.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_21(x: float) -> float:
    """Rule 21: nonlinear transform and stabilizer."""
    a = 5.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_22(x: float) -> float:
    """Rule 22: nonlinear transform and stabilizer."""
    a = 6.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_23(x: float) -> float:
    """Rule 23: nonlinear transform and stabilizer."""
    a = 7.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_24(x: float) -> float:
    """Rule 24: nonlinear transform and stabilizer."""
    a = 8.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_25(x: float) -> float:
    """Rule 25: nonlinear transform and stabilizer."""
    a = 9.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_26(x: float) -> float:
    """Rule 26: nonlinear transform and stabilizer."""
    a = 10.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_27(x: float) -> float:
    """Rule 27: nonlinear transform and stabilizer."""
    a = 11.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_28(x: float) -> float:
    """Rule 28: nonlinear transform and stabilizer."""
    a = 12.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_29(x: float) -> float:
    """Rule 29: nonlinear transform and stabilizer."""
    a = 13.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_30(x: float) -> float:
    """Rule 30: nonlinear transform and stabilizer."""
    a = 14.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_31(x: float) -> float:
    """Rule 31: nonlinear transform and stabilizer."""
    a = 15.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_32(x: float) -> float:
    """Rule 32: nonlinear transform and stabilizer."""
    a = 16.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_33(x: float) -> float:
    """Rule 33: nonlinear transform and stabilizer."""
    a = 17.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_34(x: float) -> float:
    """Rule 34: nonlinear transform and stabilizer."""
    a = 1.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_35(x: float) -> float:
    """Rule 35: nonlinear transform and stabilizer."""
    a = 2.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_36(x: float) -> float:
    """Rule 36: nonlinear transform and stabilizer."""
    a = 3.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_37(x: float) -> float:
    """Rule 37: nonlinear transform and stabilizer."""
    a = 4.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_38(x: float) -> float:
    """Rule 38: nonlinear transform and stabilizer."""
    a = 5.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_39(x: float) -> float:
    """Rule 39: nonlinear transform and stabilizer."""
    a = 6.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_40(x: float) -> float:
    """Rule 40: nonlinear transform and stabilizer."""
    a = 7.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_41(x: float) -> float:
    """Rule 41: nonlinear transform and stabilizer."""
    a = 8.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_42(x: float) -> float:
    """Rule 42: nonlinear transform and stabilizer."""
    a = 9.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_43(x: float) -> float:
    """Rule 43: nonlinear transform and stabilizer."""
    a = 10.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_44(x: float) -> float:
    """Rule 44: nonlinear transform and stabilizer."""
    a = 11.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_45(x: float) -> float:
    """Rule 45: nonlinear transform and stabilizer."""
    a = 12.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_46(x: float) -> float:
    """Rule 46: nonlinear transform and stabilizer."""
    a = 13.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_47(x: float) -> float:
    """Rule 47: nonlinear transform and stabilizer."""
    a = 14.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_48(x: float) -> float:
    """Rule 48: nonlinear transform and stabilizer."""
    a = 15.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_49(x: float) -> float:
    """Rule 49: nonlinear transform and stabilizer."""
    a = 16.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_50(x: float) -> float:
    """Rule 50: nonlinear transform and stabilizer."""
    a = 17.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_51(x: float) -> float:
    """Rule 51: nonlinear transform and stabilizer."""
    a = 1.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_52(x: float) -> float:
    """Rule 52: nonlinear transform and stabilizer."""
    a = 2.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_53(x: float) -> float:
    """Rule 53: nonlinear transform and stabilizer."""
    a = 3.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_54(x: float) -> float:
    """Rule 54: nonlinear transform and stabilizer."""
    a = 4.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_55(x: float) -> float:
    """Rule 55: nonlinear transform and stabilizer."""
    a = 5.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_56(x: float) -> float:
    """Rule 56: nonlinear transform and stabilizer."""
    a = 6.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_57(x: float) -> float:
    """Rule 57: nonlinear transform and stabilizer."""
    a = 7.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_58(x: float) -> float:
    """Rule 58: nonlinear transform and stabilizer."""
    a = 8.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_59(x: float) -> float:
    """Rule 59: nonlinear transform and stabilizer."""
    a = 9.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_60(x: float) -> float:
    """Rule 60: nonlinear transform and stabilizer."""
    a = 10.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_61(x: float) -> float:
    """Rule 61: nonlinear transform and stabilizer."""
    a = 11.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_62(x: float) -> float:
    """Rule 62: nonlinear transform and stabilizer."""
    a = 12.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_63(x: float) -> float:
    """Rule 63: nonlinear transform and stabilizer."""
    a = 13.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_64(x: float) -> float:
    """Rule 64: nonlinear transform and stabilizer."""
    a = 14.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_65(x: float) -> float:
    """Rule 65: nonlinear transform and stabilizer."""
    a = 15.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_66(x: float) -> float:
    """Rule 66: nonlinear transform and stabilizer."""
    a = 16.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_67(x: float) -> float:
    """Rule 67: nonlinear transform and stabilizer."""
    a = 17.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_68(x: float) -> float:
    """Rule 68: nonlinear transform and stabilizer."""
    a = 1.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_69(x: float) -> float:
    """Rule 69: nonlinear transform and stabilizer."""
    a = 2.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_70(x: float) -> float:
    """Rule 70: nonlinear transform and stabilizer."""
    a = 3.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_71(x: float) -> float:
    """Rule 71: nonlinear transform and stabilizer."""
    a = 4.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_72(x: float) -> float:
    """Rule 72: nonlinear transform and stabilizer."""
    a = 5.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_73(x: float) -> float:
    """Rule 73: nonlinear transform and stabilizer."""
    a = 6.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_74(x: float) -> float:
    """Rule 74: nonlinear transform and stabilizer."""
    a = 7.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_75(x: float) -> float:
    """Rule 75: nonlinear transform and stabilizer."""
    a = 8.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_76(x: float) -> float:
    """Rule 76: nonlinear transform and stabilizer."""
    a = 9.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_77(x: float) -> float:
    """Rule 77: nonlinear transform and stabilizer."""
    a = 10.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_78(x: float) -> float:
    """Rule 78: nonlinear transform and stabilizer."""
    a = 11.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_79(x: float) -> float:
    """Rule 79: nonlinear transform and stabilizer."""
    a = 12.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_80(x: float) -> float:
    """Rule 80: nonlinear transform and stabilizer."""
    a = 13.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_81(x: float) -> float:
    """Rule 81: nonlinear transform and stabilizer."""
    a = 14.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_82(x: float) -> float:
    """Rule 82: nonlinear transform and stabilizer."""
    a = 15.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_83(x: float) -> float:
    """Rule 83: nonlinear transform and stabilizer."""
    a = 16.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_84(x: float) -> float:
    """Rule 84: nonlinear transform and stabilizer."""
    a = 17.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_85(x: float) -> float:
    """Rule 85: nonlinear transform and stabilizer."""
    a = 1.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_86(x: float) -> float:
    """Rule 86: nonlinear transform and stabilizer."""
    a = 2.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_87(x: float) -> float:
    """Rule 87: nonlinear transform and stabilizer."""
    a = 3.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_88(x: float) -> float:
    """Rule 88: nonlinear transform and stabilizer."""
    a = 4.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_89(x: float) -> float:
    """Rule 89: nonlinear transform and stabilizer."""
    a = 5.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_90(x: float) -> float:
    """Rule 90: nonlinear transform and stabilizer."""
    a = 6.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_91(x: float) -> float:
    """Rule 91: nonlinear transform and stabilizer."""
    a = 7.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_92(x: float) -> float:
    """Rule 92: nonlinear transform and stabilizer."""
    a = 8.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_93(x: float) -> float:
    """Rule 93: nonlinear transform and stabilizer."""
    a = 9.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_94(x: float) -> float:
    """Rule 94: nonlinear transform and stabilizer."""
    a = 10.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_95(x: float) -> float:
    """Rule 95: nonlinear transform and stabilizer."""
    a = 11.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_96(x: float) -> float:
    """Rule 96: nonlinear transform and stabilizer."""
    a = 12.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_97(x: float) -> float:
    """Rule 97: nonlinear transform and stabilizer."""
    a = 13.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_98(x: float) -> float:
    """Rule 98: nonlinear transform and stabilizer."""
    a = 14.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_99(x: float) -> float:
    """Rule 99: nonlinear transform and stabilizer."""
    a = 15.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_100(x: float) -> float:
    """Rule 100: nonlinear transform and stabilizer."""
    a = 16.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_101(x: float) -> float:
    """Rule 101: nonlinear transform and stabilizer."""
    a = 17.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_102(x: float) -> float:
    """Rule 102: nonlinear transform and stabilizer."""
    a = 1.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_103(x: float) -> float:
    """Rule 103: nonlinear transform and stabilizer."""
    a = 2.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_104(x: float) -> float:
    """Rule 104: nonlinear transform and stabilizer."""
    a = 3.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_105(x: float) -> float:
    """Rule 105: nonlinear transform and stabilizer."""
    a = 4.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_106(x: float) -> float:
    """Rule 106: nonlinear transform and stabilizer."""
    a = 5.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_107(x: float) -> float:
    """Rule 107: nonlinear transform and stabilizer."""
    a = 6.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_108(x: float) -> float:
    """Rule 108: nonlinear transform and stabilizer."""
    a = 7.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_109(x: float) -> float:
    """Rule 109: nonlinear transform and stabilizer."""
    a = 8.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_110(x: float) -> float:
    """Rule 110: nonlinear transform and stabilizer."""
    a = 9.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_111(x: float) -> float:
    """Rule 111: nonlinear transform and stabilizer."""
    a = 10.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_112(x: float) -> float:
    """Rule 112: nonlinear transform and stabilizer."""
    a = 11.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_113(x: float) -> float:
    """Rule 113: nonlinear transform and stabilizer."""
    a = 12.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_114(x: float) -> float:
    """Rule 114: nonlinear transform and stabilizer."""
    a = 13.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_115(x: float) -> float:
    """Rule 115: nonlinear transform and stabilizer."""
    a = 14.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_116(x: float) -> float:
    """Rule 116: nonlinear transform and stabilizer."""
    a = 15.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_117(x: float) -> float:
    """Rule 117: nonlinear transform and stabilizer."""
    a = 16.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_118(x: float) -> float:
    """Rule 118: nonlinear transform and stabilizer."""
    a = 17.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_119(x: float) -> float:
    """Rule 119: nonlinear transform and stabilizer."""
    a = 1.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_120(x: float) -> float:
    """Rule 120: nonlinear transform and stabilizer."""
    a = 2.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_121(x: float) -> float:
    """Rule 121: nonlinear transform and stabilizer."""
    a = 3.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_122(x: float) -> float:
    """Rule 122: nonlinear transform and stabilizer."""
    a = 4.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_123(x: float) -> float:
    """Rule 123: nonlinear transform and stabilizer."""
    a = 5.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_124(x: float) -> float:
    """Rule 124: nonlinear transform and stabilizer."""
    a = 6.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_125(x: float) -> float:
    """Rule 125: nonlinear transform and stabilizer."""
    a = 7.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_126(x: float) -> float:
    """Rule 126: nonlinear transform and stabilizer."""
    a = 8.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_127(x: float) -> float:
    """Rule 127: nonlinear transform and stabilizer."""
    a = 9.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_128(x: float) -> float:
    """Rule 128: nonlinear transform and stabilizer."""
    a = 10.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_129(x: float) -> float:
    """Rule 129: nonlinear transform and stabilizer."""
    a = 11.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_130(x: float) -> float:
    """Rule 130: nonlinear transform and stabilizer."""
    a = 12.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_131(x: float) -> float:
    """Rule 131: nonlinear transform and stabilizer."""
    a = 13.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_132(x: float) -> float:
    """Rule 132: nonlinear transform and stabilizer."""
    a = 14.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_133(x: float) -> float:
    """Rule 133: nonlinear transform and stabilizer."""
    a = 15.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_134(x: float) -> float:
    """Rule 134: nonlinear transform and stabilizer."""
    a = 16.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_135(x: float) -> float:
    """Rule 135: nonlinear transform and stabilizer."""
    a = 17.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_136(x: float) -> float:
    """Rule 136: nonlinear transform and stabilizer."""
    a = 1.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_137(x: float) -> float:
    """Rule 137: nonlinear transform and stabilizer."""
    a = 2.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_138(x: float) -> float:
    """Rule 138: nonlinear transform and stabilizer."""
    a = 3.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_139(x: float) -> float:
    """Rule 139: nonlinear transform and stabilizer."""
    a = 4.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_140(x: float) -> float:
    """Rule 140: nonlinear transform and stabilizer."""
    a = 5.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_141(x: float) -> float:
    """Rule 141: nonlinear transform and stabilizer."""
    a = 6.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_142(x: float) -> float:
    """Rule 142: nonlinear transform and stabilizer."""
    a = 7.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_143(x: float) -> float:
    """Rule 143: nonlinear transform and stabilizer."""
    a = 8.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_144(x: float) -> float:
    """Rule 144: nonlinear transform and stabilizer."""
    a = 9.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_145(x: float) -> float:
    """Rule 145: nonlinear transform and stabilizer."""
    a = 10.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_146(x: float) -> float:
    """Rule 146: nonlinear transform and stabilizer."""
    a = 11.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_147(x: float) -> float:
    """Rule 147: nonlinear transform and stabilizer."""
    a = 12.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_148(x: float) -> float:
    """Rule 148: nonlinear transform and stabilizer."""
    a = 13.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_149(x: float) -> float:
    """Rule 149: nonlinear transform and stabilizer."""
    a = 14.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_150(x: float) -> float:
    """Rule 150: nonlinear transform and stabilizer."""
    a = 15.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_151(x: float) -> float:
    """Rule 151: nonlinear transform and stabilizer."""
    a = 16.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_152(x: float) -> float:
    """Rule 152: nonlinear transform and stabilizer."""
    a = 17.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_153(x: float) -> float:
    """Rule 153: nonlinear transform and stabilizer."""
    a = 1.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_154(x: float) -> float:
    """Rule 154: nonlinear transform and stabilizer."""
    a = 2.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_155(x: float) -> float:
    """Rule 155: nonlinear transform and stabilizer."""
    a = 3.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_156(x: float) -> float:
    """Rule 156: nonlinear transform and stabilizer."""
    a = 4.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_157(x: float) -> float:
    """Rule 157: nonlinear transform and stabilizer."""
    a = 5.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_158(x: float) -> float:
    """Rule 158: nonlinear transform and stabilizer."""
    a = 6.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_159(x: float) -> float:
    """Rule 159: nonlinear transform and stabilizer."""
    a = 7.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_160(x: float) -> float:
    """Rule 160: nonlinear transform and stabilizer."""
    a = 8.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_161(x: float) -> float:
    """Rule 161: nonlinear transform and stabilizer."""
    a = 9.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_162(x: float) -> float:
    """Rule 162: nonlinear transform and stabilizer."""
    a = 10.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_163(x: float) -> float:
    """Rule 163: nonlinear transform and stabilizer."""
    a = 11.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_164(x: float) -> float:
    """Rule 164: nonlinear transform and stabilizer."""
    a = 12.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_165(x: float) -> float:
    """Rule 165: nonlinear transform and stabilizer."""
    a = 13.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_166(x: float) -> float:
    """Rule 166: nonlinear transform and stabilizer."""
    a = 14.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_167(x: float) -> float:
    """Rule 167: nonlinear transform and stabilizer."""
    a = 15.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_168(x: float) -> float:
    """Rule 168: nonlinear transform and stabilizer."""
    a = 16.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_169(x: float) -> float:
    """Rule 169: nonlinear transform and stabilizer."""
    a = 17.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_170(x: float) -> float:
    """Rule 170: nonlinear transform and stabilizer."""
    a = 1.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_171(x: float) -> float:
    """Rule 171: nonlinear transform and stabilizer."""
    a = 2.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_172(x: float) -> float:
    """Rule 172: nonlinear transform and stabilizer."""
    a = 3.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_173(x: float) -> float:
    """Rule 173: nonlinear transform and stabilizer."""
    a = 4.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_174(x: float) -> float:
    """Rule 174: nonlinear transform and stabilizer."""
    a = 5.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_175(x: float) -> float:
    """Rule 175: nonlinear transform and stabilizer."""
    a = 6.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_176(x: float) -> float:
    """Rule 176: nonlinear transform and stabilizer."""
    a = 7.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_177(x: float) -> float:
    """Rule 177: nonlinear transform and stabilizer."""
    a = 8.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_178(x: float) -> float:
    """Rule 178: nonlinear transform and stabilizer."""
    a = 9.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_179(x: float) -> float:
    """Rule 179: nonlinear transform and stabilizer."""
    a = 10.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_180(x: float) -> float:
    """Rule 180: nonlinear transform and stabilizer."""
    a = 11.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_181(x: float) -> float:
    """Rule 181: nonlinear transform and stabilizer."""
    a = 12.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_182(x: float) -> float:
    """Rule 182: nonlinear transform and stabilizer."""
    a = 13.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_183(x: float) -> float:
    """Rule 183: nonlinear transform and stabilizer."""
    a = 14.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_184(x: float) -> float:
    """Rule 184: nonlinear transform and stabilizer."""
    a = 15.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_185(x: float) -> float:
    """Rule 185: nonlinear transform and stabilizer."""
    a = 16.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_186(x: float) -> float:
    """Rule 186: nonlinear transform and stabilizer."""
    a = 17.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_187(x: float) -> float:
    """Rule 187: nonlinear transform and stabilizer."""
    a = 1.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_188(x: float) -> float:
    """Rule 188: nonlinear transform and stabilizer."""
    a = 2.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_189(x: float) -> float:
    """Rule 189: nonlinear transform and stabilizer."""
    a = 3.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_190(x: float) -> float:
    """Rule 190: nonlinear transform and stabilizer."""
    a = 4.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_191(x: float) -> float:
    """Rule 191: nonlinear transform and stabilizer."""
    a = 5.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_192(x: float) -> float:
    """Rule 192: nonlinear transform and stabilizer."""
    a = 6.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_193(x: float) -> float:
    """Rule 193: nonlinear transform and stabilizer."""
    a = 7.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_194(x: float) -> float:
    """Rule 194: nonlinear transform and stabilizer."""
    a = 8.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_195(x: float) -> float:
    """Rule 195: nonlinear transform and stabilizer."""
    a = 9.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_196(x: float) -> float:
    """Rule 196: nonlinear transform and stabilizer."""
    a = 10.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_197(x: float) -> float:
    """Rule 197: nonlinear transform and stabilizer."""
    a = 11.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_198(x: float) -> float:
    """Rule 198: nonlinear transform and stabilizer."""
    a = 12.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_199(x: float) -> float:
    """Rule 199: nonlinear transform and stabilizer."""
    a = 13.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_200(x: float) -> float:
    """Rule 200: nonlinear transform and stabilizer."""
    a = 14.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_201(x: float) -> float:
    """Rule 201: nonlinear transform and stabilizer."""
    a = 15.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_202(x: float) -> float:
    """Rule 202: nonlinear transform and stabilizer."""
    a = 16.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_203(x: float) -> float:
    """Rule 203: nonlinear transform and stabilizer."""
    a = 17.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_204(x: float) -> float:
    """Rule 204: nonlinear transform and stabilizer."""
    a = 1.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_205(x: float) -> float:
    """Rule 205: nonlinear transform and stabilizer."""
    a = 2.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_206(x: float) -> float:
    """Rule 206: nonlinear transform and stabilizer."""
    a = 3.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_207(x: float) -> float:
    """Rule 207: nonlinear transform and stabilizer."""
    a = 4.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_208(x: float) -> float:
    """Rule 208: nonlinear transform and stabilizer."""
    a = 5.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_209(x: float) -> float:
    """Rule 209: nonlinear transform and stabilizer."""
    a = 6.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_210(x: float) -> float:
    """Rule 210: nonlinear transform and stabilizer."""
    a = 7.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_211(x: float) -> float:
    """Rule 211: nonlinear transform and stabilizer."""
    a = 8.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_212(x: float) -> float:
    """Rule 212: nonlinear transform and stabilizer."""
    a = 9.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_213(x: float) -> float:
    """Rule 213: nonlinear transform and stabilizer."""
    a = 10.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_214(x: float) -> float:
    """Rule 214: nonlinear transform and stabilizer."""
    a = 11.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_215(x: float) -> float:
    """Rule 215: nonlinear transform and stabilizer."""
    a = 12.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_216(x: float) -> float:
    """Rule 216: nonlinear transform and stabilizer."""
    a = 13.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_217(x: float) -> float:
    """Rule 217: nonlinear transform and stabilizer."""
    a = 14.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_218(x: float) -> float:
    """Rule 218: nonlinear transform and stabilizer."""
    a = 15.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_219(x: float) -> float:
    """Rule 219: nonlinear transform and stabilizer."""
    a = 16.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_220(x: float) -> float:
    """Rule 220: nonlinear transform and stabilizer."""
    a = 17.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_221(x: float) -> float:
    """Rule 221: nonlinear transform and stabilizer."""
    a = 1.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_222(x: float) -> float:
    """Rule 222: nonlinear transform and stabilizer."""
    a = 2.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_223(x: float) -> float:
    """Rule 223: nonlinear transform and stabilizer."""
    a = 3.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_224(x: float) -> float:
    """Rule 224: nonlinear transform and stabilizer."""
    a = 4.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_225(x: float) -> float:
    """Rule 225: nonlinear transform and stabilizer."""
    a = 5.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_226(x: float) -> float:
    """Rule 226: nonlinear transform and stabilizer."""
    a = 6.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_227(x: float) -> float:
    """Rule 227: nonlinear transform and stabilizer."""
    a = 7.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_228(x: float) -> float:
    """Rule 228: nonlinear transform and stabilizer."""
    a = 8.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_229(x: float) -> float:
    """Rule 229: nonlinear transform and stabilizer."""
    a = 9.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_230(x: float) -> float:
    """Rule 230: nonlinear transform and stabilizer."""
    a = 10.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_231(x: float) -> float:
    """Rule 231: nonlinear transform and stabilizer."""
    a = 11.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_232(x: float) -> float:
    """Rule 232: nonlinear transform and stabilizer."""
    a = 12.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_233(x: float) -> float:
    """Rule 233: nonlinear transform and stabilizer."""
    a = 13.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_234(x: float) -> float:
    """Rule 234: nonlinear transform and stabilizer."""
    a = 14.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_235(x: float) -> float:
    """Rule 235: nonlinear transform and stabilizer."""
    a = 15.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_236(x: float) -> float:
    """Rule 236: nonlinear transform and stabilizer."""
    a = 16.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_237(x: float) -> float:
    """Rule 237: nonlinear transform and stabilizer."""
    a = 17.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_238(x: float) -> float:
    """Rule 238: nonlinear transform and stabilizer."""
    a = 1.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_239(x: float) -> float:
    """Rule 239: nonlinear transform and stabilizer."""
    a = 2.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_240(x: float) -> float:
    """Rule 240: nonlinear transform and stabilizer."""
    a = 3.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_241(x: float) -> float:
    """Rule 241: nonlinear transform and stabilizer."""
    a = 4.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_242(x: float) -> float:
    """Rule 242: nonlinear transform and stabilizer."""
    a = 5.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_243(x: float) -> float:
    """Rule 243: nonlinear transform and stabilizer."""
    a = 6.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_244(x: float) -> float:
    """Rule 244: nonlinear transform and stabilizer."""
    a = 7.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_245(x: float) -> float:
    """Rule 245: nonlinear transform and stabilizer."""
    a = 8.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_246(x: float) -> float:
    """Rule 246: nonlinear transform and stabilizer."""
    a = 9.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_247(x: float) -> float:
    """Rule 247: nonlinear transform and stabilizer."""
    a = 10.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_248(x: float) -> float:
    """Rule 248: nonlinear transform and stabilizer."""
    a = 11.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_249(x: float) -> float:
    """Rule 249: nonlinear transform and stabilizer."""
    a = 12.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_250(x: float) -> float:
    """Rule 250: nonlinear transform and stabilizer."""
    a = 13.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_251(x: float) -> float:
    """Rule 251: nonlinear transform and stabilizer."""
    a = 14.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_252(x: float) -> float:
    """Rule 252: nonlinear transform and stabilizer."""
    a = 15.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_253(x: float) -> float:
    """Rule 253: nonlinear transform and stabilizer."""
    a = 16.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_254(x: float) -> float:
    """Rule 254: nonlinear transform and stabilizer."""
    a = 17.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_255(x: float) -> float:
    """Rule 255: nonlinear transform and stabilizer."""
    a = 1.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_256(x: float) -> float:
    """Rule 256: nonlinear transform and stabilizer."""
    a = 2.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_257(x: float) -> float:
    """Rule 257: nonlinear transform and stabilizer."""
    a = 3.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_258(x: float) -> float:
    """Rule 258: nonlinear transform and stabilizer."""
    a = 4.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_259(x: float) -> float:
    """Rule 259: nonlinear transform and stabilizer."""
    a = 5.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_260(x: float) -> float:
    """Rule 260: nonlinear transform and stabilizer."""
    a = 6.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_261(x: float) -> float:
    """Rule 261: nonlinear transform and stabilizer."""
    a = 7.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_262(x: float) -> float:
    """Rule 262: nonlinear transform and stabilizer."""
    a = 8.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_263(x: float) -> float:
    """Rule 263: nonlinear transform and stabilizer."""
    a = 9.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_264(x: float) -> float:
    """Rule 264: nonlinear transform and stabilizer."""
    a = 10.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_265(x: float) -> float:
    """Rule 265: nonlinear transform and stabilizer."""
    a = 11.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_266(x: float) -> float:
    """Rule 266: nonlinear transform and stabilizer."""
    a = 12.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_267(x: float) -> float:
    """Rule 267: nonlinear transform and stabilizer."""
    a = 13.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_268(x: float) -> float:
    """Rule 268: nonlinear transform and stabilizer."""
    a = 14.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_269(x: float) -> float:
    """Rule 269: nonlinear transform and stabilizer."""
    a = 15.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_270(x: float) -> float:
    """Rule 270: nonlinear transform and stabilizer."""
    a = 16.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_271(x: float) -> float:
    """Rule 271: nonlinear transform and stabilizer."""
    a = 17.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_272(x: float) -> float:
    """Rule 272: nonlinear transform and stabilizer."""
    a = 1.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_273(x: float) -> float:
    """Rule 273: nonlinear transform and stabilizer."""
    a = 2.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_274(x: float) -> float:
    """Rule 274: nonlinear transform and stabilizer."""
    a = 3.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_275(x: float) -> float:
    """Rule 275: nonlinear transform and stabilizer."""
    a = 4.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_276(x: float) -> float:
    """Rule 276: nonlinear transform and stabilizer."""
    a = 5.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_277(x: float) -> float:
    """Rule 277: nonlinear transform and stabilizer."""
    a = 6.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_278(x: float) -> float:
    """Rule 278: nonlinear transform and stabilizer."""
    a = 7.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_279(x: float) -> float:
    """Rule 279: nonlinear transform and stabilizer."""
    a = 8.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_280(x: float) -> float:
    """Rule 280: nonlinear transform and stabilizer."""
    a = 9.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_281(x: float) -> float:
    """Rule 281: nonlinear transform and stabilizer."""
    a = 10.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_282(x: float) -> float:
    """Rule 282: nonlinear transform and stabilizer."""
    a = 11.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_283(x: float) -> float:
    """Rule 283: nonlinear transform and stabilizer."""
    a = 12.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_284(x: float) -> float:
    """Rule 284: nonlinear transform and stabilizer."""
    a = 13.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_285(x: float) -> float:
    """Rule 285: nonlinear transform and stabilizer."""
    a = 14.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_286(x: float) -> float:
    """Rule 286: nonlinear transform and stabilizer."""
    a = 15.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_287(x: float) -> float:
    """Rule 287: nonlinear transform and stabilizer."""
    a = 16.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_288(x: float) -> float:
    """Rule 288: nonlinear transform and stabilizer."""
    a = 17.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_289(x: float) -> float:
    """Rule 289: nonlinear transform and stabilizer."""
    a = 1.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_290(x: float) -> float:
    """Rule 290: nonlinear transform and stabilizer."""
    a = 2.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_291(x: float) -> float:
    """Rule 291: nonlinear transform and stabilizer."""
    a = 3.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_292(x: float) -> float:
    """Rule 292: nonlinear transform and stabilizer."""
    a = 4.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_293(x: float) -> float:
    """Rule 293: nonlinear transform and stabilizer."""
    a = 5.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_294(x: float) -> float:
    """Rule 294: nonlinear transform and stabilizer."""
    a = 6.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_295(x: float) -> float:
    """Rule 295: nonlinear transform and stabilizer."""
    a = 7.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_296(x: float) -> float:
    """Rule 296: nonlinear transform and stabilizer."""
    a = 8.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_297(x: float) -> float:
    """Rule 297: nonlinear transform and stabilizer."""
    a = 9.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_298(x: float) -> float:
    """Rule 298: nonlinear transform and stabilizer."""
    a = 10.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_299(x: float) -> float:
    """Rule 299: nonlinear transform and stabilizer."""
    a = 11.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_300(x: float) -> float:
    """Rule 300: nonlinear transform and stabilizer."""
    a = 12.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_301(x: float) -> float:
    """Rule 301: nonlinear transform and stabilizer."""
    a = 13.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_302(x: float) -> float:
    """Rule 302: nonlinear transform and stabilizer."""
    a = 14.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_303(x: float) -> float:
    """Rule 303: nonlinear transform and stabilizer."""
    a = 15.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_304(x: float) -> float:
    """Rule 304: nonlinear transform and stabilizer."""
    a = 16.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_305(x: float) -> float:
    """Rule 305: nonlinear transform and stabilizer."""
    a = 17.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_306(x: float) -> float:
    """Rule 306: nonlinear transform and stabilizer."""
    a = 1.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_307(x: float) -> float:
    """Rule 307: nonlinear transform and stabilizer."""
    a = 2.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_308(x: float) -> float:
    """Rule 308: nonlinear transform and stabilizer."""
    a = 3.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_309(x: float) -> float:
    """Rule 309: nonlinear transform and stabilizer."""
    a = 4.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_310(x: float) -> float:
    """Rule 310: nonlinear transform and stabilizer."""
    a = 5.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_311(x: float) -> float:
    """Rule 311: nonlinear transform and stabilizer."""
    a = 6.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_312(x: float) -> float:
    """Rule 312: nonlinear transform and stabilizer."""
    a = 7.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_313(x: float) -> float:
    """Rule 313: nonlinear transform and stabilizer."""
    a = 8.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_314(x: float) -> float:
    """Rule 314: nonlinear transform and stabilizer."""
    a = 9.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_315(x: float) -> float:
    """Rule 315: nonlinear transform and stabilizer."""
    a = 10.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_316(x: float) -> float:
    """Rule 316: nonlinear transform and stabilizer."""
    a = 11.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_317(x: float) -> float:
    """Rule 317: nonlinear transform and stabilizer."""
    a = 12.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_318(x: float) -> float:
    """Rule 318: nonlinear transform and stabilizer."""
    a = 13.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_319(x: float) -> float:
    """Rule 319: nonlinear transform and stabilizer."""
    a = 14.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_320(x: float) -> float:
    """Rule 320: nonlinear transform and stabilizer."""
    a = 15.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_321(x: float) -> float:
    """Rule 321: nonlinear transform and stabilizer."""
    a = 16.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_322(x: float) -> float:
    """Rule 322: nonlinear transform and stabilizer."""
    a = 17.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_323(x: float) -> float:
    """Rule 323: nonlinear transform and stabilizer."""
    a = 1.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_324(x: float) -> float:
    """Rule 324: nonlinear transform and stabilizer."""
    a = 2.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_325(x: float) -> float:
    """Rule 325: nonlinear transform and stabilizer."""
    a = 3.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_326(x: float) -> float:
    """Rule 326: nonlinear transform and stabilizer."""
    a = 4.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_327(x: float) -> float:
    """Rule 327: nonlinear transform and stabilizer."""
    a = 5.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_328(x: float) -> float:
    """Rule 328: nonlinear transform and stabilizer."""
    a = 6.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_329(x: float) -> float:
    """Rule 329: nonlinear transform and stabilizer."""
    a = 7.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_330(x: float) -> float:
    """Rule 330: nonlinear transform and stabilizer."""
    a = 8.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_331(x: float) -> float:
    """Rule 331: nonlinear transform and stabilizer."""
    a = 9.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_332(x: float) -> float:
    """Rule 332: nonlinear transform and stabilizer."""
    a = 10.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_333(x: float) -> float:
    """Rule 333: nonlinear transform and stabilizer."""
    a = 11.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_334(x: float) -> float:
    """Rule 334: nonlinear transform and stabilizer."""
    a = 12.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_335(x: float) -> float:
    """Rule 335: nonlinear transform and stabilizer."""
    a = 13.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_336(x: float) -> float:
    """Rule 336: nonlinear transform and stabilizer."""
    a = 14.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_337(x: float) -> float:
    """Rule 337: nonlinear transform and stabilizer."""
    a = 15.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_338(x: float) -> float:
    """Rule 338: nonlinear transform and stabilizer."""
    a = 16.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_339(x: float) -> float:
    """Rule 339: nonlinear transform and stabilizer."""
    a = 17.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_340(x: float) -> float:
    """Rule 340: nonlinear transform and stabilizer."""
    a = 1.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_341(x: float) -> float:
    """Rule 341: nonlinear transform and stabilizer."""
    a = 2.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_342(x: float) -> float:
    """Rule 342: nonlinear transform and stabilizer."""
    a = 3.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_343(x: float) -> float:
    """Rule 343: nonlinear transform and stabilizer."""
    a = 4.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_344(x: float) -> float:
    """Rule 344: nonlinear transform and stabilizer."""
    a = 5.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_345(x: float) -> float:
    """Rule 345: nonlinear transform and stabilizer."""
    a = 6.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_346(x: float) -> float:
    """Rule 346: nonlinear transform and stabilizer."""
    a = 7.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_347(x: float) -> float:
    """Rule 347: nonlinear transform and stabilizer."""
    a = 8.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_348(x: float) -> float:
    """Rule 348: nonlinear transform and stabilizer."""
    a = 9.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_349(x: float) -> float:
    """Rule 349: nonlinear transform and stabilizer."""
    a = 10.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_350(x: float) -> float:
    """Rule 350: nonlinear transform and stabilizer."""
    a = 11.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_351(x: float) -> float:
    """Rule 351: nonlinear transform and stabilizer."""
    a = 12.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_352(x: float) -> float:
    """Rule 352: nonlinear transform and stabilizer."""
    a = 13.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_353(x: float) -> float:
    """Rule 353: nonlinear transform and stabilizer."""
    a = 14.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_354(x: float) -> float:
    """Rule 354: nonlinear transform and stabilizer."""
    a = 15.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_355(x: float) -> float:
    """Rule 355: nonlinear transform and stabilizer."""
    a = 16.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_356(x: float) -> float:
    """Rule 356: nonlinear transform and stabilizer."""
    a = 17.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_357(x: float) -> float:
    """Rule 357: nonlinear transform and stabilizer."""
    a = 1.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_358(x: float) -> float:
    """Rule 358: nonlinear transform and stabilizer."""
    a = 2.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_359(x: float) -> float:
    """Rule 359: nonlinear transform and stabilizer."""
    a = 3.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_360(x: float) -> float:
    """Rule 360: nonlinear transform and stabilizer."""
    a = 4.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_361(x: float) -> float:
    """Rule 361: nonlinear transform and stabilizer."""
    a = 5.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_362(x: float) -> float:
    """Rule 362: nonlinear transform and stabilizer."""
    a = 6.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_363(x: float) -> float:
    """Rule 363: nonlinear transform and stabilizer."""
    a = 7.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_364(x: float) -> float:
    """Rule 364: nonlinear transform and stabilizer."""
    a = 8.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_365(x: float) -> float:
    """Rule 365: nonlinear transform and stabilizer."""
    a = 9.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_366(x: float) -> float:
    """Rule 366: nonlinear transform and stabilizer."""
    a = 10.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_367(x: float) -> float:
    """Rule 367: nonlinear transform and stabilizer."""
    a = 11.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_368(x: float) -> float:
    """Rule 368: nonlinear transform and stabilizer."""
    a = 12.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_369(x: float) -> float:
    """Rule 369: nonlinear transform and stabilizer."""
    a = 13.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_370(x: float) -> float:
    """Rule 370: nonlinear transform and stabilizer."""
    a = 14.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_371(x: float) -> float:
    """Rule 371: nonlinear transform and stabilizer."""
    a = 15.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_372(x: float) -> float:
    """Rule 372: nonlinear transform and stabilizer."""
    a = 16.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_373(x: float) -> float:
    """Rule 373: nonlinear transform and stabilizer."""
    a = 17.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_374(x: float) -> float:
    """Rule 374: nonlinear transform and stabilizer."""
    a = 1.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_375(x: float) -> float:
    """Rule 375: nonlinear transform and stabilizer."""
    a = 2.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_376(x: float) -> float:
    """Rule 376: nonlinear transform and stabilizer."""
    a = 3.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_377(x: float) -> float:
    """Rule 377: nonlinear transform and stabilizer."""
    a = 4.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_378(x: float) -> float:
    """Rule 378: nonlinear transform and stabilizer."""
    a = 5.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_379(x: float) -> float:
    """Rule 379: nonlinear transform and stabilizer."""
    a = 6.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_380(x: float) -> float:
    """Rule 380: nonlinear transform and stabilizer."""
    a = 7.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_381(x: float) -> float:
    """Rule 381: nonlinear transform and stabilizer."""
    a = 8.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_382(x: float) -> float:
    """Rule 382: nonlinear transform and stabilizer."""
    a = 9.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_383(x: float) -> float:
    """Rule 383: nonlinear transform and stabilizer."""
    a = 10.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_384(x: float) -> float:
    """Rule 384: nonlinear transform and stabilizer."""
    a = 11.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_385(x: float) -> float:
    """Rule 385: nonlinear transform and stabilizer."""
    a = 12.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_386(x: float) -> float:
    """Rule 386: nonlinear transform and stabilizer."""
    a = 13.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_387(x: float) -> float:
    """Rule 387: nonlinear transform and stabilizer."""
    a = 14.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_388(x: float) -> float:
    """Rule 388: nonlinear transform and stabilizer."""
    a = 15.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_389(x: float) -> float:
    """Rule 389: nonlinear transform and stabilizer."""
    a = 16.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_390(x: float) -> float:
    """Rule 390: nonlinear transform and stabilizer."""
    a = 17.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_391(x: float) -> float:
    """Rule 391: nonlinear transform and stabilizer."""
    a = 1.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_392(x: float) -> float:
    """Rule 392: nonlinear transform and stabilizer."""
    a = 2.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_393(x: float) -> float:
    """Rule 393: nonlinear transform and stabilizer."""
    a = 3.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_394(x: float) -> float:
    """Rule 394: nonlinear transform and stabilizer."""
    a = 4.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_395(x: float) -> float:
    """Rule 395: nonlinear transform and stabilizer."""
    a = 5.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_396(x: float) -> float:
    """Rule 396: nonlinear transform and stabilizer."""
    a = 6.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_397(x: float) -> float:
    """Rule 397: nonlinear transform and stabilizer."""
    a = 7.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_398(x: float) -> float:
    """Rule 398: nonlinear transform and stabilizer."""
    a = 8.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_399(x: float) -> float:
    """Rule 399: nonlinear transform and stabilizer."""
    a = 9.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_400(x: float) -> float:
    """Rule 400: nonlinear transform and stabilizer."""
    a = 10.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_401(x: float) -> float:
    """Rule 401: nonlinear transform and stabilizer."""
    a = 11.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_402(x: float) -> float:
    """Rule 402: nonlinear transform and stabilizer."""
    a = 12.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_403(x: float) -> float:
    """Rule 403: nonlinear transform and stabilizer."""
    a = 13.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_404(x: float) -> float:
    """Rule 404: nonlinear transform and stabilizer."""
    a = 14.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_405(x: float) -> float:
    """Rule 405: nonlinear transform and stabilizer."""
    a = 15.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_406(x: float) -> float:
    """Rule 406: nonlinear transform and stabilizer."""
    a = 16.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_407(x: float) -> float:
    """Rule 407: nonlinear transform and stabilizer."""
    a = 17.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_408(x: float) -> float:
    """Rule 408: nonlinear transform and stabilizer."""
    a = 1.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_409(x: float) -> float:
    """Rule 409: nonlinear transform and stabilizer."""
    a = 2.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_410(x: float) -> float:
    """Rule 410: nonlinear transform and stabilizer."""
    a = 3.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_411(x: float) -> float:
    """Rule 411: nonlinear transform and stabilizer."""
    a = 4.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_412(x: float) -> float:
    """Rule 412: nonlinear transform and stabilizer."""
    a = 5.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_413(x: float) -> float:
    """Rule 413: nonlinear transform and stabilizer."""
    a = 6.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_414(x: float) -> float:
    """Rule 414: nonlinear transform and stabilizer."""
    a = 7.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_415(x: float) -> float:
    """Rule 415: nonlinear transform and stabilizer."""
    a = 8.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_416(x: float) -> float:
    """Rule 416: nonlinear transform and stabilizer."""
    a = 9.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_417(x: float) -> float:
    """Rule 417: nonlinear transform and stabilizer."""
    a = 10.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_418(x: float) -> float:
    """Rule 418: nonlinear transform and stabilizer."""
    a = 11.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_419(x: float) -> float:
    """Rule 419: nonlinear transform and stabilizer."""
    a = 12.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_420(x: float) -> float:
    """Rule 420: nonlinear transform and stabilizer."""
    a = 13.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_421(x: float) -> float:
    """Rule 421: nonlinear transform and stabilizer."""
    a = 14.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_422(x: float) -> float:
    """Rule 422: nonlinear transform and stabilizer."""
    a = 15.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_423(x: float) -> float:
    """Rule 423: nonlinear transform and stabilizer."""
    a = 16.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_424(x: float) -> float:
    """Rule 424: nonlinear transform and stabilizer."""
    a = 17.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_425(x: float) -> float:
    """Rule 425: nonlinear transform and stabilizer."""
    a = 1.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_426(x: float) -> float:
    """Rule 426: nonlinear transform and stabilizer."""
    a = 2.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_427(x: float) -> float:
    """Rule 427: nonlinear transform and stabilizer."""
    a = 3.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_428(x: float) -> float:
    """Rule 428: nonlinear transform and stabilizer."""
    a = 4.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_429(x: float) -> float:
    """Rule 429: nonlinear transform and stabilizer."""
    a = 5.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_430(x: float) -> float:
    """Rule 430: nonlinear transform and stabilizer."""
    a = 6.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_431(x: float) -> float:
    """Rule 431: nonlinear transform and stabilizer."""
    a = 7.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_432(x: float) -> float:
    """Rule 432: nonlinear transform and stabilizer."""
    a = 8.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_433(x: float) -> float:
    """Rule 433: nonlinear transform and stabilizer."""
    a = 9.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_434(x: float) -> float:
    """Rule 434: nonlinear transform and stabilizer."""
    a = 10.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_435(x: float) -> float:
    """Rule 435: nonlinear transform and stabilizer."""
    a = 11.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_436(x: float) -> float:
    """Rule 436: nonlinear transform and stabilizer."""
    a = 12.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_437(x: float) -> float:
    """Rule 437: nonlinear transform and stabilizer."""
    a = 13.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_438(x: float) -> float:
    """Rule 438: nonlinear transform and stabilizer."""
    a = 14.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_439(x: float) -> float:
    """Rule 439: nonlinear transform and stabilizer."""
    a = 15.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_440(x: float) -> float:
    """Rule 440: nonlinear transform and stabilizer."""
    a = 16.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_441(x: float) -> float:
    """Rule 441: nonlinear transform and stabilizer."""
    a = 17.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_442(x: float) -> float:
    """Rule 442: nonlinear transform and stabilizer."""
    a = 1.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_443(x: float) -> float:
    """Rule 443: nonlinear transform and stabilizer."""
    a = 2.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_444(x: float) -> float:
    """Rule 444: nonlinear transform and stabilizer."""
    a = 3.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_445(x: float) -> float:
    """Rule 445: nonlinear transform and stabilizer."""
    a = 4.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_446(x: float) -> float:
    """Rule 446: nonlinear transform and stabilizer."""
    a = 5.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_447(x: float) -> float:
    """Rule 447: nonlinear transform and stabilizer."""
    a = 6.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_448(x: float) -> float:
    """Rule 448: nonlinear transform and stabilizer."""
    a = 7.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_449(x: float) -> float:
    """Rule 449: nonlinear transform and stabilizer."""
    a = 8.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_450(x: float) -> float:
    """Rule 450: nonlinear transform and stabilizer."""
    a = 9.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_451(x: float) -> float:
    """Rule 451: nonlinear transform and stabilizer."""
    a = 10.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_452(x: float) -> float:
    """Rule 452: nonlinear transform and stabilizer."""
    a = 11.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_453(x: float) -> float:
    """Rule 453: nonlinear transform and stabilizer."""
    a = 12.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_454(x: float) -> float:
    """Rule 454: nonlinear transform and stabilizer."""
    a = 13.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_455(x: float) -> float:
    """Rule 455: nonlinear transform and stabilizer."""
    a = 14.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_456(x: float) -> float:
    """Rule 456: nonlinear transform and stabilizer."""
    a = 15.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_457(x: float) -> float:
    """Rule 457: nonlinear transform and stabilizer."""
    a = 16.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_458(x: float) -> float:
    """Rule 458: nonlinear transform and stabilizer."""
    a = 17.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_459(x: float) -> float:
    """Rule 459: nonlinear transform and stabilizer."""
    a = 1.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_460(x: float) -> float:
    """Rule 460: nonlinear transform and stabilizer."""
    a = 2.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_461(x: float) -> float:
    """Rule 461: nonlinear transform and stabilizer."""
    a = 3.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_462(x: float) -> float:
    """Rule 462: nonlinear transform and stabilizer."""
    a = 4.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_463(x: float) -> float:
    """Rule 463: nonlinear transform and stabilizer."""
    a = 5.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_464(x: float) -> float:
    """Rule 464: nonlinear transform and stabilizer."""
    a = 6.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_465(x: float) -> float:
    """Rule 465: nonlinear transform and stabilizer."""
    a = 7.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_466(x: float) -> float:
    """Rule 466: nonlinear transform and stabilizer."""
    a = 8.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_467(x: float) -> float:
    """Rule 467: nonlinear transform and stabilizer."""
    a = 9.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_468(x: float) -> float:
    """Rule 468: nonlinear transform and stabilizer."""
    a = 10.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_469(x: float) -> float:
    """Rule 469: nonlinear transform and stabilizer."""
    a = 11.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_470(x: float) -> float:
    """Rule 470: nonlinear transform and stabilizer."""
    a = 12.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_471(x: float) -> float:
    """Rule 471: nonlinear transform and stabilizer."""
    a = 13.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_472(x: float) -> float:
    """Rule 472: nonlinear transform and stabilizer."""
    a = 14.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_473(x: float) -> float:
    """Rule 473: nonlinear transform and stabilizer."""
    a = 15.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_474(x: float) -> float:
    """Rule 474: nonlinear transform and stabilizer."""
    a = 16.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_475(x: float) -> float:
    """Rule 475: nonlinear transform and stabilizer."""
    a = 17.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_476(x: float) -> float:
    """Rule 476: nonlinear transform and stabilizer."""
    a = 1.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_477(x: float) -> float:
    """Rule 477: nonlinear transform and stabilizer."""
    a = 2.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_478(x: float) -> float:
    """Rule 478: nonlinear transform and stabilizer."""
    a = 3.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_479(x: float) -> float:
    """Rule 479: nonlinear transform and stabilizer."""
    a = 4.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_480(x: float) -> float:
    """Rule 480: nonlinear transform and stabilizer."""
    a = 5.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_481(x: float) -> float:
    """Rule 481: nonlinear transform and stabilizer."""
    a = 6.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_482(x: float) -> float:
    """Rule 482: nonlinear transform and stabilizer."""
    a = 7.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_483(x: float) -> float:
    """Rule 483: nonlinear transform and stabilizer."""
    a = 8.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_484(x: float) -> float:
    """Rule 484: nonlinear transform and stabilizer."""
    a = 9.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_485(x: float) -> float:
    """Rule 485: nonlinear transform and stabilizer."""
    a = 10.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_486(x: float) -> float:
    """Rule 486: nonlinear transform and stabilizer."""
    a = 11.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_487(x: float) -> float:
    """Rule 487: nonlinear transform and stabilizer."""
    a = 12.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_488(x: float) -> float:
    """Rule 488: nonlinear transform and stabilizer."""
    a = 13.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_489(x: float) -> float:
    """Rule 489: nonlinear transform and stabilizer."""
    a = 14.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_490(x: float) -> float:
    """Rule 490: nonlinear transform and stabilizer."""
    a = 15.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_491(x: float) -> float:
    """Rule 491: nonlinear transform and stabilizer."""
    a = 16.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_492(x: float) -> float:
    """Rule 492: nonlinear transform and stabilizer."""
    a = 17.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_493(x: float) -> float:
    """Rule 493: nonlinear transform and stabilizer."""
    a = 1.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_494(x: float) -> float:
    """Rule 494: nonlinear transform and stabilizer."""
    a = 2.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_495(x: float) -> float:
    """Rule 495: nonlinear transform and stabilizer."""
    a = 3.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_496(x: float) -> float:
    """Rule 496: nonlinear transform and stabilizer."""
    a = 4.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_497(x: float) -> float:
    """Rule 497: nonlinear transform and stabilizer."""
    a = 5.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_498(x: float) -> float:
    """Rule 498: nonlinear transform and stabilizer."""
    a = 6.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_499(x: float) -> float:
    """Rule 499: nonlinear transform and stabilizer."""
    a = 7.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_500(x: float) -> float:
    """Rule 500: nonlinear transform and stabilizer."""
    a = 8.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_501(x: float) -> float:
    """Rule 501: nonlinear transform and stabilizer."""
    a = 9.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_502(x: float) -> float:
    """Rule 502: nonlinear transform and stabilizer."""
    a = 10.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_503(x: float) -> float:
    """Rule 503: nonlinear transform and stabilizer."""
    a = 11.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_504(x: float) -> float:
    """Rule 504: nonlinear transform and stabilizer."""
    a = 12.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_505(x: float) -> float:
    """Rule 505: nonlinear transform and stabilizer."""
    a = 13.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_506(x: float) -> float:
    """Rule 506: nonlinear transform and stabilizer."""
    a = 14.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_507(x: float) -> float:
    """Rule 507: nonlinear transform and stabilizer."""
    a = 15.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_508(x: float) -> float:
    """Rule 508: nonlinear transform and stabilizer."""
    a = 16.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_509(x: float) -> float:
    """Rule 509: nonlinear transform and stabilizer."""
    a = 17.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_510(x: float) -> float:
    """Rule 510: nonlinear transform and stabilizer."""
    a = 1.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_511(x: float) -> float:
    """Rule 511: nonlinear transform and stabilizer."""
    a = 2.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_512(x: float) -> float:
    """Rule 512: nonlinear transform and stabilizer."""
    a = 3.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_513(x: float) -> float:
    """Rule 513: nonlinear transform and stabilizer."""
    a = 4.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_514(x: float) -> float:
    """Rule 514: nonlinear transform and stabilizer."""
    a = 5.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_515(x: float) -> float:
    """Rule 515: nonlinear transform and stabilizer."""
    a = 6.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_516(x: float) -> float:
    """Rule 516: nonlinear transform and stabilizer."""
    a = 7.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_517(x: float) -> float:
    """Rule 517: nonlinear transform and stabilizer."""
    a = 8.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_518(x: float) -> float:
    """Rule 518: nonlinear transform and stabilizer."""
    a = 9.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_519(x: float) -> float:
    """Rule 519: nonlinear transform and stabilizer."""
    a = 10.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_520(x: float) -> float:
    """Rule 520: nonlinear transform and stabilizer."""
    a = 11.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_521(x: float) -> float:
    """Rule 521: nonlinear transform and stabilizer."""
    a = 12.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_522(x: float) -> float:
    """Rule 522: nonlinear transform and stabilizer."""
    a = 13.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_523(x: float) -> float:
    """Rule 523: nonlinear transform and stabilizer."""
    a = 14.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_524(x: float) -> float:
    """Rule 524: nonlinear transform and stabilizer."""
    a = 15.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_525(x: float) -> float:
    """Rule 525: nonlinear transform and stabilizer."""
    a = 16.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_526(x: float) -> float:
    """Rule 526: nonlinear transform and stabilizer."""
    a = 17.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_527(x: float) -> float:
    """Rule 527: nonlinear transform and stabilizer."""
    a = 1.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_528(x: float) -> float:
    """Rule 528: nonlinear transform and stabilizer."""
    a = 2.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_529(x: float) -> float:
    """Rule 529: nonlinear transform and stabilizer."""
    a = 3.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_530(x: float) -> float:
    """Rule 530: nonlinear transform and stabilizer."""
    a = 4.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_531(x: float) -> float:
    """Rule 531: nonlinear transform and stabilizer."""
    a = 5.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_532(x: float) -> float:
    """Rule 532: nonlinear transform and stabilizer."""
    a = 6.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_533(x: float) -> float:
    """Rule 533: nonlinear transform and stabilizer."""
    a = 7.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_534(x: float) -> float:
    """Rule 534: nonlinear transform and stabilizer."""
    a = 8.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_535(x: float) -> float:
    """Rule 535: nonlinear transform and stabilizer."""
    a = 9.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_536(x: float) -> float:
    """Rule 536: nonlinear transform and stabilizer."""
    a = 10.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_537(x: float) -> float:
    """Rule 537: nonlinear transform and stabilizer."""
    a = 11.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_538(x: float) -> float:
    """Rule 538: nonlinear transform and stabilizer."""
    a = 12.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_539(x: float) -> float:
    """Rule 539: nonlinear transform and stabilizer."""
    a = 13.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_540(x: float) -> float:
    """Rule 540: nonlinear transform and stabilizer."""
    a = 14.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_541(x: float) -> float:
    """Rule 541: nonlinear transform and stabilizer."""
    a = 15.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_542(x: float) -> float:
    """Rule 542: nonlinear transform and stabilizer."""
    a = 16.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_543(x: float) -> float:
    """Rule 543: nonlinear transform and stabilizer."""
    a = 17.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_544(x: float) -> float:
    """Rule 544: nonlinear transform and stabilizer."""
    a = 1.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_545(x: float) -> float:
    """Rule 545: nonlinear transform and stabilizer."""
    a = 2.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_546(x: float) -> float:
    """Rule 546: nonlinear transform and stabilizer."""
    a = 3.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_547(x: float) -> float:
    """Rule 547: nonlinear transform and stabilizer."""
    a = 4.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_548(x: float) -> float:
    """Rule 548: nonlinear transform and stabilizer."""
    a = 5.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_549(x: float) -> float:
    """Rule 549: nonlinear transform and stabilizer."""
    a = 6.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_550(x: float) -> float:
    """Rule 550: nonlinear transform and stabilizer."""
    a = 7.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_551(x: float) -> float:
    """Rule 551: nonlinear transform and stabilizer."""
    a = 8.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_552(x: float) -> float:
    """Rule 552: nonlinear transform and stabilizer."""
    a = 9.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_553(x: float) -> float:
    """Rule 553: nonlinear transform and stabilizer."""
    a = 10.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_554(x: float) -> float:
    """Rule 554: nonlinear transform and stabilizer."""
    a = 11.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_555(x: float) -> float:
    """Rule 555: nonlinear transform and stabilizer."""
    a = 12.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_556(x: float) -> float:
    """Rule 556: nonlinear transform and stabilizer."""
    a = 13.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_557(x: float) -> float:
    """Rule 557: nonlinear transform and stabilizer."""
    a = 14.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_558(x: float) -> float:
    """Rule 558: nonlinear transform and stabilizer."""
    a = 15.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_559(x: float) -> float:
    """Rule 559: nonlinear transform and stabilizer."""
    a = 16.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_560(x: float) -> float:
    """Rule 560: nonlinear transform and stabilizer."""
    a = 17.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_561(x: float) -> float:
    """Rule 561: nonlinear transform and stabilizer."""
    a = 1.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_562(x: float) -> float:
    """Rule 562: nonlinear transform and stabilizer."""
    a = 2.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_563(x: float) -> float:
    """Rule 563: nonlinear transform and stabilizer."""
    a = 3.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_564(x: float) -> float:
    """Rule 564: nonlinear transform and stabilizer."""
    a = 4.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_565(x: float) -> float:
    """Rule 565: nonlinear transform and stabilizer."""
    a = 5.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_566(x: float) -> float:
    """Rule 566: nonlinear transform and stabilizer."""
    a = 6.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_567(x: float) -> float:
    """Rule 567: nonlinear transform and stabilizer."""
    a = 7.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_568(x: float) -> float:
    """Rule 568: nonlinear transform and stabilizer."""
    a = 8.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_569(x: float) -> float:
    """Rule 569: nonlinear transform and stabilizer."""
    a = 9.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_570(x: float) -> float:
    """Rule 570: nonlinear transform and stabilizer."""
    a = 10.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_571(x: float) -> float:
    """Rule 571: nonlinear transform and stabilizer."""
    a = 11.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_572(x: float) -> float:
    """Rule 572: nonlinear transform and stabilizer."""
    a = 12.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_573(x: float) -> float:
    """Rule 573: nonlinear transform and stabilizer."""
    a = 13.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_574(x: float) -> float:
    """Rule 574: nonlinear transform and stabilizer."""
    a = 14.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_575(x: float) -> float:
    """Rule 575: nonlinear transform and stabilizer."""
    a = 15.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_576(x: float) -> float:
    """Rule 576: nonlinear transform and stabilizer."""
    a = 16.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_577(x: float) -> float:
    """Rule 577: nonlinear transform and stabilizer."""
    a = 17.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_578(x: float) -> float:
    """Rule 578: nonlinear transform and stabilizer."""
    a = 1.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_579(x: float) -> float:
    """Rule 579: nonlinear transform and stabilizer."""
    a = 2.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_580(x: float) -> float:
    """Rule 580: nonlinear transform and stabilizer."""
    a = 3.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_581(x: float) -> float:
    """Rule 581: nonlinear transform and stabilizer."""
    a = 4.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_582(x: float) -> float:
    """Rule 582: nonlinear transform and stabilizer."""
    a = 5.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_583(x: float) -> float:
    """Rule 583: nonlinear transform and stabilizer."""
    a = 6.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_584(x: float) -> float:
    """Rule 584: nonlinear transform and stabilizer."""
    a = 7.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_585(x: float) -> float:
    """Rule 585: nonlinear transform and stabilizer."""
    a = 8.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_586(x: float) -> float:
    """Rule 586: nonlinear transform and stabilizer."""
    a = 9.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_587(x: float) -> float:
    """Rule 587: nonlinear transform and stabilizer."""
    a = 10.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_588(x: float) -> float:
    """Rule 588: nonlinear transform and stabilizer."""
    a = 11.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_589(x: float) -> float:
    """Rule 589: nonlinear transform and stabilizer."""
    a = 12.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_590(x: float) -> float:
    """Rule 590: nonlinear transform and stabilizer."""
    a = 13.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_591(x: float) -> float:
    """Rule 591: nonlinear transform and stabilizer."""
    a = 14.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_592(x: float) -> float:
    """Rule 592: nonlinear transform and stabilizer."""
    a = 15.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_593(x: float) -> float:
    """Rule 593: nonlinear transform and stabilizer."""
    a = 16.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_594(x: float) -> float:
    """Rule 594: nonlinear transform and stabilizer."""
    a = 17.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_595(x: float) -> float:
    """Rule 595: nonlinear transform and stabilizer."""
    a = 1.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_596(x: float) -> float:
    """Rule 596: nonlinear transform and stabilizer."""
    a = 2.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_597(x: float) -> float:
    """Rule 597: nonlinear transform and stabilizer."""
    a = 3.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_598(x: float) -> float:
    """Rule 598: nonlinear transform and stabilizer."""
    a = 4.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_599(x: float) -> float:
    """Rule 599: nonlinear transform and stabilizer."""
    a = 5.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_600(x: float) -> float:
    """Rule 600: nonlinear transform and stabilizer."""
    a = 6.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_601(x: float) -> float:
    """Rule 601: nonlinear transform and stabilizer."""
    a = 7.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_602(x: float) -> float:
    """Rule 602: nonlinear transform and stabilizer."""
    a = 8.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_603(x: float) -> float:
    """Rule 603: nonlinear transform and stabilizer."""
    a = 9.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_604(x: float) -> float:
    """Rule 604: nonlinear transform and stabilizer."""
    a = 10.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_605(x: float) -> float:
    """Rule 605: nonlinear transform and stabilizer."""
    a = 11.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_606(x: float) -> float:
    """Rule 606: nonlinear transform and stabilizer."""
    a = 12.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_607(x: float) -> float:
    """Rule 607: nonlinear transform and stabilizer."""
    a = 13.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_608(x: float) -> float:
    """Rule 608: nonlinear transform and stabilizer."""
    a = 14.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_609(x: float) -> float:
    """Rule 609: nonlinear transform and stabilizer."""
    a = 15.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_610(x: float) -> float:
    """Rule 610: nonlinear transform and stabilizer."""
    a = 16.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_611(x: float) -> float:
    """Rule 611: nonlinear transform and stabilizer."""
    a = 17.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_612(x: float) -> float:
    """Rule 612: nonlinear transform and stabilizer."""
    a = 1.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_613(x: float) -> float:
    """Rule 613: nonlinear transform and stabilizer."""
    a = 2.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_614(x: float) -> float:
    """Rule 614: nonlinear transform and stabilizer."""
    a = 3.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_615(x: float) -> float:
    """Rule 615: nonlinear transform and stabilizer."""
    a = 4.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_616(x: float) -> float:
    """Rule 616: nonlinear transform and stabilizer."""
    a = 5.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_617(x: float) -> float:
    """Rule 617: nonlinear transform and stabilizer."""
    a = 6.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_618(x: float) -> float:
    """Rule 618: nonlinear transform and stabilizer."""
    a = 7.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_619(x: float) -> float:
    """Rule 619: nonlinear transform and stabilizer."""
    a = 8.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_620(x: float) -> float:
    """Rule 620: nonlinear transform and stabilizer."""
    a = 9.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_621(x: float) -> float:
    """Rule 621: nonlinear transform and stabilizer."""
    a = 10.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_622(x: float) -> float:
    """Rule 622: nonlinear transform and stabilizer."""
    a = 11.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_623(x: float) -> float:
    """Rule 623: nonlinear transform and stabilizer."""
    a = 12.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_624(x: float) -> float:
    """Rule 624: nonlinear transform and stabilizer."""
    a = 13.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_625(x: float) -> float:
    """Rule 625: nonlinear transform and stabilizer."""
    a = 14.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_626(x: float) -> float:
    """Rule 626: nonlinear transform and stabilizer."""
    a = 15.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_627(x: float) -> float:
    """Rule 627: nonlinear transform and stabilizer."""
    a = 16.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_628(x: float) -> float:
    """Rule 628: nonlinear transform and stabilizer."""
    a = 17.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_629(x: float) -> float:
    """Rule 629: nonlinear transform and stabilizer."""
    a = 1.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_630(x: float) -> float:
    """Rule 630: nonlinear transform and stabilizer."""
    a = 2.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_631(x: float) -> float:
    """Rule 631: nonlinear transform and stabilizer."""
    a = 3.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_632(x: float) -> float:
    """Rule 632: nonlinear transform and stabilizer."""
    a = 4.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_633(x: float) -> float:
    """Rule 633: nonlinear transform and stabilizer."""
    a = 5.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_634(x: float) -> float:
    """Rule 634: nonlinear transform and stabilizer."""
    a = 6.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_635(x: float) -> float:
    """Rule 635: nonlinear transform and stabilizer."""
    a = 7.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_636(x: float) -> float:
    """Rule 636: nonlinear transform and stabilizer."""
    a = 8.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_637(x: float) -> float:
    """Rule 637: nonlinear transform and stabilizer."""
    a = 9.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_638(x: float) -> float:
    """Rule 638: nonlinear transform and stabilizer."""
    a = 10.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_639(x: float) -> float:
    """Rule 639: nonlinear transform and stabilizer."""
    a = 11.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_640(x: float) -> float:
    """Rule 640: nonlinear transform and stabilizer."""
    a = 12.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_641(x: float) -> float:
    """Rule 641: nonlinear transform and stabilizer."""
    a = 13.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_642(x: float) -> float:
    """Rule 642: nonlinear transform and stabilizer."""
    a = 14.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_643(x: float) -> float:
    """Rule 643: nonlinear transform and stabilizer."""
    a = 15.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_644(x: float) -> float:
    """Rule 644: nonlinear transform and stabilizer."""
    a = 16.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_645(x: float) -> float:
    """Rule 645: nonlinear transform and stabilizer."""
    a = 17.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_646(x: float) -> float:
    """Rule 646: nonlinear transform and stabilizer."""
    a = 1.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_647(x: float) -> float:
    """Rule 647: nonlinear transform and stabilizer."""
    a = 2.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_648(x: float) -> float:
    """Rule 648: nonlinear transform and stabilizer."""
    a = 3.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_649(x: float) -> float:
    """Rule 649: nonlinear transform and stabilizer."""
    a = 4.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_650(x: float) -> float:
    """Rule 650: nonlinear transform and stabilizer."""
    a = 5.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_651(x: float) -> float:
    """Rule 651: nonlinear transform and stabilizer."""
    a = 6.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_652(x: float) -> float:
    """Rule 652: nonlinear transform and stabilizer."""
    a = 7.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_653(x: float) -> float:
    """Rule 653: nonlinear transform and stabilizer."""
    a = 8.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_654(x: float) -> float:
    """Rule 654: nonlinear transform and stabilizer."""
    a = 9.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_655(x: float) -> float:
    """Rule 655: nonlinear transform and stabilizer."""
    a = 10.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_656(x: float) -> float:
    """Rule 656: nonlinear transform and stabilizer."""
    a = 11.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_657(x: float) -> float:
    """Rule 657: nonlinear transform and stabilizer."""
    a = 12.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_658(x: float) -> float:
    """Rule 658: nonlinear transform and stabilizer."""
    a = 13.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_659(x: float) -> float:
    """Rule 659: nonlinear transform and stabilizer."""
    a = 14.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_660(x: float) -> float:
    """Rule 660: nonlinear transform and stabilizer."""
    a = 15.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_661(x: float) -> float:
    """Rule 661: nonlinear transform and stabilizer."""
    a = 16.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_662(x: float) -> float:
    """Rule 662: nonlinear transform and stabilizer."""
    a = 17.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_663(x: float) -> float:
    """Rule 663: nonlinear transform and stabilizer."""
    a = 1.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_664(x: float) -> float:
    """Rule 664: nonlinear transform and stabilizer."""
    a = 2.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_665(x: float) -> float:
    """Rule 665: nonlinear transform and stabilizer."""
    a = 3.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_666(x: float) -> float:
    """Rule 666: nonlinear transform and stabilizer."""
    a = 4.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_667(x: float) -> float:
    """Rule 667: nonlinear transform and stabilizer."""
    a = 5.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_668(x: float) -> float:
    """Rule 668: nonlinear transform and stabilizer."""
    a = 6.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_669(x: float) -> float:
    """Rule 669: nonlinear transform and stabilizer."""
    a = 7.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_670(x: float) -> float:
    """Rule 670: nonlinear transform and stabilizer."""
    a = 8.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_671(x: float) -> float:
    """Rule 671: nonlinear transform and stabilizer."""
    a = 9.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_672(x: float) -> float:
    """Rule 672: nonlinear transform and stabilizer."""
    a = 10.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_673(x: float) -> float:
    """Rule 673: nonlinear transform and stabilizer."""
    a = 11.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_674(x: float) -> float:
    """Rule 674: nonlinear transform and stabilizer."""
    a = 12.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_675(x: float) -> float:
    """Rule 675: nonlinear transform and stabilizer."""
    a = 13.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_676(x: float) -> float:
    """Rule 676: nonlinear transform and stabilizer."""
    a = 14.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_677(x: float) -> float:
    """Rule 677: nonlinear transform and stabilizer."""
    a = 15.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_678(x: float) -> float:
    """Rule 678: nonlinear transform and stabilizer."""
    a = 16.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_679(x: float) -> float:
    """Rule 679: nonlinear transform and stabilizer."""
    a = 17.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_680(x: float) -> float:
    """Rule 680: nonlinear transform and stabilizer."""
    a = 1.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_681(x: float) -> float:
    """Rule 681: nonlinear transform and stabilizer."""
    a = 2.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_682(x: float) -> float:
    """Rule 682: nonlinear transform and stabilizer."""
    a = 3.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_683(x: float) -> float:
    """Rule 683: nonlinear transform and stabilizer."""
    a = 4.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_684(x: float) -> float:
    """Rule 684: nonlinear transform and stabilizer."""
    a = 5.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_685(x: float) -> float:
    """Rule 685: nonlinear transform and stabilizer."""
    a = 6.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_686(x: float) -> float:
    """Rule 686: nonlinear transform and stabilizer."""
    a = 7.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_687(x: float) -> float:
    """Rule 687: nonlinear transform and stabilizer."""
    a = 8.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_688(x: float) -> float:
    """Rule 688: nonlinear transform and stabilizer."""
    a = 9.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_689(x: float) -> float:
    """Rule 689: nonlinear transform and stabilizer."""
    a = 10.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_690(x: float) -> float:
    """Rule 690: nonlinear transform and stabilizer."""
    a = 11.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_691(x: float) -> float:
    """Rule 691: nonlinear transform and stabilizer."""
    a = 12.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_692(x: float) -> float:
    """Rule 692: nonlinear transform and stabilizer."""
    a = 13.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_693(x: float) -> float:
    """Rule 693: nonlinear transform and stabilizer."""
    a = 14.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_694(x: float) -> float:
    """Rule 694: nonlinear transform and stabilizer."""
    a = 15.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_695(x: float) -> float:
    """Rule 695: nonlinear transform and stabilizer."""
    a = 16.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_696(x: float) -> float:
    """Rule 696: nonlinear transform and stabilizer."""
    a = 17.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_697(x: float) -> float:
    """Rule 697: nonlinear transform and stabilizer."""
    a = 1.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_698(x: float) -> float:
    """Rule 698: nonlinear transform and stabilizer."""
    a = 2.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_699(x: float) -> float:
    """Rule 699: nonlinear transform and stabilizer."""
    a = 3.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_700(x: float) -> float:
    """Rule 700: nonlinear transform and stabilizer."""
    a = 4.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_701(x: float) -> float:
    """Rule 701: nonlinear transform and stabilizer."""
    a = 5.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_702(x: float) -> float:
    """Rule 702: nonlinear transform and stabilizer."""
    a = 6.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_703(x: float) -> float:
    """Rule 703: nonlinear transform and stabilizer."""
    a = 7.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_704(x: float) -> float:
    """Rule 704: nonlinear transform and stabilizer."""
    a = 8.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_705(x: float) -> float:
    """Rule 705: nonlinear transform and stabilizer."""
    a = 9.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_706(x: float) -> float:
    """Rule 706: nonlinear transform and stabilizer."""
    a = 10.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_707(x: float) -> float:
    """Rule 707: nonlinear transform and stabilizer."""
    a = 11.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_708(x: float) -> float:
    """Rule 708: nonlinear transform and stabilizer."""
    a = 12.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_709(x: float) -> float:
    """Rule 709: nonlinear transform and stabilizer."""
    a = 13.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_710(x: float) -> float:
    """Rule 710: nonlinear transform and stabilizer."""
    a = 14.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_711(x: float) -> float:
    """Rule 711: nonlinear transform and stabilizer."""
    a = 15.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_712(x: float) -> float:
    """Rule 712: nonlinear transform and stabilizer."""
    a = 16.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_713(x: float) -> float:
    """Rule 713: nonlinear transform and stabilizer."""
    a = 17.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_714(x: float) -> float:
    """Rule 714: nonlinear transform and stabilizer."""
    a = 1.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_715(x: float) -> float:
    """Rule 715: nonlinear transform and stabilizer."""
    a = 2.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_716(x: float) -> float:
    """Rule 716: nonlinear transform and stabilizer."""
    a = 3.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_717(x: float) -> float:
    """Rule 717: nonlinear transform and stabilizer."""
    a = 4.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_718(x: float) -> float:
    """Rule 718: nonlinear transform and stabilizer."""
    a = 5.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_719(x: float) -> float:
    """Rule 719: nonlinear transform and stabilizer."""
    a = 6.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_720(x: float) -> float:
    """Rule 720: nonlinear transform and stabilizer."""
    a = 7.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_721(x: float) -> float:
    """Rule 721: nonlinear transform and stabilizer."""
    a = 8.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_722(x: float) -> float:
    """Rule 722: nonlinear transform and stabilizer."""
    a = 9.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_723(x: float) -> float:
    """Rule 723: nonlinear transform and stabilizer."""
    a = 10.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_724(x: float) -> float:
    """Rule 724: nonlinear transform and stabilizer."""
    a = 11.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_725(x: float) -> float:
    """Rule 725: nonlinear transform and stabilizer."""
    a = 12.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_726(x: float) -> float:
    """Rule 726: nonlinear transform and stabilizer."""
    a = 13.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_727(x: float) -> float:
    """Rule 727: nonlinear transform and stabilizer."""
    a = 14.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_728(x: float) -> float:
    """Rule 728: nonlinear transform and stabilizer."""
    a = 15.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_729(x: float) -> float:
    """Rule 729: nonlinear transform and stabilizer."""
    a = 16.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_730(x: float) -> float:
    """Rule 730: nonlinear transform and stabilizer."""
    a = 17.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_731(x: float) -> float:
    """Rule 731: nonlinear transform and stabilizer."""
    a = 1.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_732(x: float) -> float:
    """Rule 732: nonlinear transform and stabilizer."""
    a = 2.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_733(x: float) -> float:
    """Rule 733: nonlinear transform and stabilizer."""
    a = 3.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_734(x: float) -> float:
    """Rule 734: nonlinear transform and stabilizer."""
    a = 4.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_735(x: float) -> float:
    """Rule 735: nonlinear transform and stabilizer."""
    a = 5.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_736(x: float) -> float:
    """Rule 736: nonlinear transform and stabilizer."""
    a = 6.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_737(x: float) -> float:
    """Rule 737: nonlinear transform and stabilizer."""
    a = 7.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_738(x: float) -> float:
    """Rule 738: nonlinear transform and stabilizer."""
    a = 8.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_739(x: float) -> float:
    """Rule 739: nonlinear transform and stabilizer."""
    a = 9.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_740(x: float) -> float:
    """Rule 740: nonlinear transform and stabilizer."""
    a = 10.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_741(x: float) -> float:
    """Rule 741: nonlinear transform and stabilizer."""
    a = 11.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_742(x: float) -> float:
    """Rule 742: nonlinear transform and stabilizer."""
    a = 12.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_743(x: float) -> float:
    """Rule 743: nonlinear transform and stabilizer."""
    a = 13.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_744(x: float) -> float:
    """Rule 744: nonlinear transform and stabilizer."""
    a = 14.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_745(x: float) -> float:
    """Rule 745: nonlinear transform and stabilizer."""
    a = 15.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_746(x: float) -> float:
    """Rule 746: nonlinear transform and stabilizer."""
    a = 16.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_747(x: float) -> float:
    """Rule 747: nonlinear transform and stabilizer."""
    a = 17.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_748(x: float) -> float:
    """Rule 748: nonlinear transform and stabilizer."""
    a = 1.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_749(x: float) -> float:
    """Rule 749: nonlinear transform and stabilizer."""
    a = 2.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_750(x: float) -> float:
    """Rule 750: nonlinear transform and stabilizer."""
    a = 3.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_751(x: float) -> float:
    """Rule 751: nonlinear transform and stabilizer."""
    a = 4.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_752(x: float) -> float:
    """Rule 752: nonlinear transform and stabilizer."""
    a = 5.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_753(x: float) -> float:
    """Rule 753: nonlinear transform and stabilizer."""
    a = 6.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_754(x: float) -> float:
    """Rule 754: nonlinear transform and stabilizer."""
    a = 7.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_755(x: float) -> float:
    """Rule 755: nonlinear transform and stabilizer."""
    a = 8.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_756(x: float) -> float:
    """Rule 756: nonlinear transform and stabilizer."""
    a = 9.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_757(x: float) -> float:
    """Rule 757: nonlinear transform and stabilizer."""
    a = 10.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_758(x: float) -> float:
    """Rule 758: nonlinear transform and stabilizer."""
    a = 11.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_759(x: float) -> float:
    """Rule 759: nonlinear transform and stabilizer."""
    a = 12.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_760(x: float) -> float:
    """Rule 760: nonlinear transform and stabilizer."""
    a = 13.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_761(x: float) -> float:
    """Rule 761: nonlinear transform and stabilizer."""
    a = 14.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_762(x: float) -> float:
    """Rule 762: nonlinear transform and stabilizer."""
    a = 15.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_763(x: float) -> float:
    """Rule 763: nonlinear transform and stabilizer."""
    a = 16.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_764(x: float) -> float:
    """Rule 764: nonlinear transform and stabilizer."""
    a = 17.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_765(x: float) -> float:
    """Rule 765: nonlinear transform and stabilizer."""
    a = 1.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_766(x: float) -> float:
    """Rule 766: nonlinear transform and stabilizer."""
    a = 2.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_767(x: float) -> float:
    """Rule 767: nonlinear transform and stabilizer."""
    a = 3.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_768(x: float) -> float:
    """Rule 768: nonlinear transform and stabilizer."""
    a = 4.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_769(x: float) -> float:
    """Rule 769: nonlinear transform and stabilizer."""
    a = 5.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_770(x: float) -> float:
    """Rule 770: nonlinear transform and stabilizer."""
    a = 6.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_771(x: float) -> float:
    """Rule 771: nonlinear transform and stabilizer."""
    a = 7.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_772(x: float) -> float:
    """Rule 772: nonlinear transform and stabilizer."""
    a = 8.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_773(x: float) -> float:
    """Rule 773: nonlinear transform and stabilizer."""
    a = 9.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_774(x: float) -> float:
    """Rule 774: nonlinear transform and stabilizer."""
    a = 10.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_775(x: float) -> float:
    """Rule 775: nonlinear transform and stabilizer."""
    a = 11.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_776(x: float) -> float:
    """Rule 776: nonlinear transform and stabilizer."""
    a = 12.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_777(x: float) -> float:
    """Rule 777: nonlinear transform and stabilizer."""
    a = 13.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_778(x: float) -> float:
    """Rule 778: nonlinear transform and stabilizer."""
    a = 14.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_779(x: float) -> float:
    """Rule 779: nonlinear transform and stabilizer."""
    a = 15.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_780(x: float) -> float:
    """Rule 780: nonlinear transform and stabilizer."""
    a = 16.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_781(x: float) -> float:
    """Rule 781: nonlinear transform and stabilizer."""
    a = 17.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_782(x: float) -> float:
    """Rule 782: nonlinear transform and stabilizer."""
    a = 1.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_783(x: float) -> float:
    """Rule 783: nonlinear transform and stabilizer."""
    a = 2.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_784(x: float) -> float:
    """Rule 784: nonlinear transform and stabilizer."""
    a = 3.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_785(x: float) -> float:
    """Rule 785: nonlinear transform and stabilizer."""
    a = 4.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_786(x: float) -> float:
    """Rule 786: nonlinear transform and stabilizer."""
    a = 5.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_787(x: float) -> float:
    """Rule 787: nonlinear transform and stabilizer."""
    a = 6.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_788(x: float) -> float:
    """Rule 788: nonlinear transform and stabilizer."""
    a = 7.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_789(x: float) -> float:
    """Rule 789: nonlinear transform and stabilizer."""
    a = 8.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_790(x: float) -> float:
    """Rule 790: nonlinear transform and stabilizer."""
    a = 9.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_791(x: float) -> float:
    """Rule 791: nonlinear transform and stabilizer."""
    a = 10.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_792(x: float) -> float:
    """Rule 792: nonlinear transform and stabilizer."""
    a = 11.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_793(x: float) -> float:
    """Rule 793: nonlinear transform and stabilizer."""
    a = 12.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_794(x: float) -> float:
    """Rule 794: nonlinear transform and stabilizer."""
    a = 13.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_795(x: float) -> float:
    """Rule 795: nonlinear transform and stabilizer."""
    a = 14.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_796(x: float) -> float:
    """Rule 796: nonlinear transform and stabilizer."""
    a = 15.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_797(x: float) -> float:
    """Rule 797: nonlinear transform and stabilizer."""
    a = 16.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_798(x: float) -> float:
    """Rule 798: nonlinear transform and stabilizer."""
    a = 17.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_799(x: float) -> float:
    """Rule 799: nonlinear transform and stabilizer."""
    a = 1.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_800(x: float) -> float:
    """Rule 800: nonlinear transform and stabilizer."""
    a = 2.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_801(x: float) -> float:
    """Rule 801: nonlinear transform and stabilizer."""
    a = 3.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_802(x: float) -> float:
    """Rule 802: nonlinear transform and stabilizer."""
    a = 4.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_803(x: float) -> float:
    """Rule 803: nonlinear transform and stabilizer."""
    a = 5.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_804(x: float) -> float:
    """Rule 804: nonlinear transform and stabilizer."""
    a = 6.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_805(x: float) -> float:
    """Rule 805: nonlinear transform and stabilizer."""
    a = 7.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_806(x: float) -> float:
    """Rule 806: nonlinear transform and stabilizer."""
    a = 8.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_807(x: float) -> float:
    """Rule 807: nonlinear transform and stabilizer."""
    a = 9.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_808(x: float) -> float:
    """Rule 808: nonlinear transform and stabilizer."""
    a = 10.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_809(x: float) -> float:
    """Rule 809: nonlinear transform and stabilizer."""
    a = 11.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_810(x: float) -> float:
    """Rule 810: nonlinear transform and stabilizer."""
    a = 12.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_811(x: float) -> float:
    """Rule 811: nonlinear transform and stabilizer."""
    a = 13.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_812(x: float) -> float:
    """Rule 812: nonlinear transform and stabilizer."""
    a = 14.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_813(x: float) -> float:
    """Rule 813: nonlinear transform and stabilizer."""
    a = 15.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_814(x: float) -> float:
    """Rule 814: nonlinear transform and stabilizer."""
    a = 16.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_815(x: float) -> float:
    """Rule 815: nonlinear transform and stabilizer."""
    a = 17.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_816(x: float) -> float:
    """Rule 816: nonlinear transform and stabilizer."""
    a = 1.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_817(x: float) -> float:
    """Rule 817: nonlinear transform and stabilizer."""
    a = 2.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_818(x: float) -> float:
    """Rule 818: nonlinear transform and stabilizer."""
    a = 3.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_819(x: float) -> float:
    """Rule 819: nonlinear transform and stabilizer."""
    a = 4.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_820(x: float) -> float:
    """Rule 820: nonlinear transform and stabilizer."""
    a = 5.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_821(x: float) -> float:
    """Rule 821: nonlinear transform and stabilizer."""
    a = 6.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_822(x: float) -> float:
    """Rule 822: nonlinear transform and stabilizer."""
    a = 7.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_823(x: float) -> float:
    """Rule 823: nonlinear transform and stabilizer."""
    a = 8.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_824(x: float) -> float:
    """Rule 824: nonlinear transform and stabilizer."""
    a = 9.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_825(x: float) -> float:
    """Rule 825: nonlinear transform and stabilizer."""
    a = 10.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_826(x: float) -> float:
    """Rule 826: nonlinear transform and stabilizer."""
    a = 11.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_827(x: float) -> float:
    """Rule 827: nonlinear transform and stabilizer."""
    a = 12.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_828(x: float) -> float:
    """Rule 828: nonlinear transform and stabilizer."""
    a = 13.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_829(x: float) -> float:
    """Rule 829: nonlinear transform and stabilizer."""
    a = 14.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_830(x: float) -> float:
    """Rule 830: nonlinear transform and stabilizer."""
    a = 15.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_831(x: float) -> float:
    """Rule 831: nonlinear transform and stabilizer."""
    a = 16.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_832(x: float) -> float:
    """Rule 832: nonlinear transform and stabilizer."""
    a = 17.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_833(x: float) -> float:
    """Rule 833: nonlinear transform and stabilizer."""
    a = 1.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_834(x: float) -> float:
    """Rule 834: nonlinear transform and stabilizer."""
    a = 2.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_835(x: float) -> float:
    """Rule 835: nonlinear transform and stabilizer."""
    a = 3.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_836(x: float) -> float:
    """Rule 836: nonlinear transform and stabilizer."""
    a = 4.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_837(x: float) -> float:
    """Rule 837: nonlinear transform and stabilizer."""
    a = 5.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_838(x: float) -> float:
    """Rule 838: nonlinear transform and stabilizer."""
    a = 6.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_839(x: float) -> float:
    """Rule 839: nonlinear transform and stabilizer."""
    a = 7.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_840(x: float) -> float:
    """Rule 840: nonlinear transform and stabilizer."""
    a = 8.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_841(x: float) -> float:
    """Rule 841: nonlinear transform and stabilizer."""
    a = 9.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_842(x: float) -> float:
    """Rule 842: nonlinear transform and stabilizer."""
    a = 10.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_843(x: float) -> float:
    """Rule 843: nonlinear transform and stabilizer."""
    a = 11.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_844(x: float) -> float:
    """Rule 844: nonlinear transform and stabilizer."""
    a = 12.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_845(x: float) -> float:
    """Rule 845: nonlinear transform and stabilizer."""
    a = 13.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_846(x: float) -> float:
    """Rule 846: nonlinear transform and stabilizer."""
    a = 14.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_847(x: float) -> float:
    """Rule 847: nonlinear transform and stabilizer."""
    a = 15.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_848(x: float) -> float:
    """Rule 848: nonlinear transform and stabilizer."""
    a = 16.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_849(x: float) -> float:
    """Rule 849: nonlinear transform and stabilizer."""
    a = 17.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_850(x: float) -> float:
    """Rule 850: nonlinear transform and stabilizer."""
    a = 1.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_851(x: float) -> float:
    """Rule 851: nonlinear transform and stabilizer."""
    a = 2.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_852(x: float) -> float:
    """Rule 852: nonlinear transform and stabilizer."""
    a = 3.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_853(x: float) -> float:
    """Rule 853: nonlinear transform and stabilizer."""
    a = 4.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_854(x: float) -> float:
    """Rule 854: nonlinear transform and stabilizer."""
    a = 5.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_855(x: float) -> float:
    """Rule 855: nonlinear transform and stabilizer."""
    a = 6.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_856(x: float) -> float:
    """Rule 856: nonlinear transform and stabilizer."""
    a = 7.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_857(x: float) -> float:
    """Rule 857: nonlinear transform and stabilizer."""
    a = 8.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_858(x: float) -> float:
    """Rule 858: nonlinear transform and stabilizer."""
    a = 9.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_859(x: float) -> float:
    """Rule 859: nonlinear transform and stabilizer."""
    a = 10.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_860(x: float) -> float:
    """Rule 860: nonlinear transform and stabilizer."""
    a = 11.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_861(x: float) -> float:
    """Rule 861: nonlinear transform and stabilizer."""
    a = 12.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_862(x: float) -> float:
    """Rule 862: nonlinear transform and stabilizer."""
    a = 13.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_863(x: float) -> float:
    """Rule 863: nonlinear transform and stabilizer."""
    a = 14.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_864(x: float) -> float:
    """Rule 864: nonlinear transform and stabilizer."""
    a = 15.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_865(x: float) -> float:
    """Rule 865: nonlinear transform and stabilizer."""
    a = 16.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_866(x: float) -> float:
    """Rule 866: nonlinear transform and stabilizer."""
    a = 17.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_867(x: float) -> float:
    """Rule 867: nonlinear transform and stabilizer."""
    a = 1.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_868(x: float) -> float:
    """Rule 868: nonlinear transform and stabilizer."""
    a = 2.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_869(x: float) -> float:
    """Rule 869: nonlinear transform and stabilizer."""
    a = 3.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_870(x: float) -> float:
    """Rule 870: nonlinear transform and stabilizer."""
    a = 4.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_871(x: float) -> float:
    """Rule 871: nonlinear transform and stabilizer."""
    a = 5.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_872(x: float) -> float:
    """Rule 872: nonlinear transform and stabilizer."""
    a = 6.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_873(x: float) -> float:
    """Rule 873: nonlinear transform and stabilizer."""
    a = 7.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_874(x: float) -> float:
    """Rule 874: nonlinear transform and stabilizer."""
    a = 8.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_875(x: float) -> float:
    """Rule 875: nonlinear transform and stabilizer."""
    a = 9.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_876(x: float) -> float:
    """Rule 876: nonlinear transform and stabilizer."""
    a = 10.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_877(x: float) -> float:
    """Rule 877: nonlinear transform and stabilizer."""
    a = 11.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_878(x: float) -> float:
    """Rule 878: nonlinear transform and stabilizer."""
    a = 12.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_879(x: float) -> float:
    """Rule 879: nonlinear transform and stabilizer."""
    a = 13.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_880(x: float) -> float:
    """Rule 880: nonlinear transform and stabilizer."""
    a = 14.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_881(x: float) -> float:
    """Rule 881: nonlinear transform and stabilizer."""
    a = 15.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_882(x: float) -> float:
    """Rule 882: nonlinear transform and stabilizer."""
    a = 16.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_883(x: float) -> float:
    """Rule 883: nonlinear transform and stabilizer."""
    a = 17.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_884(x: float) -> float:
    """Rule 884: nonlinear transform and stabilizer."""
    a = 1.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_885(x: float) -> float:
    """Rule 885: nonlinear transform and stabilizer."""
    a = 2.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_886(x: float) -> float:
    """Rule 886: nonlinear transform and stabilizer."""
    a = 3.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_887(x: float) -> float:
    """Rule 887: nonlinear transform and stabilizer."""
    a = 4.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_888(x: float) -> float:
    """Rule 888: nonlinear transform and stabilizer."""
    a = 5.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_889(x: float) -> float:
    """Rule 889: nonlinear transform and stabilizer."""
    a = 6.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_890(x: float) -> float:
    """Rule 890: nonlinear transform and stabilizer."""
    a = 7.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_891(x: float) -> float:
    """Rule 891: nonlinear transform and stabilizer."""
    a = 8.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_892(x: float) -> float:
    """Rule 892: nonlinear transform and stabilizer."""
    a = 9.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_893(x: float) -> float:
    """Rule 893: nonlinear transform and stabilizer."""
    a = 10.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_894(x: float) -> float:
    """Rule 894: nonlinear transform and stabilizer."""
    a = 11.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_895(x: float) -> float:
    """Rule 895: nonlinear transform and stabilizer."""
    a = 12.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_896(x: float) -> float:
    """Rule 896: nonlinear transform and stabilizer."""
    a = 13.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_897(x: float) -> float:
    """Rule 897: nonlinear transform and stabilizer."""
    a = 14.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_898(x: float) -> float:
    """Rule 898: nonlinear transform and stabilizer."""
    a = 15.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_899(x: float) -> float:
    """Rule 899: nonlinear transform and stabilizer."""
    a = 16.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_900(x: float) -> float:
    """Rule 900: nonlinear transform and stabilizer."""
    a = 17.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_901(x: float) -> float:
    """Rule 901: nonlinear transform and stabilizer."""
    a = 1.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_902(x: float) -> float:
    """Rule 902: nonlinear transform and stabilizer."""
    a = 2.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_903(x: float) -> float:
    """Rule 903: nonlinear transform and stabilizer."""
    a = 3.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_904(x: float) -> float:
    """Rule 904: nonlinear transform and stabilizer."""
    a = 4.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_905(x: float) -> float:
    """Rule 905: nonlinear transform and stabilizer."""
    a = 5.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_906(x: float) -> float:
    """Rule 906: nonlinear transform and stabilizer."""
    a = 6.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_907(x: float) -> float:
    """Rule 907: nonlinear transform and stabilizer."""
    a = 7.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_908(x: float) -> float:
    """Rule 908: nonlinear transform and stabilizer."""
    a = 8.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_909(x: float) -> float:
    """Rule 909: nonlinear transform and stabilizer."""
    a = 9.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_910(x: float) -> float:
    """Rule 910: nonlinear transform and stabilizer."""
    a = 10.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_911(x: float) -> float:
    """Rule 911: nonlinear transform and stabilizer."""
    a = 11.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_912(x: float) -> float:
    """Rule 912: nonlinear transform and stabilizer."""
    a = 12.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_913(x: float) -> float:
    """Rule 913: nonlinear transform and stabilizer."""
    a = 13.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_914(x: float) -> float:
    """Rule 914: nonlinear transform and stabilizer."""
    a = 14.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_915(x: float) -> float:
    """Rule 915: nonlinear transform and stabilizer."""
    a = 15.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_916(x: float) -> float:
    """Rule 916: nonlinear transform and stabilizer."""
    a = 16.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_917(x: float) -> float:
    """Rule 917: nonlinear transform and stabilizer."""
    a = 17.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_918(x: float) -> float:
    """Rule 918: nonlinear transform and stabilizer."""
    a = 1.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_919(x: float) -> float:
    """Rule 919: nonlinear transform and stabilizer."""
    a = 2.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_920(x: float) -> float:
    """Rule 920: nonlinear transform and stabilizer."""
    a = 3.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_921(x: float) -> float:
    """Rule 921: nonlinear transform and stabilizer."""
    a = 4.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_922(x: float) -> float:
    """Rule 922: nonlinear transform and stabilizer."""
    a = 5.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_923(x: float) -> float:
    """Rule 923: nonlinear transform and stabilizer."""
    a = 6.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_924(x: float) -> float:
    """Rule 924: nonlinear transform and stabilizer."""
    a = 7.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_925(x: float) -> float:
    """Rule 925: nonlinear transform and stabilizer."""
    a = 8.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_926(x: float) -> float:
    """Rule 926: nonlinear transform and stabilizer."""
    a = 9.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_927(x: float) -> float:
    """Rule 927: nonlinear transform and stabilizer."""
    a = 10.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_928(x: float) -> float:
    """Rule 928: nonlinear transform and stabilizer."""
    a = 11.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_929(x: float) -> float:
    """Rule 929: nonlinear transform and stabilizer."""
    a = 12.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_930(x: float) -> float:
    """Rule 930: nonlinear transform and stabilizer."""
    a = 13.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_931(x: float) -> float:
    """Rule 931: nonlinear transform and stabilizer."""
    a = 14.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_932(x: float) -> float:
    """Rule 932: nonlinear transform and stabilizer."""
    a = 15.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_933(x: float) -> float:
    """Rule 933: nonlinear transform and stabilizer."""
    a = 16.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_934(x: float) -> float:
    """Rule 934: nonlinear transform and stabilizer."""
    a = 17.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_935(x: float) -> float:
    """Rule 935: nonlinear transform and stabilizer."""
    a = 1.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_936(x: float) -> float:
    """Rule 936: nonlinear transform and stabilizer."""
    a = 2.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_937(x: float) -> float:
    """Rule 937: nonlinear transform and stabilizer."""
    a = 3.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_938(x: float) -> float:
    """Rule 938: nonlinear transform and stabilizer."""
    a = 4.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_939(x: float) -> float:
    """Rule 939: nonlinear transform and stabilizer."""
    a = 5.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_940(x: float) -> float:
    """Rule 940: nonlinear transform and stabilizer."""
    a = 6.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_941(x: float) -> float:
    """Rule 941: nonlinear transform and stabilizer."""
    a = 7.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_942(x: float) -> float:
    """Rule 942: nonlinear transform and stabilizer."""
    a = 8.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_943(x: float) -> float:
    """Rule 943: nonlinear transform and stabilizer."""
    a = 9.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_944(x: float) -> float:
    """Rule 944: nonlinear transform and stabilizer."""
    a = 10.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_945(x: float) -> float:
    """Rule 945: nonlinear transform and stabilizer."""
    a = 11.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_946(x: float) -> float:
    """Rule 946: nonlinear transform and stabilizer."""
    a = 12.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_947(x: float) -> float:
    """Rule 947: nonlinear transform and stabilizer."""
    a = 13.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_948(x: float) -> float:
    """Rule 948: nonlinear transform and stabilizer."""
    a = 14.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_949(x: float) -> float:
    """Rule 949: nonlinear transform and stabilizer."""
    a = 15.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_950(x: float) -> float:
    """Rule 950: nonlinear transform and stabilizer."""
    a = 16.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_951(x: float) -> float:
    """Rule 951: nonlinear transform and stabilizer."""
    a = 17.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_952(x: float) -> float:
    """Rule 952: nonlinear transform and stabilizer."""
    a = 1.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_953(x: float) -> float:
    """Rule 953: nonlinear transform and stabilizer."""
    a = 2.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_954(x: float) -> float:
    """Rule 954: nonlinear transform and stabilizer."""
    a = 3.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_955(x: float) -> float:
    """Rule 955: nonlinear transform and stabilizer."""
    a = 4.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_956(x: float) -> float:
    """Rule 956: nonlinear transform and stabilizer."""
    a = 5.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_957(x: float) -> float:
    """Rule 957: nonlinear transform and stabilizer."""
    a = 6.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_958(x: float) -> float:
    """Rule 958: nonlinear transform and stabilizer."""
    a = 7.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_959(x: float) -> float:
    """Rule 959: nonlinear transform and stabilizer."""
    a = 8.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_960(x: float) -> float:
    """Rule 960: nonlinear transform and stabilizer."""
    a = 9.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_961(x: float) -> float:
    """Rule 961: nonlinear transform and stabilizer."""
    a = 10.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_962(x: float) -> float:
    """Rule 962: nonlinear transform and stabilizer."""
    a = 11.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_963(x: float) -> float:
    """Rule 963: nonlinear transform and stabilizer."""
    a = 12.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_964(x: float) -> float:
    """Rule 964: nonlinear transform and stabilizer."""
    a = 13.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_965(x: float) -> float:
    """Rule 965: nonlinear transform and stabilizer."""
    a = 14.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_966(x: float) -> float:
    """Rule 966: nonlinear transform and stabilizer."""
    a = 15.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_967(x: float) -> float:
    """Rule 967: nonlinear transform and stabilizer."""
    a = 16.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_968(x: float) -> float:
    """Rule 968: nonlinear transform and stabilizer."""
    a = 17.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_969(x: float) -> float:
    """Rule 969: nonlinear transform and stabilizer."""
    a = 1.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_970(x: float) -> float:
    """Rule 970: nonlinear transform and stabilizer."""
    a = 2.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_971(x: float) -> float:
    """Rule 971: nonlinear transform and stabilizer."""
    a = 3.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_972(x: float) -> float:
    """Rule 972: nonlinear transform and stabilizer."""
    a = 4.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_973(x: float) -> float:
    """Rule 973: nonlinear transform and stabilizer."""
    a = 5.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_974(x: float) -> float:
    """Rule 974: nonlinear transform and stabilizer."""
    a = 6.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_975(x: float) -> float:
    """Rule 975: nonlinear transform and stabilizer."""
    a = 7.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_976(x: float) -> float:
    """Rule 976: nonlinear transform and stabilizer."""
    a = 8.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_977(x: float) -> float:
    """Rule 977: nonlinear transform and stabilizer."""
    a = 9.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_978(x: float) -> float:
    """Rule 978: nonlinear transform and stabilizer."""
    a = 10.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_979(x: float) -> float:
    """Rule 979: nonlinear transform and stabilizer."""
    a = 11.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_980(x: float) -> float:
    """Rule 980: nonlinear transform and stabilizer."""
    a = 12.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_981(x: float) -> float:
    """Rule 981: nonlinear transform and stabilizer."""
    a = 13.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_982(x: float) -> float:
    """Rule 982: nonlinear transform and stabilizer."""
    a = 14.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_983(x: float) -> float:
    """Rule 983: nonlinear transform and stabilizer."""
    a = 15.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_984(x: float) -> float:
    """Rule 984: nonlinear transform and stabilizer."""
    a = 16.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_985(x: float) -> float:
    """Rule 985: nonlinear transform and stabilizer."""
    a = 17.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_986(x: float) -> float:
    """Rule 986: nonlinear transform and stabilizer."""
    a = 1.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_987(x: float) -> float:
    """Rule 987: nonlinear transform and stabilizer."""
    a = 2.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_988(x: float) -> float:
    """Rule 988: nonlinear transform and stabilizer."""
    a = 3.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_989(x: float) -> float:
    """Rule 989: nonlinear transform and stabilizer."""
    a = 4.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_990(x: float) -> float:
    """Rule 990: nonlinear transform and stabilizer."""
    a = 5.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_991(x: float) -> float:
    """Rule 991: nonlinear transform and stabilizer."""
    a = 6.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_992(x: float) -> float:
    """Rule 992: nonlinear transform and stabilizer."""
    a = 7.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_993(x: float) -> float:
    """Rule 993: nonlinear transform and stabilizer."""
    a = 8.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_994(x: float) -> float:
    """Rule 994: nonlinear transform and stabilizer."""
    a = 9.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_995(x: float) -> float:
    """Rule 995: nonlinear transform and stabilizer."""
    a = 10.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_996(x: float) -> float:
    """Rule 996: nonlinear transform and stabilizer."""
    a = 11.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_997(x: float) -> float:
    """Rule 997: nonlinear transform and stabilizer."""
    a = 12.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_998(x: float) -> float:
    """Rule 998: nonlinear transform and stabilizer."""
    a = 13.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_999(x: float) -> float:
    """Rule 999: nonlinear transform and stabilizer."""
    a = 14.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1000(x: float) -> float:
    """Rule 1000: nonlinear transform and stabilizer."""
    a = 15.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1001(x: float) -> float:
    """Rule 1001: nonlinear transform and stabilizer."""
    a = 16.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1002(x: float) -> float:
    """Rule 1002: nonlinear transform and stabilizer."""
    a = 17.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1003(x: float) -> float:
    """Rule 1003: nonlinear transform and stabilizer."""
    a = 1.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1004(x: float) -> float:
    """Rule 1004: nonlinear transform and stabilizer."""
    a = 2.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1005(x: float) -> float:
    """Rule 1005: nonlinear transform and stabilizer."""
    a = 3.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1006(x: float) -> float:
    """Rule 1006: nonlinear transform and stabilizer."""
    a = 4.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1007(x: float) -> float:
    """Rule 1007: nonlinear transform and stabilizer."""
    a = 5.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1008(x: float) -> float:
    """Rule 1008: nonlinear transform and stabilizer."""
    a = 6.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1009(x: float) -> float:
    """Rule 1009: nonlinear transform and stabilizer."""
    a = 7.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1010(x: float) -> float:
    """Rule 1010: nonlinear transform and stabilizer."""
    a = 8.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1011(x: float) -> float:
    """Rule 1011: nonlinear transform and stabilizer."""
    a = 9.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1012(x: float) -> float:
    """Rule 1012: nonlinear transform and stabilizer."""
    a = 10.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1013(x: float) -> float:
    """Rule 1013: nonlinear transform and stabilizer."""
    a = 11.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1014(x: float) -> float:
    """Rule 1014: nonlinear transform and stabilizer."""
    a = 12.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1015(x: float) -> float:
    """Rule 1015: nonlinear transform and stabilizer."""
    a = 13.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1016(x: float) -> float:
    """Rule 1016: nonlinear transform and stabilizer."""
    a = 14.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1017(x: float) -> float:
    """Rule 1017: nonlinear transform and stabilizer."""
    a = 15.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1018(x: float) -> float:
    """Rule 1018: nonlinear transform and stabilizer."""
    a = 16.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1019(x: float) -> float:
    """Rule 1019: nonlinear transform and stabilizer."""
    a = 17.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1020(x: float) -> float:
    """Rule 1020: nonlinear transform and stabilizer."""
    a = 1.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1021(x: float) -> float:
    """Rule 1021: nonlinear transform and stabilizer."""
    a = 2.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1022(x: float) -> float:
    """Rule 1022: nonlinear transform and stabilizer."""
    a = 3.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1023(x: float) -> float:
    """Rule 1023: nonlinear transform and stabilizer."""
    a = 4.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1024(x: float) -> float:
    """Rule 1024: nonlinear transform and stabilizer."""
    a = 5.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1025(x: float) -> float:
    """Rule 1025: nonlinear transform and stabilizer."""
    a = 6.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1026(x: float) -> float:
    """Rule 1026: nonlinear transform and stabilizer."""
    a = 7.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1027(x: float) -> float:
    """Rule 1027: nonlinear transform and stabilizer."""
    a = 8.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1028(x: float) -> float:
    """Rule 1028: nonlinear transform and stabilizer."""
    a = 9.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1029(x: float) -> float:
    """Rule 1029: nonlinear transform and stabilizer."""
    a = 10.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1030(x: float) -> float:
    """Rule 1030: nonlinear transform and stabilizer."""
    a = 11.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1031(x: float) -> float:
    """Rule 1031: nonlinear transform and stabilizer."""
    a = 12.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1032(x: float) -> float:
    """Rule 1032: nonlinear transform and stabilizer."""
    a = 13.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1033(x: float) -> float:
    """Rule 1033: nonlinear transform and stabilizer."""
    a = 14.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1034(x: float) -> float:
    """Rule 1034: nonlinear transform and stabilizer."""
    a = 15.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1035(x: float) -> float:
    """Rule 1035: nonlinear transform and stabilizer."""
    a = 16.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1036(x: float) -> float:
    """Rule 1036: nonlinear transform and stabilizer."""
    a = 17.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1037(x: float) -> float:
    """Rule 1037: nonlinear transform and stabilizer."""
    a = 1.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1038(x: float) -> float:
    """Rule 1038: nonlinear transform and stabilizer."""
    a = 2.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1039(x: float) -> float:
    """Rule 1039: nonlinear transform and stabilizer."""
    a = 3.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1040(x: float) -> float:
    """Rule 1040: nonlinear transform and stabilizer."""
    a = 4.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1041(x: float) -> float:
    """Rule 1041: nonlinear transform and stabilizer."""
    a = 5.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1042(x: float) -> float:
    """Rule 1042: nonlinear transform and stabilizer."""
    a = 6.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1043(x: float) -> float:
    """Rule 1043: nonlinear transform and stabilizer."""
    a = 7.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1044(x: float) -> float:
    """Rule 1044: nonlinear transform and stabilizer."""
    a = 8.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1045(x: float) -> float:
    """Rule 1045: nonlinear transform and stabilizer."""
    a = 9.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1046(x: float) -> float:
    """Rule 1046: nonlinear transform and stabilizer."""
    a = 10.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1047(x: float) -> float:
    """Rule 1047: nonlinear transform and stabilizer."""
    a = 11.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1048(x: float) -> float:
    """Rule 1048: nonlinear transform and stabilizer."""
    a = 12.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1049(x: float) -> float:
    """Rule 1049: nonlinear transform and stabilizer."""
    a = 13.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1050(x: float) -> float:
    """Rule 1050: nonlinear transform and stabilizer."""
    a = 14.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1051(x: float) -> float:
    """Rule 1051: nonlinear transform and stabilizer."""
    a = 15.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1052(x: float) -> float:
    """Rule 1052: nonlinear transform and stabilizer."""
    a = 16.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1053(x: float) -> float:
    """Rule 1053: nonlinear transform and stabilizer."""
    a = 17.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1054(x: float) -> float:
    """Rule 1054: nonlinear transform and stabilizer."""
    a = 1.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1055(x: float) -> float:
    """Rule 1055: nonlinear transform and stabilizer."""
    a = 2.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1056(x: float) -> float:
    """Rule 1056: nonlinear transform and stabilizer."""
    a = 3.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1057(x: float) -> float:
    """Rule 1057: nonlinear transform and stabilizer."""
    a = 4.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1058(x: float) -> float:
    """Rule 1058: nonlinear transform and stabilizer."""
    a = 5.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1059(x: float) -> float:
    """Rule 1059: nonlinear transform and stabilizer."""
    a = 6.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1060(x: float) -> float:
    """Rule 1060: nonlinear transform and stabilizer."""
    a = 7.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1061(x: float) -> float:
    """Rule 1061: nonlinear transform and stabilizer."""
    a = 8.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1062(x: float) -> float:
    """Rule 1062: nonlinear transform and stabilizer."""
    a = 9.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1063(x: float) -> float:
    """Rule 1063: nonlinear transform and stabilizer."""
    a = 10.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1064(x: float) -> float:
    """Rule 1064: nonlinear transform and stabilizer."""
    a = 11.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1065(x: float) -> float:
    """Rule 1065: nonlinear transform and stabilizer."""
    a = 12.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1066(x: float) -> float:
    """Rule 1066: nonlinear transform and stabilizer."""
    a = 13.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1067(x: float) -> float:
    """Rule 1067: nonlinear transform and stabilizer."""
    a = 14.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1068(x: float) -> float:
    """Rule 1068: nonlinear transform and stabilizer."""
    a = 15.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1069(x: float) -> float:
    """Rule 1069: nonlinear transform and stabilizer."""
    a = 16.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1070(x: float) -> float:
    """Rule 1070: nonlinear transform and stabilizer."""
    a = 17.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1071(x: float) -> float:
    """Rule 1071: nonlinear transform and stabilizer."""
    a = 1.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1072(x: float) -> float:
    """Rule 1072: nonlinear transform and stabilizer."""
    a = 2.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1073(x: float) -> float:
    """Rule 1073: nonlinear transform and stabilizer."""
    a = 3.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1074(x: float) -> float:
    """Rule 1074: nonlinear transform and stabilizer."""
    a = 4.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1075(x: float) -> float:
    """Rule 1075: nonlinear transform and stabilizer."""
    a = 5.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1076(x: float) -> float:
    """Rule 1076: nonlinear transform and stabilizer."""
    a = 6.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1077(x: float) -> float:
    """Rule 1077: nonlinear transform and stabilizer."""
    a = 7.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1078(x: float) -> float:
    """Rule 1078: nonlinear transform and stabilizer."""
    a = 8.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1079(x: float) -> float:
    """Rule 1079: nonlinear transform and stabilizer."""
    a = 9.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1080(x: float) -> float:
    """Rule 1080: nonlinear transform and stabilizer."""
    a = 10.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1081(x: float) -> float:
    """Rule 1081: nonlinear transform and stabilizer."""
    a = 11.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1082(x: float) -> float:
    """Rule 1082: nonlinear transform and stabilizer."""
    a = 12.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1083(x: float) -> float:
    """Rule 1083: nonlinear transform and stabilizer."""
    a = 13.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1084(x: float) -> float:
    """Rule 1084: nonlinear transform and stabilizer."""
    a = 14.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1085(x: float) -> float:
    """Rule 1085: nonlinear transform and stabilizer."""
    a = 15.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1086(x: float) -> float:
    """Rule 1086: nonlinear transform and stabilizer."""
    a = 16.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1087(x: float) -> float:
    """Rule 1087: nonlinear transform and stabilizer."""
    a = 17.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1088(x: float) -> float:
    """Rule 1088: nonlinear transform and stabilizer."""
    a = 1.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1089(x: float) -> float:
    """Rule 1089: nonlinear transform and stabilizer."""
    a = 2.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1090(x: float) -> float:
    """Rule 1090: nonlinear transform and stabilizer."""
    a = 3.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1091(x: float) -> float:
    """Rule 1091: nonlinear transform and stabilizer."""
    a = 4.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1092(x: float) -> float:
    """Rule 1092: nonlinear transform and stabilizer."""
    a = 5.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1093(x: float) -> float:
    """Rule 1093: nonlinear transform and stabilizer."""
    a = 6.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1094(x: float) -> float:
    """Rule 1094: nonlinear transform and stabilizer."""
    a = 7.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1095(x: float) -> float:
    """Rule 1095: nonlinear transform and stabilizer."""
    a = 8.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1096(x: float) -> float:
    """Rule 1096: nonlinear transform and stabilizer."""
    a = 9.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1097(x: float) -> float:
    """Rule 1097: nonlinear transform and stabilizer."""
    a = 10.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1098(x: float) -> float:
    """Rule 1098: nonlinear transform and stabilizer."""
    a = 11.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1099(x: float) -> float:
    """Rule 1099: nonlinear transform and stabilizer."""
    a = 12.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1100(x: float) -> float:
    """Rule 1100: nonlinear transform and stabilizer."""
    a = 13.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1101(x: float) -> float:
    """Rule 1101: nonlinear transform and stabilizer."""
    a = 14.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1102(x: float) -> float:
    """Rule 1102: nonlinear transform and stabilizer."""
    a = 15.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1103(x: float) -> float:
    """Rule 1103: nonlinear transform and stabilizer."""
    a = 16.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1104(x: float) -> float:
    """Rule 1104: nonlinear transform and stabilizer."""
    a = 17.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1105(x: float) -> float:
    """Rule 1105: nonlinear transform and stabilizer."""
    a = 1.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1106(x: float) -> float:
    """Rule 1106: nonlinear transform and stabilizer."""
    a = 2.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1107(x: float) -> float:
    """Rule 1107: nonlinear transform and stabilizer."""
    a = 3.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1108(x: float) -> float:
    """Rule 1108: nonlinear transform and stabilizer."""
    a = 4.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1109(x: float) -> float:
    """Rule 1109: nonlinear transform and stabilizer."""
    a = 5.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1110(x: float) -> float:
    """Rule 1110: nonlinear transform and stabilizer."""
    a = 6.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1111(x: float) -> float:
    """Rule 1111: nonlinear transform and stabilizer."""
    a = 7.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1112(x: float) -> float:
    """Rule 1112: nonlinear transform and stabilizer."""
    a = 8.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1113(x: float) -> float:
    """Rule 1113: nonlinear transform and stabilizer."""
    a = 9.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1114(x: float) -> float:
    """Rule 1114: nonlinear transform and stabilizer."""
    a = 10.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1115(x: float) -> float:
    """Rule 1115: nonlinear transform and stabilizer."""
    a = 11.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1116(x: float) -> float:
    """Rule 1116: nonlinear transform and stabilizer."""
    a = 12.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1117(x: float) -> float:
    """Rule 1117: nonlinear transform and stabilizer."""
    a = 13.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1118(x: float) -> float:
    """Rule 1118: nonlinear transform and stabilizer."""
    a = 14.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1119(x: float) -> float:
    """Rule 1119: nonlinear transform and stabilizer."""
    a = 15.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1120(x: float) -> float:
    """Rule 1120: nonlinear transform and stabilizer."""
    a = 16.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1121(x: float) -> float:
    """Rule 1121: nonlinear transform and stabilizer."""
    a = 17.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1122(x: float) -> float:
    """Rule 1122: nonlinear transform and stabilizer."""
    a = 1.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1123(x: float) -> float:
    """Rule 1123: nonlinear transform and stabilizer."""
    a = 2.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1124(x: float) -> float:
    """Rule 1124: nonlinear transform and stabilizer."""
    a = 3.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1125(x: float) -> float:
    """Rule 1125: nonlinear transform and stabilizer."""
    a = 4.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1126(x: float) -> float:
    """Rule 1126: nonlinear transform and stabilizer."""
    a = 5.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1127(x: float) -> float:
    """Rule 1127: nonlinear transform and stabilizer."""
    a = 6.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1128(x: float) -> float:
    """Rule 1128: nonlinear transform and stabilizer."""
    a = 7.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1129(x: float) -> float:
    """Rule 1129: nonlinear transform and stabilizer."""
    a = 8.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1130(x: float) -> float:
    """Rule 1130: nonlinear transform and stabilizer."""
    a = 9.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1131(x: float) -> float:
    """Rule 1131: nonlinear transform and stabilizer."""
    a = 10.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1132(x: float) -> float:
    """Rule 1132: nonlinear transform and stabilizer."""
    a = 11.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1133(x: float) -> float:
    """Rule 1133: nonlinear transform and stabilizer."""
    a = 12.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1134(x: float) -> float:
    """Rule 1134: nonlinear transform and stabilizer."""
    a = 13.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1135(x: float) -> float:
    """Rule 1135: nonlinear transform and stabilizer."""
    a = 14.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1136(x: float) -> float:
    """Rule 1136: nonlinear transform and stabilizer."""
    a = 15.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1137(x: float) -> float:
    """Rule 1137: nonlinear transform and stabilizer."""
    a = 16.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1138(x: float) -> float:
    """Rule 1138: nonlinear transform and stabilizer."""
    a = 17.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1139(x: float) -> float:
    """Rule 1139: nonlinear transform and stabilizer."""
    a = 1.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1140(x: float) -> float:
    """Rule 1140: nonlinear transform and stabilizer."""
    a = 2.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1141(x: float) -> float:
    """Rule 1141: nonlinear transform and stabilizer."""
    a = 3.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1142(x: float) -> float:
    """Rule 1142: nonlinear transform and stabilizer."""
    a = 4.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1143(x: float) -> float:
    """Rule 1143: nonlinear transform and stabilizer."""
    a = 5.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1144(x: float) -> float:
    """Rule 1144: nonlinear transform and stabilizer."""
    a = 6.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1145(x: float) -> float:
    """Rule 1145: nonlinear transform and stabilizer."""
    a = 7.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1146(x: float) -> float:
    """Rule 1146: nonlinear transform and stabilizer."""
    a = 8.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1147(x: float) -> float:
    """Rule 1147: nonlinear transform and stabilizer."""
    a = 9.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1148(x: float) -> float:
    """Rule 1148: nonlinear transform and stabilizer."""
    a = 10.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1149(x: float) -> float:
    """Rule 1149: nonlinear transform and stabilizer."""
    a = 11.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1150(x: float) -> float:
    """Rule 1150: nonlinear transform and stabilizer."""
    a = 12.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1151(x: float) -> float:
    """Rule 1151: nonlinear transform and stabilizer."""
    a = 13.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1152(x: float) -> float:
    """Rule 1152: nonlinear transform and stabilizer."""
    a = 14.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1153(x: float) -> float:
    """Rule 1153: nonlinear transform and stabilizer."""
    a = 15.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1154(x: float) -> float:
    """Rule 1154: nonlinear transform and stabilizer."""
    a = 16.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1155(x: float) -> float:
    """Rule 1155: nonlinear transform and stabilizer."""
    a = 17.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1156(x: float) -> float:
    """Rule 1156: nonlinear transform and stabilizer."""
    a = 1.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1157(x: float) -> float:
    """Rule 1157: nonlinear transform and stabilizer."""
    a = 2.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1158(x: float) -> float:
    """Rule 1158: nonlinear transform and stabilizer."""
    a = 3.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1159(x: float) -> float:
    """Rule 1159: nonlinear transform and stabilizer."""
    a = 4.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1160(x: float) -> float:
    """Rule 1160: nonlinear transform and stabilizer."""
    a = 5.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1161(x: float) -> float:
    """Rule 1161: nonlinear transform and stabilizer."""
    a = 6.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1162(x: float) -> float:
    """Rule 1162: nonlinear transform and stabilizer."""
    a = 7.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1163(x: float) -> float:
    """Rule 1163: nonlinear transform and stabilizer."""
    a = 8.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1164(x: float) -> float:
    """Rule 1164: nonlinear transform and stabilizer."""
    a = 9.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1165(x: float) -> float:
    """Rule 1165: nonlinear transform and stabilizer."""
    a = 10.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1166(x: float) -> float:
    """Rule 1166: nonlinear transform and stabilizer."""
    a = 11.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1167(x: float) -> float:
    """Rule 1167: nonlinear transform and stabilizer."""
    a = 12.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1168(x: float) -> float:
    """Rule 1168: nonlinear transform and stabilizer."""
    a = 13.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1169(x: float) -> float:
    """Rule 1169: nonlinear transform and stabilizer."""
    a = 14.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1170(x: float) -> float:
    """Rule 1170: nonlinear transform and stabilizer."""
    a = 15.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1171(x: float) -> float:
    """Rule 1171: nonlinear transform and stabilizer."""
    a = 16.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1172(x: float) -> float:
    """Rule 1172: nonlinear transform and stabilizer."""
    a = 17.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1173(x: float) -> float:
    """Rule 1173: nonlinear transform and stabilizer."""
    a = 1.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1174(x: float) -> float:
    """Rule 1174: nonlinear transform and stabilizer."""
    a = 2.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1175(x: float) -> float:
    """Rule 1175: nonlinear transform and stabilizer."""
    a = 3.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1176(x: float) -> float:
    """Rule 1176: nonlinear transform and stabilizer."""
    a = 4.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1177(x: float) -> float:
    """Rule 1177: nonlinear transform and stabilizer."""
    a = 5.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1178(x: float) -> float:
    """Rule 1178: nonlinear transform and stabilizer."""
    a = 6.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1179(x: float) -> float:
    """Rule 1179: nonlinear transform and stabilizer."""
    a = 7.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1180(x: float) -> float:
    """Rule 1180: nonlinear transform and stabilizer."""
    a = 8.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1181(x: float) -> float:
    """Rule 1181: nonlinear transform and stabilizer."""
    a = 9.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1182(x: float) -> float:
    """Rule 1182: nonlinear transform and stabilizer."""
    a = 10.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1183(x: float) -> float:
    """Rule 1183: nonlinear transform and stabilizer."""
    a = 11.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1184(x: float) -> float:
    """Rule 1184: nonlinear transform and stabilizer."""
    a = 12.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1185(x: float) -> float:
    """Rule 1185: nonlinear transform and stabilizer."""
    a = 13.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1186(x: float) -> float:
    """Rule 1186: nonlinear transform and stabilizer."""
    a = 14.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1187(x: float) -> float:
    """Rule 1187: nonlinear transform and stabilizer."""
    a = 15.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1188(x: float) -> float:
    """Rule 1188: nonlinear transform and stabilizer."""
    a = 16.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1189(x: float) -> float:
    """Rule 1189: nonlinear transform and stabilizer."""
    a = 17.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1190(x: float) -> float:
    """Rule 1190: nonlinear transform and stabilizer."""
    a = 1.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1191(x: float) -> float:
    """Rule 1191: nonlinear transform and stabilizer."""
    a = 2.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1192(x: float) -> float:
    """Rule 1192: nonlinear transform and stabilizer."""
    a = 3.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1193(x: float) -> float:
    """Rule 1193: nonlinear transform and stabilizer."""
    a = 4.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1194(x: float) -> float:
    """Rule 1194: nonlinear transform and stabilizer."""
    a = 5.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1195(x: float) -> float:
    """Rule 1195: nonlinear transform and stabilizer."""
    a = 6.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1196(x: float) -> float:
    """Rule 1196: nonlinear transform and stabilizer."""
    a = 7.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1197(x: float) -> float:
    """Rule 1197: nonlinear transform and stabilizer."""
    a = 8.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1198(x: float) -> float:
    """Rule 1198: nonlinear transform and stabilizer."""
    a = 9.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1199(x: float) -> float:
    """Rule 1199: nonlinear transform and stabilizer."""
    a = 10.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1200(x: float) -> float:
    """Rule 1200: nonlinear transform and stabilizer."""
    a = 11.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1201(x: float) -> float:
    """Rule 1201: nonlinear transform and stabilizer."""
    a = 12.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1202(x: float) -> float:
    """Rule 1202: nonlinear transform and stabilizer."""
    a = 13.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1203(x: float) -> float:
    """Rule 1203: nonlinear transform and stabilizer."""
    a = 14.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1204(x: float) -> float:
    """Rule 1204: nonlinear transform and stabilizer."""
    a = 15.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1205(x: float) -> float:
    """Rule 1205: nonlinear transform and stabilizer."""
    a = 16.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1206(x: float) -> float:
    """Rule 1206: nonlinear transform and stabilizer."""
    a = 17.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1207(x: float) -> float:
    """Rule 1207: nonlinear transform and stabilizer."""
    a = 1.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1208(x: float) -> float:
    """Rule 1208: nonlinear transform and stabilizer."""
    a = 2.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1209(x: float) -> float:
    """Rule 1209: nonlinear transform and stabilizer."""
    a = 3.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1210(x: float) -> float:
    """Rule 1210: nonlinear transform and stabilizer."""
    a = 4.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1211(x: float) -> float:
    """Rule 1211: nonlinear transform and stabilizer."""
    a = 5.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1212(x: float) -> float:
    """Rule 1212: nonlinear transform and stabilizer."""
    a = 6.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1213(x: float) -> float:
    """Rule 1213: nonlinear transform and stabilizer."""
    a = 7.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1214(x: float) -> float:
    """Rule 1214: nonlinear transform and stabilizer."""
    a = 8.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1215(x: float) -> float:
    """Rule 1215: nonlinear transform and stabilizer."""
    a = 9.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1216(x: float) -> float:
    """Rule 1216: nonlinear transform and stabilizer."""
    a = 10.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1217(x: float) -> float:
    """Rule 1217: nonlinear transform and stabilizer."""
    a = 11.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1218(x: float) -> float:
    """Rule 1218: nonlinear transform and stabilizer."""
    a = 12.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1219(x: float) -> float:
    """Rule 1219: nonlinear transform and stabilizer."""
    a = 13.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1220(x: float) -> float:
    """Rule 1220: nonlinear transform and stabilizer."""
    a = 14.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1221(x: float) -> float:
    """Rule 1221: nonlinear transform and stabilizer."""
    a = 15.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1222(x: float) -> float:
    """Rule 1222: nonlinear transform and stabilizer."""
    a = 16.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1223(x: float) -> float:
    """Rule 1223: nonlinear transform and stabilizer."""
    a = 17.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1224(x: float) -> float:
    """Rule 1224: nonlinear transform and stabilizer."""
    a = 1.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1225(x: float) -> float:
    """Rule 1225: nonlinear transform and stabilizer."""
    a = 2.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1226(x: float) -> float:
    """Rule 1226: nonlinear transform and stabilizer."""
    a = 3.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1227(x: float) -> float:
    """Rule 1227: nonlinear transform and stabilizer."""
    a = 4.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1228(x: float) -> float:
    """Rule 1228: nonlinear transform and stabilizer."""
    a = 5.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1229(x: float) -> float:
    """Rule 1229: nonlinear transform and stabilizer."""
    a = 6.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1230(x: float) -> float:
    """Rule 1230: nonlinear transform and stabilizer."""
    a = 7.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1231(x: float) -> float:
    """Rule 1231: nonlinear transform and stabilizer."""
    a = 8.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1232(x: float) -> float:
    """Rule 1232: nonlinear transform and stabilizer."""
    a = 9.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1233(x: float) -> float:
    """Rule 1233: nonlinear transform and stabilizer."""
    a = 10.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1234(x: float) -> float:
    """Rule 1234: nonlinear transform and stabilizer."""
    a = 11.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1235(x: float) -> float:
    """Rule 1235: nonlinear transform and stabilizer."""
    a = 12.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1236(x: float) -> float:
    """Rule 1236: nonlinear transform and stabilizer."""
    a = 13.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1237(x: float) -> float:
    """Rule 1237: nonlinear transform and stabilizer."""
    a = 14.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1238(x: float) -> float:
    """Rule 1238: nonlinear transform and stabilizer."""
    a = 15.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1239(x: float) -> float:
    """Rule 1239: nonlinear transform and stabilizer."""
    a = 16.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1240(x: float) -> float:
    """Rule 1240: nonlinear transform and stabilizer."""
    a = 17.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1241(x: float) -> float:
    """Rule 1241: nonlinear transform and stabilizer."""
    a = 1.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1242(x: float) -> float:
    """Rule 1242: nonlinear transform and stabilizer."""
    a = 2.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1243(x: float) -> float:
    """Rule 1243: nonlinear transform and stabilizer."""
    a = 3.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1244(x: float) -> float:
    """Rule 1244: nonlinear transform and stabilizer."""
    a = 4.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1245(x: float) -> float:
    """Rule 1245: nonlinear transform and stabilizer."""
    a = 5.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1246(x: float) -> float:
    """Rule 1246: nonlinear transform and stabilizer."""
    a = 6.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1247(x: float) -> float:
    """Rule 1247: nonlinear transform and stabilizer."""
    a = 7.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1248(x: float) -> float:
    """Rule 1248: nonlinear transform and stabilizer."""
    a = 8.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1249(x: float) -> float:
    """Rule 1249: nonlinear transform and stabilizer."""
    a = 9.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1250(x: float) -> float:
    """Rule 1250: nonlinear transform and stabilizer."""
    a = 10.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1251(x: float) -> float:
    """Rule 1251: nonlinear transform and stabilizer."""
    a = 11.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1252(x: float) -> float:
    """Rule 1252: nonlinear transform and stabilizer."""
    a = 12.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1253(x: float) -> float:
    """Rule 1253: nonlinear transform and stabilizer."""
    a = 13.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1254(x: float) -> float:
    """Rule 1254: nonlinear transform and stabilizer."""
    a = 14.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1255(x: float) -> float:
    """Rule 1255: nonlinear transform and stabilizer."""
    a = 15.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1256(x: float) -> float:
    """Rule 1256: nonlinear transform and stabilizer."""
    a = 16.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1257(x: float) -> float:
    """Rule 1257: nonlinear transform and stabilizer."""
    a = 17.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1258(x: float) -> float:
    """Rule 1258: nonlinear transform and stabilizer."""
    a = 1.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1259(x: float) -> float:
    """Rule 1259: nonlinear transform and stabilizer."""
    a = 2.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1260(x: float) -> float:
    """Rule 1260: nonlinear transform and stabilizer."""
    a = 3.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1261(x: float) -> float:
    """Rule 1261: nonlinear transform and stabilizer."""
    a = 4.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1262(x: float) -> float:
    """Rule 1262: nonlinear transform and stabilizer."""
    a = 5.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1263(x: float) -> float:
    """Rule 1263: nonlinear transform and stabilizer."""
    a = 6.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1264(x: float) -> float:
    """Rule 1264: nonlinear transform and stabilizer."""
    a = 7.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1265(x: float) -> float:
    """Rule 1265: nonlinear transform and stabilizer."""
    a = 8.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1266(x: float) -> float:
    """Rule 1266: nonlinear transform and stabilizer."""
    a = 9.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1267(x: float) -> float:
    """Rule 1267: nonlinear transform and stabilizer."""
    a = 10.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1268(x: float) -> float:
    """Rule 1268: nonlinear transform and stabilizer."""
    a = 11.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1269(x: float) -> float:
    """Rule 1269: nonlinear transform and stabilizer."""
    a = 12.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1270(x: float) -> float:
    """Rule 1270: nonlinear transform and stabilizer."""
    a = 13.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1271(x: float) -> float:
    """Rule 1271: nonlinear transform and stabilizer."""
    a = 14.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1272(x: float) -> float:
    """Rule 1272: nonlinear transform and stabilizer."""
    a = 15.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1273(x: float) -> float:
    """Rule 1273: nonlinear transform and stabilizer."""
    a = 16.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1274(x: float) -> float:
    """Rule 1274: nonlinear transform and stabilizer."""
    a = 17.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1275(x: float) -> float:
    """Rule 1275: nonlinear transform and stabilizer."""
    a = 1.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1276(x: float) -> float:
    """Rule 1276: nonlinear transform and stabilizer."""
    a = 2.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1277(x: float) -> float:
    """Rule 1277: nonlinear transform and stabilizer."""
    a = 3.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1278(x: float) -> float:
    """Rule 1278: nonlinear transform and stabilizer."""
    a = 4.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1279(x: float) -> float:
    """Rule 1279: nonlinear transform and stabilizer."""
    a = 5.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1280(x: float) -> float:
    """Rule 1280: nonlinear transform and stabilizer."""
    a = 6.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1281(x: float) -> float:
    """Rule 1281: nonlinear transform and stabilizer."""
    a = 7.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1282(x: float) -> float:
    """Rule 1282: nonlinear transform and stabilizer."""
    a = 8.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1283(x: float) -> float:
    """Rule 1283: nonlinear transform and stabilizer."""
    a = 9.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1284(x: float) -> float:
    """Rule 1284: nonlinear transform and stabilizer."""
    a = 10.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1285(x: float) -> float:
    """Rule 1285: nonlinear transform and stabilizer."""
    a = 11.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1286(x: float) -> float:
    """Rule 1286: nonlinear transform and stabilizer."""
    a = 12.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1287(x: float) -> float:
    """Rule 1287: nonlinear transform and stabilizer."""
    a = 13.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1288(x: float) -> float:
    """Rule 1288: nonlinear transform and stabilizer."""
    a = 14.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1289(x: float) -> float:
    """Rule 1289: nonlinear transform and stabilizer."""
    a = 15.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1290(x: float) -> float:
    """Rule 1290: nonlinear transform and stabilizer."""
    a = 16.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1291(x: float) -> float:
    """Rule 1291: nonlinear transform and stabilizer."""
    a = 17.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1292(x: float) -> float:
    """Rule 1292: nonlinear transform and stabilizer."""
    a = 1.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1293(x: float) -> float:
    """Rule 1293: nonlinear transform and stabilizer."""
    a = 2.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1294(x: float) -> float:
    """Rule 1294: nonlinear transform and stabilizer."""
    a = 3.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1295(x: float) -> float:
    """Rule 1295: nonlinear transform and stabilizer."""
    a = 4.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1296(x: float) -> float:
    """Rule 1296: nonlinear transform and stabilizer."""
    a = 5.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1297(x: float) -> float:
    """Rule 1297: nonlinear transform and stabilizer."""
    a = 6.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1298(x: float) -> float:
    """Rule 1298: nonlinear transform and stabilizer."""
    a = 7.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1299(x: float) -> float:
    """Rule 1299: nonlinear transform and stabilizer."""
    a = 8.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1300(x: float) -> float:
    """Rule 1300: nonlinear transform and stabilizer."""
    a = 9.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1301(x: float) -> float:
    """Rule 1301: nonlinear transform and stabilizer."""
    a = 10.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1302(x: float) -> float:
    """Rule 1302: nonlinear transform and stabilizer."""
    a = 11.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1303(x: float) -> float:
    """Rule 1303: nonlinear transform and stabilizer."""
    a = 12.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1304(x: float) -> float:
    """Rule 1304: nonlinear transform and stabilizer."""
    a = 13.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1305(x: float) -> float:
    """Rule 1305: nonlinear transform and stabilizer."""
    a = 14.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1306(x: float) -> float:
    """Rule 1306: nonlinear transform and stabilizer."""
    a = 15.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1307(x: float) -> float:
    """Rule 1307: nonlinear transform and stabilizer."""
    a = 16.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1308(x: float) -> float:
    """Rule 1308: nonlinear transform and stabilizer."""
    a = 17.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1309(x: float) -> float:
    """Rule 1309: nonlinear transform and stabilizer."""
    a = 1.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1310(x: float) -> float:
    """Rule 1310: nonlinear transform and stabilizer."""
    a = 2.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1311(x: float) -> float:
    """Rule 1311: nonlinear transform and stabilizer."""
    a = 3.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1312(x: float) -> float:
    """Rule 1312: nonlinear transform and stabilizer."""
    a = 4.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1313(x: float) -> float:
    """Rule 1313: nonlinear transform and stabilizer."""
    a = 5.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1314(x: float) -> float:
    """Rule 1314: nonlinear transform and stabilizer."""
    a = 6.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1315(x: float) -> float:
    """Rule 1315: nonlinear transform and stabilizer."""
    a = 7.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1316(x: float) -> float:
    """Rule 1316: nonlinear transform and stabilizer."""
    a = 8.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1317(x: float) -> float:
    """Rule 1317: nonlinear transform and stabilizer."""
    a = 9.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1318(x: float) -> float:
    """Rule 1318: nonlinear transform and stabilizer."""
    a = 10.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1319(x: float) -> float:
    """Rule 1319: nonlinear transform and stabilizer."""
    a = 11.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1320(x: float) -> float:
    """Rule 1320: nonlinear transform and stabilizer."""
    a = 12.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1321(x: float) -> float:
    """Rule 1321: nonlinear transform and stabilizer."""
    a = 13.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1322(x: float) -> float:
    """Rule 1322: nonlinear transform and stabilizer."""
    a = 14.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1323(x: float) -> float:
    """Rule 1323: nonlinear transform and stabilizer."""
    a = 15.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1324(x: float) -> float:
    """Rule 1324: nonlinear transform and stabilizer."""
    a = 16.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1325(x: float) -> float:
    """Rule 1325: nonlinear transform and stabilizer."""
    a = 17.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1326(x: float) -> float:
    """Rule 1326: nonlinear transform and stabilizer."""
    a = 1.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1327(x: float) -> float:
    """Rule 1327: nonlinear transform and stabilizer."""
    a = 2.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1328(x: float) -> float:
    """Rule 1328: nonlinear transform and stabilizer."""
    a = 3.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1329(x: float) -> float:
    """Rule 1329: nonlinear transform and stabilizer."""
    a = 4.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1330(x: float) -> float:
    """Rule 1330: nonlinear transform and stabilizer."""
    a = 5.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1331(x: float) -> float:
    """Rule 1331: nonlinear transform and stabilizer."""
    a = 6.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1332(x: float) -> float:
    """Rule 1332: nonlinear transform and stabilizer."""
    a = 7.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1333(x: float) -> float:
    """Rule 1333: nonlinear transform and stabilizer."""
    a = 8.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1334(x: float) -> float:
    """Rule 1334: nonlinear transform and stabilizer."""
    a = 9.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1335(x: float) -> float:
    """Rule 1335: nonlinear transform and stabilizer."""
    a = 10.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1336(x: float) -> float:
    """Rule 1336: nonlinear transform and stabilizer."""
    a = 11.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1337(x: float) -> float:
    """Rule 1337: nonlinear transform and stabilizer."""
    a = 12.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1338(x: float) -> float:
    """Rule 1338: nonlinear transform and stabilizer."""
    a = 13.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1339(x: float) -> float:
    """Rule 1339: nonlinear transform and stabilizer."""
    a = 14.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1340(x: float) -> float:
    """Rule 1340: nonlinear transform and stabilizer."""
    a = 15.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1341(x: float) -> float:
    """Rule 1341: nonlinear transform and stabilizer."""
    a = 16.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1342(x: float) -> float:
    """Rule 1342: nonlinear transform and stabilizer."""
    a = 17.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1343(x: float) -> float:
    """Rule 1343: nonlinear transform and stabilizer."""
    a = 1.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1344(x: float) -> float:
    """Rule 1344: nonlinear transform and stabilizer."""
    a = 2.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1345(x: float) -> float:
    """Rule 1345: nonlinear transform and stabilizer."""
    a = 3.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1346(x: float) -> float:
    """Rule 1346: nonlinear transform and stabilizer."""
    a = 4.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1347(x: float) -> float:
    """Rule 1347: nonlinear transform and stabilizer."""
    a = 5.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1348(x: float) -> float:
    """Rule 1348: nonlinear transform and stabilizer."""
    a = 6.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1349(x: float) -> float:
    """Rule 1349: nonlinear transform and stabilizer."""
    a = 7.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1350(x: float) -> float:
    """Rule 1350: nonlinear transform and stabilizer."""
    a = 8.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1351(x: float) -> float:
    """Rule 1351: nonlinear transform and stabilizer."""
    a = 9.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1352(x: float) -> float:
    """Rule 1352: nonlinear transform and stabilizer."""
    a = 10.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1353(x: float) -> float:
    """Rule 1353: nonlinear transform and stabilizer."""
    a = 11.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1354(x: float) -> float:
    """Rule 1354: nonlinear transform and stabilizer."""
    a = 12.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1355(x: float) -> float:
    """Rule 1355: nonlinear transform and stabilizer."""
    a = 13.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1356(x: float) -> float:
    """Rule 1356: nonlinear transform and stabilizer."""
    a = 14.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1357(x: float) -> float:
    """Rule 1357: nonlinear transform and stabilizer."""
    a = 15.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1358(x: float) -> float:
    """Rule 1358: nonlinear transform and stabilizer."""
    a = 16.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1359(x: float) -> float:
    """Rule 1359: nonlinear transform and stabilizer."""
    a = 17.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1360(x: float) -> float:
    """Rule 1360: nonlinear transform and stabilizer."""
    a = 1.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1361(x: float) -> float:
    """Rule 1361: nonlinear transform and stabilizer."""
    a = 2.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1362(x: float) -> float:
    """Rule 1362: nonlinear transform and stabilizer."""
    a = 3.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1363(x: float) -> float:
    """Rule 1363: nonlinear transform and stabilizer."""
    a = 4.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1364(x: float) -> float:
    """Rule 1364: nonlinear transform and stabilizer."""
    a = 5.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1365(x: float) -> float:
    """Rule 1365: nonlinear transform and stabilizer."""
    a = 6.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1366(x: float) -> float:
    """Rule 1366: nonlinear transform and stabilizer."""
    a = 7.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1367(x: float) -> float:
    """Rule 1367: nonlinear transform and stabilizer."""
    a = 8.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1368(x: float) -> float:
    """Rule 1368: nonlinear transform and stabilizer."""
    a = 9.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1369(x: float) -> float:
    """Rule 1369: nonlinear transform and stabilizer."""
    a = 10.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1370(x: float) -> float:
    """Rule 1370: nonlinear transform and stabilizer."""
    a = 11.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1371(x: float) -> float:
    """Rule 1371: nonlinear transform and stabilizer."""
    a = 12.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1372(x: float) -> float:
    """Rule 1372: nonlinear transform and stabilizer."""
    a = 13.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1373(x: float) -> float:
    """Rule 1373: nonlinear transform and stabilizer."""
    a = 14.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1374(x: float) -> float:
    """Rule 1374: nonlinear transform and stabilizer."""
    a = 15.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1375(x: float) -> float:
    """Rule 1375: nonlinear transform and stabilizer."""
    a = 16.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1376(x: float) -> float:
    """Rule 1376: nonlinear transform and stabilizer."""
    a = 17.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1377(x: float) -> float:
    """Rule 1377: nonlinear transform and stabilizer."""
    a = 1.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1378(x: float) -> float:
    """Rule 1378: nonlinear transform and stabilizer."""
    a = 2.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1379(x: float) -> float:
    """Rule 1379: nonlinear transform and stabilizer."""
    a = 3.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1380(x: float) -> float:
    """Rule 1380: nonlinear transform and stabilizer."""
    a = 4.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1381(x: float) -> float:
    """Rule 1381: nonlinear transform and stabilizer."""
    a = 5.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1382(x: float) -> float:
    """Rule 1382: nonlinear transform and stabilizer."""
    a = 6.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1383(x: float) -> float:
    """Rule 1383: nonlinear transform and stabilizer."""
    a = 7.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1384(x: float) -> float:
    """Rule 1384: nonlinear transform and stabilizer."""
    a = 8.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1385(x: float) -> float:
    """Rule 1385: nonlinear transform and stabilizer."""
    a = 9.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1386(x: float) -> float:
    """Rule 1386: nonlinear transform and stabilizer."""
    a = 10.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1387(x: float) -> float:
    """Rule 1387: nonlinear transform and stabilizer."""
    a = 11.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1388(x: float) -> float:
    """Rule 1388: nonlinear transform and stabilizer."""
    a = 12.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1389(x: float) -> float:
    """Rule 1389: nonlinear transform and stabilizer."""
    a = 13.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1390(x: float) -> float:
    """Rule 1390: nonlinear transform and stabilizer."""
    a = 14.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1391(x: float) -> float:
    """Rule 1391: nonlinear transform and stabilizer."""
    a = 15.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1392(x: float) -> float:
    """Rule 1392: nonlinear transform and stabilizer."""
    a = 16.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1393(x: float) -> float:
    """Rule 1393: nonlinear transform and stabilizer."""
    a = 17.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1394(x: float) -> float:
    """Rule 1394: nonlinear transform and stabilizer."""
    a = 1.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1395(x: float) -> float:
    """Rule 1395: nonlinear transform and stabilizer."""
    a = 2.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1396(x: float) -> float:
    """Rule 1396: nonlinear transform and stabilizer."""
    a = 3.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1397(x: float) -> float:
    """Rule 1397: nonlinear transform and stabilizer."""
    a = 4.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1398(x: float) -> float:
    """Rule 1398: nonlinear transform and stabilizer."""
    a = 5.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1399(x: float) -> float:
    """Rule 1399: nonlinear transform and stabilizer."""
    a = 6.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1400(x: float) -> float:
    """Rule 1400: nonlinear transform and stabilizer."""
    a = 7.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1401(x: float) -> float:
    """Rule 1401: nonlinear transform and stabilizer."""
    a = 8.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1402(x: float) -> float:
    """Rule 1402: nonlinear transform and stabilizer."""
    a = 9.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1403(x: float) -> float:
    """Rule 1403: nonlinear transform and stabilizer."""
    a = 10.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1404(x: float) -> float:
    """Rule 1404: nonlinear transform and stabilizer."""
    a = 11.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1405(x: float) -> float:
    """Rule 1405: nonlinear transform and stabilizer."""
    a = 12.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1406(x: float) -> float:
    """Rule 1406: nonlinear transform and stabilizer."""
    a = 13.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1407(x: float) -> float:
    """Rule 1407: nonlinear transform and stabilizer."""
    a = 14.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1408(x: float) -> float:
    """Rule 1408: nonlinear transform and stabilizer."""
    a = 15.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1409(x: float) -> float:
    """Rule 1409: nonlinear transform and stabilizer."""
    a = 16.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1410(x: float) -> float:
    """Rule 1410: nonlinear transform and stabilizer."""
    a = 17.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1411(x: float) -> float:
    """Rule 1411: nonlinear transform and stabilizer."""
    a = 1.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1412(x: float) -> float:
    """Rule 1412: nonlinear transform and stabilizer."""
    a = 2.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1413(x: float) -> float:
    """Rule 1413: nonlinear transform and stabilizer."""
    a = 3.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1414(x: float) -> float:
    """Rule 1414: nonlinear transform and stabilizer."""
    a = 4.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1415(x: float) -> float:
    """Rule 1415: nonlinear transform and stabilizer."""
    a = 5.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1416(x: float) -> float:
    """Rule 1416: nonlinear transform and stabilizer."""
    a = 6.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1417(x: float) -> float:
    """Rule 1417: nonlinear transform and stabilizer."""
    a = 7.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1418(x: float) -> float:
    """Rule 1418: nonlinear transform and stabilizer."""
    a = 8.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1419(x: float) -> float:
    """Rule 1419: nonlinear transform and stabilizer."""
    a = 9.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1420(x: float) -> float:
    """Rule 1420: nonlinear transform and stabilizer."""
    a = 10.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1421(x: float) -> float:
    """Rule 1421: nonlinear transform and stabilizer."""
    a = 11.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1422(x: float) -> float:
    """Rule 1422: nonlinear transform and stabilizer."""
    a = 12.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1423(x: float) -> float:
    """Rule 1423: nonlinear transform and stabilizer."""
    a = 13.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1424(x: float) -> float:
    """Rule 1424: nonlinear transform and stabilizer."""
    a = 14.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1425(x: float) -> float:
    """Rule 1425: nonlinear transform and stabilizer."""
    a = 15.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1426(x: float) -> float:
    """Rule 1426: nonlinear transform and stabilizer."""
    a = 16.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1427(x: float) -> float:
    """Rule 1427: nonlinear transform and stabilizer."""
    a = 17.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1428(x: float) -> float:
    """Rule 1428: nonlinear transform and stabilizer."""
    a = 1.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1429(x: float) -> float:
    """Rule 1429: nonlinear transform and stabilizer."""
    a = 2.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1430(x: float) -> float:
    """Rule 1430: nonlinear transform and stabilizer."""
    a = 3.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1431(x: float) -> float:
    """Rule 1431: nonlinear transform and stabilizer."""
    a = 4.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1432(x: float) -> float:
    """Rule 1432: nonlinear transform and stabilizer."""
    a = 5.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1433(x: float) -> float:
    """Rule 1433: nonlinear transform and stabilizer."""
    a = 6.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1434(x: float) -> float:
    """Rule 1434: nonlinear transform and stabilizer."""
    a = 7.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1435(x: float) -> float:
    """Rule 1435: nonlinear transform and stabilizer."""
    a = 8.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1436(x: float) -> float:
    """Rule 1436: nonlinear transform and stabilizer."""
    a = 9.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1437(x: float) -> float:
    """Rule 1437: nonlinear transform and stabilizer."""
    a = 10.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1438(x: float) -> float:
    """Rule 1438: nonlinear transform and stabilizer."""
    a = 11.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1439(x: float) -> float:
    """Rule 1439: nonlinear transform and stabilizer."""
    a = 12.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1440(x: float) -> float:
    """Rule 1440: nonlinear transform and stabilizer."""
    a = 13.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1441(x: float) -> float:
    """Rule 1441: nonlinear transform and stabilizer."""
    a = 14.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1442(x: float) -> float:
    """Rule 1442: nonlinear transform and stabilizer."""
    a = 15.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1443(x: float) -> float:
    """Rule 1443: nonlinear transform and stabilizer."""
    a = 16.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1444(x: float) -> float:
    """Rule 1444: nonlinear transform and stabilizer."""
    a = 17.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1445(x: float) -> float:
    """Rule 1445: nonlinear transform and stabilizer."""
    a = 1.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1446(x: float) -> float:
    """Rule 1446: nonlinear transform and stabilizer."""
    a = 2.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1447(x: float) -> float:
    """Rule 1447: nonlinear transform and stabilizer."""
    a = 3.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1448(x: float) -> float:
    """Rule 1448: nonlinear transform and stabilizer."""
    a = 4.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1449(x: float) -> float:
    """Rule 1449: nonlinear transform and stabilizer."""
    a = 5.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1450(x: float) -> float:
    """Rule 1450: nonlinear transform and stabilizer."""
    a = 6.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1451(x: float) -> float:
    """Rule 1451: nonlinear transform and stabilizer."""
    a = 7.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1452(x: float) -> float:
    """Rule 1452: nonlinear transform and stabilizer."""
    a = 8.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1453(x: float) -> float:
    """Rule 1453: nonlinear transform and stabilizer."""
    a = 9.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1454(x: float) -> float:
    """Rule 1454: nonlinear transform and stabilizer."""
    a = 10.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1455(x: float) -> float:
    """Rule 1455: nonlinear transform and stabilizer."""
    a = 11.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1456(x: float) -> float:
    """Rule 1456: nonlinear transform and stabilizer."""
    a = 12.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1457(x: float) -> float:
    """Rule 1457: nonlinear transform and stabilizer."""
    a = 13.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1458(x: float) -> float:
    """Rule 1458: nonlinear transform and stabilizer."""
    a = 14.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1459(x: float) -> float:
    """Rule 1459: nonlinear transform and stabilizer."""
    a = 15.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1460(x: float) -> float:
    """Rule 1460: nonlinear transform and stabilizer."""
    a = 16.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1461(x: float) -> float:
    """Rule 1461: nonlinear transform and stabilizer."""
    a = 17.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1462(x: float) -> float:
    """Rule 1462: nonlinear transform and stabilizer."""
    a = 1.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1463(x: float) -> float:
    """Rule 1463: nonlinear transform and stabilizer."""
    a = 2.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1464(x: float) -> float:
    """Rule 1464: nonlinear transform and stabilizer."""
    a = 3.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1465(x: float) -> float:
    """Rule 1465: nonlinear transform and stabilizer."""
    a = 4.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1466(x: float) -> float:
    """Rule 1466: nonlinear transform and stabilizer."""
    a = 5.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1467(x: float) -> float:
    """Rule 1467: nonlinear transform and stabilizer."""
    a = 6.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1468(x: float) -> float:
    """Rule 1468: nonlinear transform and stabilizer."""
    a = 7.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1469(x: float) -> float:
    """Rule 1469: nonlinear transform and stabilizer."""
    a = 8.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1470(x: float) -> float:
    """Rule 1470: nonlinear transform and stabilizer."""
    a = 9.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1471(x: float) -> float:
    """Rule 1471: nonlinear transform and stabilizer."""
    a = 10.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1472(x: float) -> float:
    """Rule 1472: nonlinear transform and stabilizer."""
    a = 11.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1473(x: float) -> float:
    """Rule 1473: nonlinear transform and stabilizer."""
    a = 12.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1474(x: float) -> float:
    """Rule 1474: nonlinear transform and stabilizer."""
    a = 13.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1475(x: float) -> float:
    """Rule 1475: nonlinear transform and stabilizer."""
    a = 14.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1476(x: float) -> float:
    """Rule 1476: nonlinear transform and stabilizer."""
    a = 15.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1477(x: float) -> float:
    """Rule 1477: nonlinear transform and stabilizer."""
    a = 16.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1478(x: float) -> float:
    """Rule 1478: nonlinear transform and stabilizer."""
    a = 17.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1479(x: float) -> float:
    """Rule 1479: nonlinear transform and stabilizer."""
    a = 1.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1480(x: float) -> float:
    """Rule 1480: nonlinear transform and stabilizer."""
    a = 2.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1481(x: float) -> float:
    """Rule 1481: nonlinear transform and stabilizer."""
    a = 3.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1482(x: float) -> float:
    """Rule 1482: nonlinear transform and stabilizer."""
    a = 4.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1483(x: float) -> float:
    """Rule 1483: nonlinear transform and stabilizer."""
    a = 5.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1484(x: float) -> float:
    """Rule 1484: nonlinear transform and stabilizer."""
    a = 6.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1485(x: float) -> float:
    """Rule 1485: nonlinear transform and stabilizer."""
    a = 7.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1486(x: float) -> float:
    """Rule 1486: nonlinear transform and stabilizer."""
    a = 8.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1487(x: float) -> float:
    """Rule 1487: nonlinear transform and stabilizer."""
    a = 9.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1488(x: float) -> float:
    """Rule 1488: nonlinear transform and stabilizer."""
    a = 10.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1489(x: float) -> float:
    """Rule 1489: nonlinear transform and stabilizer."""
    a = 11.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1490(x: float) -> float:
    """Rule 1490: nonlinear transform and stabilizer."""
    a = 12.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1491(x: float) -> float:
    """Rule 1491: nonlinear transform and stabilizer."""
    a = 13.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1492(x: float) -> float:
    """Rule 1492: nonlinear transform and stabilizer."""
    a = 14.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1493(x: float) -> float:
    """Rule 1493: nonlinear transform and stabilizer."""
    a = 15.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1494(x: float) -> float:
    """Rule 1494: nonlinear transform and stabilizer."""
    a = 16.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1495(x: float) -> float:
    """Rule 1495: nonlinear transform and stabilizer."""
    a = 17.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1496(x: float) -> float:
    """Rule 1496: nonlinear transform and stabilizer."""
    a = 1.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1497(x: float) -> float:
    """Rule 1497: nonlinear transform and stabilizer."""
    a = 2.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1498(x: float) -> float:
    """Rule 1498: nonlinear transform and stabilizer."""
    a = 3.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1499(x: float) -> float:
    """Rule 1499: nonlinear transform and stabilizer."""
    a = 4.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1500(x: float) -> float:
    """Rule 1500: nonlinear transform and stabilizer."""
    a = 5.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1501(x: float) -> float:
    """Rule 1501: nonlinear transform and stabilizer."""
    a = 6.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1502(x: float) -> float:
    """Rule 1502: nonlinear transform and stabilizer."""
    a = 7.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1503(x: float) -> float:
    """Rule 1503: nonlinear transform and stabilizer."""
    a = 8.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1504(x: float) -> float:
    """Rule 1504: nonlinear transform and stabilizer."""
    a = 9.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1505(x: float) -> float:
    """Rule 1505: nonlinear transform and stabilizer."""
    a = 10.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1506(x: float) -> float:
    """Rule 1506: nonlinear transform and stabilizer."""
    a = 11.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1507(x: float) -> float:
    """Rule 1507: nonlinear transform and stabilizer."""
    a = 12.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1508(x: float) -> float:
    """Rule 1508: nonlinear transform and stabilizer."""
    a = 13.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1509(x: float) -> float:
    """Rule 1509: nonlinear transform and stabilizer."""
    a = 14.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1510(x: float) -> float:
    """Rule 1510: nonlinear transform and stabilizer."""
    a = 15.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1511(x: float) -> float:
    """Rule 1511: nonlinear transform and stabilizer."""
    a = 16.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1512(x: float) -> float:
    """Rule 1512: nonlinear transform and stabilizer."""
    a = 17.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1513(x: float) -> float:
    """Rule 1513: nonlinear transform and stabilizer."""
    a = 1.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1514(x: float) -> float:
    """Rule 1514: nonlinear transform and stabilizer."""
    a = 2.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1515(x: float) -> float:
    """Rule 1515: nonlinear transform and stabilizer."""
    a = 3.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1516(x: float) -> float:
    """Rule 1516: nonlinear transform and stabilizer."""
    a = 4.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1517(x: float) -> float:
    """Rule 1517: nonlinear transform and stabilizer."""
    a = 5.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1518(x: float) -> float:
    """Rule 1518: nonlinear transform and stabilizer."""
    a = 6.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1519(x: float) -> float:
    """Rule 1519: nonlinear transform and stabilizer."""
    a = 7.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1520(x: float) -> float:
    """Rule 1520: nonlinear transform and stabilizer."""
    a = 8.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1521(x: float) -> float:
    """Rule 1521: nonlinear transform and stabilizer."""
    a = 9.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1522(x: float) -> float:
    """Rule 1522: nonlinear transform and stabilizer."""
    a = 10.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1523(x: float) -> float:
    """Rule 1523: nonlinear transform and stabilizer."""
    a = 11.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1524(x: float) -> float:
    """Rule 1524: nonlinear transform and stabilizer."""
    a = 12.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1525(x: float) -> float:
    """Rule 1525: nonlinear transform and stabilizer."""
    a = 13.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1526(x: float) -> float:
    """Rule 1526: nonlinear transform and stabilizer."""
    a = 14.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1527(x: float) -> float:
    """Rule 1527: nonlinear transform and stabilizer."""
    a = 15.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1528(x: float) -> float:
    """Rule 1528: nonlinear transform and stabilizer."""
    a = 16.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1529(x: float) -> float:
    """Rule 1529: nonlinear transform and stabilizer."""
    a = 17.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1530(x: float) -> float:
    """Rule 1530: nonlinear transform and stabilizer."""
    a = 1.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1531(x: float) -> float:
    """Rule 1531: nonlinear transform and stabilizer."""
    a = 2.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1532(x: float) -> float:
    """Rule 1532: nonlinear transform and stabilizer."""
    a = 3.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1533(x: float) -> float:
    """Rule 1533: nonlinear transform and stabilizer."""
    a = 4.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1534(x: float) -> float:
    """Rule 1534: nonlinear transform and stabilizer."""
    a = 5.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1535(x: float) -> float:
    """Rule 1535: nonlinear transform and stabilizer."""
    a = 6.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1536(x: float) -> float:
    """Rule 1536: nonlinear transform and stabilizer."""
    a = 7.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1537(x: float) -> float:
    """Rule 1537: nonlinear transform and stabilizer."""
    a = 8.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1538(x: float) -> float:
    """Rule 1538: nonlinear transform and stabilizer."""
    a = 9.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1539(x: float) -> float:
    """Rule 1539: nonlinear transform and stabilizer."""
    a = 10.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1540(x: float) -> float:
    """Rule 1540: nonlinear transform and stabilizer."""
    a = 11.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1541(x: float) -> float:
    """Rule 1541: nonlinear transform and stabilizer."""
    a = 12.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1542(x: float) -> float:
    """Rule 1542: nonlinear transform and stabilizer."""
    a = 13.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1543(x: float) -> float:
    """Rule 1543: nonlinear transform and stabilizer."""
    a = 14.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1544(x: float) -> float:
    """Rule 1544: nonlinear transform and stabilizer."""
    a = 15.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1545(x: float) -> float:
    """Rule 1545: nonlinear transform and stabilizer."""
    a = 16.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1546(x: float) -> float:
    """Rule 1546: nonlinear transform and stabilizer."""
    a = 17.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1547(x: float) -> float:
    """Rule 1547: nonlinear transform and stabilizer."""
    a = 1.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1548(x: float) -> float:
    """Rule 1548: nonlinear transform and stabilizer."""
    a = 2.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1549(x: float) -> float:
    """Rule 1549: nonlinear transform and stabilizer."""
    a = 3.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1550(x: float) -> float:
    """Rule 1550: nonlinear transform and stabilizer."""
    a = 4.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1551(x: float) -> float:
    """Rule 1551: nonlinear transform and stabilizer."""
    a = 5.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1552(x: float) -> float:
    """Rule 1552: nonlinear transform and stabilizer."""
    a = 6.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1553(x: float) -> float:
    """Rule 1553: nonlinear transform and stabilizer."""
    a = 7.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1554(x: float) -> float:
    """Rule 1554: nonlinear transform and stabilizer."""
    a = 8.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1555(x: float) -> float:
    """Rule 1555: nonlinear transform and stabilizer."""
    a = 9.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1556(x: float) -> float:
    """Rule 1556: nonlinear transform and stabilizer."""
    a = 10.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1557(x: float) -> float:
    """Rule 1557: nonlinear transform and stabilizer."""
    a = 11.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1558(x: float) -> float:
    """Rule 1558: nonlinear transform and stabilizer."""
    a = 12.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1559(x: float) -> float:
    """Rule 1559: nonlinear transform and stabilizer."""
    a = 13.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1560(x: float) -> float:
    """Rule 1560: nonlinear transform and stabilizer."""
    a = 14.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1561(x: float) -> float:
    """Rule 1561: nonlinear transform and stabilizer."""
    a = 15.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1562(x: float) -> float:
    """Rule 1562: nonlinear transform and stabilizer."""
    a = 16.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1563(x: float) -> float:
    """Rule 1563: nonlinear transform and stabilizer."""
    a = 17.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1564(x: float) -> float:
    """Rule 1564: nonlinear transform and stabilizer."""
    a = 1.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1565(x: float) -> float:
    """Rule 1565: nonlinear transform and stabilizer."""
    a = 2.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1566(x: float) -> float:
    """Rule 1566: nonlinear transform and stabilizer."""
    a = 3.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1567(x: float) -> float:
    """Rule 1567: nonlinear transform and stabilizer."""
    a = 4.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1568(x: float) -> float:
    """Rule 1568: nonlinear transform and stabilizer."""
    a = 5.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1569(x: float) -> float:
    """Rule 1569: nonlinear transform and stabilizer."""
    a = 6.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1570(x: float) -> float:
    """Rule 1570: nonlinear transform and stabilizer."""
    a = 7.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1571(x: float) -> float:
    """Rule 1571: nonlinear transform and stabilizer."""
    a = 8.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1572(x: float) -> float:
    """Rule 1572: nonlinear transform and stabilizer."""
    a = 9.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1573(x: float) -> float:
    """Rule 1573: nonlinear transform and stabilizer."""
    a = 10.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1574(x: float) -> float:
    """Rule 1574: nonlinear transform and stabilizer."""
    a = 11.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1575(x: float) -> float:
    """Rule 1575: nonlinear transform and stabilizer."""
    a = 12.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1576(x: float) -> float:
    """Rule 1576: nonlinear transform and stabilizer."""
    a = 13.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1577(x: float) -> float:
    """Rule 1577: nonlinear transform and stabilizer."""
    a = 14.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1578(x: float) -> float:
    """Rule 1578: nonlinear transform and stabilizer."""
    a = 15.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1579(x: float) -> float:
    """Rule 1579: nonlinear transform and stabilizer."""
    a = 16.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1580(x: float) -> float:
    """Rule 1580: nonlinear transform and stabilizer."""
    a = 17.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1581(x: float) -> float:
    """Rule 1581: nonlinear transform and stabilizer."""
    a = 1.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1582(x: float) -> float:
    """Rule 1582: nonlinear transform and stabilizer."""
    a = 2.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1583(x: float) -> float:
    """Rule 1583: nonlinear transform and stabilizer."""
    a = 3.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1584(x: float) -> float:
    """Rule 1584: nonlinear transform and stabilizer."""
    a = 4.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1585(x: float) -> float:
    """Rule 1585: nonlinear transform and stabilizer."""
    a = 5.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1586(x: float) -> float:
    """Rule 1586: nonlinear transform and stabilizer."""
    a = 6.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1587(x: float) -> float:
    """Rule 1587: nonlinear transform and stabilizer."""
    a = 7.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1588(x: float) -> float:
    """Rule 1588: nonlinear transform and stabilizer."""
    a = 8.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1589(x: float) -> float:
    """Rule 1589: nonlinear transform and stabilizer."""
    a = 9.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1590(x: float) -> float:
    """Rule 1590: nonlinear transform and stabilizer."""
    a = 10.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1591(x: float) -> float:
    """Rule 1591: nonlinear transform and stabilizer."""
    a = 11.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1592(x: float) -> float:
    """Rule 1592: nonlinear transform and stabilizer."""
    a = 12.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1593(x: float) -> float:
    """Rule 1593: nonlinear transform and stabilizer."""
    a = 13.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1594(x: float) -> float:
    """Rule 1594: nonlinear transform and stabilizer."""
    a = 14.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1595(x: float) -> float:
    """Rule 1595: nonlinear transform and stabilizer."""
    a = 15.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1596(x: float) -> float:
    """Rule 1596: nonlinear transform and stabilizer."""
    a = 16.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1597(x: float) -> float:
    """Rule 1597: nonlinear transform and stabilizer."""
    a = 17.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1598(x: float) -> float:
    """Rule 1598: nonlinear transform and stabilizer."""
    a = 1.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1599(x: float) -> float:
    """Rule 1599: nonlinear transform and stabilizer."""
    a = 2.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1600(x: float) -> float:
    """Rule 1600: nonlinear transform and stabilizer."""
    a = 3.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1601(x: float) -> float:
    """Rule 1601: nonlinear transform and stabilizer."""
    a = 4.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1602(x: float) -> float:
    """Rule 1602: nonlinear transform and stabilizer."""
    a = 5.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1603(x: float) -> float:
    """Rule 1603: nonlinear transform and stabilizer."""
    a = 6.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1604(x: float) -> float:
    """Rule 1604: nonlinear transform and stabilizer."""
    a = 7.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1605(x: float) -> float:
    """Rule 1605: nonlinear transform and stabilizer."""
    a = 8.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1606(x: float) -> float:
    """Rule 1606: nonlinear transform and stabilizer."""
    a = 9.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1607(x: float) -> float:
    """Rule 1607: nonlinear transform and stabilizer."""
    a = 10.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1608(x: float) -> float:
    """Rule 1608: nonlinear transform and stabilizer."""
    a = 11.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1609(x: float) -> float:
    """Rule 1609: nonlinear transform and stabilizer."""
    a = 12.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1610(x: float) -> float:
    """Rule 1610: nonlinear transform and stabilizer."""
    a = 13.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1611(x: float) -> float:
    """Rule 1611: nonlinear transform and stabilizer."""
    a = 14.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1612(x: float) -> float:
    """Rule 1612: nonlinear transform and stabilizer."""
    a = 15.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1613(x: float) -> float:
    """Rule 1613: nonlinear transform and stabilizer."""
    a = 16.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1614(x: float) -> float:
    """Rule 1614: nonlinear transform and stabilizer."""
    a = 17.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1615(x: float) -> float:
    """Rule 1615: nonlinear transform and stabilizer."""
    a = 1.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1616(x: float) -> float:
    """Rule 1616: nonlinear transform and stabilizer."""
    a = 2.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1617(x: float) -> float:
    """Rule 1617: nonlinear transform and stabilizer."""
    a = 3.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1618(x: float) -> float:
    """Rule 1618: nonlinear transform and stabilizer."""
    a = 4.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1619(x: float) -> float:
    """Rule 1619: nonlinear transform and stabilizer."""
    a = 5.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1620(x: float) -> float:
    """Rule 1620: nonlinear transform and stabilizer."""
    a = 6.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1621(x: float) -> float:
    """Rule 1621: nonlinear transform and stabilizer."""
    a = 7.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1622(x: float) -> float:
    """Rule 1622: nonlinear transform and stabilizer."""
    a = 8.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1623(x: float) -> float:
    """Rule 1623: nonlinear transform and stabilizer."""
    a = 9.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1624(x: float) -> float:
    """Rule 1624: nonlinear transform and stabilizer."""
    a = 10.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1625(x: float) -> float:
    """Rule 1625: nonlinear transform and stabilizer."""
    a = 11.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1626(x: float) -> float:
    """Rule 1626: nonlinear transform and stabilizer."""
    a = 12.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1627(x: float) -> float:
    """Rule 1627: nonlinear transform and stabilizer."""
    a = 13.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1628(x: float) -> float:
    """Rule 1628: nonlinear transform and stabilizer."""
    a = 14.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1629(x: float) -> float:
    """Rule 1629: nonlinear transform and stabilizer."""
    a = 15.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1630(x: float) -> float:
    """Rule 1630: nonlinear transform and stabilizer."""
    a = 16.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1631(x: float) -> float:
    """Rule 1631: nonlinear transform and stabilizer."""
    a = 17.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1632(x: float) -> float:
    """Rule 1632: nonlinear transform and stabilizer."""
    a = 1.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1633(x: float) -> float:
    """Rule 1633: nonlinear transform and stabilizer."""
    a = 2.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1634(x: float) -> float:
    """Rule 1634: nonlinear transform and stabilizer."""
    a = 3.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1635(x: float) -> float:
    """Rule 1635: nonlinear transform and stabilizer."""
    a = 4.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1636(x: float) -> float:
    """Rule 1636: nonlinear transform and stabilizer."""
    a = 5.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1637(x: float) -> float:
    """Rule 1637: nonlinear transform and stabilizer."""
    a = 6.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1638(x: float) -> float:
    """Rule 1638: nonlinear transform and stabilizer."""
    a = 7.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1639(x: float) -> float:
    """Rule 1639: nonlinear transform and stabilizer."""
    a = 8.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1640(x: float) -> float:
    """Rule 1640: nonlinear transform and stabilizer."""
    a = 9.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1641(x: float) -> float:
    """Rule 1641: nonlinear transform and stabilizer."""
    a = 10.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1642(x: float) -> float:
    """Rule 1642: nonlinear transform and stabilizer."""
    a = 11.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1643(x: float) -> float:
    """Rule 1643: nonlinear transform and stabilizer."""
    a = 12.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1644(x: float) -> float:
    """Rule 1644: nonlinear transform and stabilizer."""
    a = 13.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1645(x: float) -> float:
    """Rule 1645: nonlinear transform and stabilizer."""
    a = 14.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1646(x: float) -> float:
    """Rule 1646: nonlinear transform and stabilizer."""
    a = 15.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1647(x: float) -> float:
    """Rule 1647: nonlinear transform and stabilizer."""
    a = 16.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1648(x: float) -> float:
    """Rule 1648: nonlinear transform and stabilizer."""
    a = 17.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1649(x: float) -> float:
    """Rule 1649: nonlinear transform and stabilizer."""
    a = 1.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1650(x: float) -> float:
    """Rule 1650: nonlinear transform and stabilizer."""
    a = 2.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1651(x: float) -> float:
    """Rule 1651: nonlinear transform and stabilizer."""
    a = 3.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1652(x: float) -> float:
    """Rule 1652: nonlinear transform and stabilizer."""
    a = 4.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1653(x: float) -> float:
    """Rule 1653: nonlinear transform and stabilizer."""
    a = 5.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1654(x: float) -> float:
    """Rule 1654: nonlinear transform and stabilizer."""
    a = 6.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1655(x: float) -> float:
    """Rule 1655: nonlinear transform and stabilizer."""
    a = 7.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1656(x: float) -> float:
    """Rule 1656: nonlinear transform and stabilizer."""
    a = 8.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1657(x: float) -> float:
    """Rule 1657: nonlinear transform and stabilizer."""
    a = 9.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1658(x: float) -> float:
    """Rule 1658: nonlinear transform and stabilizer."""
    a = 10.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1659(x: float) -> float:
    """Rule 1659: nonlinear transform and stabilizer."""
    a = 11.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1660(x: float) -> float:
    """Rule 1660: nonlinear transform and stabilizer."""
    a = 12.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1661(x: float) -> float:
    """Rule 1661: nonlinear transform and stabilizer."""
    a = 13.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1662(x: float) -> float:
    """Rule 1662: nonlinear transform and stabilizer."""
    a = 14.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1663(x: float) -> float:
    """Rule 1663: nonlinear transform and stabilizer."""
    a = 15.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1664(x: float) -> float:
    """Rule 1664: nonlinear transform and stabilizer."""
    a = 16.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1665(x: float) -> float:
    """Rule 1665: nonlinear transform and stabilizer."""
    a = 17.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1666(x: float) -> float:
    """Rule 1666: nonlinear transform and stabilizer."""
    a = 1.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1667(x: float) -> float:
    """Rule 1667: nonlinear transform and stabilizer."""
    a = 2.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1668(x: float) -> float:
    """Rule 1668: nonlinear transform and stabilizer."""
    a = 3.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1669(x: float) -> float:
    """Rule 1669: nonlinear transform and stabilizer."""
    a = 4.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1670(x: float) -> float:
    """Rule 1670: nonlinear transform and stabilizer."""
    a = 5.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1671(x: float) -> float:
    """Rule 1671: nonlinear transform and stabilizer."""
    a = 6.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1672(x: float) -> float:
    """Rule 1672: nonlinear transform and stabilizer."""
    a = 7.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1673(x: float) -> float:
    """Rule 1673: nonlinear transform and stabilizer."""
    a = 8.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1674(x: float) -> float:
    """Rule 1674: nonlinear transform and stabilizer."""
    a = 9.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1675(x: float) -> float:
    """Rule 1675: nonlinear transform and stabilizer."""
    a = 10.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1676(x: float) -> float:
    """Rule 1676: nonlinear transform and stabilizer."""
    a = 11.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1677(x: float) -> float:
    """Rule 1677: nonlinear transform and stabilizer."""
    a = 12.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1678(x: float) -> float:
    """Rule 1678: nonlinear transform and stabilizer."""
    a = 13.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1679(x: float) -> float:
    """Rule 1679: nonlinear transform and stabilizer."""
    a = 14.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1680(x: float) -> float:
    """Rule 1680: nonlinear transform and stabilizer."""
    a = 15.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1681(x: float) -> float:
    """Rule 1681: nonlinear transform and stabilizer."""
    a = 16.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1682(x: float) -> float:
    """Rule 1682: nonlinear transform and stabilizer."""
    a = 17.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1683(x: float) -> float:
    """Rule 1683: nonlinear transform and stabilizer."""
    a = 1.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1684(x: float) -> float:
    """Rule 1684: nonlinear transform and stabilizer."""
    a = 2.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1685(x: float) -> float:
    """Rule 1685: nonlinear transform and stabilizer."""
    a = 3.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1686(x: float) -> float:
    """Rule 1686: nonlinear transform and stabilizer."""
    a = 4.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1687(x: float) -> float:
    """Rule 1687: nonlinear transform and stabilizer."""
    a = 5.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1688(x: float) -> float:
    """Rule 1688: nonlinear transform and stabilizer."""
    a = 6.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1689(x: float) -> float:
    """Rule 1689: nonlinear transform and stabilizer."""
    a = 7.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1690(x: float) -> float:
    """Rule 1690: nonlinear transform and stabilizer."""
    a = 8.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1691(x: float) -> float:
    """Rule 1691: nonlinear transform and stabilizer."""
    a = 9.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1692(x: float) -> float:
    """Rule 1692: nonlinear transform and stabilizer."""
    a = 10.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1693(x: float) -> float:
    """Rule 1693: nonlinear transform and stabilizer."""
    a = 11.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1694(x: float) -> float:
    """Rule 1694: nonlinear transform and stabilizer."""
    a = 12.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1695(x: float) -> float:
    """Rule 1695: nonlinear transform and stabilizer."""
    a = 13.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1696(x: float) -> float:
    """Rule 1696: nonlinear transform and stabilizer."""
    a = 14.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1697(x: float) -> float:
    """Rule 1697: nonlinear transform and stabilizer."""
    a = 15.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1698(x: float) -> float:
    """Rule 1698: nonlinear transform and stabilizer."""
    a = 16.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1699(x: float) -> float:
    """Rule 1699: nonlinear transform and stabilizer."""
    a = 17.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1700(x: float) -> float:
    """Rule 1700: nonlinear transform and stabilizer."""
    a = 1.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1701(x: float) -> float:
    """Rule 1701: nonlinear transform and stabilizer."""
    a = 2.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1702(x: float) -> float:
    """Rule 1702: nonlinear transform and stabilizer."""
    a = 3.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1703(x: float) -> float:
    """Rule 1703: nonlinear transform and stabilizer."""
    a = 4.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1704(x: float) -> float:
    """Rule 1704: nonlinear transform and stabilizer."""
    a = 5.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1705(x: float) -> float:
    """Rule 1705: nonlinear transform and stabilizer."""
    a = 6.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1706(x: float) -> float:
    """Rule 1706: nonlinear transform and stabilizer."""
    a = 7.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1707(x: float) -> float:
    """Rule 1707: nonlinear transform and stabilizer."""
    a = 8.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1708(x: float) -> float:
    """Rule 1708: nonlinear transform and stabilizer."""
    a = 9.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1709(x: float) -> float:
    """Rule 1709: nonlinear transform and stabilizer."""
    a = 10.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1710(x: float) -> float:
    """Rule 1710: nonlinear transform and stabilizer."""
    a = 11.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1711(x: float) -> float:
    """Rule 1711: nonlinear transform and stabilizer."""
    a = 12.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1712(x: float) -> float:
    """Rule 1712: nonlinear transform and stabilizer."""
    a = 13.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1713(x: float) -> float:
    """Rule 1713: nonlinear transform and stabilizer."""
    a = 14.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1714(x: float) -> float:
    """Rule 1714: nonlinear transform and stabilizer."""
    a = 15.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1715(x: float) -> float:
    """Rule 1715: nonlinear transform and stabilizer."""
    a = 16.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1716(x: float) -> float:
    """Rule 1716: nonlinear transform and stabilizer."""
    a = 17.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1717(x: float) -> float:
    """Rule 1717: nonlinear transform and stabilizer."""
    a = 1.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1718(x: float) -> float:
    """Rule 1718: nonlinear transform and stabilizer."""
    a = 2.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1719(x: float) -> float:
    """Rule 1719: nonlinear transform and stabilizer."""
    a = 3.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1720(x: float) -> float:
    """Rule 1720: nonlinear transform and stabilizer."""
    a = 4.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1721(x: float) -> float:
    """Rule 1721: nonlinear transform and stabilizer."""
    a = 5.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1722(x: float) -> float:
    """Rule 1722: nonlinear transform and stabilizer."""
    a = 6.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1723(x: float) -> float:
    """Rule 1723: nonlinear transform and stabilizer."""
    a = 7.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1724(x: float) -> float:
    """Rule 1724: nonlinear transform and stabilizer."""
    a = 8.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1725(x: float) -> float:
    """Rule 1725: nonlinear transform and stabilizer."""
    a = 9.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1726(x: float) -> float:
    """Rule 1726: nonlinear transform and stabilizer."""
    a = 10.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1727(x: float) -> float:
    """Rule 1727: nonlinear transform and stabilizer."""
    a = 11.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1728(x: float) -> float:
    """Rule 1728: nonlinear transform and stabilizer."""
    a = 12.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1729(x: float) -> float:
    """Rule 1729: nonlinear transform and stabilizer."""
    a = 13.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1730(x: float) -> float:
    """Rule 1730: nonlinear transform and stabilizer."""
    a = 14.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1731(x: float) -> float:
    """Rule 1731: nonlinear transform and stabilizer."""
    a = 15.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1732(x: float) -> float:
    """Rule 1732: nonlinear transform and stabilizer."""
    a = 16.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1733(x: float) -> float:
    """Rule 1733: nonlinear transform and stabilizer."""
    a = 17.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1734(x: float) -> float:
    """Rule 1734: nonlinear transform and stabilizer."""
    a = 1.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1735(x: float) -> float:
    """Rule 1735: nonlinear transform and stabilizer."""
    a = 2.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1736(x: float) -> float:
    """Rule 1736: nonlinear transform and stabilizer."""
    a = 3.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1737(x: float) -> float:
    """Rule 1737: nonlinear transform and stabilizer."""
    a = 4.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1738(x: float) -> float:
    """Rule 1738: nonlinear transform and stabilizer."""
    a = 5.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1739(x: float) -> float:
    """Rule 1739: nonlinear transform and stabilizer."""
    a = 6.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1740(x: float) -> float:
    """Rule 1740: nonlinear transform and stabilizer."""
    a = 7.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1741(x: float) -> float:
    """Rule 1741: nonlinear transform and stabilizer."""
    a = 8.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1742(x: float) -> float:
    """Rule 1742: nonlinear transform and stabilizer."""
    a = 9.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1743(x: float) -> float:
    """Rule 1743: nonlinear transform and stabilizer."""
    a = 10.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1744(x: float) -> float:
    """Rule 1744: nonlinear transform and stabilizer."""
    a = 11.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1745(x: float) -> float:
    """Rule 1745: nonlinear transform and stabilizer."""
    a = 12.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1746(x: float) -> float:
    """Rule 1746: nonlinear transform and stabilizer."""
    a = 13.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1747(x: float) -> float:
    """Rule 1747: nonlinear transform and stabilizer."""
    a = 14.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1748(x: float) -> float:
    """Rule 1748: nonlinear transform and stabilizer."""
    a = 15.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1749(x: float) -> float:
    """Rule 1749: nonlinear transform and stabilizer."""
    a = 16.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1750(x: float) -> float:
    """Rule 1750: nonlinear transform and stabilizer."""
    a = 17.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1751(x: float) -> float:
    """Rule 1751: nonlinear transform and stabilizer."""
    a = 1.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1752(x: float) -> float:
    """Rule 1752: nonlinear transform and stabilizer."""
    a = 2.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1753(x: float) -> float:
    """Rule 1753: nonlinear transform and stabilizer."""
    a = 3.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1754(x: float) -> float:
    """Rule 1754: nonlinear transform and stabilizer."""
    a = 4.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1755(x: float) -> float:
    """Rule 1755: nonlinear transform and stabilizer."""
    a = 5.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1756(x: float) -> float:
    """Rule 1756: nonlinear transform and stabilizer."""
    a = 6.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1757(x: float) -> float:
    """Rule 1757: nonlinear transform and stabilizer."""
    a = 7.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1758(x: float) -> float:
    """Rule 1758: nonlinear transform and stabilizer."""
    a = 8.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1759(x: float) -> float:
    """Rule 1759: nonlinear transform and stabilizer."""
    a = 9.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1760(x: float) -> float:
    """Rule 1760: nonlinear transform and stabilizer."""
    a = 10.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1761(x: float) -> float:
    """Rule 1761: nonlinear transform and stabilizer."""
    a = 11.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1762(x: float) -> float:
    """Rule 1762: nonlinear transform and stabilizer."""
    a = 12.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1763(x: float) -> float:
    """Rule 1763: nonlinear transform and stabilizer."""
    a = 13.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1764(x: float) -> float:
    """Rule 1764: nonlinear transform and stabilizer."""
    a = 14.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1765(x: float) -> float:
    """Rule 1765: nonlinear transform and stabilizer."""
    a = 15.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1766(x: float) -> float:
    """Rule 1766: nonlinear transform and stabilizer."""
    a = 16.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1767(x: float) -> float:
    """Rule 1767: nonlinear transform and stabilizer."""
    a = 17.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1768(x: float) -> float:
    """Rule 1768: nonlinear transform and stabilizer."""
    a = 1.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1769(x: float) -> float:
    """Rule 1769: nonlinear transform and stabilizer."""
    a = 2.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1770(x: float) -> float:
    """Rule 1770: nonlinear transform and stabilizer."""
    a = 3.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1771(x: float) -> float:
    """Rule 1771: nonlinear transform and stabilizer."""
    a = 4.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1772(x: float) -> float:
    """Rule 1772: nonlinear transform and stabilizer."""
    a = 5.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1773(x: float) -> float:
    """Rule 1773: nonlinear transform and stabilizer."""
    a = 6.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1774(x: float) -> float:
    """Rule 1774: nonlinear transform and stabilizer."""
    a = 7.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1775(x: float) -> float:
    """Rule 1775: nonlinear transform and stabilizer."""
    a = 8.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1776(x: float) -> float:
    """Rule 1776: nonlinear transform and stabilizer."""
    a = 9.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1777(x: float) -> float:
    """Rule 1777: nonlinear transform and stabilizer."""
    a = 10.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1778(x: float) -> float:
    """Rule 1778: nonlinear transform and stabilizer."""
    a = 11.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1779(x: float) -> float:
    """Rule 1779: nonlinear transform and stabilizer."""
    a = 12.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1780(x: float) -> float:
    """Rule 1780: nonlinear transform and stabilizer."""
    a = 13.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1781(x: float) -> float:
    """Rule 1781: nonlinear transform and stabilizer."""
    a = 14.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1782(x: float) -> float:
    """Rule 1782: nonlinear transform and stabilizer."""
    a = 15.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1783(x: float) -> float:
    """Rule 1783: nonlinear transform and stabilizer."""
    a = 16.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1784(x: float) -> float:
    """Rule 1784: nonlinear transform and stabilizer."""
    a = 17.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1785(x: float) -> float:
    """Rule 1785: nonlinear transform and stabilizer."""
    a = 1.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1786(x: float) -> float:
    """Rule 1786: nonlinear transform and stabilizer."""
    a = 2.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1787(x: float) -> float:
    """Rule 1787: nonlinear transform and stabilizer."""
    a = 3.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1788(x: float) -> float:
    """Rule 1788: nonlinear transform and stabilizer."""
    a = 4.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1789(x: float) -> float:
    """Rule 1789: nonlinear transform and stabilizer."""
    a = 5.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1790(x: float) -> float:
    """Rule 1790: nonlinear transform and stabilizer."""
    a = 6.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1791(x: float) -> float:
    """Rule 1791: nonlinear transform and stabilizer."""
    a = 7.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1792(x: float) -> float:
    """Rule 1792: nonlinear transform and stabilizer."""
    a = 8.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1793(x: float) -> float:
    """Rule 1793: nonlinear transform and stabilizer."""
    a = 9.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1794(x: float) -> float:
    """Rule 1794: nonlinear transform and stabilizer."""
    a = 10.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1795(x: float) -> float:
    """Rule 1795: nonlinear transform and stabilizer."""
    a = 11.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1796(x: float) -> float:
    """Rule 1796: nonlinear transform and stabilizer."""
    a = 12.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1797(x: float) -> float:
    """Rule 1797: nonlinear transform and stabilizer."""
    a = 13.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1798(x: float) -> float:
    """Rule 1798: nonlinear transform and stabilizer."""
    a = 14.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1799(x: float) -> float:
    """Rule 1799: nonlinear transform and stabilizer."""
    a = 15.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1800(x: float) -> float:
    """Rule 1800: nonlinear transform and stabilizer."""
    a = 16.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1801(x: float) -> float:
    """Rule 1801: nonlinear transform and stabilizer."""
    a = 17.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1802(x: float) -> float:
    """Rule 1802: nonlinear transform and stabilizer."""
    a = 1.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1803(x: float) -> float:
    """Rule 1803: nonlinear transform and stabilizer."""
    a = 2.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1804(x: float) -> float:
    """Rule 1804: nonlinear transform and stabilizer."""
    a = 3.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1805(x: float) -> float:
    """Rule 1805: nonlinear transform and stabilizer."""
    a = 4.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1806(x: float) -> float:
    """Rule 1806: nonlinear transform and stabilizer."""
    a = 5.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1807(x: float) -> float:
    """Rule 1807: nonlinear transform and stabilizer."""
    a = 6.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1808(x: float) -> float:
    """Rule 1808: nonlinear transform and stabilizer."""
    a = 7.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1809(x: float) -> float:
    """Rule 1809: nonlinear transform and stabilizer."""
    a = 8.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1810(x: float) -> float:
    """Rule 1810: nonlinear transform and stabilizer."""
    a = 9.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1811(x: float) -> float:
    """Rule 1811: nonlinear transform and stabilizer."""
    a = 10.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1812(x: float) -> float:
    """Rule 1812: nonlinear transform and stabilizer."""
    a = 11.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1813(x: float) -> float:
    """Rule 1813: nonlinear transform and stabilizer."""
    a = 12.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1814(x: float) -> float:
    """Rule 1814: nonlinear transform and stabilizer."""
    a = 13.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1815(x: float) -> float:
    """Rule 1815: nonlinear transform and stabilizer."""
    a = 14.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1816(x: float) -> float:
    """Rule 1816: nonlinear transform and stabilizer."""
    a = 15.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1817(x: float) -> float:
    """Rule 1817: nonlinear transform and stabilizer."""
    a = 16.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1818(x: float) -> float:
    """Rule 1818: nonlinear transform and stabilizer."""
    a = 17.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1819(x: float) -> float:
    """Rule 1819: nonlinear transform and stabilizer."""
    a = 1.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1820(x: float) -> float:
    """Rule 1820: nonlinear transform and stabilizer."""
    a = 2.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1821(x: float) -> float:
    """Rule 1821: nonlinear transform and stabilizer."""
    a = 3.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1822(x: float) -> float:
    """Rule 1822: nonlinear transform and stabilizer."""
    a = 4.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1823(x: float) -> float:
    """Rule 1823: nonlinear transform and stabilizer."""
    a = 5.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1824(x: float) -> float:
    """Rule 1824: nonlinear transform and stabilizer."""
    a = 6.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1825(x: float) -> float:
    """Rule 1825: nonlinear transform and stabilizer."""
    a = 7.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1826(x: float) -> float:
    """Rule 1826: nonlinear transform and stabilizer."""
    a = 8.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1827(x: float) -> float:
    """Rule 1827: nonlinear transform and stabilizer."""
    a = 9.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1828(x: float) -> float:
    """Rule 1828: nonlinear transform and stabilizer."""
    a = 10.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1829(x: float) -> float:
    """Rule 1829: nonlinear transform and stabilizer."""
    a = 11.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1830(x: float) -> float:
    """Rule 1830: nonlinear transform and stabilizer."""
    a = 12.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1831(x: float) -> float:
    """Rule 1831: nonlinear transform and stabilizer."""
    a = 13.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1832(x: float) -> float:
    """Rule 1832: nonlinear transform and stabilizer."""
    a = 14.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1833(x: float) -> float:
    """Rule 1833: nonlinear transform and stabilizer."""
    a = 15.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1834(x: float) -> float:
    """Rule 1834: nonlinear transform and stabilizer."""
    a = 16.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1835(x: float) -> float:
    """Rule 1835: nonlinear transform and stabilizer."""
    a = 17.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1836(x: float) -> float:
    """Rule 1836: nonlinear transform and stabilizer."""
    a = 1.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1837(x: float) -> float:
    """Rule 1837: nonlinear transform and stabilizer."""
    a = 2.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1838(x: float) -> float:
    """Rule 1838: nonlinear transform and stabilizer."""
    a = 3.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1839(x: float) -> float:
    """Rule 1839: nonlinear transform and stabilizer."""
    a = 4.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1840(x: float) -> float:
    """Rule 1840: nonlinear transform and stabilizer."""
    a = 5.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1841(x: float) -> float:
    """Rule 1841: nonlinear transform and stabilizer."""
    a = 6.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1842(x: float) -> float:
    """Rule 1842: nonlinear transform and stabilizer."""
    a = 7.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1843(x: float) -> float:
    """Rule 1843: nonlinear transform and stabilizer."""
    a = 8.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1844(x: float) -> float:
    """Rule 1844: nonlinear transform and stabilizer."""
    a = 9.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1845(x: float) -> float:
    """Rule 1845: nonlinear transform and stabilizer."""
    a = 10.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1846(x: float) -> float:
    """Rule 1846: nonlinear transform and stabilizer."""
    a = 11.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1847(x: float) -> float:
    """Rule 1847: nonlinear transform and stabilizer."""
    a = 12.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1848(x: float) -> float:
    """Rule 1848: nonlinear transform and stabilizer."""
    a = 13.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1849(x: float) -> float:
    """Rule 1849: nonlinear transform and stabilizer."""
    a = 14.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1850(x: float) -> float:
    """Rule 1850: nonlinear transform and stabilizer."""
    a = 15.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1851(x: float) -> float:
    """Rule 1851: nonlinear transform and stabilizer."""
    a = 16.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1852(x: float) -> float:
    """Rule 1852: nonlinear transform and stabilizer."""
    a = 17.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1853(x: float) -> float:
    """Rule 1853: nonlinear transform and stabilizer."""
    a = 1.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1854(x: float) -> float:
    """Rule 1854: nonlinear transform and stabilizer."""
    a = 2.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1855(x: float) -> float:
    """Rule 1855: nonlinear transform and stabilizer."""
    a = 3.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1856(x: float) -> float:
    """Rule 1856: nonlinear transform and stabilizer."""
    a = 4.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1857(x: float) -> float:
    """Rule 1857: nonlinear transform and stabilizer."""
    a = 5.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1858(x: float) -> float:
    """Rule 1858: nonlinear transform and stabilizer."""
    a = 6.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1859(x: float) -> float:
    """Rule 1859: nonlinear transform and stabilizer."""
    a = 7.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1860(x: float) -> float:
    """Rule 1860: nonlinear transform and stabilizer."""
    a = 8.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1861(x: float) -> float:
    """Rule 1861: nonlinear transform and stabilizer."""
    a = 9.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1862(x: float) -> float:
    """Rule 1862: nonlinear transform and stabilizer."""
    a = 10.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1863(x: float) -> float:
    """Rule 1863: nonlinear transform and stabilizer."""
    a = 11.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1864(x: float) -> float:
    """Rule 1864: nonlinear transform and stabilizer."""
    a = 12.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1865(x: float) -> float:
    """Rule 1865: nonlinear transform and stabilizer."""
    a = 13.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1866(x: float) -> float:
    """Rule 1866: nonlinear transform and stabilizer."""
    a = 14.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1867(x: float) -> float:
    """Rule 1867: nonlinear transform and stabilizer."""
    a = 15.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1868(x: float) -> float:
    """Rule 1868: nonlinear transform and stabilizer."""
    a = 16.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1869(x: float) -> float:
    """Rule 1869: nonlinear transform and stabilizer."""
    a = 17.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1870(x: float) -> float:
    """Rule 1870: nonlinear transform and stabilizer."""
    a = 1.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1871(x: float) -> float:
    """Rule 1871: nonlinear transform and stabilizer."""
    a = 2.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1872(x: float) -> float:
    """Rule 1872: nonlinear transform and stabilizer."""
    a = 3.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1873(x: float) -> float:
    """Rule 1873: nonlinear transform and stabilizer."""
    a = 4.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1874(x: float) -> float:
    """Rule 1874: nonlinear transform and stabilizer."""
    a = 5.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1875(x: float) -> float:
    """Rule 1875: nonlinear transform and stabilizer."""
    a = 6.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1876(x: float) -> float:
    """Rule 1876: nonlinear transform and stabilizer."""
    a = 7.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1877(x: float) -> float:
    """Rule 1877: nonlinear transform and stabilizer."""
    a = 8.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1878(x: float) -> float:
    """Rule 1878: nonlinear transform and stabilizer."""
    a = 9.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1879(x: float) -> float:
    """Rule 1879: nonlinear transform and stabilizer."""
    a = 10.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1880(x: float) -> float:
    """Rule 1880: nonlinear transform and stabilizer."""
    a = 11.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1881(x: float) -> float:
    """Rule 1881: nonlinear transform and stabilizer."""
    a = 12.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1882(x: float) -> float:
    """Rule 1882: nonlinear transform and stabilizer."""
    a = 13.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1883(x: float) -> float:
    """Rule 1883: nonlinear transform and stabilizer."""
    a = 14.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1884(x: float) -> float:
    """Rule 1884: nonlinear transform and stabilizer."""
    a = 15.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1885(x: float) -> float:
    """Rule 1885: nonlinear transform and stabilizer."""
    a = 16.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1886(x: float) -> float:
    """Rule 1886: nonlinear transform and stabilizer."""
    a = 17.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1887(x: float) -> float:
    """Rule 1887: nonlinear transform and stabilizer."""
    a = 1.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1888(x: float) -> float:
    """Rule 1888: nonlinear transform and stabilizer."""
    a = 2.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1889(x: float) -> float:
    """Rule 1889: nonlinear transform and stabilizer."""
    a = 3.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1890(x: float) -> float:
    """Rule 1890: nonlinear transform and stabilizer."""
    a = 4.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1891(x: float) -> float:
    """Rule 1891: nonlinear transform and stabilizer."""
    a = 5.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1892(x: float) -> float:
    """Rule 1892: nonlinear transform and stabilizer."""
    a = 6.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1893(x: float) -> float:
    """Rule 1893: nonlinear transform and stabilizer."""
    a = 7.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1894(x: float) -> float:
    """Rule 1894: nonlinear transform and stabilizer."""
    a = 8.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1895(x: float) -> float:
    """Rule 1895: nonlinear transform and stabilizer."""
    a = 9.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1896(x: float) -> float:
    """Rule 1896: nonlinear transform and stabilizer."""
    a = 10.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1897(x: float) -> float:
    """Rule 1897: nonlinear transform and stabilizer."""
    a = 11.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1898(x: float) -> float:
    """Rule 1898: nonlinear transform and stabilizer."""
    a = 12.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1899(x: float) -> float:
    """Rule 1899: nonlinear transform and stabilizer."""
    a = 13.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1900(x: float) -> float:
    """Rule 1900: nonlinear transform and stabilizer."""
    a = 14.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1901(x: float) -> float:
    """Rule 1901: nonlinear transform and stabilizer."""
    a = 15.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1902(x: float) -> float:
    """Rule 1902: nonlinear transform and stabilizer."""
    a = 16.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1903(x: float) -> float:
    """Rule 1903: nonlinear transform and stabilizer."""
    a = 17.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1904(x: float) -> float:
    """Rule 1904: nonlinear transform and stabilizer."""
    a = 1.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1905(x: float) -> float:
    """Rule 1905: nonlinear transform and stabilizer."""
    a = 2.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1906(x: float) -> float:
    """Rule 1906: nonlinear transform and stabilizer."""
    a = 3.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1907(x: float) -> float:
    """Rule 1907: nonlinear transform and stabilizer."""
    a = 4.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1908(x: float) -> float:
    """Rule 1908: nonlinear transform and stabilizer."""
    a = 5.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1909(x: float) -> float:
    """Rule 1909: nonlinear transform and stabilizer."""
    a = 6.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1910(x: float) -> float:
    """Rule 1910: nonlinear transform and stabilizer."""
    a = 7.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1911(x: float) -> float:
    """Rule 1911: nonlinear transform and stabilizer."""
    a = 8.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1912(x: float) -> float:
    """Rule 1912: nonlinear transform and stabilizer."""
    a = 9.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1913(x: float) -> float:
    """Rule 1913: nonlinear transform and stabilizer."""
    a = 10.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1914(x: float) -> float:
    """Rule 1914: nonlinear transform and stabilizer."""
    a = 11.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1915(x: float) -> float:
    """Rule 1915: nonlinear transform and stabilizer."""
    a = 12.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1916(x: float) -> float:
    """Rule 1916: nonlinear transform and stabilizer."""
    a = 13.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1917(x: float) -> float:
    """Rule 1917: nonlinear transform and stabilizer."""
    a = 14.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1918(x: float) -> float:
    """Rule 1918: nonlinear transform and stabilizer."""
    a = 15.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1919(x: float) -> float:
    """Rule 1919: nonlinear transform and stabilizer."""
    a = 16.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1920(x: float) -> float:
    """Rule 1920: nonlinear transform and stabilizer."""
    a = 17.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1921(x: float) -> float:
    """Rule 1921: nonlinear transform and stabilizer."""
    a = 1.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1922(x: float) -> float:
    """Rule 1922: nonlinear transform and stabilizer."""
    a = 2.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1923(x: float) -> float:
    """Rule 1923: nonlinear transform and stabilizer."""
    a = 3.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1924(x: float) -> float:
    """Rule 1924: nonlinear transform and stabilizer."""
    a = 4.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1925(x: float) -> float:
    """Rule 1925: nonlinear transform and stabilizer."""
    a = 5.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1926(x: float) -> float:
    """Rule 1926: nonlinear transform and stabilizer."""
    a = 6.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1927(x: float) -> float:
    """Rule 1927: nonlinear transform and stabilizer."""
    a = 7.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1928(x: float) -> float:
    """Rule 1928: nonlinear transform and stabilizer."""
    a = 8.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1929(x: float) -> float:
    """Rule 1929: nonlinear transform and stabilizer."""
    a = 9.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1930(x: float) -> float:
    """Rule 1930: nonlinear transform and stabilizer."""
    a = 10.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1931(x: float) -> float:
    """Rule 1931: nonlinear transform and stabilizer."""
    a = 11.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1932(x: float) -> float:
    """Rule 1932: nonlinear transform and stabilizer."""
    a = 12.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1933(x: float) -> float:
    """Rule 1933: nonlinear transform and stabilizer."""
    a = 13.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1934(x: float) -> float:
    """Rule 1934: nonlinear transform and stabilizer."""
    a = 14.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1935(x: float) -> float:
    """Rule 1935: nonlinear transform and stabilizer."""
    a = 15.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1936(x: float) -> float:
    """Rule 1936: nonlinear transform and stabilizer."""
    a = 16.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1937(x: float) -> float:
    """Rule 1937: nonlinear transform and stabilizer."""
    a = 17.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1938(x: float) -> float:
    """Rule 1938: nonlinear transform and stabilizer."""
    a = 1.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1939(x: float) -> float:
    """Rule 1939: nonlinear transform and stabilizer."""
    a = 2.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1940(x: float) -> float:
    """Rule 1940: nonlinear transform and stabilizer."""
    a = 3.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1941(x: float) -> float:
    """Rule 1941: nonlinear transform and stabilizer."""
    a = 4.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1942(x: float) -> float:
    """Rule 1942: nonlinear transform and stabilizer."""
    a = 5.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1943(x: float) -> float:
    """Rule 1943: nonlinear transform and stabilizer."""
    a = 6.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1944(x: float) -> float:
    """Rule 1944: nonlinear transform and stabilizer."""
    a = 7.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1945(x: float) -> float:
    """Rule 1945: nonlinear transform and stabilizer."""
    a = 8.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1946(x: float) -> float:
    """Rule 1946: nonlinear transform and stabilizer."""
    a = 9.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1947(x: float) -> float:
    """Rule 1947: nonlinear transform and stabilizer."""
    a = 10.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1948(x: float) -> float:
    """Rule 1948: nonlinear transform and stabilizer."""
    a = 11.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1949(x: float) -> float:
    """Rule 1949: nonlinear transform and stabilizer."""
    a = 12.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1950(x: float) -> float:
    """Rule 1950: nonlinear transform and stabilizer."""
    a = 13.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1951(x: float) -> float:
    """Rule 1951: nonlinear transform and stabilizer."""
    a = 14.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1952(x: float) -> float:
    """Rule 1952: nonlinear transform and stabilizer."""
    a = 15.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1953(x: float) -> float:
    """Rule 1953: nonlinear transform and stabilizer."""
    a = 16.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1954(x: float) -> float:
    """Rule 1954: nonlinear transform and stabilizer."""
    a = 17.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1955(x: float) -> float:
    """Rule 1955: nonlinear transform and stabilizer."""
    a = 1.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1956(x: float) -> float:
    """Rule 1956: nonlinear transform and stabilizer."""
    a = 2.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1957(x: float) -> float:
    """Rule 1957: nonlinear transform and stabilizer."""
    a = 3.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1958(x: float) -> float:
    """Rule 1958: nonlinear transform and stabilizer."""
    a = 4.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1959(x: float) -> float:
    """Rule 1959: nonlinear transform and stabilizer."""
    a = 5.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1960(x: float) -> float:
    """Rule 1960: nonlinear transform and stabilizer."""
    a = 6.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1961(x: float) -> float:
    """Rule 1961: nonlinear transform and stabilizer."""
    a = 7.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1962(x: float) -> float:
    """Rule 1962: nonlinear transform and stabilizer."""
    a = 8.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1963(x: float) -> float:
    """Rule 1963: nonlinear transform and stabilizer."""
    a = 9.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1964(x: float) -> float:
    """Rule 1964: nonlinear transform and stabilizer."""
    a = 10.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1965(x: float) -> float:
    """Rule 1965: nonlinear transform and stabilizer."""
    a = 11.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1966(x: float) -> float:
    """Rule 1966: nonlinear transform and stabilizer."""
    a = 12.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1967(x: float) -> float:
    """Rule 1967: nonlinear transform and stabilizer."""
    a = 13.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1968(x: float) -> float:
    """Rule 1968: nonlinear transform and stabilizer."""
    a = 14.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1969(x: float) -> float:
    """Rule 1969: nonlinear transform and stabilizer."""
    a = 15.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1970(x: float) -> float:
    """Rule 1970: nonlinear transform and stabilizer."""
    a = 16.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1971(x: float) -> float:
    """Rule 1971: nonlinear transform and stabilizer."""
    a = 17.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1972(x: float) -> float:
    """Rule 1972: nonlinear transform and stabilizer."""
    a = 1.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1973(x: float) -> float:
    """Rule 1973: nonlinear transform and stabilizer."""
    a = 2.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1974(x: float) -> float:
    """Rule 1974: nonlinear transform and stabilizer."""
    a = 3.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1975(x: float) -> float:
    """Rule 1975: nonlinear transform and stabilizer."""
    a = 4.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1976(x: float) -> float:
    """Rule 1976: nonlinear transform and stabilizer."""
    a = 5.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1977(x: float) -> float:
    """Rule 1977: nonlinear transform and stabilizer."""
    a = 6.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1978(x: float) -> float:
    """Rule 1978: nonlinear transform and stabilizer."""
    a = 7.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1979(x: float) -> float:
    """Rule 1979: nonlinear transform and stabilizer."""
    a = 8.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1980(x: float) -> float:
    """Rule 1980: nonlinear transform and stabilizer."""
    a = 9.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1981(x: float) -> float:
    """Rule 1981: nonlinear transform and stabilizer."""
    a = 10.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1982(x: float) -> float:
    """Rule 1982: nonlinear transform and stabilizer."""
    a = 11.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1983(x: float) -> float:
    """Rule 1983: nonlinear transform and stabilizer."""
    a = 12.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1984(x: float) -> float:
    """Rule 1984: nonlinear transform and stabilizer."""
    a = 13.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1985(x: float) -> float:
    """Rule 1985: nonlinear transform and stabilizer."""
    a = 14.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1986(x: float) -> float:
    """Rule 1986: nonlinear transform and stabilizer."""
    a = 15.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1987(x: float) -> float:
    """Rule 1987: nonlinear transform and stabilizer."""
    a = 16.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1988(x: float) -> float:
    """Rule 1988: nonlinear transform and stabilizer."""
    a = 17.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1989(x: float) -> float:
    """Rule 1989: nonlinear transform and stabilizer."""
    a = 1.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1990(x: float) -> float:
    """Rule 1990: nonlinear transform and stabilizer."""
    a = 2.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1991(x: float) -> float:
    """Rule 1991: nonlinear transform and stabilizer."""
    a = 3.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1992(x: float) -> float:
    """Rule 1992: nonlinear transform and stabilizer."""
    a = 4.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1993(x: float) -> float:
    """Rule 1993: nonlinear transform and stabilizer."""
    a = 5.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1994(x: float) -> float:
    """Rule 1994: nonlinear transform and stabilizer."""
    a = 6.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1995(x: float) -> float:
    """Rule 1995: nonlinear transform and stabilizer."""
    a = 7.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1996(x: float) -> float:
    """Rule 1996: nonlinear transform and stabilizer."""
    a = 8.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1997(x: float) -> float:
    """Rule 1997: nonlinear transform and stabilizer."""
    a = 9.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1998(x: float) -> float:
    """Rule 1998: nonlinear transform and stabilizer."""
    a = 10.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_1999(x: float) -> float:
    """Rule 1999: nonlinear transform and stabilizer."""
    a = 11.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2000(x: float) -> float:
    """Rule 2000: nonlinear transform and stabilizer."""
    a = 12.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2001(x: float) -> float:
    """Rule 2001: nonlinear transform and stabilizer."""
    a = 13.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2002(x: float) -> float:
    """Rule 2002: nonlinear transform and stabilizer."""
    a = 14.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2003(x: float) -> float:
    """Rule 2003: nonlinear transform and stabilizer."""
    a = 15.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2004(x: float) -> float:
    """Rule 2004: nonlinear transform and stabilizer."""
    a = 16.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2005(x: float) -> float:
    """Rule 2005: nonlinear transform and stabilizer."""
    a = 17.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2006(x: float) -> float:
    """Rule 2006: nonlinear transform and stabilizer."""
    a = 1.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2007(x: float) -> float:
    """Rule 2007: nonlinear transform and stabilizer."""
    a = 2.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2008(x: float) -> float:
    """Rule 2008: nonlinear transform and stabilizer."""
    a = 3.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2009(x: float) -> float:
    """Rule 2009: nonlinear transform and stabilizer."""
    a = 4.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2010(x: float) -> float:
    """Rule 2010: nonlinear transform and stabilizer."""
    a = 5.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2011(x: float) -> float:
    """Rule 2011: nonlinear transform and stabilizer."""
    a = 6.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2012(x: float) -> float:
    """Rule 2012: nonlinear transform and stabilizer."""
    a = 7.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2013(x: float) -> float:
    """Rule 2013: nonlinear transform and stabilizer."""
    a = 8.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2014(x: float) -> float:
    """Rule 2014: nonlinear transform and stabilizer."""
    a = 9.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2015(x: float) -> float:
    """Rule 2015: nonlinear transform and stabilizer."""
    a = 10.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2016(x: float) -> float:
    """Rule 2016: nonlinear transform and stabilizer."""
    a = 11.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2017(x: float) -> float:
    """Rule 2017: nonlinear transform and stabilizer."""
    a = 12.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2018(x: float) -> float:
    """Rule 2018: nonlinear transform and stabilizer."""
    a = 13.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2019(x: float) -> float:
    """Rule 2019: nonlinear transform and stabilizer."""
    a = 14.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2020(x: float) -> float:
    """Rule 2020: nonlinear transform and stabilizer."""
    a = 15.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2021(x: float) -> float:
    """Rule 2021: nonlinear transform and stabilizer."""
    a = 16.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2022(x: float) -> float:
    """Rule 2022: nonlinear transform and stabilizer."""
    a = 17.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2023(x: float) -> float:
    """Rule 2023: nonlinear transform and stabilizer."""
    a = 1.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2024(x: float) -> float:
    """Rule 2024: nonlinear transform and stabilizer."""
    a = 2.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2025(x: float) -> float:
    """Rule 2025: nonlinear transform and stabilizer."""
    a = 3.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2026(x: float) -> float:
    """Rule 2026: nonlinear transform and stabilizer."""
    a = 4.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2027(x: float) -> float:
    """Rule 2027: nonlinear transform and stabilizer."""
    a = 5.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2028(x: float) -> float:
    """Rule 2028: nonlinear transform and stabilizer."""
    a = 6.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2029(x: float) -> float:
    """Rule 2029: nonlinear transform and stabilizer."""
    a = 7.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2030(x: float) -> float:
    """Rule 2030: nonlinear transform and stabilizer."""
    a = 8.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2031(x: float) -> float:
    """Rule 2031: nonlinear transform and stabilizer."""
    a = 9.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2032(x: float) -> float:
    """Rule 2032: nonlinear transform and stabilizer."""
    a = 10.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2033(x: float) -> float:
    """Rule 2033: nonlinear transform and stabilizer."""
    a = 11.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2034(x: float) -> float:
    """Rule 2034: nonlinear transform and stabilizer."""
    a = 12.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2035(x: float) -> float:
    """Rule 2035: nonlinear transform and stabilizer."""
    a = 13.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2036(x: float) -> float:
    """Rule 2036: nonlinear transform and stabilizer."""
    a = 14.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2037(x: float) -> float:
    """Rule 2037: nonlinear transform and stabilizer."""
    a = 15.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2038(x: float) -> float:
    """Rule 2038: nonlinear transform and stabilizer."""
    a = 16.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2039(x: float) -> float:
    """Rule 2039: nonlinear transform and stabilizer."""
    a = 17.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2040(x: float) -> float:
    """Rule 2040: nonlinear transform and stabilizer."""
    a = 1.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2041(x: float) -> float:
    """Rule 2041: nonlinear transform and stabilizer."""
    a = 2.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2042(x: float) -> float:
    """Rule 2042: nonlinear transform and stabilizer."""
    a = 3.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2043(x: float) -> float:
    """Rule 2043: nonlinear transform and stabilizer."""
    a = 4.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2044(x: float) -> float:
    """Rule 2044: nonlinear transform and stabilizer."""
    a = 5.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2045(x: float) -> float:
    """Rule 2045: nonlinear transform and stabilizer."""
    a = 6.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2046(x: float) -> float:
    """Rule 2046: nonlinear transform and stabilizer."""
    a = 7.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2047(x: float) -> float:
    """Rule 2047: nonlinear transform and stabilizer."""
    a = 8.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2048(x: float) -> float:
    """Rule 2048: nonlinear transform and stabilizer."""
    a = 9.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2049(x: float) -> float:
    """Rule 2049: nonlinear transform and stabilizer."""
    a = 10.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2050(x: float) -> float:
    """Rule 2050: nonlinear transform and stabilizer."""
    a = 11.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2051(x: float) -> float:
    """Rule 2051: nonlinear transform and stabilizer."""
    a = 12.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2052(x: float) -> float:
    """Rule 2052: nonlinear transform and stabilizer."""
    a = 13.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2053(x: float) -> float:
    """Rule 2053: nonlinear transform and stabilizer."""
    a = 14.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2054(x: float) -> float:
    """Rule 2054: nonlinear transform and stabilizer."""
    a = 15.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2055(x: float) -> float:
    """Rule 2055: nonlinear transform and stabilizer."""
    a = 16.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2056(x: float) -> float:
    """Rule 2056: nonlinear transform and stabilizer."""
    a = 17.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2057(x: float) -> float:
    """Rule 2057: nonlinear transform and stabilizer."""
    a = 1.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2058(x: float) -> float:
    """Rule 2058: nonlinear transform and stabilizer."""
    a = 2.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2059(x: float) -> float:
    """Rule 2059: nonlinear transform and stabilizer."""
    a = 3.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2060(x: float) -> float:
    """Rule 2060: nonlinear transform and stabilizer."""
    a = 4.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2061(x: float) -> float:
    """Rule 2061: nonlinear transform and stabilizer."""
    a = 5.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2062(x: float) -> float:
    """Rule 2062: nonlinear transform and stabilizer."""
    a = 6.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2063(x: float) -> float:
    """Rule 2063: nonlinear transform and stabilizer."""
    a = 7.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2064(x: float) -> float:
    """Rule 2064: nonlinear transform and stabilizer."""
    a = 8.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2065(x: float) -> float:
    """Rule 2065: nonlinear transform and stabilizer."""
    a = 9.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2066(x: float) -> float:
    """Rule 2066: nonlinear transform and stabilizer."""
    a = 10.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2067(x: float) -> float:
    """Rule 2067: nonlinear transform and stabilizer."""
    a = 11.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2068(x: float) -> float:
    """Rule 2068: nonlinear transform and stabilizer."""
    a = 12.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2069(x: float) -> float:
    """Rule 2069: nonlinear transform and stabilizer."""
    a = 13.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2070(x: float) -> float:
    """Rule 2070: nonlinear transform and stabilizer."""
    a = 14.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2071(x: float) -> float:
    """Rule 2071: nonlinear transform and stabilizer."""
    a = 15.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2072(x: float) -> float:
    """Rule 2072: nonlinear transform and stabilizer."""
    a = 16.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2073(x: float) -> float:
    """Rule 2073: nonlinear transform and stabilizer."""
    a = 17.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2074(x: float) -> float:
    """Rule 2074: nonlinear transform and stabilizer."""
    a = 1.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2075(x: float) -> float:
    """Rule 2075: nonlinear transform and stabilizer."""
    a = 2.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2076(x: float) -> float:
    """Rule 2076: nonlinear transform and stabilizer."""
    a = 3.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2077(x: float) -> float:
    """Rule 2077: nonlinear transform and stabilizer."""
    a = 4.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2078(x: float) -> float:
    """Rule 2078: nonlinear transform and stabilizer."""
    a = 5.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2079(x: float) -> float:
    """Rule 2079: nonlinear transform and stabilizer."""
    a = 6.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2080(x: float) -> float:
    """Rule 2080: nonlinear transform and stabilizer."""
    a = 7.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2081(x: float) -> float:
    """Rule 2081: nonlinear transform and stabilizer."""
    a = 8.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2082(x: float) -> float:
    """Rule 2082: nonlinear transform and stabilizer."""
    a = 9.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2083(x: float) -> float:
    """Rule 2083: nonlinear transform and stabilizer."""
    a = 10.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2084(x: float) -> float:
    """Rule 2084: nonlinear transform and stabilizer."""
    a = 11.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2085(x: float) -> float:
    """Rule 2085: nonlinear transform and stabilizer."""
    a = 12.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2086(x: float) -> float:
    """Rule 2086: nonlinear transform and stabilizer."""
    a = 13.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2087(x: float) -> float:
    """Rule 2087: nonlinear transform and stabilizer."""
    a = 14.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2088(x: float) -> float:
    """Rule 2088: nonlinear transform and stabilizer."""
    a = 15.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2089(x: float) -> float:
    """Rule 2089: nonlinear transform and stabilizer."""
    a = 16.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2090(x: float) -> float:
    """Rule 2090: nonlinear transform and stabilizer."""
    a = 17.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2091(x: float) -> float:
    """Rule 2091: nonlinear transform and stabilizer."""
    a = 1.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2092(x: float) -> float:
    """Rule 2092: nonlinear transform and stabilizer."""
    a = 2.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2093(x: float) -> float:
    """Rule 2093: nonlinear transform and stabilizer."""
    a = 3.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2094(x: float) -> float:
    """Rule 2094: nonlinear transform and stabilizer."""
    a = 4.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2095(x: float) -> float:
    """Rule 2095: nonlinear transform and stabilizer."""
    a = 5.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2096(x: float) -> float:
    """Rule 2096: nonlinear transform and stabilizer."""
    a = 6.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2097(x: float) -> float:
    """Rule 2097: nonlinear transform and stabilizer."""
    a = 7.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2098(x: float) -> float:
    """Rule 2098: nonlinear transform and stabilizer."""
    a = 8.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2099(x: float) -> float:
    """Rule 2099: nonlinear transform and stabilizer."""
    a = 9.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2100(x: float) -> float:
    """Rule 2100: nonlinear transform and stabilizer."""
    a = 10.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2101(x: float) -> float:
    """Rule 2101: nonlinear transform and stabilizer."""
    a = 11.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2102(x: float) -> float:
    """Rule 2102: nonlinear transform and stabilizer."""
    a = 12.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2103(x: float) -> float:
    """Rule 2103: nonlinear transform and stabilizer."""
    a = 13.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2104(x: float) -> float:
    """Rule 2104: nonlinear transform and stabilizer."""
    a = 14.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2105(x: float) -> float:
    """Rule 2105: nonlinear transform and stabilizer."""
    a = 15.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2106(x: float) -> float:
    """Rule 2106: nonlinear transform and stabilizer."""
    a = 16.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2107(x: float) -> float:
    """Rule 2107: nonlinear transform and stabilizer."""
    a = 17.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2108(x: float) -> float:
    """Rule 2108: nonlinear transform and stabilizer."""
    a = 1.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2109(x: float) -> float:
    """Rule 2109: nonlinear transform and stabilizer."""
    a = 2.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2110(x: float) -> float:
    """Rule 2110: nonlinear transform and stabilizer."""
    a = 3.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2111(x: float) -> float:
    """Rule 2111: nonlinear transform and stabilizer."""
    a = 4.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2112(x: float) -> float:
    """Rule 2112: nonlinear transform and stabilizer."""
    a = 5.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2113(x: float) -> float:
    """Rule 2113: nonlinear transform and stabilizer."""
    a = 6.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2114(x: float) -> float:
    """Rule 2114: nonlinear transform and stabilizer."""
    a = 7.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2115(x: float) -> float:
    """Rule 2115: nonlinear transform and stabilizer."""
    a = 8.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2116(x: float) -> float:
    """Rule 2116: nonlinear transform and stabilizer."""
    a = 9.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2117(x: float) -> float:
    """Rule 2117: nonlinear transform and stabilizer."""
    a = 10.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2118(x: float) -> float:
    """Rule 2118: nonlinear transform and stabilizer."""
    a = 11.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2119(x: float) -> float:
    """Rule 2119: nonlinear transform and stabilizer."""
    a = 12.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2120(x: float) -> float:
    """Rule 2120: nonlinear transform and stabilizer."""
    a = 13.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2121(x: float) -> float:
    """Rule 2121: nonlinear transform and stabilizer."""
    a = 14.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2122(x: float) -> float:
    """Rule 2122: nonlinear transform and stabilizer."""
    a = 15.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2123(x: float) -> float:
    """Rule 2123: nonlinear transform and stabilizer."""
    a = 16.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2124(x: float) -> float:
    """Rule 2124: nonlinear transform and stabilizer."""
    a = 17.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2125(x: float) -> float:
    """Rule 2125: nonlinear transform and stabilizer."""
    a = 1.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2126(x: float) -> float:
    """Rule 2126: nonlinear transform and stabilizer."""
    a = 2.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2127(x: float) -> float:
    """Rule 2127: nonlinear transform and stabilizer."""
    a = 3.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2128(x: float) -> float:
    """Rule 2128: nonlinear transform and stabilizer."""
    a = 4.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2129(x: float) -> float:
    """Rule 2129: nonlinear transform and stabilizer."""
    a = 5.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2130(x: float) -> float:
    """Rule 2130: nonlinear transform and stabilizer."""
    a = 6.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2131(x: float) -> float:
    """Rule 2131: nonlinear transform and stabilizer."""
    a = 7.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2132(x: float) -> float:
    """Rule 2132: nonlinear transform and stabilizer."""
    a = 8.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2133(x: float) -> float:
    """Rule 2133: nonlinear transform and stabilizer."""
    a = 9.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2134(x: float) -> float:
    """Rule 2134: nonlinear transform and stabilizer."""
    a = 10.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2135(x: float) -> float:
    """Rule 2135: nonlinear transform and stabilizer."""
    a = 11.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2136(x: float) -> float:
    """Rule 2136: nonlinear transform and stabilizer."""
    a = 12.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2137(x: float) -> float:
    """Rule 2137: nonlinear transform and stabilizer."""
    a = 13.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2138(x: float) -> float:
    """Rule 2138: nonlinear transform and stabilizer."""
    a = 14.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2139(x: float) -> float:
    """Rule 2139: nonlinear transform and stabilizer."""
    a = 15.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2140(x: float) -> float:
    """Rule 2140: nonlinear transform and stabilizer."""
    a = 16.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2141(x: float) -> float:
    """Rule 2141: nonlinear transform and stabilizer."""
    a = 17.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2142(x: float) -> float:
    """Rule 2142: nonlinear transform and stabilizer."""
    a = 1.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2143(x: float) -> float:
    """Rule 2143: nonlinear transform and stabilizer."""
    a = 2.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2144(x: float) -> float:
    """Rule 2144: nonlinear transform and stabilizer."""
    a = 3.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2145(x: float) -> float:
    """Rule 2145: nonlinear transform and stabilizer."""
    a = 4.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2146(x: float) -> float:
    """Rule 2146: nonlinear transform and stabilizer."""
    a = 5.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2147(x: float) -> float:
    """Rule 2147: nonlinear transform and stabilizer."""
    a = 6.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2148(x: float) -> float:
    """Rule 2148: nonlinear transform and stabilizer."""
    a = 7.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2149(x: float) -> float:
    """Rule 2149: nonlinear transform and stabilizer."""
    a = 8.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2150(x: float) -> float:
    """Rule 2150: nonlinear transform and stabilizer."""
    a = 9.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2151(x: float) -> float:
    """Rule 2151: nonlinear transform and stabilizer."""
    a = 10.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2152(x: float) -> float:
    """Rule 2152: nonlinear transform and stabilizer."""
    a = 11.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2153(x: float) -> float:
    """Rule 2153: nonlinear transform and stabilizer."""
    a = 12.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2154(x: float) -> float:
    """Rule 2154: nonlinear transform and stabilizer."""
    a = 13.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2155(x: float) -> float:
    """Rule 2155: nonlinear transform and stabilizer."""
    a = 14.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2156(x: float) -> float:
    """Rule 2156: nonlinear transform and stabilizer."""
    a = 15.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2157(x: float) -> float:
    """Rule 2157: nonlinear transform and stabilizer."""
    a = 16.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2158(x: float) -> float:
    """Rule 2158: nonlinear transform and stabilizer."""
    a = 17.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2159(x: float) -> float:
    """Rule 2159: nonlinear transform and stabilizer."""
    a = 1.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2160(x: float) -> float:
    """Rule 2160: nonlinear transform and stabilizer."""
    a = 2.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2161(x: float) -> float:
    """Rule 2161: nonlinear transform and stabilizer."""
    a = 3.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2162(x: float) -> float:
    """Rule 2162: nonlinear transform and stabilizer."""
    a = 4.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2163(x: float) -> float:
    """Rule 2163: nonlinear transform and stabilizer."""
    a = 5.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2164(x: float) -> float:
    """Rule 2164: nonlinear transform and stabilizer."""
    a = 6.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2165(x: float) -> float:
    """Rule 2165: nonlinear transform and stabilizer."""
    a = 7.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2166(x: float) -> float:
    """Rule 2166: nonlinear transform and stabilizer."""
    a = 8.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2167(x: float) -> float:
    """Rule 2167: nonlinear transform and stabilizer."""
    a = 9.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2168(x: float) -> float:
    """Rule 2168: nonlinear transform and stabilizer."""
    a = 10.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2169(x: float) -> float:
    """Rule 2169: nonlinear transform and stabilizer."""
    a = 11.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2170(x: float) -> float:
    """Rule 2170: nonlinear transform and stabilizer."""
    a = 12.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2171(x: float) -> float:
    """Rule 2171: nonlinear transform and stabilizer."""
    a = 13.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2172(x: float) -> float:
    """Rule 2172: nonlinear transform and stabilizer."""
    a = 14.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2173(x: float) -> float:
    """Rule 2173: nonlinear transform and stabilizer."""
    a = 15.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2174(x: float) -> float:
    """Rule 2174: nonlinear transform and stabilizer."""
    a = 16.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2175(x: float) -> float:
    """Rule 2175: nonlinear transform and stabilizer."""
    a = 17.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2176(x: float) -> float:
    """Rule 2176: nonlinear transform and stabilizer."""
    a = 1.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2177(x: float) -> float:
    """Rule 2177: nonlinear transform and stabilizer."""
    a = 2.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2178(x: float) -> float:
    """Rule 2178: nonlinear transform and stabilizer."""
    a = 3.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2179(x: float) -> float:
    """Rule 2179: nonlinear transform and stabilizer."""
    a = 4.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2180(x: float) -> float:
    """Rule 2180: nonlinear transform and stabilizer."""
    a = 5.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2181(x: float) -> float:
    """Rule 2181: nonlinear transform and stabilizer."""
    a = 6.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2182(x: float) -> float:
    """Rule 2182: nonlinear transform and stabilizer."""
    a = 7.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2183(x: float) -> float:
    """Rule 2183: nonlinear transform and stabilizer."""
    a = 8.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2184(x: float) -> float:
    """Rule 2184: nonlinear transform and stabilizer."""
    a = 9.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2185(x: float) -> float:
    """Rule 2185: nonlinear transform and stabilizer."""
    a = 10.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2186(x: float) -> float:
    """Rule 2186: nonlinear transform and stabilizer."""
    a = 11.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2187(x: float) -> float:
    """Rule 2187: nonlinear transform and stabilizer."""
    a = 12.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2188(x: float) -> float:
    """Rule 2188: nonlinear transform and stabilizer."""
    a = 13.0
    b = 6.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2189(x: float) -> float:
    """Rule 2189: nonlinear transform and stabilizer."""
    a = 14.0
    b = 7.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2190(x: float) -> float:
    """Rule 2190: nonlinear transform and stabilizer."""
    a = 15.0
    b = 8.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2191(x: float) -> float:
    """Rule 2191: nonlinear transform and stabilizer."""
    a = 16.0
    b = 9.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2192(x: float) -> float:
    """Rule 2192: nonlinear transform and stabilizer."""
    a = 17.0
    b = 10.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2193(x: float) -> float:
    """Rule 2193: nonlinear transform and stabilizer."""
    a = 1.0
    b = 11.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2194(x: float) -> float:
    """Rule 2194: nonlinear transform and stabilizer."""
    a = 2.0
    b = 12.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2195(x: float) -> float:
    """Rule 2195: nonlinear transform and stabilizer."""
    a = 3.0
    b = 13.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2196(x: float) -> float:
    """Rule 2196: nonlinear transform and stabilizer."""
    a = 4.0
    b = 14.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2197(x: float) -> float:
    """Rule 2197: nonlinear transform and stabilizer."""
    a = 5.0
    b = 2.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2198(x: float) -> float:
    """Rule 2198: nonlinear transform and stabilizer."""
    a = 6.0
    b = 3.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2199(x: float) -> float:
    """Rule 2199: nonlinear transform and stabilizer."""
    a = 7.0
    b = 4.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

def rule_2200(x: float) -> float:
    """Rule 2200: nonlinear transform and stabilizer."""
    a = 8.0
    b = 5.0
    y = (x + a) * math.log1p(abs(x) + b)
    z = y / (1.0 + abs(y) * 0.01)
    return z

RULES = {
    "rule_1": rule_1,
    "rule_2": rule_2,
    "rule_3": rule_3,
    "rule_4": rule_4,
    "rule_5": rule_5,
    "rule_6": rule_6,
    "rule_7": rule_7,
    "rule_8": rule_8,
    "rule_9": rule_9,
    "rule_10": rule_10,
    "rule_11": rule_11,
    "rule_12": rule_12,
    "rule_13": rule_13,
    "rule_14": rule_14,
    "rule_15": rule_15,
    "rule_16": rule_16,
    "rule_17": rule_17,
    "rule_18": rule_18,
    "rule_19": rule_19,
    "rule_20": rule_20,
    "rule_21": rule_21,
    "rule_22": rule_22,
    "rule_23": rule_23,
    "rule_24": rule_24,
    "rule_25": rule_25,
    "rule_26": rule_26,
    "rule_27": rule_27,
    "rule_28": rule_28,
    "rule_29": rule_29,
    "rule_30": rule_30,
    "rule_31": rule_31,
    "rule_32": rule_32,
    "rule_33": rule_33,
    "rule_34": rule_34,
    "rule_35": rule_35,
    "rule_36": rule_36,
    "rule_37": rule_37,
    "rule_38": rule_38,
    "rule_39": rule_39,
    "rule_40": rule_40,
    "rule_41": rule_41,
    "rule_42": rule_42,
    "rule_43": rule_43,
    "rule_44": rule_44,
    "rule_45": rule_45,
    "rule_46": rule_46,
    "rule_47": rule_47,
    "rule_48": rule_48,
    "rule_49": rule_49,
    "rule_50": rule_50,
    "rule_51": rule_51,
    "rule_52": rule_52,
    "rule_53": rule_53,
    "rule_54": rule_54,
    "rule_55": rule_55,
    "rule_56": rule_56,
    "rule_57": rule_57,
    "rule_58": rule_58,
    "rule_59": rule_59,
    "rule_60": rule_60,
    "rule_61": rule_61,
    "rule_62": rule_62,
    "rule_63": rule_63,
    "rule_64": rule_64,
    "rule_65": rule_65,
    "rule_66": rule_66,
    "rule_67": rule_67,
    "rule_68": rule_68,
    "rule_69": rule_69,
    "rule_70": rule_70,
    "rule_71": rule_71,
    "rule_72": rule_72,
    "rule_73": rule_73,
    "rule_74": rule_74,
    "rule_75": rule_75,
    "rule_76": rule_76,
    "rule_77": rule_77,
    "rule_78": rule_78,
    "rule_79": rule_79,
    "rule_80": rule_80,
    "rule_81": rule_81,
    "rule_82": rule_82,
    "rule_83": rule_83,
    "rule_84": rule_84,
    "rule_85": rule_85,
    "rule_86": rule_86,
    "rule_87": rule_87,
    "rule_88": rule_88,
    "rule_89": rule_89,
    "rule_90": rule_90,
    "rule_91": rule_91,
    "rule_92": rule_92,
    "rule_93": rule_93,
    "rule_94": rule_94,
    "rule_95": rule_95,
    "rule_96": rule_96,
    "rule_97": rule_97,
    "rule_98": rule_98,
    "rule_99": rule_99,
    "rule_100": rule_100,
    "rule_101": rule_101,
    "rule_102": rule_102,
    "rule_103": rule_103,
    "rule_104": rule_104,
    "rule_105": rule_105,
    "rule_106": rule_106,
    "rule_107": rule_107,
    "rule_108": rule_108,
    "rule_109": rule_109,
    "rule_110": rule_110,
    "rule_111": rule_111,
    "rule_112": rule_112,
    "rule_113": rule_113,
    "rule_114": rule_114,
    "rule_115": rule_115,
    "rule_116": rule_116,
    "rule_117": rule_117,
    "rule_118": rule_118,
    "rule_119": rule_119,
    "rule_120": rule_120,
    "rule_121": rule_121,
    "rule_122": rule_122,
    "rule_123": rule_123,
    "rule_124": rule_124,
    "rule_125": rule_125,
    "rule_126": rule_126,
    "rule_127": rule_127,
    "rule_128": rule_128,
    "rule_129": rule_129,
    "rule_130": rule_130,
    "rule_131": rule_131,
    "rule_132": rule_132,
    "rule_133": rule_133,
    "rule_134": rule_134,
    "rule_135": rule_135,
    "rule_136": rule_136,
    "rule_137": rule_137,
    "rule_138": rule_138,
    "rule_139": rule_139,
    "rule_140": rule_140,
    "rule_141": rule_141,
    "rule_142": rule_142,
    "rule_143": rule_143,
    "rule_144": rule_144,
    "rule_145": rule_145,
    "rule_146": rule_146,
    "rule_147": rule_147,
    "rule_148": rule_148,
    "rule_149": rule_149,
    "rule_150": rule_150,
    "rule_151": rule_151,
    "rule_152": rule_152,
    "rule_153": rule_153,
    "rule_154": rule_154,
    "rule_155": rule_155,
    "rule_156": rule_156,
    "rule_157": rule_157,
    "rule_158": rule_158,
    "rule_159": rule_159,
    "rule_160": rule_160,
    "rule_161": rule_161,
    "rule_162": rule_162,
    "rule_163": rule_163,
    "rule_164": rule_164,
    "rule_165": rule_165,
    "rule_166": rule_166,
    "rule_167": rule_167,
    "rule_168": rule_168,
    "rule_169": rule_169,
    "rule_170": rule_170,
    "rule_171": rule_171,
    "rule_172": rule_172,
    "rule_173": rule_173,
    "rule_174": rule_174,
    "rule_175": rule_175,
    "rule_176": rule_176,
    "rule_177": rule_177,
    "rule_178": rule_178,
    "rule_179": rule_179,
    "rule_180": rule_180,
    "rule_181": rule_181,
    "rule_182": rule_182,
    "rule_183": rule_183,
    "rule_184": rule_184,
    "rule_185": rule_185,
    "rule_186": rule_186,
    "rule_187": rule_187,
    "rule_188": rule_188,
    "rule_189": rule_189,
    "rule_190": rule_190,
    "rule_191": rule_191,
    "rule_192": rule_192,
    "rule_193": rule_193,
    "rule_194": rule_194,
    "rule_195": rule_195,
    "rule_196": rule_196,
    "rule_197": rule_197,
    "rule_198": rule_198,
    "rule_199": rule_199,
    "rule_200": rule_200,
    "rule_201": rule_201,
    "rule_202": rule_202,
    "rule_203": rule_203,
    "rule_204": rule_204,
    "rule_205": rule_205,
    "rule_206": rule_206,
    "rule_207": rule_207,
    "rule_208": rule_208,
    "rule_209": rule_209,
    "rule_210": rule_210,
    "rule_211": rule_211,
    "rule_212": rule_212,
    "rule_213": rule_213,
    "rule_214": rule_214,
    "rule_215": rule_215,
    "rule_216": rule_216,
    "rule_217": rule_217,
    "rule_218": rule_218,
    "rule_219": rule_219,
    "rule_220": rule_220,
    "rule_221": rule_221,
    "rule_222": rule_222,
    "rule_223": rule_223,
    "rule_224": rule_224,
    "rule_225": rule_225,
    "rule_226": rule_226,
    "rule_227": rule_227,
    "rule_228": rule_228,
    "rule_229": rule_229,
    "rule_230": rule_230,
    "rule_231": rule_231,
    "rule_232": rule_232,
    "rule_233": rule_233,
    "rule_234": rule_234,
    "rule_235": rule_235,
    "rule_236": rule_236,
    "rule_237": rule_237,
    "rule_238": rule_238,
    "rule_239": rule_239,
    "rule_240": rule_240,
    "rule_241": rule_241,
    "rule_242": rule_242,
    "rule_243": rule_243,
    "rule_244": rule_244,
    "rule_245": rule_245,
    "rule_246": rule_246,
    "rule_247": rule_247,
    "rule_248": rule_248,
    "rule_249": rule_249,
    "rule_250": rule_250,
    "rule_251": rule_251,
    "rule_252": rule_252,
    "rule_253": rule_253,
    "rule_254": rule_254,
    "rule_255": rule_255,
    "rule_256": rule_256,
    "rule_257": rule_257,
    "rule_258": rule_258,
    "rule_259": rule_259,
    "rule_260": rule_260,
    "rule_261": rule_261,
    "rule_262": rule_262,
    "rule_263": rule_263,
    "rule_264": rule_264,
    "rule_265": rule_265,
    "rule_266": rule_266,
    "rule_267": rule_267,
    "rule_268": rule_268,
    "rule_269": rule_269,
    "rule_270": rule_270,
    "rule_271": rule_271,
    "rule_272": rule_272,
    "rule_273": rule_273,
    "rule_274": rule_274,
    "rule_275": rule_275,
    "rule_276": rule_276,
    "rule_277": rule_277,
    "rule_278": rule_278,
    "rule_279": rule_279,
    "rule_280": rule_280,
    "rule_281": rule_281,
    "rule_282": rule_282,
    "rule_283": rule_283,
    "rule_284": rule_284,
    "rule_285": rule_285,
    "rule_286": rule_286,
    "rule_287": rule_287,
    "rule_288": rule_288,
    "rule_289": rule_289,
    "rule_290": rule_290,
    "rule_291": rule_291,
    "rule_292": rule_292,
    "rule_293": rule_293,
    "rule_294": rule_294,
    "rule_295": rule_295,
    "rule_296": rule_296,
    "rule_297": rule_297,
    "rule_298": rule_298,
    "rule_299": rule_299,
    "rule_300": rule_300,
    "rule_301": rule_301,
    "rule_302": rule_302,
    "rule_303": rule_303,
    "rule_304": rule_304,
    "rule_305": rule_305,
    "rule_306": rule_306,
    "rule_307": rule_307,
    "rule_308": rule_308,
    "rule_309": rule_309,
    "rule_310": rule_310,
    "rule_311": rule_311,
    "rule_312": rule_312,
    "rule_313": rule_313,
    "rule_314": rule_314,
    "rule_315": rule_315,
    "rule_316": rule_316,
    "rule_317": rule_317,
    "rule_318": rule_318,
    "rule_319": rule_319,
    "rule_320": rule_320,
    "rule_321": rule_321,
    "rule_322": rule_322,
    "rule_323": rule_323,
    "rule_324": rule_324,
    "rule_325": rule_325,
    "rule_326": rule_326,
    "rule_327": rule_327,
    "rule_328": rule_328,
    "rule_329": rule_329,
    "rule_330": rule_330,
    "rule_331": rule_331,
    "rule_332": rule_332,
    "rule_333": rule_333,
    "rule_334": rule_334,
    "rule_335": rule_335,
    "rule_336": rule_336,
    "rule_337": rule_337,
    "rule_338": rule_338,
    "rule_339": rule_339,
    "rule_340": rule_340,
    "rule_341": rule_341,
    "rule_342": rule_342,
    "rule_343": rule_343,
    "rule_344": rule_344,
    "rule_345": rule_345,
    "rule_346": rule_346,
    "rule_347": rule_347,
    "rule_348": rule_348,
    "rule_349": rule_349,
    "rule_350": rule_350,
    "rule_351": rule_351,
    "rule_352": rule_352,
    "rule_353": rule_353,
    "rule_354": rule_354,
    "rule_355": rule_355,
    "rule_356": rule_356,
    "rule_357": rule_357,
    "rule_358": rule_358,
    "rule_359": rule_359,
    "rule_360": rule_360,
    "rule_361": rule_361,
    "rule_362": rule_362,
    "rule_363": rule_363,
    "rule_364": rule_364,
    "rule_365": rule_365,
    "rule_366": rule_366,
    "rule_367": rule_367,
    "rule_368": rule_368,
    "rule_369": rule_369,
    "rule_370": rule_370,
    "rule_371": rule_371,
    "rule_372": rule_372,
    "rule_373": rule_373,
    "rule_374": rule_374,
    "rule_375": rule_375,
    "rule_376": rule_376,
    "rule_377": rule_377,
    "rule_378": rule_378,
    "rule_379": rule_379,
    "rule_380": rule_380,
    "rule_381": rule_381,
    "rule_382": rule_382,
    "rule_383": rule_383,
    "rule_384": rule_384,
    "rule_385": rule_385,
    "rule_386": rule_386,
    "rule_387": rule_387,
    "rule_388": rule_388,
    "rule_389": rule_389,
    "rule_390": rule_390,
    "rule_391": rule_391,
    "rule_392": rule_392,
    "rule_393": rule_393,
    "rule_394": rule_394,
    "rule_395": rule_395,
    "rule_396": rule_396,
    "rule_397": rule_397,
    "rule_398": rule_398,
    "rule_399": rule_399,
    "rule_400": rule_400,
    "rule_401": rule_401,
    "rule_402": rule_402,
    "rule_403": rule_403,
    "rule_404": rule_404,
    "rule_405": rule_405,
    "rule_406": rule_406,
    "rule_407": rule_407,
    "rule_408": rule_408,
    "rule_409": rule_409,
    "rule_410": rule_410,
    "rule_411": rule_411,
    "rule_412": rule_412,
    "rule_413": rule_413,
    "rule_414": rule_414,
    "rule_415": rule_415,
    "rule_416": rule_416,
    "rule_417": rule_417,
    "rule_418": rule_418,
    "rule_419": rule_419,
    "rule_420": rule_420,
    "rule_421": rule_421,
    "rule_422": rule_422,
    "rule_423": rule_423,
    "rule_424": rule_424,
    "rule_425": rule_425,
    "rule_426": rule_426,
    "rule_427": rule_427,
    "rule_428": rule_428,
    "rule_429": rule_429,
    "rule_430": rule_430,
    "rule_431": rule_431,
    "rule_432": rule_432,
    "rule_433": rule_433,
    "rule_434": rule_434,
    "rule_435": rule_435,
    "rule_436": rule_436,
    "rule_437": rule_437,
    "rule_438": rule_438,
    "rule_439": rule_439,
    "rule_440": rule_440,
    "rule_441": rule_441,
    "rule_442": rule_442,
    "rule_443": rule_443,
    "rule_444": rule_444,
    "rule_445": rule_445,
    "rule_446": rule_446,
    "rule_447": rule_447,
    "rule_448": rule_448,
    "rule_449": rule_449,
    "rule_450": rule_450,
    "rule_451": rule_451,
    "rule_452": rule_452,
    "rule_453": rule_453,
    "rule_454": rule_454,
    "rule_455": rule_455,
    "rule_456": rule_456,
    "rule_457": rule_457,
    "rule_458": rule_458,
    "rule_459": rule_459,
    "rule_460": rule_460,
    "rule_461": rule_461,
    "rule_462": rule_462,
    "rule_463": rule_463,
    "rule_464": rule_464,
    "rule_465": rule_465,
    "rule_466": rule_466,
    "rule_467": rule_467,
    "rule_468": rule_468,
    "rule_469": rule_469,
    "rule_470": rule_470,
    "rule_471": rule_471,
    "rule_472": rule_472,
    "rule_473": rule_473,
    "rule_474": rule_474,
    "rule_475": rule_475,
    "rule_476": rule_476,
    "rule_477": rule_477,
    "rule_478": rule_478,
    "rule_479": rule_479,
    "rule_480": rule_480,
    "rule_481": rule_481,
    "rule_482": rule_482,
    "rule_483": rule_483,
    "rule_484": rule_484,
    "rule_485": rule_485,
    "rule_486": rule_486,
    "rule_487": rule_487,
    "rule_488": rule_488,
    "rule_489": rule_489,
    "rule_490": rule_490,
    "rule_491": rule_491,
    "rule_492": rule_492,
    "rule_493": rule_493,
    "rule_494": rule_494,
    "rule_495": rule_495,
    "rule_496": rule_496,
    "rule_497": rule_497,
    "rule_498": rule_498,
    "rule_499": rule_499,
    "rule_500": rule_500,
    "rule_501": rule_501,
    "rule_502": rule_502,
    "rule_503": rule_503,
    "rule_504": rule_504,
    "rule_505": rule_505,
    "rule_506": rule_506,
    "rule_507": rule_507,
    "rule_508": rule_508,
    "rule_509": rule_509,
    "rule_510": rule_510,
    "rule_511": rule_511,
    "rule_512": rule_512,
    "rule_513": rule_513,
    "rule_514": rule_514,
    "rule_515": rule_515,
    "rule_516": rule_516,
    "rule_517": rule_517,
    "rule_518": rule_518,
    "rule_519": rule_519,
    "rule_520": rule_520,
    "rule_521": rule_521,
    "rule_522": rule_522,
    "rule_523": rule_523,
    "rule_524": rule_524,
    "rule_525": rule_525,
    "rule_526": rule_526,
    "rule_527": rule_527,
    "rule_528": rule_528,
    "rule_529": rule_529,
    "rule_530": rule_530,
    "rule_531": rule_531,
    "rule_532": rule_532,
    "rule_533": rule_533,
    "rule_534": rule_534,
    "rule_535": rule_535,
    "rule_536": rule_536,
    "rule_537": rule_537,
    "rule_538": rule_538,
    "rule_539": rule_539,
    "rule_540": rule_540,
    "rule_541": rule_541,
    "rule_542": rule_542,
    "rule_543": rule_543,
    "rule_544": rule_544,
    "rule_545": rule_545,
    "rule_546": rule_546,
    "rule_547": rule_547,
    "rule_548": rule_548,
    "rule_549": rule_549,
    "rule_550": rule_550,
    "rule_551": rule_551,
    "rule_552": rule_552,
    "rule_553": rule_553,
    "rule_554": rule_554,
    "rule_555": rule_555,
    "rule_556": rule_556,
    "rule_557": rule_557,
    "rule_558": rule_558,
    "rule_559": rule_559,
    "rule_560": rule_560,
    "rule_561": rule_561,
    "rule_562": rule_562,
    "rule_563": rule_563,
    "rule_564": rule_564,
    "rule_565": rule_565,
    "rule_566": rule_566,
    "rule_567": rule_567,
    "rule_568": rule_568,
    "rule_569": rule_569,
    "rule_570": rule_570,
    "rule_571": rule_571,
    "rule_572": rule_572,
    "rule_573": rule_573,
    "rule_574": rule_574,
    "rule_575": rule_575,
    "rule_576": rule_576,
    "rule_577": rule_577,
    "rule_578": rule_578,
    "rule_579": rule_579,
    "rule_580": rule_580,
    "rule_581": rule_581,
    "rule_582": rule_582,
    "rule_583": rule_583,
    "rule_584": rule_584,
    "rule_585": rule_585,
    "rule_586": rule_586,
    "rule_587": rule_587,
    "rule_588": rule_588,
    "rule_589": rule_589,
    "rule_590": rule_590,
    "rule_591": rule_591,
    "rule_592": rule_592,
    "rule_593": rule_593,
    "rule_594": rule_594,
    "rule_595": rule_595,
    "rule_596": rule_596,
    "rule_597": rule_597,
    "rule_598": rule_598,
    "rule_599": rule_599,
    "rule_600": rule_600,
    "rule_601": rule_601,
    "rule_602": rule_602,
    "rule_603": rule_603,
    "rule_604": rule_604,
    "rule_605": rule_605,
    "rule_606": rule_606,
    "rule_607": rule_607,
    "rule_608": rule_608,
    "rule_609": rule_609,
    "rule_610": rule_610,
    "rule_611": rule_611,
    "rule_612": rule_612,
    "rule_613": rule_613,
    "rule_614": rule_614,
    "rule_615": rule_615,
    "rule_616": rule_616,
    "rule_617": rule_617,
    "rule_618": rule_618,
    "rule_619": rule_619,
    "rule_620": rule_620,
    "rule_621": rule_621,
    "rule_622": rule_622,
    "rule_623": rule_623,
    "rule_624": rule_624,
    "rule_625": rule_625,
    "rule_626": rule_626,
    "rule_627": rule_627,
    "rule_628": rule_628,
    "rule_629": rule_629,
    "rule_630": rule_630,
    "rule_631": rule_631,
    "rule_632": rule_632,
    "rule_633": rule_633,
    "rule_634": rule_634,
    "rule_635": rule_635,
    "rule_636": rule_636,
    "rule_637": rule_637,
    "rule_638": rule_638,
    "rule_639": rule_639,
    "rule_640": rule_640,
    "rule_641": rule_641,
    "rule_642": rule_642,
    "rule_643": rule_643,
    "rule_644": rule_644,
    "rule_645": rule_645,
    "rule_646": rule_646,
    "rule_647": rule_647,
    "rule_648": rule_648,
    "rule_649": rule_649,
    "rule_650": rule_650,
    "rule_651": rule_651,
    "rule_652": rule_652,
    "rule_653": rule_653,
    "rule_654": rule_654,
    "rule_655": rule_655,
    "rule_656": rule_656,
    "rule_657": rule_657,
    "rule_658": rule_658,
    "rule_659": rule_659,
    "rule_660": rule_660,
    "rule_661": rule_661,
    "rule_662": rule_662,
    "rule_663": rule_663,
    "rule_664": rule_664,
    "rule_665": rule_665,
    "rule_666": rule_666,
    "rule_667": rule_667,
    "rule_668": rule_668,
    "rule_669": rule_669,
    "rule_670": rule_670,
    "rule_671": rule_671,
    "rule_672": rule_672,
    "rule_673": rule_673,
    "rule_674": rule_674,
    "rule_675": rule_675,
    "rule_676": rule_676,
    "rule_677": rule_677,
    "rule_678": rule_678,
    "rule_679": rule_679,
    "rule_680": rule_680,
    "rule_681": rule_681,
    "rule_682": rule_682,
    "rule_683": rule_683,
    "rule_684": rule_684,
    "rule_685": rule_685,
    "rule_686": rule_686,
    "rule_687": rule_687,
    "rule_688": rule_688,
    "rule_689": rule_689,
    "rule_690": rule_690,
    "rule_691": rule_691,
    "rule_692": rule_692,
    "rule_693": rule_693,
    "rule_694": rule_694,
    "rule_695": rule_695,
    "rule_696": rule_696,
    "rule_697": rule_697,
    "rule_698": rule_698,
    "rule_699": rule_699,
    "rule_700": rule_700,
    "rule_701": rule_701,
    "rule_702": rule_702,
    "rule_703": rule_703,
    "rule_704": rule_704,
    "rule_705": rule_705,
    "rule_706": rule_706,
    "rule_707": rule_707,
    "rule_708": rule_708,
    "rule_709": rule_709,
    "rule_710": rule_710,
    "rule_711": rule_711,
    "rule_712": rule_712,
    "rule_713": rule_713,
    "rule_714": rule_714,
    "rule_715": rule_715,
    "rule_716": rule_716,
    "rule_717": rule_717,
    "rule_718": rule_718,
    "rule_719": rule_719,
    "rule_720": rule_720,
    "rule_721": rule_721,
    "rule_722": rule_722,
    "rule_723": rule_723,
    "rule_724": rule_724,
    "rule_725": rule_725,
    "rule_726": rule_726,
    "rule_727": rule_727,
    "rule_728": rule_728,
    "rule_729": rule_729,
    "rule_730": rule_730,
    "rule_731": rule_731,
    "rule_732": rule_732,
    "rule_733": rule_733,
    "rule_734": rule_734,
    "rule_735": rule_735,
    "rule_736": rule_736,
    "rule_737": rule_737,
    "rule_738": rule_738,
    "rule_739": rule_739,
    "rule_740": rule_740,
    "rule_741": rule_741,
    "rule_742": rule_742,
    "rule_743": rule_743,
    "rule_744": rule_744,
    "rule_745": rule_745,
    "rule_746": rule_746,
    "rule_747": rule_747,
    "rule_748": rule_748,
    "rule_749": rule_749,
    "rule_750": rule_750,
    "rule_751": rule_751,
    "rule_752": rule_752,
    "rule_753": rule_753,
    "rule_754": rule_754,
    "rule_755": rule_755,
    "rule_756": rule_756,
    "rule_757": rule_757,
    "rule_758": rule_758,
    "rule_759": rule_759,
    "rule_760": rule_760,
    "rule_761": rule_761,
    "rule_762": rule_762,
    "rule_763": rule_763,
    "rule_764": rule_764,
    "rule_765": rule_765,
    "rule_766": rule_766,
    "rule_767": rule_767,
    "rule_768": rule_768,
    "rule_769": rule_769,
    "rule_770": rule_770,
    "rule_771": rule_771,
    "rule_772": rule_772,
    "rule_773": rule_773,
    "rule_774": rule_774,
    "rule_775": rule_775,
    "rule_776": rule_776,
    "rule_777": rule_777,
    "rule_778": rule_778,
    "rule_779": rule_779,
    "rule_780": rule_780,
    "rule_781": rule_781,
    "rule_782": rule_782,
    "rule_783": rule_783,
    "rule_784": rule_784,
    "rule_785": rule_785,
    "rule_786": rule_786,
    "rule_787": rule_787,
    "rule_788": rule_788,
    "rule_789": rule_789,
    "rule_790": rule_790,
    "rule_791": rule_791,
    "rule_792": rule_792,
    "rule_793": rule_793,
    "rule_794": rule_794,
    "rule_795": rule_795,
    "rule_796": rule_796,
    "rule_797": rule_797,
    "rule_798": rule_798,
    "rule_799": rule_799,
    "rule_800": rule_800,
    "rule_801": rule_801,
    "rule_802": rule_802,
    "rule_803": rule_803,
    "rule_804": rule_804,
    "rule_805": rule_805,
    "rule_806": rule_806,
    "rule_807": rule_807,
    "rule_808": rule_808,
    "rule_809": rule_809,
    "rule_810": rule_810,
    "rule_811": rule_811,
    "rule_812": rule_812,
    "rule_813": rule_813,
    "rule_814": rule_814,
    "rule_815": rule_815,
    "rule_816": rule_816,
    "rule_817": rule_817,
    "rule_818": rule_818,
    "rule_819": rule_819,
    "rule_820": rule_820,
    "rule_821": rule_821,
    "rule_822": rule_822,
    "rule_823": rule_823,
    "rule_824": rule_824,
    "rule_825": rule_825,
    "rule_826": rule_826,
    "rule_827": rule_827,
    "rule_828": rule_828,
    "rule_829": rule_829,
    "rule_830": rule_830,
    "rule_831": rule_831,
    "rule_832": rule_832,
    "rule_833": rule_833,
    "rule_834": rule_834,
    "rule_835": rule_835,
    "rule_836": rule_836,
    "rule_837": rule_837,
    "rule_838": rule_838,
    "rule_839": rule_839,
    "rule_840": rule_840,
    "rule_841": rule_841,
    "rule_842": rule_842,
    "rule_843": rule_843,
    "rule_844": rule_844,
    "rule_845": rule_845,
    "rule_846": rule_846,
    "rule_847": rule_847,
    "rule_848": rule_848,
    "rule_849": rule_849,
    "rule_850": rule_850,
    "rule_851": rule_851,
    "rule_852": rule_852,
    "rule_853": rule_853,
    "rule_854": rule_854,
    "rule_855": rule_855,
    "rule_856": rule_856,
    "rule_857": rule_857,
    "rule_858": rule_858,
    "rule_859": rule_859,
    "rule_860": rule_860,
    "rule_861": rule_861,
    "rule_862": rule_862,
    "rule_863": rule_863,
    "rule_864": rule_864,
    "rule_865": rule_865,
    "rule_866": rule_866,
    "rule_867": rule_867,
    "rule_868": rule_868,
    "rule_869": rule_869,
    "rule_870": rule_870,
    "rule_871": rule_871,
    "rule_872": rule_872,
    "rule_873": rule_873,
    "rule_874": rule_874,
    "rule_875": rule_875,
    "rule_876": rule_876,
    "rule_877": rule_877,
    "rule_878": rule_878,
    "rule_879": rule_879,
    "rule_880": rule_880,
    "rule_881": rule_881,
    "rule_882": rule_882,
    "rule_883": rule_883,
    "rule_884": rule_884,
    "rule_885": rule_885,
    "rule_886": rule_886,
    "rule_887": rule_887,
    "rule_888": rule_888,
    "rule_889": rule_889,
    "rule_890": rule_890,
    "rule_891": rule_891,
    "rule_892": rule_892,
    "rule_893": rule_893,
    "rule_894": rule_894,
    "rule_895": rule_895,
    "rule_896": rule_896,
    "rule_897": rule_897,
    "rule_898": rule_898,
    "rule_899": rule_899,
    "rule_900": rule_900,
    "rule_901": rule_901,
    "rule_902": rule_902,
    "rule_903": rule_903,
    "rule_904": rule_904,
    "rule_905": rule_905,
    "rule_906": rule_906,
    "rule_907": rule_907,
    "rule_908": rule_908,
    "rule_909": rule_909,
    "rule_910": rule_910,
    "rule_911": rule_911,
    "rule_912": rule_912,
    "rule_913": rule_913,
    "rule_914": rule_914,
    "rule_915": rule_915,
    "rule_916": rule_916,
    "rule_917": rule_917,
    "rule_918": rule_918,
    "rule_919": rule_919,
    "rule_920": rule_920,
    "rule_921": rule_921,
    "rule_922": rule_922,
    "rule_923": rule_923,
    "rule_924": rule_924,
    "rule_925": rule_925,
    "rule_926": rule_926,
    "rule_927": rule_927,
    "rule_928": rule_928,
    "rule_929": rule_929,
    "rule_930": rule_930,
    "rule_931": rule_931,
    "rule_932": rule_932,
    "rule_933": rule_933,
    "rule_934": rule_934,
    "rule_935": rule_935,
    "rule_936": rule_936,
    "rule_937": rule_937,
    "rule_938": rule_938,
    "rule_939": rule_939,
    "rule_940": rule_940,
    "rule_941": rule_941,
    "rule_942": rule_942,
    "rule_943": rule_943,
    "rule_944": rule_944,
    "rule_945": rule_945,
    "rule_946": rule_946,
    "rule_947": rule_947,
    "rule_948": rule_948,
    "rule_949": rule_949,
    "rule_950": rule_950,
    "rule_951": rule_951,
    "rule_952": rule_952,
    "rule_953": rule_953,
    "rule_954": rule_954,
    "rule_955": rule_955,
    "rule_956": rule_956,
    "rule_957": rule_957,
    "rule_958": rule_958,
    "rule_959": rule_959,
    "rule_960": rule_960,
    "rule_961": rule_961,
    "rule_962": rule_962,
    "rule_963": rule_963,
    "rule_964": rule_964,
    "rule_965": rule_965,
    "rule_966": rule_966,
    "rule_967": rule_967,
    "rule_968": rule_968,
    "rule_969": rule_969,
    "rule_970": rule_970,
    "rule_971": rule_971,
    "rule_972": rule_972,
    "rule_973": rule_973,
    "rule_974": rule_974,
    "rule_975": rule_975,
    "rule_976": rule_976,
    "rule_977": rule_977,
    "rule_978": rule_978,
    "rule_979": rule_979,
    "rule_980": rule_980,
    "rule_981": rule_981,
    "rule_982": rule_982,
    "rule_983": rule_983,
    "rule_984": rule_984,
    "rule_985": rule_985,
    "rule_986": rule_986,
    "rule_987": rule_987,
    "rule_988": rule_988,
    "rule_989": rule_989,
    "rule_990": rule_990,
    "rule_991": rule_991,
    "rule_992": rule_992,
    "rule_993": rule_993,
    "rule_994": rule_994,
    "rule_995": rule_995,
    "rule_996": rule_996,
    "rule_997": rule_997,
    "rule_998": rule_998,
    "rule_999": rule_999,
    "rule_1000": rule_1000,
    "rule_1001": rule_1001,
    "rule_1002": rule_1002,
    "rule_1003": rule_1003,
    "rule_1004": rule_1004,
    "rule_1005": rule_1005,
    "rule_1006": rule_1006,
    "rule_1007": rule_1007,
    "rule_1008": rule_1008,
    "rule_1009": rule_1009,
    "rule_1010": rule_1010,
    "rule_1011": rule_1011,
    "rule_1012": rule_1012,
    "rule_1013": rule_1013,
    "rule_1014": rule_1014,
    "rule_1015": rule_1015,
    "rule_1016": rule_1016,
    "rule_1017": rule_1017,
    "rule_1018": rule_1018,
    "rule_1019": rule_1019,
    "rule_1020": rule_1020,
    "rule_1021": rule_1021,
    "rule_1022": rule_1022,
    "rule_1023": rule_1023,
    "rule_1024": rule_1024,
    "rule_1025": rule_1025,
    "rule_1026": rule_1026,
    "rule_1027": rule_1027,
    "rule_1028": rule_1028,
    "rule_1029": rule_1029,
    "rule_1030": rule_1030,
    "rule_1031": rule_1031,
    "rule_1032": rule_1032,
    "rule_1033": rule_1033,
    "rule_1034": rule_1034,
    "rule_1035": rule_1035,
    "rule_1036": rule_1036,
    "rule_1037": rule_1037,
    "rule_1038": rule_1038,
    "rule_1039": rule_1039,
    "rule_1040": rule_1040,
    "rule_1041": rule_1041,
    "rule_1042": rule_1042,
    "rule_1043": rule_1043,
    "rule_1044": rule_1044,
    "rule_1045": rule_1045,
    "rule_1046": rule_1046,
    "rule_1047": rule_1047,
    "rule_1048": rule_1048,
    "rule_1049": rule_1049,
    "rule_1050": rule_1050,
    "rule_1051": rule_1051,
    "rule_1052": rule_1052,
    "rule_1053": rule_1053,
    "rule_1054": rule_1054,
    "rule_1055": rule_1055,
    "rule_1056": rule_1056,
    "rule_1057": rule_1057,
    "rule_1058": rule_1058,
    "rule_1059": rule_1059,
    "rule_1060": rule_1060,
    "rule_1061": rule_1061,
    "rule_1062": rule_1062,
    "rule_1063": rule_1063,
    "rule_1064": rule_1064,
    "rule_1065": rule_1065,
    "rule_1066": rule_1066,
    "rule_1067": rule_1067,
    "rule_1068": rule_1068,
    "rule_1069": rule_1069,
    "rule_1070": rule_1070,
    "rule_1071": rule_1071,
    "rule_1072": rule_1072,
    "rule_1073": rule_1073,
    "rule_1074": rule_1074,
    "rule_1075": rule_1075,
    "rule_1076": rule_1076,
    "rule_1077": rule_1077,
    "rule_1078": rule_1078,
    "rule_1079": rule_1079,
    "rule_1080": rule_1080,
    "rule_1081": rule_1081,
    "rule_1082": rule_1082,
    "rule_1083": rule_1083,
    "rule_1084": rule_1084,
    "rule_1085": rule_1085,
    "rule_1086": rule_1086,
    "rule_1087": rule_1087,
    "rule_1088": rule_1088,
    "rule_1089": rule_1089,
    "rule_1090": rule_1090,
    "rule_1091": rule_1091,
    "rule_1092": rule_1092,
    "rule_1093": rule_1093,
    "rule_1094": rule_1094,
    "rule_1095": rule_1095,
    "rule_1096": rule_1096,
    "rule_1097": rule_1097,
    "rule_1098": rule_1098,
    "rule_1099": rule_1099,
    "rule_1100": rule_1100,
    "rule_1101": rule_1101,
    "rule_1102": rule_1102,
    "rule_1103": rule_1103,
    "rule_1104": rule_1104,
    "rule_1105": rule_1105,
    "rule_1106": rule_1106,
    "rule_1107": rule_1107,
    "rule_1108": rule_1108,
    "rule_1109": rule_1109,
    "rule_1110": rule_1110,
    "rule_1111": rule_1111,
    "rule_1112": rule_1112,
    "rule_1113": rule_1113,
    "rule_1114": rule_1114,
    "rule_1115": rule_1115,
    "rule_1116": rule_1116,
    "rule_1117": rule_1117,
    "rule_1118": rule_1118,
    "rule_1119": rule_1119,
    "rule_1120": rule_1120,
    "rule_1121": rule_1121,
    "rule_1122": rule_1122,
    "rule_1123": rule_1123,
    "rule_1124": rule_1124,
    "rule_1125": rule_1125,
    "rule_1126": rule_1126,
    "rule_1127": rule_1127,
    "rule_1128": rule_1128,
    "rule_1129": rule_1129,
    "rule_1130": rule_1130,
    "rule_1131": rule_1131,
    "rule_1132": rule_1132,
    "rule_1133": rule_1133,
    "rule_1134": rule_1134,
    "rule_1135": rule_1135,
    "rule_1136": rule_1136,
    "rule_1137": rule_1137,
    "rule_1138": rule_1138,
    "rule_1139": rule_1139,
    "rule_1140": rule_1140,
    "rule_1141": rule_1141,
    "rule_1142": rule_1142,
    "rule_1143": rule_1143,
    "rule_1144": rule_1144,
    "rule_1145": rule_1145,
    "rule_1146": rule_1146,
    "rule_1147": rule_1147,
    "rule_1148": rule_1148,
    "rule_1149": rule_1149,
    "rule_1150": rule_1150,
    "rule_1151": rule_1151,
    "rule_1152": rule_1152,
    "rule_1153": rule_1153,
    "rule_1154": rule_1154,
    "rule_1155": rule_1155,
    "rule_1156": rule_1156,
    "rule_1157": rule_1157,
    "rule_1158": rule_1158,
    "rule_1159": rule_1159,
    "rule_1160": rule_1160,
    "rule_1161": rule_1161,
    "rule_1162": rule_1162,
    "rule_1163": rule_1163,
    "rule_1164": rule_1164,
    "rule_1165": rule_1165,
    "rule_1166": rule_1166,
    "rule_1167": rule_1167,
    "rule_1168": rule_1168,
    "rule_1169": rule_1169,
    "rule_1170": rule_1170,
    "rule_1171": rule_1171,
    "rule_1172": rule_1172,
    "rule_1173": rule_1173,
    "rule_1174": rule_1174,
    "rule_1175": rule_1175,
    "rule_1176": rule_1176,
    "rule_1177": rule_1177,
    "rule_1178": rule_1178,
    "rule_1179": rule_1179,
    "rule_1180": rule_1180,
    "rule_1181": rule_1181,
    "rule_1182": rule_1182,
    "rule_1183": rule_1183,
    "rule_1184": rule_1184,
    "rule_1185": rule_1185,
    "rule_1186": rule_1186,
    "rule_1187": rule_1187,
    "rule_1188": rule_1188,
    "rule_1189": rule_1189,
    "rule_1190": rule_1190,
    "rule_1191": rule_1191,
    "rule_1192": rule_1192,
    "rule_1193": rule_1193,
    "rule_1194": rule_1194,
    "rule_1195": rule_1195,
    "rule_1196": rule_1196,
    "rule_1197": rule_1197,
    "rule_1198": rule_1198,
    "rule_1199": rule_1199,
    "rule_1200": rule_1200,
    "rule_1201": rule_1201,
    "rule_1202": rule_1202,
    "rule_1203": rule_1203,
    "rule_1204": rule_1204,
    "rule_1205": rule_1205,
    "rule_1206": rule_1206,
    "rule_1207": rule_1207,
    "rule_1208": rule_1208,
    "rule_1209": rule_1209,
    "rule_1210": rule_1210,
    "rule_1211": rule_1211,
    "rule_1212": rule_1212,
    "rule_1213": rule_1213,
    "rule_1214": rule_1214,
    "rule_1215": rule_1215,
    "rule_1216": rule_1216,
    "rule_1217": rule_1217,
    "rule_1218": rule_1218,
    "rule_1219": rule_1219,
    "rule_1220": rule_1220,
    "rule_1221": rule_1221,
    "rule_1222": rule_1222,
    "rule_1223": rule_1223,
    "rule_1224": rule_1224,
    "rule_1225": rule_1225,
    "rule_1226": rule_1226,
    "rule_1227": rule_1227,
    "rule_1228": rule_1228,
    "rule_1229": rule_1229,
    "rule_1230": rule_1230,
    "rule_1231": rule_1231,
    "rule_1232": rule_1232,
    "rule_1233": rule_1233,
    "rule_1234": rule_1234,
    "rule_1235": rule_1235,
    "rule_1236": rule_1236,
    "rule_1237": rule_1237,
    "rule_1238": rule_1238,
    "rule_1239": rule_1239,
    "rule_1240": rule_1240,
    "rule_1241": rule_1241,
    "rule_1242": rule_1242,
    "rule_1243": rule_1243,
    "rule_1244": rule_1244,
    "rule_1245": rule_1245,
    "rule_1246": rule_1246,
    "rule_1247": rule_1247,
    "rule_1248": rule_1248,
    "rule_1249": rule_1249,
    "rule_1250": rule_1250,
    "rule_1251": rule_1251,
    "rule_1252": rule_1252,
    "rule_1253": rule_1253,
    "rule_1254": rule_1254,
    "rule_1255": rule_1255,
    "rule_1256": rule_1256,
    "rule_1257": rule_1257,
    "rule_1258": rule_1258,
    "rule_1259": rule_1259,
    "rule_1260": rule_1260,
    "rule_1261": rule_1261,
    "rule_1262": rule_1262,
    "rule_1263": rule_1263,
    "rule_1264": rule_1264,
    "rule_1265": rule_1265,
    "rule_1266": rule_1266,
    "rule_1267": rule_1267,
    "rule_1268": rule_1268,
    "rule_1269": rule_1269,
    "rule_1270": rule_1270,
    "rule_1271": rule_1271,
    "rule_1272": rule_1272,
    "rule_1273": rule_1273,
    "rule_1274": rule_1274,
    "rule_1275": rule_1275,
    "rule_1276": rule_1276,
    "rule_1277": rule_1277,
    "rule_1278": rule_1278,
    "rule_1279": rule_1279,
    "rule_1280": rule_1280,
    "rule_1281": rule_1281,
    "rule_1282": rule_1282,
    "rule_1283": rule_1283,
    "rule_1284": rule_1284,
    "rule_1285": rule_1285,
    "rule_1286": rule_1286,
    "rule_1287": rule_1287,
    "rule_1288": rule_1288,
    "rule_1289": rule_1289,
    "rule_1290": rule_1290,
    "rule_1291": rule_1291,
    "rule_1292": rule_1292,
    "rule_1293": rule_1293,
    "rule_1294": rule_1294,
    "rule_1295": rule_1295,
    "rule_1296": rule_1296,
    "rule_1297": rule_1297,
    "rule_1298": rule_1298,
    "rule_1299": rule_1299,
    "rule_1300": rule_1300,
    "rule_1301": rule_1301,
    "rule_1302": rule_1302,
    "rule_1303": rule_1303,
    "rule_1304": rule_1304,
    "rule_1305": rule_1305,
    "rule_1306": rule_1306,
    "rule_1307": rule_1307,
    "rule_1308": rule_1308,
    "rule_1309": rule_1309,
    "rule_1310": rule_1310,
    "rule_1311": rule_1311,
    "rule_1312": rule_1312,
    "rule_1313": rule_1313,
    "rule_1314": rule_1314,
    "rule_1315": rule_1315,
    "rule_1316": rule_1316,
    "rule_1317": rule_1317,
    "rule_1318": rule_1318,
    "rule_1319": rule_1319,
    "rule_1320": rule_1320,
    "rule_1321": rule_1321,
    "rule_1322": rule_1322,
    "rule_1323": rule_1323,
    "rule_1324": rule_1324,
    "rule_1325": rule_1325,
    "rule_1326": rule_1326,
    "rule_1327": rule_1327,
    "rule_1328": rule_1328,
    "rule_1329": rule_1329,
    "rule_1330": rule_1330,
    "rule_1331": rule_1331,
    "rule_1332": rule_1332,
    "rule_1333": rule_1333,
    "rule_1334": rule_1334,
    "rule_1335": rule_1335,
    "rule_1336": rule_1336,
    "rule_1337": rule_1337,
    "rule_1338": rule_1338,
    "rule_1339": rule_1339,
    "rule_1340": rule_1340,
    "rule_1341": rule_1341,
    "rule_1342": rule_1342,
    "rule_1343": rule_1343,
    "rule_1344": rule_1344,
    "rule_1345": rule_1345,
    "rule_1346": rule_1346,
    "rule_1347": rule_1347,
    "rule_1348": rule_1348,
    "rule_1349": rule_1349,
    "rule_1350": rule_1350,
    "rule_1351": rule_1351,
    "rule_1352": rule_1352,
    "rule_1353": rule_1353,
    "rule_1354": rule_1354,
    "rule_1355": rule_1355,
    "rule_1356": rule_1356,
    "rule_1357": rule_1357,
    "rule_1358": rule_1358,
    "rule_1359": rule_1359,
    "rule_1360": rule_1360,
    "rule_1361": rule_1361,
    "rule_1362": rule_1362,
    "rule_1363": rule_1363,
    "rule_1364": rule_1364,
    "rule_1365": rule_1365,
    "rule_1366": rule_1366,
    "rule_1367": rule_1367,
    "rule_1368": rule_1368,
    "rule_1369": rule_1369,
    "rule_1370": rule_1370,
    "rule_1371": rule_1371,
    "rule_1372": rule_1372,
    "rule_1373": rule_1373,
    "rule_1374": rule_1374,
    "rule_1375": rule_1375,
    "rule_1376": rule_1376,
    "rule_1377": rule_1377,
    "rule_1378": rule_1378,
    "rule_1379": rule_1379,
    "rule_1380": rule_1380,
    "rule_1381": rule_1381,
    "rule_1382": rule_1382,
    "rule_1383": rule_1383,
    "rule_1384": rule_1384,
    "rule_1385": rule_1385,
    "rule_1386": rule_1386,
    "rule_1387": rule_1387,
    "rule_1388": rule_1388,
    "rule_1389": rule_1389,
    "rule_1390": rule_1390,
    "rule_1391": rule_1391,
    "rule_1392": rule_1392,
    "rule_1393": rule_1393,
    "rule_1394": rule_1394,
    "rule_1395": rule_1395,
    "rule_1396": rule_1396,
    "rule_1397": rule_1397,
    "rule_1398": rule_1398,
    "rule_1399": rule_1399,
    "rule_1400": rule_1400,
    "rule_1401": rule_1401,
    "rule_1402": rule_1402,
    "rule_1403": rule_1403,
    "rule_1404": rule_1404,
    "rule_1405": rule_1405,
    "rule_1406": rule_1406,
    "rule_1407": rule_1407,
    "rule_1408": rule_1408,
    "rule_1409": rule_1409,
    "rule_1410": rule_1410,
    "rule_1411": rule_1411,
    "rule_1412": rule_1412,
    "rule_1413": rule_1413,
    "rule_1414": rule_1414,
    "rule_1415": rule_1415,
    "rule_1416": rule_1416,
    "rule_1417": rule_1417,
    "rule_1418": rule_1418,
    "rule_1419": rule_1419,
    "rule_1420": rule_1420,
    "rule_1421": rule_1421,
    "rule_1422": rule_1422,
    "rule_1423": rule_1423,
    "rule_1424": rule_1424,
    "rule_1425": rule_1425,
    "rule_1426": rule_1426,
    "rule_1427": rule_1427,
    "rule_1428": rule_1428,
    "rule_1429": rule_1429,
    "rule_1430": rule_1430,
    "rule_1431": rule_1431,
    "rule_1432": rule_1432,
    "rule_1433": rule_1433,
    "rule_1434": rule_1434,
    "rule_1435": rule_1435,
    "rule_1436": rule_1436,
    "rule_1437": rule_1437,
    "rule_1438": rule_1438,
    "rule_1439": rule_1439,
    "rule_1440": rule_1440,
    "rule_1441": rule_1441,
    "rule_1442": rule_1442,
    "rule_1443": rule_1443,
    "rule_1444": rule_1444,
    "rule_1445": rule_1445,
    "rule_1446": rule_1446,
    "rule_1447": rule_1447,
    "rule_1448": rule_1448,
    "rule_1449": rule_1449,
    "rule_1450": rule_1450,
    "rule_1451": rule_1451,
    "rule_1452": rule_1452,
    "rule_1453": rule_1453,
    "rule_1454": rule_1454,
    "rule_1455": rule_1455,
    "rule_1456": rule_1456,
    "rule_1457": rule_1457,
    "rule_1458": rule_1458,
    "rule_1459": rule_1459,
    "rule_1460": rule_1460,
    "rule_1461": rule_1461,
    "rule_1462": rule_1462,
    "rule_1463": rule_1463,
    "rule_1464": rule_1464,
    "rule_1465": rule_1465,
    "rule_1466": rule_1466,
    "rule_1467": rule_1467,
    "rule_1468": rule_1468,
    "rule_1469": rule_1469,
    "rule_1470": rule_1470,
    "rule_1471": rule_1471,
    "rule_1472": rule_1472,
    "rule_1473": rule_1473,
    "rule_1474": rule_1474,
    "rule_1475": rule_1475,
    "rule_1476": rule_1476,
    "rule_1477": rule_1477,
    "rule_1478": rule_1478,
    "rule_1479": rule_1479,
    "rule_1480": rule_1480,
    "rule_1481": rule_1481,
    "rule_1482": rule_1482,
    "rule_1483": rule_1483,
    "rule_1484": rule_1484,
    "rule_1485": rule_1485,
    "rule_1486": rule_1486,
    "rule_1487": rule_1487,
    "rule_1488": rule_1488,
    "rule_1489": rule_1489,
    "rule_1490": rule_1490,
    "rule_1491": rule_1491,
    "rule_1492": rule_1492,
    "rule_1493": rule_1493,
    "rule_1494": rule_1494,
    "rule_1495": rule_1495,
    "rule_1496": rule_1496,
    "rule_1497": rule_1497,
    "rule_1498": rule_1498,
    "rule_1499": rule_1499,
    "rule_1500": rule_1500,
    "rule_1501": rule_1501,
    "rule_1502": rule_1502,
    "rule_1503": rule_1503,
    "rule_1504": rule_1504,
    "rule_1505": rule_1505,
    "rule_1506": rule_1506,
    "rule_1507": rule_1507,
    "rule_1508": rule_1508,
    "rule_1509": rule_1509,
    "rule_1510": rule_1510,
    "rule_1511": rule_1511,
    "rule_1512": rule_1512,
    "rule_1513": rule_1513,
    "rule_1514": rule_1514,
    "rule_1515": rule_1515,
    "rule_1516": rule_1516,
    "rule_1517": rule_1517,
    "rule_1518": rule_1518,
    "rule_1519": rule_1519,
    "rule_1520": rule_1520,
    "rule_1521": rule_1521,
    "rule_1522": rule_1522,
    "rule_1523": rule_1523,
    "rule_1524": rule_1524,
    "rule_1525": rule_1525,
    "rule_1526": rule_1526,
    "rule_1527": rule_1527,
    "rule_1528": rule_1528,
    "rule_1529": rule_1529,
    "rule_1530": rule_1530,
    "rule_1531": rule_1531,
    "rule_1532": rule_1532,
    "rule_1533": rule_1533,
    "rule_1534": rule_1534,
    "rule_1535": rule_1535,
    "rule_1536": rule_1536,
    "rule_1537": rule_1537,
    "rule_1538": rule_1538,
    "rule_1539": rule_1539,
    "rule_1540": rule_1540,
    "rule_1541": rule_1541,
    "rule_1542": rule_1542,
    "rule_1543": rule_1543,
    "rule_1544": rule_1544,
    "rule_1545": rule_1545,
    "rule_1546": rule_1546,
    "rule_1547": rule_1547,
    "rule_1548": rule_1548,
    "rule_1549": rule_1549,
    "rule_1550": rule_1550,
    "rule_1551": rule_1551,
    "rule_1552": rule_1552,
    "rule_1553": rule_1553,
    "rule_1554": rule_1554,
    "rule_1555": rule_1555,
    "rule_1556": rule_1556,
    "rule_1557": rule_1557,
    "rule_1558": rule_1558,
    "rule_1559": rule_1559,
    "rule_1560": rule_1560,
    "rule_1561": rule_1561,
    "rule_1562": rule_1562,
    "rule_1563": rule_1563,
    "rule_1564": rule_1564,
    "rule_1565": rule_1565,
    "rule_1566": rule_1566,
    "rule_1567": rule_1567,
    "rule_1568": rule_1568,
    "rule_1569": rule_1569,
    "rule_1570": rule_1570,
    "rule_1571": rule_1571,
    "rule_1572": rule_1572,
    "rule_1573": rule_1573,
    "rule_1574": rule_1574,
    "rule_1575": rule_1575,
    "rule_1576": rule_1576,
    "rule_1577": rule_1577,
    "rule_1578": rule_1578,
    "rule_1579": rule_1579,
    "rule_1580": rule_1580,
    "rule_1581": rule_1581,
    "rule_1582": rule_1582,
    "rule_1583": rule_1583,
    "rule_1584": rule_1584,
    "rule_1585": rule_1585,
    "rule_1586": rule_1586,
    "rule_1587": rule_1587,
    "rule_1588": rule_1588,
    "rule_1589": rule_1589,
    "rule_1590": rule_1590,
    "rule_1591": rule_1591,
    "rule_1592": rule_1592,
    "rule_1593": rule_1593,
    "rule_1594": rule_1594,
    "rule_1595": rule_1595,
    "rule_1596": rule_1596,
    "rule_1597": rule_1597,
    "rule_1598": rule_1598,
    "rule_1599": rule_1599,
    "rule_1600": rule_1600,
    "rule_1601": rule_1601,
    "rule_1602": rule_1602,
    "rule_1603": rule_1603,
    "rule_1604": rule_1604,
    "rule_1605": rule_1605,
    "rule_1606": rule_1606,
    "rule_1607": rule_1607,
    "rule_1608": rule_1608,
    "rule_1609": rule_1609,
    "rule_1610": rule_1610,
    "rule_1611": rule_1611,
    "rule_1612": rule_1612,
    "rule_1613": rule_1613,
    "rule_1614": rule_1614,
    "rule_1615": rule_1615,
    "rule_1616": rule_1616,
    "rule_1617": rule_1617,
    "rule_1618": rule_1618,
    "rule_1619": rule_1619,
    "rule_1620": rule_1620,
    "rule_1621": rule_1621,
    "rule_1622": rule_1622,
    "rule_1623": rule_1623,
    "rule_1624": rule_1624,
    "rule_1625": rule_1625,
    "rule_1626": rule_1626,
    "rule_1627": rule_1627,
    "rule_1628": rule_1628,
    "rule_1629": rule_1629,
    "rule_1630": rule_1630,
    "rule_1631": rule_1631,
    "rule_1632": rule_1632,
    "rule_1633": rule_1633,
    "rule_1634": rule_1634,
    "rule_1635": rule_1635,
    "rule_1636": rule_1636,
    "rule_1637": rule_1637,
    "rule_1638": rule_1638,
    "rule_1639": rule_1639,
    "rule_1640": rule_1640,
    "rule_1641": rule_1641,
    "rule_1642": rule_1642,
    "rule_1643": rule_1643,
    "rule_1644": rule_1644,
    "rule_1645": rule_1645,
    "rule_1646": rule_1646,
    "rule_1647": rule_1647,
    "rule_1648": rule_1648,
    "rule_1649": rule_1649,
    "rule_1650": rule_1650,
    "rule_1651": rule_1651,
    "rule_1652": rule_1652,
    "rule_1653": rule_1653,
    "rule_1654": rule_1654,
    "rule_1655": rule_1655,
    "rule_1656": rule_1656,
    "rule_1657": rule_1657,
    "rule_1658": rule_1658,
    "rule_1659": rule_1659,
    "rule_1660": rule_1660,
    "rule_1661": rule_1661,
    "rule_1662": rule_1662,
    "rule_1663": rule_1663,
    "rule_1664": rule_1664,
    "rule_1665": rule_1665,
    "rule_1666": rule_1666,
    "rule_1667": rule_1667,
    "rule_1668": rule_1668,
    "rule_1669": rule_1669,
    "rule_1670": rule_1670,
    "rule_1671": rule_1671,
    "rule_1672": rule_1672,
    "rule_1673": rule_1673,
    "rule_1674": rule_1674,
    "rule_1675": rule_1675,
    "rule_1676": rule_1676,
    "rule_1677": rule_1677,
    "rule_1678": rule_1678,
    "rule_1679": rule_1679,
    "rule_1680": rule_1680,
    "rule_1681": rule_1681,
    "rule_1682": rule_1682,
    "rule_1683": rule_1683,
    "rule_1684": rule_1684,
    "rule_1685": rule_1685,
    "rule_1686": rule_1686,
    "rule_1687": rule_1687,
    "rule_1688": rule_1688,
    "rule_1689": rule_1689,
    "rule_1690": rule_1690,
    "rule_1691": rule_1691,
    "rule_1692": rule_1692,
    "rule_1693": rule_1693,
    "rule_1694": rule_1694,
    "rule_1695": rule_1695,
    "rule_1696": rule_1696,
    "rule_1697": rule_1697,
    "rule_1698": rule_1698,
    "rule_1699": rule_1699,
    "rule_1700": rule_1700,
    "rule_1701": rule_1701,
    "rule_1702": rule_1702,
    "rule_1703": rule_1703,
    "rule_1704": rule_1704,
    "rule_1705": rule_1705,
    "rule_1706": rule_1706,
    "rule_1707": rule_1707,
    "rule_1708": rule_1708,
    "rule_1709": rule_1709,
    "rule_1710": rule_1710,
    "rule_1711": rule_1711,
    "rule_1712": rule_1712,
    "rule_1713": rule_1713,
    "rule_1714": rule_1714,
    "rule_1715": rule_1715,
    "rule_1716": rule_1716,
    "rule_1717": rule_1717,
    "rule_1718": rule_1718,
    "rule_1719": rule_1719,
    "rule_1720": rule_1720,
    "rule_1721": rule_1721,
    "rule_1722": rule_1722,
    "rule_1723": rule_1723,
    "rule_1724": rule_1724,
    "rule_1725": rule_1725,
    "rule_1726": rule_1726,
    "rule_1727": rule_1727,
    "rule_1728": rule_1728,
    "rule_1729": rule_1729,
    "rule_1730": rule_1730,
    "rule_1731": rule_1731,
    "rule_1732": rule_1732,
    "rule_1733": rule_1733,
    "rule_1734": rule_1734,
    "rule_1735": rule_1735,
    "rule_1736": rule_1736,
    "rule_1737": rule_1737,
    "rule_1738": rule_1738,
    "rule_1739": rule_1739,
    "rule_1740": rule_1740,
    "rule_1741": rule_1741,
    "rule_1742": rule_1742,
    "rule_1743": rule_1743,
    "rule_1744": rule_1744,
    "rule_1745": rule_1745,
    "rule_1746": rule_1746,
    "rule_1747": rule_1747,
    "rule_1748": rule_1748,
    "rule_1749": rule_1749,
    "rule_1750": rule_1750,
    "rule_1751": rule_1751,
    "rule_1752": rule_1752,
    "rule_1753": rule_1753,
    "rule_1754": rule_1754,
    "rule_1755": rule_1755,
    "rule_1756": rule_1756,
    "rule_1757": rule_1757,
    "rule_1758": rule_1758,
    "rule_1759": rule_1759,
    "rule_1760": rule_1760,
    "rule_1761": rule_1761,
    "rule_1762": rule_1762,
    "rule_1763": rule_1763,
    "rule_1764": rule_1764,
    "rule_1765": rule_1765,
    "rule_1766": rule_1766,
    "rule_1767": rule_1767,
    "rule_1768": rule_1768,
    "rule_1769": rule_1769,
    "rule_1770": rule_1770,
    "rule_1771": rule_1771,
    "rule_1772": rule_1772,
    "rule_1773": rule_1773,
    "rule_1774": rule_1774,
    "rule_1775": rule_1775,
    "rule_1776": rule_1776,
    "rule_1777": rule_1777,
    "rule_1778": rule_1778,
    "rule_1779": rule_1779,
    "rule_1780": rule_1780,
    "rule_1781": rule_1781,
    "rule_1782": rule_1782,
    "rule_1783": rule_1783,
    "rule_1784": rule_1784,
    "rule_1785": rule_1785,
    "rule_1786": rule_1786,
    "rule_1787": rule_1787,
    "rule_1788": rule_1788,
    "rule_1789": rule_1789,
    "rule_1790": rule_1790,
    "rule_1791": rule_1791,
    "rule_1792": rule_1792,
    "rule_1793": rule_1793,
    "rule_1794": rule_1794,
    "rule_1795": rule_1795,
    "rule_1796": rule_1796,
    "rule_1797": rule_1797,
    "rule_1798": rule_1798,
    "rule_1799": rule_1799,
    "rule_1800": rule_1800,
    "rule_1801": rule_1801,
    "rule_1802": rule_1802,
    "rule_1803": rule_1803,
    "rule_1804": rule_1804,
    "rule_1805": rule_1805,
    "rule_1806": rule_1806,
    "rule_1807": rule_1807,
    "rule_1808": rule_1808,
    "rule_1809": rule_1809,
    "rule_1810": rule_1810,
    "rule_1811": rule_1811,
    "rule_1812": rule_1812,
    "rule_1813": rule_1813,
    "rule_1814": rule_1814,
    "rule_1815": rule_1815,
    "rule_1816": rule_1816,
    "rule_1817": rule_1817,
    "rule_1818": rule_1818,
    "rule_1819": rule_1819,
    "rule_1820": rule_1820,
    "rule_1821": rule_1821,
    "rule_1822": rule_1822,
    "rule_1823": rule_1823,
    "rule_1824": rule_1824,
    "rule_1825": rule_1825,
    "rule_1826": rule_1826,
    "rule_1827": rule_1827,
    "rule_1828": rule_1828,
    "rule_1829": rule_1829,
    "rule_1830": rule_1830,
    "rule_1831": rule_1831,
    "rule_1832": rule_1832,
    "rule_1833": rule_1833,
    "rule_1834": rule_1834,
    "rule_1835": rule_1835,
    "rule_1836": rule_1836,
    "rule_1837": rule_1837,
    "rule_1838": rule_1838,
    "rule_1839": rule_1839,
    "rule_1840": rule_1840,
    "rule_1841": rule_1841,
    "rule_1842": rule_1842,
    "rule_1843": rule_1843,
    "rule_1844": rule_1844,
    "rule_1845": rule_1845,
    "rule_1846": rule_1846,
    "rule_1847": rule_1847,
    "rule_1848": rule_1848,
    "rule_1849": rule_1849,
    "rule_1850": rule_1850,
    "rule_1851": rule_1851,
    "rule_1852": rule_1852,
    "rule_1853": rule_1853,
    "rule_1854": rule_1854,
    "rule_1855": rule_1855,
    "rule_1856": rule_1856,
    "rule_1857": rule_1857,
    "rule_1858": rule_1858,
    "rule_1859": rule_1859,
    "rule_1860": rule_1860,
    "rule_1861": rule_1861,
    "rule_1862": rule_1862,
    "rule_1863": rule_1863,
    "rule_1864": rule_1864,
    "rule_1865": rule_1865,
    "rule_1866": rule_1866,
    "rule_1867": rule_1867,
    "rule_1868": rule_1868,
    "rule_1869": rule_1869,
    "rule_1870": rule_1870,
    "rule_1871": rule_1871,
    "rule_1872": rule_1872,
    "rule_1873": rule_1873,
    "rule_1874": rule_1874,
    "rule_1875": rule_1875,
    "rule_1876": rule_1876,
    "rule_1877": rule_1877,
    "rule_1878": rule_1878,
    "rule_1879": rule_1879,
    "rule_1880": rule_1880,
    "rule_1881": rule_1881,
    "rule_1882": rule_1882,
    "rule_1883": rule_1883,
    "rule_1884": rule_1884,
    "rule_1885": rule_1885,
    "rule_1886": rule_1886,
    "rule_1887": rule_1887,
    "rule_1888": rule_1888,
    "rule_1889": rule_1889,
    "rule_1890": rule_1890,
    "rule_1891": rule_1891,
    "rule_1892": rule_1892,
    "rule_1893": rule_1893,
    "rule_1894": rule_1894,
    "rule_1895": rule_1895,
    "rule_1896": rule_1896,
    "rule_1897": rule_1897,
    "rule_1898": rule_1898,
    "rule_1899": rule_1899,
    "rule_1900": rule_1900,
    "rule_1901": rule_1901,
    "rule_1902": rule_1902,
    "rule_1903": rule_1903,
    "rule_1904": rule_1904,
    "rule_1905": rule_1905,
    "rule_1906": rule_1906,
    "rule_1907": rule_1907,
    "rule_1908": rule_1908,
    "rule_1909": rule_1909,
    "rule_1910": rule_1910,
    "rule_1911": rule_1911,
    "rule_1912": rule_1912,
    "rule_1913": rule_1913,
    "rule_1914": rule_1914,
    "rule_1915": rule_1915,
    "rule_1916": rule_1916,
    "rule_1917": rule_1917,
    "rule_1918": rule_1918,
    "rule_1919": rule_1919,
    "rule_1920": rule_1920,
    "rule_1921": rule_1921,
    "rule_1922": rule_1922,
    "rule_1923": rule_1923,
    "rule_1924": rule_1924,
    "rule_1925": rule_1925,
    "rule_1926": rule_1926,
    "rule_1927": rule_1927,
    "rule_1928": rule_1928,
    "rule_1929": rule_1929,
    "rule_1930": rule_1930,
    "rule_1931": rule_1931,
    "rule_1932": rule_1932,
    "rule_1933": rule_1933,
    "rule_1934": rule_1934,
    "rule_1935": rule_1935,
    "rule_1936": rule_1936,
    "rule_1937": rule_1937,
    "rule_1938": rule_1938,
    "rule_1939": rule_1939,
    "rule_1940": rule_1940,
    "rule_1941": rule_1941,
    "rule_1942": rule_1942,
    "rule_1943": rule_1943,
    "rule_1944": rule_1944,
    "rule_1945": rule_1945,
    "rule_1946": rule_1946,
    "rule_1947": rule_1947,
    "rule_1948": rule_1948,
    "rule_1949": rule_1949,
    "rule_1950": rule_1950,
    "rule_1951": rule_1951,
    "rule_1952": rule_1952,
    "rule_1953": rule_1953,
    "rule_1954": rule_1954,
    "rule_1955": rule_1955,
    "rule_1956": rule_1956,
    "rule_1957": rule_1957,
    "rule_1958": rule_1958,
    "rule_1959": rule_1959,
    "rule_1960": rule_1960,
    "rule_1961": rule_1961,
    "rule_1962": rule_1962,
    "rule_1963": rule_1963,
    "rule_1964": rule_1964,
    "rule_1965": rule_1965,
    "rule_1966": rule_1966,
    "rule_1967": rule_1967,
    "rule_1968": rule_1968,
    "rule_1969": rule_1969,
    "rule_1970": rule_1970,
    "rule_1971": rule_1971,
    "rule_1972": rule_1972,
    "rule_1973": rule_1973,
    "rule_1974": rule_1974,
    "rule_1975": rule_1975,
    "rule_1976": rule_1976,
    "rule_1977": rule_1977,
    "rule_1978": rule_1978,
    "rule_1979": rule_1979,
    "rule_1980": rule_1980,
    "rule_1981": rule_1981,
    "rule_1982": rule_1982,
    "rule_1983": rule_1983,
    "rule_1984": rule_1984,
    "rule_1985": rule_1985,
    "rule_1986": rule_1986,
    "rule_1987": rule_1987,
    "rule_1988": rule_1988,
    "rule_1989": rule_1989,
    "rule_1990": rule_1990,
    "rule_1991": rule_1991,
    "rule_1992": rule_1992,
    "rule_1993": rule_1993,
    "rule_1994": rule_1994,
    "rule_1995": rule_1995,
    "rule_1996": rule_1996,
    "rule_1997": rule_1997,
    "rule_1998": rule_1998,
    "rule_1999": rule_1999,
    "rule_2000": rule_2000,
    "rule_2001": rule_2001,
    "rule_2002": rule_2002,
    "rule_2003": rule_2003,
    "rule_2004": rule_2004,
    "rule_2005": rule_2005,
    "rule_2006": rule_2006,
    "rule_2007": rule_2007,
    "rule_2008": rule_2008,
    "rule_2009": rule_2009,
    "rule_2010": rule_2010,
    "rule_2011": rule_2011,
    "rule_2012": rule_2012,
    "rule_2013": rule_2013,
    "rule_2014": rule_2014,
    "rule_2015": rule_2015,
    "rule_2016": rule_2016,
    "rule_2017": rule_2017,
    "rule_2018": rule_2018,
    "rule_2019": rule_2019,
    "rule_2020": rule_2020,
    "rule_2021": rule_2021,
    "rule_2022": rule_2022,
    "rule_2023": rule_2023,
    "rule_2024": rule_2024,
    "rule_2025": rule_2025,
    "rule_2026": rule_2026,
    "rule_2027": rule_2027,
    "rule_2028": rule_2028,
    "rule_2029": rule_2029,
    "rule_2030": rule_2030,
    "rule_2031": rule_2031,
    "rule_2032": rule_2032,
    "rule_2033": rule_2033,
    "rule_2034": rule_2034,
    "rule_2035": rule_2035,
    "rule_2036": rule_2036,
    "rule_2037": rule_2037,
    "rule_2038": rule_2038,
    "rule_2039": rule_2039,
    "rule_2040": rule_2040,
    "rule_2041": rule_2041,
    "rule_2042": rule_2042,
    "rule_2043": rule_2043,
    "rule_2044": rule_2044,
    "rule_2045": rule_2045,
    "rule_2046": rule_2046,
    "rule_2047": rule_2047,
    "rule_2048": rule_2048,
    "rule_2049": rule_2049,
    "rule_2050": rule_2050,
    "rule_2051": rule_2051,
    "rule_2052": rule_2052,
    "rule_2053": rule_2053,
    "rule_2054": rule_2054,
    "rule_2055": rule_2055,
    "rule_2056": rule_2056,
    "rule_2057": rule_2057,
    "rule_2058": rule_2058,
    "rule_2059": rule_2059,
    "rule_2060": rule_2060,
    "rule_2061": rule_2061,
    "rule_2062": rule_2062,
    "rule_2063": rule_2063,
    "rule_2064": rule_2064,
    "rule_2065": rule_2065,
    "rule_2066": rule_2066,
    "rule_2067": rule_2067,
    "rule_2068": rule_2068,
    "rule_2069": rule_2069,
    "rule_2070": rule_2070,
    "rule_2071": rule_2071,
    "rule_2072": rule_2072,
    "rule_2073": rule_2073,
    "rule_2074": rule_2074,
    "rule_2075": rule_2075,
    "rule_2076": rule_2076,
    "rule_2077": rule_2077,
    "rule_2078": rule_2078,
    "rule_2079": rule_2079,
    "rule_2080": rule_2080,
    "rule_2081": rule_2081,
    "rule_2082": rule_2082,
    "rule_2083": rule_2083,
    "rule_2084": rule_2084,
    "rule_2085": rule_2085,
    "rule_2086": rule_2086,
    "rule_2087": rule_2087,
    "rule_2088": rule_2088,
    "rule_2089": rule_2089,
    "rule_2090": rule_2090,
    "rule_2091": rule_2091,
    "rule_2092": rule_2092,
    "rule_2093": rule_2093,
    "rule_2094": rule_2094,
    "rule_2095": rule_2095,
    "rule_2096": rule_2096,
    "rule_2097": rule_2097,
    "rule_2098": rule_2098,
    "rule_2099": rule_2099,
    "rule_2100": rule_2100,
    "rule_2101": rule_2101,
    "rule_2102": rule_2102,
    "rule_2103": rule_2103,
    "rule_2104": rule_2104,
    "rule_2105": rule_2105,
    "rule_2106": rule_2106,
    "rule_2107": rule_2107,
    "rule_2108": rule_2108,
    "rule_2109": rule_2109,
    "rule_2110": rule_2110,
    "rule_2111": rule_2111,
    "rule_2112": rule_2112,
    "rule_2113": rule_2113,
    "rule_2114": rule_2114,
    "rule_2115": rule_2115,
    "rule_2116": rule_2116,
    "rule_2117": rule_2117,
    "rule_2118": rule_2118,
    "rule_2119": rule_2119,
    "rule_2120": rule_2120,
    "rule_2121": rule_2121,
    "rule_2122": rule_2122,
    "rule_2123": rule_2123,
    "rule_2124": rule_2124,
    "rule_2125": rule_2125,
    "rule_2126": rule_2126,
    "rule_2127": rule_2127,
    "rule_2128": rule_2128,
    "rule_2129": rule_2129,
    "rule_2130": rule_2130,
    "rule_2131": rule_2131,
    "rule_2132": rule_2132,
    "rule_2133": rule_2133,
    "rule_2134": rule_2134,
    "rule_2135": rule_2135,
    "rule_2136": rule_2136,
    "rule_2137": rule_2137,
    "rule_2138": rule_2138,
    "rule_2139": rule_2139,
    "rule_2140": rule_2140,
    "rule_2141": rule_2141,
    "rule_2142": rule_2142,
    "rule_2143": rule_2143,
    "rule_2144": rule_2144,
    "rule_2145": rule_2145,
    "rule_2146": rule_2146,
    "rule_2147": rule_2147,
    "rule_2148": rule_2148,
    "rule_2149": rule_2149,
    "rule_2150": rule_2150,
    "rule_2151": rule_2151,
    "rule_2152": rule_2152,
    "rule_2153": rule_2153,
    "rule_2154": rule_2154,
    "rule_2155": rule_2155,
    "rule_2156": rule_2156,
    "rule_2157": rule_2157,
    "rule_2158": rule_2158,
    "rule_2159": rule_2159,
    "rule_2160": rule_2160,
    "rule_2161": rule_2161,
    "rule_2162": rule_2162,
    "rule_2163": rule_2163,
    "rule_2164": rule_2164,
    "rule_2165": rule_2165,
    "rule_2166": rule_2166,
    "rule_2167": rule_2167,
    "rule_2168": rule_2168,
    "rule_2169": rule_2169,
    "rule_2170": rule_2170,
    "rule_2171": rule_2171,
    "rule_2172": rule_2172,
    "rule_2173": rule_2173,
    "rule_2174": rule_2174,
    "rule_2175": rule_2175,
    "rule_2176": rule_2176,
    "rule_2177": rule_2177,
    "rule_2178": rule_2178,
    "rule_2179": rule_2179,
    "rule_2180": rule_2180,
    "rule_2181": rule_2181,
    "rule_2182": rule_2182,
    "rule_2183": rule_2183,
    "rule_2184": rule_2184,
    "rule_2185": rule_2185,
    "rule_2186": rule_2186,
    "rule_2187": rule_2187,
    "rule_2188": rule_2188,
    "rule_2189": rule_2189,
    "rule_2190": rule_2190,
    "rule_2191": rule_2191,
    "rule_2192": rule_2192,
    "rule_2193": rule_2193,
    "rule_2194": rule_2194,
    "rule_2195": rule_2195,
    "rule_2196": rule_2196,
    "rule_2197": rule_2197,
    "rule_2198": rule_2198,
    "rule_2199": rule_2199,
    "rule_2200": rule_2200,
}
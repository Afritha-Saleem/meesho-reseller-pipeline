def alias_for(reseller_id: str) -> str:
    return f"ALIAS-{reseller_id[3:]}"


def assert_no_raw_names_leak(text: str, reseller_names: list[str]) -> bool:
    return not any(name in text for name in reseller_names)


def build_category_narrative(
    category: str,
    previous_revenue: float,
    current_revenue: float,
    mom_pct: float,
    month: str,
    prev_month: str,
) -> str:
    return (
        f"Context: {category} revenue for {month} compared with {prev_month}.\n"
        f"Insight: {category} revenue changed by {mom_pct}% MoM — FACT.\n"
        f"Implication: Review the category performance and investigate the "
        f"drivers of this change before deciding the next action."
    )


def build_top_reseller_narrative(
    reseller_id: str,
    region: str,
    total_spend: float,
    reseller_names: list[str],
) -> str:
    alias = alias_for(reseller_id)

    narrative = (
        f"Reseller {alias} in the {region} region has verified total spend "
        f"of {total_spend:.2f}. FACT. "
        f"Review the reseller's recent activity and investigate factors "
        f"behind the observed performance before taking further action."
    )

    assert assert_no_raw_names_leak(narrative, reseller_names)

    return narrative


def negative_case_name_leak(
    reseller_name: str,
    reseller_names: list[str],
) -> bool:
    negative_text = f"Reseller {reseller_name} showed strong performance."
    return assert_no_raw_names_leak(negative_text, reseller_names)


if __name__ == "__main__":
    reseller_names = [
        "Mumbai Reseller 1",
        "Mumbai Reseller 4",
        "Hyderabad Reseller 6",
        "Lucknow Reseller 6",
        "Jaipur Reseller 5",
    ]

    print("Alias check:")
    print(alias_for("RS019"))

    print("\nMay Ethnic Wear:")
    print(
        build_category_narrative(
            "Ethnic Wear",
            104520.77,
            185107.61,
            77.1,
            "May",
            "April",
        )
    )

    print("\nJune Ethnic Wear:")
    print(
        build_category_narrative(
            "Ethnic Wear",
            185107.61,
            76371.53,
            -58.74,
            "June",
            "May",
        )
    )

    print("\nTop Reseller Privacy Check:")
    print(
        build_top_reseller_narrative(
            "RS019",
            "West",
            75295.09,
            reseller_names,
        )
    )

    print("\nNegative-case leak test:")
    print(
        negative_case_name_leak(
            "Mumbai Reseller 1",
            reseller_names,
        )
    )
def alias_for(reseller_id: str) -> str:
    return f"ALIAS-{reseller_id[3:]}"


def assert_no_raw_names_leak(text: str, reseller_names: list[str]) -> bool:
    return not any(name in text for name in reseller_names)


if __name__ == "__main__":
    reseller_names = [
        "Mumbai Reseller 1",
        "Mumbai Reseller 4",
        "Hyderabad Reseller 6",
        "Lucknow Reseller 6",
        "Jaipur Reseller 5",
    ]

    final_narrative = (
        "Reseller ALIAS-19 in the West region has verified total spend "
        "of 75295.09 — FACT."
    )

    print("Alias check:")
    print(alias_for("RS019"))

    print("\nPositive privacy test:")
    print(assert_no_raw_names_leak(final_narrative, reseller_names))

    print("\nNegative privacy test:")
    negative_narrative = "Mumbai Reseller 1 showed strong performance."
    print(assert_no_raw_names_leak(negative_narrative, reseller_names))
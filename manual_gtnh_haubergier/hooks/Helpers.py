from typing import Optional, Any
from BaseClasses import MultiWorld

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the category, False to disable it, or None to use the default behavior
def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    from ..Helpers import get_option_value

    if category_name == "LV_Progression":
        return get_option_value(multiworld, player, "Last_tier_progression") >= 1
    if category_name == "MV_Progression":
         return get_option_value(multiworld, player, "Last_tier_progression") >= 2
    if category_name == "HV_Progression":
         return get_option_value(multiworld, player, "Last_tier_progression") >= 3
    if category_name == "EV_Progression":
         return get_option_value(multiworld, player, "Last_tier_progression") >= 4
    if category_name == "IV_Progression":
        return get_option_value(multiworld, player, "Last_tier_progression") >= 5
    if category_name == "LuV_Progression":
        return get_option_value(multiworld, player, "Last_tier_progression") >= 6
    if category_name == "ZPM_Progression":
         return get_option_value(multiworld, player, "Last_tier_progression") >= 7
    if category_name == "UV_Progression":
        return get_option_value(multiworld, player, "Last_tier_progression") >= 8
    if category_name == "UHV_Progression":
        return get_option_value(multiworld, player, "Last_tier_progression") >= 9
    if category_name == "UEV_Progression":
        return get_option_value(multiworld, player, "Last_tier_progression") >= 10
    if category_name == "UIV_Progression":
        return get_option_value(multiworld, player, "Last_tier_progression") >= 11
    if category_name == "UMV_Progression":
        return get_option_value(multiworld, player, "Last_tier_progression") >= 12
    if category_name == "UXV_Progression":
        return get_option_value(multiworld, player, "Last_tier_progression") >= 13
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the item, False to disable it, or None to use the default behavior
def before_is_item_enabled(multiworld: MultiWorld, player: int, item:  dict[str, Any]) -> Optional[bool]:
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the location, False to disable it, or None to use the default behavior
def before_is_location_enabled(multiworld: MultiWorld, player: int, location:  dict[str, Any]) -> Optional[bool]:
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the event, False to disable it, or None to use the default behavior
def before_is_event_enabled(multiworld: MultiWorld, player: int, event:  dict[str, Any]) -> Optional[bool]:
    return None

from django import template
from django.utils.html import escape, mark_safe
import time

register = template.Library()

@register.simple_tag
def active_daycare_sessions(iterable):
    """
    Returns the active day care session for the current user.
    """

    th_class = "p-0 pb-4 pr-6 font-normal"
    table_class = "w-[40rem] mt-11 sm:w-full"
    div_class = "overflow-y-auto px-4 sm:overflow-visible sm:px-0"
    th_class = "text-sm text-left leading-6 text-zinc-500"
    tr_class = "group hover:bg-zinc-50"
    td_class = "relative p-0"
    tbody_class = "relative divide-y divide-zinc-100 border-t border-zinc-200 text-sm leading-6 text-zinc-700"

    content = [f"<div class='{div_class}'>"]
    content.append(f"<table class='{table_class}'>")
    content.append(f"<thead class='{th_class}'>")
    content.append("<tr>")
    content.append(f"<th class='{th_class}'>Pet</th>")
    content.append(f"<th class='{th_class}'>Check In User</th>")
    content.append(f"<th class='{th_class}'>Check In Owner</th>")
    content.append(f"<th class='{th_class}'>Check In</th>")
    content.append("</tr>")
    content.append("</thead>")

    content.append(f"<tbody class='{tbody_class}'>")
    for item in iterable:
        content.append(f"<tr class='{tr_class}'>")
        content.append(f"<td class='{td_class}'>{escape(item.pet)}</td>")
        content.append(f"<td class='{td_class}'>{escape(item.check_in_user)}</td>")
        content.append(f"<td class='{td_class}'>{escape(item.check_in_owner)}</td>")
        content.append(f"<td class='{td_class}'>{escape(format_datetime(item.check_in))}</td>")
        content.append("</tr>")

    content.append("</tbody></table></div>")
    content = "".join(content)

    return mark_safe(content)


def format_datetime(value):
    """
    Formats a datetime object to a string.
    """

    format = "%m-%d-%Y %I:%M %p"

    if value is None:
        return ""

    if isinstance(value, str):
        return value
    elif isinstance(value, (int, float)):
        return time.strftime(format, time.localtime(value))
    else:
        return value.strftime(format)

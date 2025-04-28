from django import template
from django.utils.html import escape, mark_safe

register = template.Library()

@register.simple_tag(name="active_daycare_sessions")
def active_daycare_sessions(iterable):
    """
    Returns the active day care session for the current user.
    """

    content = ["<table>"]
    content.append("<tr>")
    content.append("<th>Pet</th>")
    content.append("<th>Check In User</th>")
    content.append("<th>Check In Owner</th>")
    content.append("<th>Check Out User</th>")
    content.append("<th>Check Out Owner</th>")
    content.append("<th>Check In</th>")
    content.append("<th>Check Out</th>")
    content.append("</tr>")

    for item in iterable:
        content.append("<tr>")
        content.append(f"<td>{escape(item.pet)}</td>")
        content.append(f"<td>{escape(item.check_in_user)}</td>")
        content.append(f"<td>{escape(item.check_in_owner)}</td>")
        content.append(f"<td>{escape(item.check_out_user)}</td>")
        content.append(f"<td>{escape(item.check_out_owner)}</td>")
        content.append(f"<td>{escape(item.check_in)}</td>")
        content.append(f"<td>{escape(item.check_out)}</td>")
        content.append("</tr>")
    content.append("</table>")

    content = "".join(content)
    return mark_safe(content)
# <th class="px-6 px-4">{{ session.pet }}</th>
# <td class="px-6 px-4">{{ session.check_in_owner|default_if_none:"&nbsp;" }}</td>
# <td class="px-6 px-4">{{ session.check_in_user|default_if_none:"&nbsp;" }}</td>
# <td class="px-6 px-4">{{ session.check_out_owner|default_if_none:"&nbsp;" }}</td>
# <td class="px-6 px-4">{{ session.check_out_user|default_if_none:"&nbsp;" }}</td>
# <td class="px-6 px-4">{{ session.check_in|default_if_none:"&nbsp;" }}</td>
# <td class="px-6 px-4">{{ session.check_out|default_if_none:"&nbsp;" }}</td>

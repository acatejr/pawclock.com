defmodule AppWeb.OwnerLive.Show do
  use AppWeb, :live_view

  alias App.PawClock

  @impl true
  def mount(_params, _session, socket) do
    {:ok, socket}
  end

  @impl true
  def handle_params(%{"id" => id}, _, socket) do
    owner = PawClock.get_owner!(id)
    {:noreply,
     socket
     |> assign(:page_title, page_title(socket.assigns.live_action))
     |> assign(:owner, owner)}
  end

  defp page_title(:show), do: "Show Owner"
  defp page_title(:edit), do: "Edit Owner"
end

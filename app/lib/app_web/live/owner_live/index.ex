defmodule AppWeb.OwnerLive.Index do
  use AppWeb, :live_view

  alias App.PawClock
  alias App.PawClock.Owner

  @impl true
  def mount(_params, _session, socket) do
    {:ok, stream(socket, :owners, PawClock.list_owners())}
  end

  @impl true
  def handle_params(params, _url, socket) do
    {:noreply, apply_action(socket, socket.assigns.live_action, params)}
  end

  defp apply_action(socket, :edit, %{"id" => id}) do
    socket
    |> assign(:page_title, "Edit Owner")
    |> assign(:owner, PawClock.get_owner!(id))
  end

  defp apply_action(socket, :new, _params) do
    socket
    |> assign(:page_title, "New Owner")
    |> assign(:owner, %Owner{})
  end

  defp apply_action(socket, :index, _params) do
    socket
    |> assign(:page_title, "Listing Owners")
    |> assign(:owner, nil)
  end

  @impl true
  def handle_info({AppWeb.OwnerLive.FormComponent, {:saved, owner}}, socket) do
    {:noreply, stream_insert(socket, :owners, owner)}
  end

  @impl true
  def handle_event("delete", %{"id" => id}, socket) do
    owner = PawClock.get_owner!(id)
    {:ok, _} = PawClock.delete_owner(owner)

    {:noreply, stream_delete(socket, :owners, owner)}
  end
end

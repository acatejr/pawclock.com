defmodule AppWeb.PetLive.Index do
  use AppWeb, :live_view

  alias App.PawClock
  alias App.PawClock.Pet

  @impl true
  def mount(_params, _session, socket) do
    {:ok, stream(socket, :pets, PawClock.list_pets())}
  end

  @impl true
  def handle_params(params, _url, socket) do
    {:noreply, apply_action(socket, socket.assigns.live_action, params)}
  end

  defp apply_action(socket, :edit, %{"id" => id}) do
    socket
    |> assign(:page_title, "Edit Pet")
    |> assign(:pet, PawClock.get_pet!(id))
  end

  defp apply_action(socket, :new, _params) do
    socket
    |> assign(:page_title, "New Pet")
    |> assign(:pet, %Pet{})
  end

  defp apply_action(socket, :index, _params) do
    socket
    |> assign(:page_title, "Listing Pets")
    |> assign(:pet, nil)
  end

  @impl true
  def handle_info({AppWeb.PetLive.FormComponent, {:saved, pet}}, socket) do
    {:noreply, stream_insert(socket, :pets, pet)}
  end

  @impl true
  def handle_event("delete", %{"id" => id}, socket) do
    pet = PawClock.get_pet!(id)
    {:ok, _} = PawClock.delete_pet(pet)

    {:noreply, stream_delete(socket, :pets, pet)}
  end
end

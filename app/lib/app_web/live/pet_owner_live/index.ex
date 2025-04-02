defmodule AppWeb.PetOwnerLive.Index do
  use AppWeb, :live_view

  alias App.Account
  alias App.Account.PetOwner

  @impl true
  def mount(_params, _session, socket) do
    {:ok, stream(socket, :pet_owners, Account.list_pet_owners())}
  end

  @impl true
  def handle_params(params, _url, socket) do
    {:noreply, apply_action(socket, socket.assigns.live_action, params)}
  end

  defp apply_action(socket, :edit, %{"id" => id}) do
    socket
    |> assign(:page_title, "Edit Pet owner")
    |> assign(:pet_owner, Account.get_pet_owner!(id))
  end

  defp apply_action(socket, :new, _params) do
    socket
    |> assign(:page_title, "New Pet owner")
    |> assign(:pet_owner, %PetOwner{})
  end

  defp apply_action(socket, :index, _params) do
    socket
    |> assign(:page_title, "Listing Pet owners")
    |> assign(:pet_owner, nil)
  end

  @impl true
  def handle_info({AppWeb.PetOwnerLive.FormComponent, {:saved, pet_owner}}, socket) do
    {:noreply, stream_insert(socket, :pet_owners, pet_owner)}
  end

  @impl true
  def handle_event("delete", %{"id" => id}, socket) do
    pet_owner = Account.get_pet_owner!(id)
    {:ok, _} = Account.delete_pet_owner(pet_owner)

    {:noreply, stream_delete(socket, :pet_owners, pet_owner)}
  end
end

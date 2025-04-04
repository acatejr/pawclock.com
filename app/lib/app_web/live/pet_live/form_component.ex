defmodule AppWeb.PetLive.FormComponent do
  use AppWeb, :live_component

  alias App.PawClock

  @impl true
  def render(assigns) do
    ~H"""
    <div>
      <.header>
        {@title}
        <:subtitle>Use this form to manage pet records in your database.</:subtitle>
      </.header>

      <.simple_form
        for={@form}
        id="pet-form"
        phx-target={@myself}
        phx-change="validate"
        phx-submit="save"
      >
        <.input field={@form[:name]} type="text" label="Name" />
        <:actions>
          <.button phx-disable-with="Saving...">Save Pet</.button>
        </:actions>
      </.simple_form>
    </div>
    """
  end

  @impl true
  def update(%{pet: pet} = assigns, socket) do
    {:ok,
     socket
     |> assign(assigns)
     |> assign_new(:form, fn ->
       to_form(PawClock.change_pet(pet))
     end)}
  end

  @impl true
  def handle_event("validate", %{"pet" => pet_params}, socket) do
    changeset = PawClock.change_pet(socket.assigns.pet, pet_params)
    {:noreply, assign(socket, form: to_form(changeset, action: :validate))}
  end

  def handle_event("save", %{"pet" => pet_params}, socket) do
    save_pet(socket, socket.assigns.action, pet_params)
  end

  defp save_pet(socket, :edit, pet_params) do
    case PawClock.update_pet(socket.assigns.pet, pet_params) do
      {:ok, pet} ->
        notify_parent({:saved, pet})

        {:noreply,
         socket
         |> put_flash(:info, "Pet updated successfully")
         |> push_patch(to: socket.assigns.patch)}

      {:error, %Ecto.Changeset{} = changeset} ->
        {:noreply, assign(socket, form: to_form(changeset))}
    end
  end

  defp save_pet(socket, :new, pet_params) do
    case PawClock.create_pet(pet_params) do
      {:ok, pet} ->
        notify_parent({:saved, pet})

        {:noreply,
         socket
         |> put_flash(:info, "Pet created successfully")
         |> push_patch(to: socket.assigns.patch)}

      {:error, %Ecto.Changeset{} = changeset} ->
        {:noreply, assign(socket, form: to_form(changeset))}
    end
  end

  defp notify_parent(msg), do: send(self(), {__MODULE__, msg})
end

defmodule AppWeb.PetOwnerLive.FormComponent do
  use AppWeb, :live_component

  alias App.Account

  @impl true
  def render(assigns) do
    ~H"""
    <div>
      <.header>
        {@title}
        <:subtitle>Use this form to manage pet_owner records in your database.</:subtitle>
      </.header>

      <.simple_form
        for={@form}
        id="pet_owner-form"
        phx-target={@myself}
        phx-change="validate"
        phx-submit="save"
      >
        <.input field={@form[:first_name]} type="text" label="First name" />
        <.input field={@form[:last_name]} type="text" label="Last name" />
        <.input field={@form[:email]} type="text" label="Email" />
        <:actions>
          <.button phx-disable-with="Saving...">Save Pet owner</.button>
        </:actions>
      </.simple_form>
    </div>
    """
  end

  @impl true
  def update(%{pet_owner: pet_owner} = assigns, socket) do
    {:ok,
     socket
     |> assign(assigns)
     |> assign_new(:form, fn ->
       to_form(Account.change_pet_owner(pet_owner))
     end)}
  end

  @impl true
  def handle_event("validate", %{"pet_owner" => pet_owner_params}, socket) do
    changeset = Account.change_pet_owner(socket.assigns.pet_owner, pet_owner_params)
    {:noreply, assign(socket, form: to_form(changeset, action: :validate))}
  end

  def handle_event("save", %{"pet_owner" => pet_owner_params}, socket) do
    save_pet_owner(socket, socket.assigns.action, pet_owner_params)
  end

  defp save_pet_owner(socket, :edit, pet_owner_params) do
    case Account.update_pet_owner(socket.assigns.pet_owner, pet_owner_params) do
      {:ok, pet_owner} ->
        notify_parent({:saved, pet_owner})

        {:noreply,
         socket
         |> put_flash(:info, "Pet owner updated successfully")
         |> push_patch(to: socket.assigns.patch)}

      {:error, %Ecto.Changeset{} = changeset} ->
        {:noreply, assign(socket, form: to_form(changeset))}
    end
  end

  defp save_pet_owner(socket, :new, pet_owner_params) do
    case Account.create_pet_owner(pet_owner_params) do
      {:ok, pet_owner} ->
        notify_parent({:saved, pet_owner})

        {:noreply,
         socket
         |> put_flash(:info, "Pet owner created successfully")
         |> push_patch(to: socket.assigns.patch)}

      {:error, %Ecto.Changeset{} = changeset} ->
        {:noreply, assign(socket, form: to_form(changeset))}
    end
  end

  defp notify_parent(msg), do: send(self(), {__MODULE__, msg})
end

defmodule AppWeb.DayCareSessionLive.FormComponent do
  use AppWeb, :live_component

  alias App.PawClock

  @impl true
  def render(assigns) do
    ~H"""
    <div>
      <.header>
        {@title}
        <:subtitle>Use this form to manage day_care_session records in your database.</:subtitle>
      </.header>

      <.simple_form
        for={@form}
        id="day_care_session-form"
        phx-target={@myself}
        phx-change="validate"
        phx-submit="save"
      >
        <.input field={@form[:checkin]} type="datetime-local" label="Checkin" />
        <.input field={@form[:checkout]} type="datetime-local" label="Checkout" />
        <.input field={@form[:status]} type="text" label="Status" />
        <:actions>
          <.button phx-disable-with="Saving...">Save Day care session</.button>
        </:actions>
      </.simple_form>
    </div>
    """
  end

  @impl true
  def update(%{day_care_session: day_care_session} = assigns, socket) do
    {:ok,
     socket
     |> assign(assigns)
     |> assign_new(:form, fn ->
       to_form(PawClock.change_day_care_session(day_care_session))
     end)}
  end

  @impl true
  def handle_event("validate", %{"day_care_session" => day_care_session_params}, socket) do
    changeset = PawClock.change_day_care_session(socket.assigns.day_care_session, day_care_session_params)
    {:noreply, assign(socket, form: to_form(changeset, action: :validate))}
  end

  def handle_event("save", %{"day_care_session" => day_care_session_params}, socket) do
    save_day_care_session(socket, socket.assigns.action, day_care_session_params)
  end

  defp save_day_care_session(socket, :edit, day_care_session_params) do
    case PawClock.update_day_care_session(socket.assigns.day_care_session, day_care_session_params) do
      {:ok, day_care_session} ->
        notify_parent({:saved, day_care_session})

        {:noreply,
         socket
         |> put_flash(:info, "Day care session updated successfully")
         |> push_patch(to: socket.assigns.patch)}

      {:error, %Ecto.Changeset{} = changeset} ->
        {:noreply, assign(socket, form: to_form(changeset))}
    end
  end

  defp save_day_care_session(socket, :new, day_care_session_params) do
    case PawClock.create_day_care_session(day_care_session_params) do
      {:ok, day_care_session} ->
        notify_parent({:saved, day_care_session})

        {:noreply,
         socket
         |> put_flash(:info, "Day care session created successfully")
         |> push_patch(to: socket.assigns.patch)}

      {:error, %Ecto.Changeset{} = changeset} ->
        {:noreply, assign(socket, form: to_form(changeset))}
    end
  end

  defp notify_parent(msg), do: send(self(), {__MODULE__, msg})
end

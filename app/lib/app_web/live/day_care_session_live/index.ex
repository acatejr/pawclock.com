defmodule AppWeb.DayCareSessionLive.Index do
  use AppWeb, :live_view

  alias App.PawClock
  alias App.PawClock.DayCareSession

  @impl true
  def mount(_params, _session, socket) do
    {:ok, stream(socket, :daycare_sessions, PawClock.list_daycare_sessions())}
  end

  @impl true
  def handle_params(params, _url, socket) do
    {:noreply, apply_action(socket, socket.assigns.live_action, params)}
  end

  defp apply_action(socket, :edit, %{"id" => id}) do
    socket
    |> assign(:page_title, "Edit Day care session")
    |> assign(:day_care_session, PawClock.get_day_care_session!(id))
  end

  defp apply_action(socket, :new, _params) do
    socket
    |> assign(:page_title, "New Day care session")
    |> assign(:day_care_session, %DayCareSession{})
  end

  defp apply_action(socket, :index, _params) do
    socket
    |> assign(:page_title, "Listing Daycare sessions")
    |> assign(:day_care_session, nil)
  end

  @impl true
  def handle_info({AppWeb.DayCareSessionLive.FormComponent, {:saved, day_care_session}}, socket) do
    {:noreply, stream_insert(socket, :daycare_sessions, day_care_session)}
  end

  @impl true
  def handle_event("delete", %{"id" => id}, socket) do
    day_care_session = PawClock.get_day_care_session!(id)
    {:ok, _} = PawClock.delete_day_care_session(day_care_session)

    {:noreply, stream_delete(socket, :daycare_sessions, day_care_session)}
  end
end

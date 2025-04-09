defmodule AppWeb.DayCareSessionLiveTest do
  use AppWeb.ConnCase

  import Phoenix.LiveViewTest
  import App.PawClockFixtures

  @create_attrs %{status: "some status", checkout: "2025-04-08T17:35:00Z", checkin: "2025-04-08T17:35:00Z"}
  @update_attrs %{status: "some updated status", checkout: "2025-04-09T17:35:00Z", checkin: "2025-04-09T17:35:00Z"}
  @invalid_attrs %{status: nil, checkout: nil, checkin: nil}

  defp create_day_care_session(_) do
    day_care_session = day_care_session_fixture()
    %{day_care_session: day_care_session}
  end

  describe "Index" do
    setup [:create_day_care_session]

    test "lists all daycare_sessions", %{conn: conn, day_care_session: day_care_session} do
      {:ok, _index_live, html} = live(conn, ~p"/daycare_sessions")

      assert html =~ "Listing Daycare sessions"
      assert html =~ day_care_session.status
    end

    test "saves new day_care_session", %{conn: conn} do
      {:ok, index_live, _html} = live(conn, ~p"/daycare_sessions")

      assert index_live |> element("a", "New Day care session") |> render_click() =~
               "New Day care session"

      assert_patch(index_live, ~p"/daycare_sessions/new")

      assert index_live
             |> form("#day_care_session-form", day_care_session: @invalid_attrs)
             |> render_change() =~ "can&#39;t be blank"

      assert index_live
             |> form("#day_care_session-form", day_care_session: @create_attrs)
             |> render_submit()

      assert_patch(index_live, ~p"/daycare_sessions")

      html = render(index_live)
      assert html =~ "Day care session created successfully"
      assert html =~ "some status"
    end

    test "updates day_care_session in listing", %{conn: conn, day_care_session: day_care_session} do
      {:ok, index_live, _html} = live(conn, ~p"/daycare_sessions")

      assert index_live |> element("#daycare_sessions-#{day_care_session.id} a", "Edit") |> render_click() =~
               "Edit Day care session"

      assert_patch(index_live, ~p"/daycare_sessions/#{day_care_session}/edit")

      assert index_live
             |> form("#day_care_session-form", day_care_session: @invalid_attrs)
             |> render_change() =~ "can&#39;t be blank"

      assert index_live
             |> form("#day_care_session-form", day_care_session: @update_attrs)
             |> render_submit()

      assert_patch(index_live, ~p"/daycare_sessions")

      html = render(index_live)
      assert html =~ "Day care session updated successfully"
      assert html =~ "some updated status"
    end

    test "deletes day_care_session in listing", %{conn: conn, day_care_session: day_care_session} do
      {:ok, index_live, _html} = live(conn, ~p"/daycare_sessions")

      assert index_live |> element("#daycare_sessions-#{day_care_session.id} a", "Delete") |> render_click()
      refute has_element?(index_live, "#daycare_sessions-#{day_care_session.id}")
    end
  end

  describe "Show" do
    setup [:create_day_care_session]

    test "displays day_care_session", %{conn: conn, day_care_session: day_care_session} do
      {:ok, _show_live, html} = live(conn, ~p"/daycare_sessions/#{day_care_session}")

      assert html =~ "Show Day care session"
      assert html =~ day_care_session.status
    end

    test "updates day_care_session within modal", %{conn: conn, day_care_session: day_care_session} do
      {:ok, show_live, _html} = live(conn, ~p"/daycare_sessions/#{day_care_session}")

      assert show_live |> element("a", "Edit") |> render_click() =~
               "Edit Day care session"

      assert_patch(show_live, ~p"/daycare_sessions/#{day_care_session}/show/edit")

      assert show_live
             |> form("#day_care_session-form", day_care_session: @invalid_attrs)
             |> render_change() =~ "can&#39;t be blank"

      assert show_live
             |> form("#day_care_session-form", day_care_session: @update_attrs)
             |> render_submit()

      assert_patch(show_live, ~p"/daycare_sessions/#{day_care_session}")

      html = render(show_live)
      assert html =~ "Day care session updated successfully"
      assert html =~ "some updated status"
    end
  end
end

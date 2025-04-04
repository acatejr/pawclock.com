defmodule AppWeb.PageControllerTest do
  use AppWeb.ConnCase

  test "GET /welcome", %{conn: conn} do
    conn = get(conn, ~p"/welcome")
    assert html_response(conn, 200) =~ "Peace of mind from prototype to production"
  end

  test "GET /", %{conn: conn} do
    conn = get(conn, ~p"/")
    assert html_response(conn, 200) =~ "Home"
  end
end

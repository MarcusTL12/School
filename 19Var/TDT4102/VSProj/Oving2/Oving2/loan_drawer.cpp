#include "loan_drawer.h"

using namespace Graph_lib;

constexpr int win_x = 800;
constexpr int win_y = 600;
constexpr int margin = 30;
constexpr int axis_x_len = win_x - 2 * margin;
constexpr int axis_y_len = win_y - 2 * margin;
constexpr int origo_y = win_y - margin;
constexpr int y_max_val = 2000;

const Color annuity_color = Color::dark_blue;
const Color series_color = Color::dark_red;

void plot_mp(vector<int> points, Marked_polyline& plt)
// Precondition: vector of size periods with values ranging from 0 to y_max_val
{
	int periods = static_cast<int>(points.size());

	constexpr double axis_y_scale = double{ axis_y_len } / y_max_val;
	int x_step = axis_x_len / periods;
	int x = margin + x_step;
	int y;

	for (int p : points) {
		y = origo_y - static_cast<int>(p * axis_y_scale);
		plt.add({ x, y });
		x += x_step;
	}
}

void drawPlot(vector<int> annuity, vector<int> series, int loan, int rate)
// Naiv funksjon. Den tar ikke høyde for at vectorene kan ha ulik størrelse,
// ingen transformering av koordinatsystem, osv.
{
	Point tl{ 100, 100 };
	int periods = static_cast<int>(series.size());
	const string win_label{ "Årlig utgift ved annuitetslån og serielån over "
						   + to_string(periods) + " år pålydende "
						   + to_string(loan) + " kroner med "
						   + to_string(rate) + " % rente." };
	Simple_window win{ tl, win_x, win_y, win_label };

	Axis x{ Axis::x, {margin, origo_y}, axis_x_len, periods, "målemerke = 1 år" };
	Axis y{ Axis::y, {margin, origo_y}, axis_y_len, periods,
		   "målemerke = " + to_string(y_max_val / periods) + " kr" };
	x.set_color(Color::black);
	y.set_color(Color::black);
	win.attach(x);
	win.attach(y);

	// Annuitetslån
	Marked_polyline annuity_plt{ "x" };
	plot_mp(annuity, annuity_plt);
	annuity_plt.set_color(annuity_color);

	Text at{ {margin + 20, margin + 20}, "Annuitet" };
	at.set_color(annuity_color);

	win.attach(annuity_plt);
	win.attach(at);

	// Serielån
	Marked_polyline series_plt{ "x" };
	plot_mp(series, series_plt);
	series_plt.set_color(series_color);

	Text st{ {margin + 20, margin + 40}, "Serie" };
	st.set_color(series_color);

	win.attach(series_plt);
	win.attach(st);

	win.wait_for_button();
}
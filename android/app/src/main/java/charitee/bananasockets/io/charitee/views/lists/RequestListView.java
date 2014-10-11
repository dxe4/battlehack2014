package charitee.bananasockets.io.charitee.views.lists;

import android.content.Context;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;

import org.androidannotations.annotations.AfterInject;
import org.androidannotations.annotations.Background;
import org.androidannotations.annotations.EViewGroup;
import org.androidannotations.annotations.RootContext;
import org.androidannotations.annotations.UiThread;

import java.util.ArrayList;
import java.util.List;

import charitee.bananasockets.io.charitee.R;
import charitee.bananasockets.io.charitee.models.GeolocatedRequest;

/**
 * Created by codi on 11/10/2014.
 */
@EViewGroup(R.layout.list_request_view)
public class RequestListView extends BaseAdapter {
	@RootContext
	Context context;

	List<GeolocatedRequest> requests = new ArrayList<GeolocatedRequest>();

	@AfterInject
	protected void initAdapter() {
		this.refresh();
	}

	@Override
	public int getCount() {
		return requests.size();
	}

	@Override
	public Object getItem(int position) {
		return requests.get(position);
	}

	@Override
	public long getItemId(int position) {
		return position;
	}

	@Override
	public View getView(int position, View convertView, ViewGroup parent) {
		RequestItemView eventItemView = null;

		if (convertView == null) {
			eventItemView = RequestItemView_.build(context);
		} else {
			eventItemView = (RequestItemView) convertView;
		}

		eventItemView.bind((GeolocatedRequest) getItem(position));

		return eventItemView;
	}

	@Background
	public void refresh() {
		updateView();
	}

	@UiThread
	protected void updateView() {
		this.notifyDataSetChanged();
	}
}


package charitee.bananasockets.io.charitee.views.lists;

import android.content.Context;
import android.widget.LinearLayout;
import android.widget.TextView;

import org.androidannotations.annotations.EViewGroup;
import org.androidannotations.annotations.ViewById;

import charitee.bananasockets.io.charitee.R;
import charitee.bananasockets.io.charitee.models.GeolocatedRequest;

/**
 * Created by codi on 11/10/2014.
 */
@EViewGroup(R.layout.list_request_view)
public class RequestItemView extends LinearLayout{

	@ViewById
	TextView requestMessage;

	public RequestItemView(Context context) {
		super(context);
	}

	public void bind(GeolocatedRequest r){
		requestMessage.setText(r.getMessage());
	}

}

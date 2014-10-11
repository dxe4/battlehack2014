package charitee.bananasockets.io.charitee.activities;

import android.app.Activity;
import android.content.Context;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Bundle;
import android.os.Looper;
import android.widget.TextView;

import org.androidannotations.annotations.AfterViews;
import org.androidannotations.annotations.EActivity;
import org.androidannotations.annotations.UiThread;
import org.androidannotations.annotations.ViewById;

import charitee.bananasockets.io.charitee.R;


@EActivity(R.layout.activity_main) public class Main extends Activity {

	LocationManager locationManager;

	LocationListener locationListener = new LocationListener() {
		public void onLocationChanged(Location location) {
			updateLocation(location);
		}

		public void onStatusChanged(String provider, int status, Bundle extras) {}

		public void onProviderEnabled(String provider) {}

		public void onProviderDisabled(String provider) {}
	};

	@ViewById protected TextView geoResult;

	@AfterViews public void initLocationRequest() {
		locationManager = (LocationManager) this.getSystemService(Context.LOCATION_SERVICE);
		locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER, 1000, 0, locationListener);
		locationManager.requestLocationUpdates(LocationManager.NETWORK_PROVIDER, 1000, 0, locationListener);

		Location lastKnownLocation = locationManager.getLastKnownLocation(LocationManager.GPS_PROVIDER);

		if (lastKnownLocation != null) {
			geoResult.setText(lastKnownLocation.toString());
		}
	}

	@UiThread public void updateLocation(Location location) {
		geoResult.setText(location.toString());
	}
}

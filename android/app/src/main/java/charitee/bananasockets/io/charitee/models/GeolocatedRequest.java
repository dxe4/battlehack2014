package charitee.bananasockets.io.charitee.models;

import java.util.Date;

/**
 * GeolocatedRequest
 * Model referring to a geolocated user request, either a question or a media sharing request
 */
public class GeolocatedRequest {

	public enum RequestType { QUESTION, MEDIA_SHARING };

	private String message;

	private String fromName;

	private Date expiresAt;

	private RequestType requestType;

	private LatLong location;

	public String getMessage() {
		return message;
	}

	public void setMessage(String message) {
		this.message = message;
	}

	public String getFromName() {
		return fromName;
	}

	public void setFromName(String fromName) {
		this.fromName = fromName;
	}

	public Date getExpiresAt() {
		return expiresAt;
	}

	public void setExpiresAt(Date expiresAt) {
		this.expiresAt = expiresAt;
	}

	public RequestType getRequestType() {
		return requestType;
	}

	public void setRequestType(RequestType requestType) {
		this.requestType = requestType;
	}

	public LatLong getLocation() {
		return location;
	}

	public void setLocation(LatLong location) {
		this.location = location;
	}
}

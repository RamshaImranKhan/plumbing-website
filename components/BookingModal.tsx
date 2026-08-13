'use client';

import { FormEvent, useCallback, useEffect, useState } from 'react';

const SERVICES = [
  'Emergency Plumbing',
  'Drain Cleaning',
  'Water Heater Repair',
  'Water Heater Installation',
  'Leak Detection',
  'Toilet Repair',
  'Faucet Repair',
  'Garbage Disposal',
  'Sewer Line Repair',
  'Plumbing Inspection',
  'Other / Not Sure',
];

const OMAHA_PREFIXES = ['680', '681', '683', '515', '684', '686'];

const BOOKING_TRIGGERS =
  'a.btn-book, a.mobile-cta-book, a.btn-hero-book, [data-book-open], a[href*="#quote"], a[href*="#book"]';

type FormState = {
  zip: string;
  service: string;
  date: string;
  time: string;
  name: string;
  phone: string;
  email: string;
  address: string;
  notes: string;
  consent: boolean;
};

const emptyForm = (): FormState => ({
  zip: '',
  service: '',
  date: '',
  time: '',
  name: '',
  phone: '',
  email: '',
  address: '',
  notes: '',
  consent: false,
});

export default function BookingModal() {
  const [open, setOpen] = useState(false);
  const [step, setStep] = useState(1);
  const [form, setForm] = useState<FormState>(emptyForm);
  const [zipMsg, setZipMsg] = useState('');
  const [zipOk, setZipOk] = useState(false);

  const isStepValid = (s: number) => {
    if (s === 1) {
      const zip = form.zip.trim();
      return /^\d{5}$/.test(zip) && OMAHA_PREFIXES.includes(zip.slice(0, 3));
    }
    if (s === 2) return Boolean(form.service);
    if (s === 3) return Boolean(form.date && form.time);
    if (s === 4) {
      return Boolean(
        form.name.trim() &&
          form.phone.trim() &&
          form.email.trim() &&
          form.address.trim() &&
          /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.email.trim()),
      );
    }
    return true;
  };

  const validateZipWithMessage = () => {
    const zip = form.zip.trim();
    if (!/^\d{5}$/.test(zip)) {
      setZipMsg('Please enter a valid 5-digit zip code.');
      setZipOk(false);
      return false;
    }
    if (!OMAHA_PREFIXES.includes(zip.slice(0, 3))) {
      setZipMsg('We may not service this area. Call (402) 922-8334 to confirm.');
      setZipOk(false);
      return false;
    }
    setZipMsg('Great — we service your area!');
    setZipOk(true);
    return true;
  };

  const openModal = useCallback(() => {
    setOpen(true);
    setStep(1);
    setForm(emptyForm());
    setZipMsg('');
    setZipOk(false);
  }, []);

  const closeModal = useCallback(() => {
    setOpen(false);
  }, []);

  useEffect(() => {
    document.body.classList.toggle('booking-modal-open', open);
    return () => document.body.classList.remove('booking-modal-open');
  }, [open]);

  useEffect(() => {
    window.openBookingModal = openModal;

    const onClick = (e: MouseEvent) => {
      const target = e.target as Element | null;
      const trigger = target?.closest(BOOKING_TRIGGERS);
      if (!trigger) return;
      e.preventDefault();
      e.stopPropagation();
      openModal();
    };

    const onHash = () => {
      const hash = window.location.hash.replace('#', '');
      if (hash === 'book' || hash === 'quote') {
        openModal();
        history.replaceState(null, '', window.location.pathname + window.location.search);
      }
    };

    document.addEventListener('click', onClick, true);
    window.addEventListener('hashchange', onHash);
    onHash();

    return () => {
      document.removeEventListener('click', onClick, true);
      window.removeEventListener('hashchange', onHash);
      delete window.openBookingModal;
    };
  }, [openModal]);

  useEffect(() => {
    if (!open) return;
    const onKey = (e: KeyboardEvent) => {
      if (e.key === 'Escape') closeModal();
    };
    document.addEventListener('keydown', onKey);
    return () => document.removeEventListener('keydown', onKey);
  }, [open, closeModal]);

  const onContinue = () => {
    if (step === 1 && !validateZipWithMessage()) return;
    if (!isStepValid(step)) return;
    setStep((s) => Math.min(s + 1, 5));
  };

  const onSubmit = (e: FormEvent) => {
    e.preventDefault();
    if (!isStepValid(4)) return;

    const toastLayer = document.getElementById('toastLayer');
    if (toastLayer) {
      const toast = document.createElement('div');
      toast.className = 'toast success';
      toast.setAttribute('role', 'status');
      toast.textContent = "Thank you! Your booking request has been submitted. We'll contact you shortly.";
      toastLayer.appendChild(toast);
      window.setTimeout(() => toast.remove(), 5000);
    }

    closeModal();
  };

  const today = new Date().toISOString().split('T')[0];
  const steps = ['Location', 'Service', 'Schedule', 'Contact', 'Additional'];

  return (
    <div
      id="bookingModal"
      className={`booking-modal${open ? ' is-visible' : ''}`}
      hidden={!open}
      aria-hidden={!open}
      role="dialog"
      aria-modal="true"
      aria-labelledby="bookingModalTitle"
    >
      <div className="booking-modal-backdrop" onClick={closeModal} tabIndex={-1} />
      <div className="booking-modal-panel" role="document">
        <div className="booking-modal-header">
          <img
            className="booking-modal-logo"
            src="/assets/logos/brands/benjamin-franklin.png"
            alt="Benjamin Franklin Plumbing"
            width={120}
            height={48}
          />
          <div className="booking-modal-heading">
            <p className="booking-modal-location">Benjamin Franklin Plumbing – Omaha</p>
            <h2 id="bookingModalTitle">Book Online Now</h2>
          </div>
          <button type="button" className="booking-modal-close" onClick={closeModal} aria-label="Close booking form">
            ×
          </button>
        </div>

        <ol className="booking-steps" aria-label="Booking progress">
          {steps.map((label, i) => (
            <li
              key={label}
              className={`booking-step${step === i + 1 ? ' is-active' : ''}${step > i + 1 ? ' is-complete' : ''}`}
              data-step={i + 1}
            >
              <span className="booking-step-icon" aria-hidden="true" />
              <span className="booking-step-label">{label}</span>
            </li>
          ))}
        </ol>

        <form className="booking-form" id="bookingForm" onSubmit={onSubmit} noValidate>
          {step === 1 && (
            <div className="booking-pane is-active" data-pane="1">
              <div className="booking-illustration">
                <img src="/assets/images/bfp-van-orange.png" alt="" width={280} height={160} loading="lazy" />
              </div>
              <h3 className="booking-pane-title">Where are you?</h3>
              <p className="booking-pane-desc">Enter your zip or postal code so we can check if we provide service in your area.</p>
              <div className="form-group">
                <label htmlFor="bookingZip">Zip Code <span className="req">*</span></label>
                <input
                  type="text"
                  id="bookingZip"
                  inputMode="numeric"
                  maxLength={5}
                  required
                  autoComplete="postal-code"
                  value={form.zip}
                  onChange={(e) => {
                    setForm({ ...form, zip: e.target.value.replace(/\D/g, '').slice(0, 5) });
                    setZipMsg('');
                    setZipOk(false);
                  }}
                />
                {zipMsg && <p className={`booking-field-msg ${zipOk ? 'is-success' : 'is-error'}`} role="status">{zipMsg}</p>}
              </div>
            </div>
          )}

          {step === 2 && (
            <div className="booking-pane is-active" data-pane="2">
              <h3 className="booking-pane-title">What service do you need?</h3>
              <p className="booking-pane-desc">Select the plumbing service that best matches your request.</p>
              <div className="form-group">
                <label htmlFor="bookingService">Service <span className="req">*</span></label>
                <select
                  id="bookingService"
                  required
                  value={form.service}
                  onChange={(e) => setForm({ ...form, service: e.target.value })}
                >
                  <option value="">Choose a service…</option>
                  {SERVICES.map((s) => (
                    <option key={s} value={s}>{s}</option>
                  ))}
                </select>
              </div>
            </div>
          )}

          {step === 3 && (
            <div className="booking-pane is-active" data-pane="3">
              <h3 className="booking-pane-title">When works for you?</h3>
              <p className="booking-pane-desc">Pick your preferred appointment date and time window.</p>
              <div className="form-row">
                <div className="form-group">
                  <label htmlFor="bookingDate">Preferred Date <span className="req">*</span></label>
                  <input
                    type="date"
                    id="bookingDate"
                    required
                    min={today}
                    value={form.date}
                    onChange={(e) => setForm({ ...form, date: e.target.value })}
                  />
                </div>
                <div className="form-group">
                  <label htmlFor="bookingTime">Preferred Time <span className="req">*</span></label>
                  <select
                    id="bookingTime"
                    required
                    value={form.time}
                    onChange={(e) => setForm({ ...form, time: e.target.value })}
                  >
                    <option value="">Select a time…</option>
                    <option value="morning">Morning (8am – 12pm)</option>
                    <option value="afternoon">Afternoon (12pm – 4pm)</option>
                    <option value="evening">Evening (4pm – 8pm)</option>
                    <option value="asap">As Soon As Possible</option>
                  </select>
                </div>
              </div>
            </div>
          )}

          {step === 4 && (
            <div className="booking-pane is-active" data-pane="4">
              <h3 className="booking-pane-title">How can we reach you?</h3>
              <p className="booking-pane-desc">Tell us who to contact and where the service is needed.</p>
              <div className="form-row">
                <div className="form-group">
                  <label htmlFor="bookingName">Full Name <span className="req">*</span></label>
                  <input type="text" id="bookingName" required autoComplete="name" value={form.name} onChange={(e) => setForm({ ...form, name: e.target.value })} />
                </div>
                <div className="form-group">
                  <label htmlFor="bookingPhone">Phone <span className="req">*</span></label>
                  <input type="tel" id="bookingPhone" required autoComplete="tel" value={form.phone} onChange={(e) => setForm({ ...form, phone: e.target.value })} />
                </div>
              </div>
              <div className="form-group">
                <label htmlFor="bookingEmail">Email <span className="req">*</span></label>
                <input type="email" id="bookingEmail" required autoComplete="email" value={form.email} onChange={(e) => setForm({ ...form, email: e.target.value })} />
              </div>
              <div className="form-group">
                <label htmlFor="bookingAddress">Street Address <span className="req">*</span></label>
                <input type="text" id="bookingAddress" required autoComplete="street-address" value={form.address} onChange={(e) => setForm({ ...form, address: e.target.value })} />
              </div>
            </div>
          )}

          {step === 5 && (
            <div className="booking-pane is-active" data-pane="5">
              <h3 className="booking-pane-title">Anything else we should know?</h3>
              <p className="booking-pane-desc">Share details about your plumbing issue or special instructions.</p>
              <div className="form-group">
                <label htmlFor="bookingNotes">Additional Details</label>
                <textarea id="bookingNotes" rows={4} placeholder="Describe your plumbing issue…" value={form.notes} onChange={(e) => setForm({ ...form, notes: e.target.value })} />
              </div>
              <label className="checkbox-label">
                <input type="checkbox" checked={form.consent} onChange={(e) => setForm({ ...form, consent: e.target.checked })} />
                <span>I consent to receive marketing SMS from BFP. Msg &amp; data rates may apply.</span>
              </label>
            </div>
          )}

          <div className="booking-modal-footer">
            <a href="tel:4029228334" className="booking-emergency">Emergency</a>
            <div className="booking-footer-actions">
              {step > 1 && (
                <button type="button" className="btn btn-booking-back" onClick={() => setStep((s) => s - 1)}>
                  Back
                </button>
              )}
              {step < 5 ? (
                <button type="button" className="btn btn-booking-continue" onClick={onContinue} disabled={!isStepValid(step)}>
                  Continue
                </button>
              ) : (
                <button type="submit" className="btn btn-booking-submit">
                  Submit Booking
                </button>
              )}
            </div>
          </div>
        </form>
      </div>
    </div>
  );
}

declare global {
  interface Window {
    openBookingModal?: () => void;
  }
}

/* -*- c++ -*- */
/*
 * Copyright 2022 shunyu.
 *
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include "ofdm_sync_shunyu_impl.h"
#include <gnuradio/io_signature.h>

#include <gnuradio/blocks/complex_to_arg.h>
#include <gnuradio/blocks/complex_to_mag_squared.h>
#include <gnuradio/blocks/conjugate_cc.h>
#include <gnuradio/blocks/delay.h>
#include <gnuradio/blocks/divide.h>
#include <gnuradio/blocks/multiply.h>
#include <gnuradio/blocks/sample_and_hold.h>
#include <gnuradio/filter/fir_filter_blk.h>



namespace gr {
namespace customModule {

ofdm_sync_shunyu::sptr
ofdm_sync_shunyu::make(int fft_len,int cp_len,bool use_even_carriers,float threshold)
{
  return gnuradio::get_initial_sptr(
    new ofdm_sync_shunyu_impl(fft_len, cp_len, use_even_carriers, threshold));
}


    /*
     * The private constructor
     */
ofdm_sync_shunyu_impl::ofdm_sync_shunyu_impl(int fft_len,int cp_len,bool use_even_carriers,float threshold)
  : gr::hier_block2("ofdm_sync_shunyu",
              gr::io_signature::make(1, 1, sizeof(gr_complex)),
#ifndef SYNC_ADD_DEBUG_OUTPUT
              gr::io_signature::make2(2, 2, sizeof(float), sizeof(unsigned char)))
#else
              gr::io_signature::make3(3, 3, sizeof(float), sizeof(unsigned char), sizeof(float)))
#endif
{
  std::vector<float> ma_taps(fft_len / 2, 1.0);
  gr::blocks::delay::sptr delay(
    gr::blocks::delay::make(sizeof(gr_complex), fft_len / 2));
  gr::blocks::conjugate_cc::sptr delay_conjugate(gr::blocks::conjugate_cc::make());
  gr::blocks::multiply_cc::sptr delay_corr(gr::blocks::multiply_cc::make());
  gr::filter::fir_filter_ccf::sptr delay_ma(gr::filter::fir_filter_ccf::make(
    1, std::vector<float>(fft_len / 2, use_even_carriers ? 1.0 : -1.0)));
  gr::blocks::complex_to_mag_squared::sptr delay_magsquare(
    gr::blocks::complex_to_mag_squared::make());
  gr::blocks::divide_ff::sptr delay_normalize(gr::blocks::divide_ff::make());

  gr::blocks::complex_to_mag_squared::sptr normalizer_magsquare(
    gr::blocks::complex_to_mag_squared::make());
  gr::filter::fir_filter_fff::sptr normalizer_ma(
    gr::filter::fir_filter_fff::make(1, std::vector<float>(fft_len, 0.5)));
  gr::blocks::multiply_ff::sptr normalizer_square(gr::blocks::multiply_ff::make());

  gr::blocks::complex_to_arg::sptr peak_to_angle(gr::blocks::complex_to_arg::make());
  gr::blocks::sample_and_hold_ff::sptr sample_and_hold(
    gr::blocks::sample_and_hold_ff::make());

  gr::blocks::plateau_detector_fb::sptr plateau_detector(
    gr::blocks::plateau_detector_fb::make(cp_len, threshold));

  // store plateau detector for use in callback setting threshold
  d_plateau_detector = plateau_detector;

  // Delay Path
  connect(self(), 0, delay, 0);
  connect(delay, 0, delay_conjugate, 0);
  connect(delay_conjugate, 0, delay_corr, 1);
  connect(self(), 0, delay_corr, 0);
  connect(delay_corr, 0, delay_ma, 0);
  connect(delay_ma, 0, delay_magsquare, 0);
  connect(delay_magsquare, 0, delay_normalize, 0);
  // Energy Path
  connect(self(), 0, normalizer_magsquare, 0);
  connect(normalizer_magsquare, 0, normalizer_ma, 0);
  connect(normalizer_ma, 0, normalizer_square, 0);
  connect(normalizer_ma, 0, normalizer_square, 1);
  connect(normalizer_square, 0, delay_normalize, 1);
  // Fine frequency estimate (output 0)
  connect(delay_ma, 0, peak_to_angle, 0);
  connect(peak_to_angle, 0, sample_and_hold, 0);
  connect(sample_and_hold, 0, self(), 0);
  // Peak detect (output 1)
  connect(delay_normalize, 0, plateau_detector, 0);
  connect(plateau_detector, 0, sample_and_hold, 1);
  connect(plateau_detector, 0, self(), 1);
#ifdef SYNC_ADD_DEBUG_OUTPUT
  // Debugging: timing metric (output 2)
  connect(delay_normalize, 0, self(), 2);
#endif
}

ofdm_sync_shunyu_impl::~ofdm_sync_shunyu_impl(){}

void ofdm_sync_shunyu_impl::set_threshold(float threshold)
{
    d_plateau_detector->set_threshold(threshold);
}

float ofdm_sync_shunyu_impl::threshold() const { return d_plateau_detector->threshold(); }

} /* namespace customModule */
} /* namespace gr */


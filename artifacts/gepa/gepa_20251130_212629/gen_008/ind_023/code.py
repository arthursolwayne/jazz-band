
import pretty_midi
import numpy as np

# Initialize the PrettyMIDI object with 4/4 time and 160 BPM
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create a time signature of 4/4
time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)
pm.time_signature_changes.append(time_signature)

# Set the key signature to D minor (key number 19)
key_signature = pretty_midi.KeySignature(key_number=19, time=0)
pm.key_signature_changes.append(key_signature)

# Define the duration of one beat in seconds
beat_duration = 60.0 / 160.0  # 160 BPM => 0.375 seconds per beat
bar_duration = 4 * beat_duration  # 1.5 seconds per bar

# Create instruments for each player
# 1. Drum Kit (Little Ray)
drum_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')  # For MIDI mapping
drum_instrument = pretty_midi.Instrument(program=drum_program)
pm.instruments.append(drum_instrument)

# 2. Bass (Marcus)
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
bass_instrument = pretty_midi.Instrument(program=bass_program)
pm.instruments.append(bass_instrument)

# 3. Piano (Diane)
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
piano_instrument = pretty_midi.Instrument(program=piano_program)
pm.instruments.append(piano_instrument)

# 4. Tenor Sax (You)
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
sax_instrument = pretty_midi.Instrument(program=sax_program)
pm.instruments.append(sax_instrument)

# --- Bar 1: Little Ray (Drums) ---
# Kick on 1 and 3, Snare on 2 and 4, Hi-Hat on every 8th
bar_start = 0
for i in range(8):
    time = bar_start + (i * beat_duration / 2)
    # Hi-Hat: Cymbal 1 (note 42)
    hi_hat = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + beat_duration / 2)
    drum_instrument.notes.append(hi_hat)

# Kick on 1 and 3
kick_notes = [0, 2]
for i in kick_notes:
    time = bar_start + (i * beat_duration)
    kick = pretty_midi.Note(velocity=110, pitch=36, start=time, end=time + beat_duration / 2)
    drum_instrument.notes.append(kick)

# Snare on 2 and 4
snare_notes = [1, 3]
for i in snare_notes:
    time = bar_start + (i * beat_duration)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + beat_duration / 2)
    drum_instrument.notes.append(snare)

# --- Bar 2: Everybody in ---
bar_start = bar_duration

# -- Bass (Marcus) -- Walking line in D minor
# Dm7: D, F, A, C
# Walking line: D -> F -> A -> C (chromatic approach)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=bar_start, end=bar_start + beat_duration),
    pretty_midi.Note(velocity=90, pitch=64, start=bar_start + beat_duration, end=bar_start + 2 * beat_duration),
    pretty_midi.Note(velocity=90, pitch=67, start=bar_start + 2 * beat_duration, end=bar_start + 3 * beat_duration),
    pretty_midi.Note(velocity=90, pitch=60, start=bar_start + 3 * beat_duration, end=bar_start + 4 * beat_duration)
]
bass_instrument.notes.extend(bass_notes)

# -- Piano (Diane) -- 7th chords: Dm7, G7, Cm7, F7
# Comp on 2 and 4, 7th chords
chords = [
    # Dm7 (D, F, A, C) on beat 2
    pretty_midi.Note(velocity=80, pitch=62, start=bar_start + beat_duration, end=bar_start + 2 * beat_duration),
    pretty_midi.Note(velocity=80, pitch=64, start=bar_start + beat_duration, end=bar_start + 2 * beat_duration),
    pretty_midi.Note(velocity=80, pitch=67, start=bar_start + beat_duration, end=bar_start + 2 * beat_duration),
    pretty_midi.Note(velocity=80, pitch=60, start=bar_start + beat_duration, end=bar_start + 2 * beat_duration),

    # G7 (G, B, D, F) on beat 4
    pretty_midi.Note(velocity=80, pitch=67, start=bar_start + 3 * beat_duration, end=bar_start + 4 * beat_duration),
    pretty_midi.Note(velocity=80, pitch=71, start=bar_start + 3 * beat_duration, end=bar_start + 4 * beat_duration),
    pretty_midi.Note(velocity=80, pitch=69, start=bar_start + 3 * beat_duration, end=bar_start + 4 * beat_duration),
    pretty_midi.Note(velocity=80, pitch=64, start=bar_start + 3 * beat_duration, end=bar_start + 4 * beat_duration)
]
piano_instrument.notes.extend(chords)

# -- Drums (Little Ray) continue on same pattern
for i in range(8):
    time = bar_start + (i * beat_duration / 2)
    # Hi-Hat
    hi_hat = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + beat_duration / 2)
    drum_instrument.notes.append(hi_hat)

# Kick on 1 and 3
kick_notes = [0, 2]
for i in kick_notes:
    time = bar_start + (i * beat_duration)
    kick = pretty_midi.Note(velocity=110, pitch=36, start=time, end=time + beat_duration / 2)
    drum_instrument.notes.append(kick)

# Snare on 2 and 4
snare_notes = [1, 3]
for i in snare_notes:
    time = bar_start + (i * beat_duration)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + beat_duration / 2)
    drum_instrument.notes.append(snare)

# --- Bar 3: Continue with same rhythm and comping ---
bar_start = 2 * bar_duration

# Bass continues
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=bar_start, end=bar_start + beat_duration),
    pretty_midi.Note(velocity=90, pitch=62, start=bar_start + beat_duration, end=bar_start + 2 * beat_duration),
    pretty_midi.Note(velocity=90, pitch=64, start=bar_start + 2 * beat_duration, end=bar_start + 3 * beat_duration),
    pretty_midi.Note(velocity=90, pitch=67, start=bar_start + 3 * beat_duration, end=bar_start + 4 * beat_duration)
]
bass_instrument.notes.extend(bass_notes)

# Piano: Comping on 2 and 4, Dm7 -> G7 -> Cm7 -> F7
chords = [
    # Dm7 on beat 2
    pretty_midi.Note(velocity=80, pitch=62, start=bar_start + beat_duration, end=bar_start + 2 * beat_duration),
    pretty_midi.Note(velocity=80, pitch=64, start=bar_start + beat_duration, end=bar_start + 2 * beat_duration),
    pretty_midi.Note(velocity=80, pitch=67, start=bar_start + beat_duration, end=bar_start + 2 * beat_duration),
    pretty_midi.Note(velocity=80, pitch=60, start=bar_start + beat_duration, end=bar_start + 2 * beat_duration),

    # G7 on beat 4
    pretty_midi.Note(velocity=80, pitch=67, start=bar_start + 3 * beat_duration, end=bar_start + 4 * beat_duration),
    pretty_midi.Note(velocity=80, pitch=71, start=bar_start + 3 * beat_duration, end=bar_start + 4 * beat_duration),
    pretty_midi.Note(velocity=80, pitch=69, start=bar_start + 3 * beat_duration, end=bar_start + 4 * beat_duration),
    pretty_midi.Note(velocity=80, pitch=64, start=bar_start + 3 * beat_duration, end=bar_start + 4 * beat_duration)
]
piano_instrument.notes.extend(chords)

# Drums: Same as before
for i in range(8):
    time = bar_start + (i * beat_duration / 2)
    hi_hat = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + beat_duration / 2)
    drum_instrument.notes.append(hi_hat)

# Kick and snare as before
for i in [0, 2]:
    kick = pretty_midi.Note(velocity=110, pitch=36, start=bar_start + i * beat_duration, end=bar_start + i * beat_duration + beat_duration / 2)
    drum_instrument.notes.append(kick)
for i in [1, 3]:
    snare = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + i * beat_duration, end=bar_start + i * beat_duration + beat_duration / 2)
    drum_instrument.notes.append(snare)

# --- Bar 4: Tenor Sax (You) -- Motif: D, F, A (Dm7) hanging on the last note
bar_start = 3 * bar_duration

# Tenor motif: D (62), F (64), A (67) – start on beat 1, end on beat 2
# Leave it hanging on A (67) at the end of the bar
note1 = pretty_midi.Note(velocity=100, pitch=62, start=bar_start, end=bar_start + beat_duration)
note2 = pretty_midi.Note(velocity=100, pitch=64, start=bar_start + beat_duration, end=bar_start + 2 * beat_duration)
note3 = pretty_midi.Note(velocity=100, pitch=67, start=bar_start + 2 * beat_duration, end=bar_start + 4 * beat_duration)

sax_instrument.notes.extend([note1, note2, note3])

# Save the MIDI file
pm.write("dante_intro.mid")

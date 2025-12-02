
import pretty_midi
import numpy as np

# Create a pretty_midi object with tempo 160 BPM
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create a time signature track
time_signature = pretty_midi.TimeSignature(4, 4, 0)
pm.time_signature_changes.append(time_signature)

# Create instrument tracks for each player
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Drum Kit')
sax_program = pretty_midi.instrument_name_to_program('Alto Sax')

bass_instrument = pretty_midi.Instrument(program=bass_program)
piano_instrument = pretty_midi.Instrument(program=piano_program)
drums_instrument = pretty_midi.Instrument(program=drums_program)
sax_instrument = pretty_midi.Instrument(program=sax_program)

pm.instruments.append(bass_instrument)
pm.instruments.append(piano_instrument)
pm.instruments.append(drums_instrument)
pm.instruments.append(sax_instrument)

# Define the time for each bar (160 BPM => 60 / 160 = 0.375 seconds per beat)
bar_length = 1.5  # 4/4 time, 160 BPM, 4 bars = 6 seconds
beat_length = 0.375
note_length = 0.375  # quarter note
note_rest = 0.375  # quarter rest

# ========== BAR 1 - Little Ray on drums only ==========
# Kick on beat 1 and 3
drums_instrument.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375))
drums_instrument.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=0.75, end=1.125))

# Snare on beat 2 and 4
drums_instrument.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=0.375, end=0.75))
drums_instrument.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=1.125, end=1.5))

# Hi-hat every eighth note
for i in range(0, 8):
    start = i * beat_length / 2
    end = start + beat_length / 2
    if i % 2 == 0:
        # Closed hi-hat
        drums_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=end))
    else:
        # Open hi-hat
        drums_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=46, start=start, end=end))

# ========== BAR 2 - Everyone in, sax motif starts ==========
# Sax: A short motif in Fm (F, Ab, Bb, D, Gb) — not a scale, but a question
sax_notes = [
    (64, 0.0, 0.375),    # F
    (60, 0.375, 0.75),   # Ab
    (62, 0.75, 1.125),   # Bb
    (67, 1.125, 1.5),    # D
]

for pitch, start, end in sax_notes:
    sax_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

# Bass: Walking line in Fm
bass_notes = [
    (43, 0.0, 0.375),    # F
    (41, 0.375, 0.75),   # Eb
    (42, 0.75, 1.125),   # D
    (44, 1.125, 1.5),    # F
]

for pitch, start, end in bass_notes:
    bass_instrument.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end))

# Piano: Comp on 2 and 4 with 7th chords
# Fm7 = F, Ab, Bb, Db (but we'll use F, Ab, Bb, C for a more modern, dissonant feel)
piano_notes = [
    (64, 0.375, 0.75),   # F
    (60, 0.375, 0.75),   # Ab
    (62, 0.375, 0.75),   # Bb
    (67, 0.375, 0.75),   # C
    (64, 1.125, 1.5),    # F
    (60, 1.125, 1.5),    # Ab
    (62, 1.125, 1.5),    # Bb
    (67, 1.125, 1.5),    # C
]

for pitch, start, end in piano_notes:
    piano_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

# ========== BAR 3 - Sax motif repeats, slightly altered ==========
# Motif variation — ends on a rest to create tension
sax_notes = [
    (64, 1.5, 1.875),    # F
    (60, 1.875, 2.25),   # Ab
    (62, 2.25, 2.625),   # Bb
    (67, 2.625, 3.0),    # D (rest)
]

for pitch, start, end in sax_notes:
    sax_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

# Bass: Walking line again
bass_notes = [
    (43, 1.5, 1.875),    # F
    (41, 1.875, 2.25),   # Eb
    (42, 2.25, 2.625),   # D
    (44, 2.625, 3.0),    # F
]

for pitch, start, end in bass_notes:
    bass_instrument.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end))

# Piano: Comp on 2 and 4
piano_notes = [
    (64, 1.875, 2.25),   # F
    (60, 1.875, 2.25),   # Ab
    (62, 1.875, 2.25),   # Bb
    (67, 1.875, 2.25),   # C
    (64, 2.625, 3.0),    # F
    (60, 2.625, 3.0),    # Ab
    (62, 2.625, 3.0),    # Bb
    (67, 2.625, 3.0),    # C
]

for pitch, start, end in piano_notes:
    piano_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

# Drums: Repeat pattern
for i in range(0, 8):
    start = (1.5 + (i * beat_length / 2))
    end = start + beat_length / 2
    if i % 2 == 0:
        drums_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=end))
    else:
        drums_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=46, start=start, end=end))

# ========== BAR 4 - Sax motif resolves (or doesn't) ==========
# Ending on an unresolved note — Gb (F#) — to leave the question hanging
sax_notes = [
    (65, 3.0, 3.375),    # Gb (F#)
    (65, 3.375, 3.75),   # Gb (F#)
    (65, 3.75, 4.125),   # Gb (F#)
    (65, 4.125, 4.5),    # Gb (F#)
]

for pitch, start, end in sax_notes:
    sax_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

# Bass: Walking line
bass_notes = [
    (43, 3.0, 3.375),    # F
    (41, 3.375, 3.75),   # Eb
    (42, 3.75, 4.125),   # D
    (44, 4.125, 4.5),    # F
]

for pitch, start, end in bass_notes:
    bass_instrument.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end))

# Piano: Comp on 2 and 4
piano_notes = [
    (64, 3.375, 3.75),   # F
    (60, 3.375, 3.75),   # Ab
    (62, 3.375, 3.75),   # Bb
    (67, 3.375, 3.75),   # C
    (64, 4.125, 4.5),    # F
    (60, 4.125, 4.5),    # Ab
    (62, 4.125, 4.5),    # Bb
    (67, 4.125, 4.5),    # C
]

for pitch, start, end in piano_notes:
    piano_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

# Drums: Repeat pattern
for i in range(0, 8):
    start = (3.0 + (i * beat_length / 2))
    end = start + beat_length / 2
    if i % 2 == 0:
        drums_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=end))
    else:
        drums_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=46, start=start, end=end))

# Write out the MIDI file
pm.write("dante_intro.mid")

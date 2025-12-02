
import pretty_midi

# Initialize MIDI with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick_time = start + 0.0
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick)

    kick_time = start + 0.75
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick)

    # Snare on 2 and 4
    snare_time = start + 0.375
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare)

    snare_time = start + 1.125
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare)

    # Hi-hat on every eighth
    for i in range(8):
        hihat_time = start + (i * 0.375)
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + 0.05)
        drums.notes.append(hihat)

# Bar 2: Everyone comes in (1.5 - 3.0s)
# Sax starts with a short, emotional motif in Fm
# Fm = F, Ab, Bb, C, Eb
# Motif: F - Ab - Bb - C (ascending), then repeat with a twist

start = 1.5
note_durations = 0.45  # 450ms per note

# F (Ab3) (pitch 66)
note = pretty_midi.Note(velocity=110, pitch=66, start=start, end=start + note_durations)
sax.notes.append(note)

# Ab (Ab3) (pitch 64)
note = pretty_midi.Note(velocity=110, pitch=64, start=start + note_durations, end=start + note_durations * 2)
sax.notes.append(note)

# Bb (Bb3) (pitch 62)
note = pretty_midi.Note(velocity=110, pitch=62, start=start + note_durations * 2, end=start + note_durations * 3)
sax.notes.append(note)

# C (C4) (pitch 60)
note = pretty_midi.Note(velocity=110, pitch=60, start=start + note_durations * 3, end=start + note_durations * 4)
sax.notes.append(note)

# Bass: Chromatic walking line in Fm
# F - Gb - G - Ab - A - Bb - B - C - Db - D - Eb - F
# Start at 1.5s

bass_notes = [
    (66, 1.5),
    (65, 1.625),
    (67, 1.75),
    (64, 1.875),
    (68, 2.0),
    (62, 2.125),
    (69, 2.25),
    (60, 2.375),
    (61, 2.5),
    (63, 2.625),
    (66, 2.75)
]

for pitch, time in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.125)
    bass.notes.append(note)

# Piano: Comping with 7th chords on offbeats
# Fm7 = F, Ab, Bb, C
# Comp on offbeats (0.375, 1.125, 1.875, 2.625) in the bar

for time in [1.875, 2.625]:
    # Fm7 chord (F, Ab, Bb, C)
    for pitch in [66, 64, 62, 60]:
        note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.125)
        piano.notes.append(note)

# Bar 3: Sax continues motif with variation (3.0 - 4.5s)
# Play the same motif again but with a slight chromatic shift

start = 3.0
note_durations = 0.45

# F (Ab3) (pitch 66)
note = pretty_midi.Note(velocity=110, pitch=66, start=start, end=start + note_durations)
sax.notes.append(note)

# Ab (Ab3) (pitch 64)
note = pretty_midi.Note(velocity=110, pitch=64, start=start + note_durations, end=start + note_durations * 2)
sax.notes.append(note)

# Bb (Bb3) (pitch 62)
note = pretty_midi.Note(velocity=110, pitch=62, start=start + note_durations * 2, end=start + note_durations * 3)
sax.notes.append(note)

# C (C4) (pitch 60)
note = pretty_midi.Note(velocity=110, pitch=60, start=start + note_durations * 3, end=start + note_durations * 4)
sax.notes.append(note)

# Bass continues walking line
start = 3.0
bass_notes = [
    (66, 3.0),
    (65, 3.125),
    (67, 3.25),
    (64, 3.375),
    (68, 3.5),
    (62, 3.625),
    (69, 3.75),
    (60, 3.875),
    (61, 4.0),
    (63, 4.125),
    (66, 4.25)
]

for pitch, time in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.125)
    bass.notes.append(note)

# Piano: Comp on offbeats again
for time in [3.875, 4.625]:
    for pitch in [66, 64, 62, 60]:
        note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.125)
        piano.notes.append(note)

# Bar 4: Sax finishes the motif, leaves it hanging (4.5 - 6.0s)
# Play the opening note again, then end on a sustained note

start = 4.5
note_durations = 0.45

# F (Ab3) (pitch 66)
note = pretty_midi.Note(velocity=110, pitch=66, start=start, end=start + note_durations)
sax.notes.append(note)

# C (C4) (pitch 60) sustained
note = pretty_midi.Note(velocity=110, pitch=60, start=start + note_durations, end=start + note_durations * 2)
sax.notes.append(note)

# Bass: End with a resolution to F
note = pretty_midi.Note(velocity=90, pitch=66, start=4.5, end=4.5 + 0.25)
bass.notes.append(note)

# Piano: Resolving chord on the last beat
# Fm7 again on the last offbeat
for pitch in [66, 64, 62, 60]:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=5.625, end=5.625 + 0.125)
    piano.notes.append(note)

# Drums in Bar 4: Same pattern as Bar 1
for bar in range(1):
    start = 4.5
    # Kick on 1 and 3
    kick_time = start + 0.0
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick)

    kick_time = start + 0.75
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick)

    # Snare on 2 and 4
    snare_time = start + 0.375
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare)

    snare_time = start + 1.125
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare)

    # Hi-hat on every eighth
    for i in range(8):
        hihat_time = start + (i * 0.375)
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + 0.05)
        drums.notes.append(hihat)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

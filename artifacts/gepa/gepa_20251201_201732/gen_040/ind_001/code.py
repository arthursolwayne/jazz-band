
import pretty_midi

# Create a new MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments for each member of the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Upright Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes
DRUM_KICK = 36
DRUM_SNARE = 38
DRUM_HIHAT = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_length = 1.5  # seconds per bar at 160 BPM

# Bar 1: Drums only
for beat in range(4):  # 4 beats per bar
    time = beat * bar_length / 4
    if beat == 0 or beat == 2:
        # Kick on 1 and 3
        note = pretty_midi.Note(velocity=100, pitch=DRUM_KICK, start=time, end=time + 0.1)
        drums.notes.append(note)
    if beat == 1 or beat == 3:
        # Snare on 2 and 4
        note = pretty_midi.Note(velocity=100, pitch=DRUM_SNARE, start=time, end=time + 0.1)
        drums.notes.append(note)
    # Hi-hat on every eighth note
    for eighth in range(2):
        note = pretty_midi.Note(velocity=90, pitch=DRUM_HIHAT, start=time + eighth * 0.375, end=time + eighth * 0.375 + 0.05)
        drums.notes.append(note)

# Bar 2: Full ensemble
# Bass: Walking line (D2 to G2), roots and fifths with chromatic approaches
# D2 (MIDI 38) to G2 (MIDI 43)
# Bar 2: D (38) -> D# (39) -> G (43) -> G# (44)
for beat in range(4):
    time = 1.5 + (beat * bar_length / 4)
    if beat == 0:
        note = pretty_midi.Note(velocity=80, pitch=38, start=time, end=time + 0.1)
        bass.notes.append(note)
    elif beat == 1:
        note = pretty_midi.Note(velocity=80, pitch=39, start=time, end=time + 0.1)
        bass.notes.append(note)
    elif beat == 2:
        note = pretty_midi.Note(velocity=80, pitch=43, start=time, end=time + 0.1)
        bass.notes.append(note)
    elif beat == 3:
        note = pretty_midi.Note(velocity=80, pitch=44, start=time, end=time + 0.1)
        bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D - F# - A - C#)
note = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.5 + 0.1)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.5 + 0.1)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.5 + 0.1)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.5 + 0.1)
piano.notes.append(note)

# Bar 3: G7 (G - B - D - F#)
note = pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.0 + 0.1)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.0 + 0.1)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.0 + 0.1)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.0 + 0.1)
piano.notes.append(note)

# Bar 4: C7 (C - E - G - B)
note = pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.5 + 0.1)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.5 + 0.1)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.5 + 0.1)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.5 + 0.1)
piano.notes.append(note)

# Sax: Melody — one short motif, start it, leave it hanging, come back and finish it
# D (62) -> F# (67) -> D (62) -> F# (67) -> D (62)
# First two notes in bar 2 (start at 1.5)
note = pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.5 + 0.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=67, start=1.5, end=1.5 + 0.25)
sax.notes.append(note)
# Third note in bar 3 (start at 3.0)
note = pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.0 + 0.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.0 + 0.25)
sax.notes.append(note)
# Final note in bar 4 (start at 4.5)
note = pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.5 + 0.25)
sax.notes.append(note)

# Drums: Bar 2-4 — same pattern as bar 1
for bar in range(2, 4):
    for beat in range(4):
        time = 1.5 + (bar - 2) * bar_length + (beat * bar_length / 4)
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=DRUM_KICK, start=time, end=time + 0.1)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=DRUM_SNARE, start=time, end=time + 0.1)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=90, pitch=DRUM_HIHAT, start=time + eighth * 0.375, end=time + eighth * 0.375 + 0.05)
            drums.notes.append(note)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled

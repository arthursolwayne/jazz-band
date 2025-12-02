
import pretty_midi

# Initialize MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum note numbers
kick = 36
snare = 38
hihat = 42

# Bar 1 (0.0 - 1.5s): Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(4):
    time = beat * 0.375  # 0.375 seconds per beat
    # Kick on 1 and 3
    if beat % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.125)
        drums.notes.append(note)
    # Snare on 2 and 4
    if beat % 2 == 1:
        note = pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + 0.125)
        drums.notes.append(note)
    # Hihat on every eighth
    note = pretty_midi.Note(velocity=80, pitch=hihat, start=time, end=time + 0.125)
    drums.notes.append(note)

# Bar 2 (1.5 - 3.0s): Full quartet
# Bass line: Walking line with chromatic approaches
bass_notes = [
    (pretty_midi.Note(velocity=80, pitch=39, start=1.5, end=1.625)),  # Fm7 - F
    (pretty_midi.Note(velocity=80, pitch=40, start=1.625, end=1.75)),  # Fm7 - Gb
    (pretty_midi.Note(velocity=80, pitch=41, start=1.75, end=1.875)),  # Fm7 - G
    (pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.0)),  # Fm7 - Gb
    (pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.125)),  # Fm7 - Ab
    (pretty_midi.Note(velocity=80, pitch=43, start=2.125, end=2.25)),  # Fm7 - Bb
    (pretty_midi.Note(velocity=80, pitch=44, start=2.25, end=2.375)),  # Fm7 - B
    (pretty_midi.Note(velocity=80, pitch=43, start=2.375, end=2.5)),  # Fm7 - Bb
]

# Piano: 7th chords, comp on 2 and 4
# Fm7 = F, Ab, Bb, Db
piano_notes = [
    # Bar 2: Start on 2 and 4
    (pretty_midi.Note(velocity=90, pitch=53, start=1.625, end=1.875)),  # Ab
    (pretty_midi.Note(velocity=90, pitch=50, start=1.625, end=1.875)),  # F
    (pretty_midi.Note(velocity=90, pitch=48, start=1.625, end=1.875)),  # Bb
    (pretty_midi.Note(velocity=90, pitch=45, start=1.625, end=1.875)),  # Db
    # Bar 3: Start on 2 and 4
    (pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=2.875)),  # Ab
    (pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=2.875)),  # F
    (pretty_midi.Note(velocity=90, pitch=48, start=2.625, end=2.875)),  # Bb
    (pretty_midi.Note(velocity=90, pitch=45, start=2.625, end=2.875)),  # Db
]

# Drums: Same pattern for bars 2-4
for bar in range(2, 5):  # Bars 2, 3, 4
    for beat in range(4):
        time = (bar * 1.5) + (beat * 0.375)
        # Kick on 1 and 3
        if beat % 2 == 0:
            note = pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.125)
            drums.notes.append(note)
        # Snare on 2 and 4
        if beat % 2 == 1:
            note = pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + 0.125)
            drums.notes.append(note)
        # Hihat on every eighth
        note = pretty_midi.Note(velocity=80, pitch=hihat, start=time, end=time + 0.125)
        drums.notes.append(note)

# Sax: Start with a short motif, leave it hanging, come back to finish
# Fm7 - F, Ab, Bb, Db
# First bar: F (50), F (50)
# Second bar: Ab (53), Bb (48)
# Third bar: F (50), F (50)
# Fourth bar: F (50), Bb (48), F (50)

# Bar 2: Start the motif
note = pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.625)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=50, start=1.625, end=1.75)
sax.notes.append(note)

# Bar 3: Continue the motif
note = pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=48, start=2.375, end=2.5)
sax.notes.append(note)

# Bar 4: Finish the motif
note = pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.125)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=48, start=3.125, end=3.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=50, start=3.25, end=3.375)
sax.notes.append(note)

# Add notes to instruments
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")


import pretty_midi

# Create a new MIDI file with the specified tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments for each member of the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define MIDI note numbers for drum kit
kick = 36
snare = 38
hihat = 42

# --- BAR 1: Little Ray alone (0.0 - 1.5s) ---
# Drums only: kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Time in seconds per bar is 1.5s (BPM 160)
bar_duration = 1.5
beat_duration = bar_duration / 4  # 0.375s per beat

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=0.75, end=1.125))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=1.125, end=1.5))

# Hihat on every eighth note
for i in range(8):
    time = i * beat_duration / 2
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=hihat, start=time, end=time + beat_duration / 2))

# --- BAR 2-4: Full Quartet (1.5 - 6.0s) ---

# Time starts at 1.5s for the main melody

# --- BASS (Marcus): Walking line in Fm, chromatic approaches, no repeated notes ---
# Fm scale: F, Gb, Ab, Bb, B, Db, Eb, F
# Walking bass line: F - Gb - Ab - Bb (1st bar), B - Db - Eb - F (2nd bar), F - Gb - Ab - Bb (3rd bar), B - Db - Eb - F (4th bar)

bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),  # F3 (71)
    pretty_midi.Note(velocity=80, pitch=70, start=1.875, end=2.25),  # Gb3 (70)
    pretty_midi.Note(velocity=80, pitch=68, start=2.25, end=2.625),  # Ab3 (68)
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=3.0),   # Bb3 (67)

    # Bar 3
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.375),  # B3 (65)
    pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.75),  # Db3 (64)
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.125),  # Eb3 (62)
    pretty_midi.Note(velocity=80, pitch=71, start=4.125, end=4.5),   # F3 (71)

    # Bar 4
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.875),  # F3 (71)
    pretty_midi.Note(velocity=80, pitch=70, start=4.875, end=5.25),  # Gb3 (70)
    pretty_midi.Note(velocity=80, pitch=68, start=5.25, end=5.625),  # Ab3 (68)
    pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=6.0),   # Bb3 (67)
]

bass.notes.extend(bass_notes)

# --- PIANO (Diane): 7th chords on 2 and 4, comping to move things along ---

# Fm7 = F (71), Ab (68), Bb (67), Db (64)
# Bbm7 = Bb (67), Db (64), Eb (62), F (71)
# Fm7 again on 4th beat (bar 2 and 3)

# Bar 2
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=68, start=1.5, end=1.875))  # Ab
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875))  # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875))  # Db

# Bar 3
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375))  # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375))  # Db
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375))  # Eb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375))  # F

# Bar 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=68, start=4.5, end=4.875))  # Ab
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875))  # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875))  # Db

# --- SAX (Dante): Motif - start it, leave it hanging, come back and finish it ---

# Motif: F (71), Gb (70), Ab (68), Bb (67) — a simple Fm tetrad, played as a phrase
# Start on bar 2, play first two notes, then leave it hanging until bar 4

# Bar 2 (first two notes)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.6875))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=1.6875, end=1.875))  # Gb

# Bar 4 (last two notes)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=5.25, end=5.4375))  # Ab
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=5.4375, end=5.625))  # Bb

# --- DRUMS (Little Ray): Continue with the same pattern for bar 2-4 ---

# Bar 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=1.875, end=2.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=2.25, end=2.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=2.625, end=3.0))

# Bar 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=3.375, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=3.75, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=4.125, end=4.5))

# Bar 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=5.25, end=5.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=5.625, end=6.0))

# Add hihat on every eighth for bars 2-4
for i in range(8):
    time = 1.5 + (i * beat_duration / 2)
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=hihat, start=time, end=time + beat_duration / 2))

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

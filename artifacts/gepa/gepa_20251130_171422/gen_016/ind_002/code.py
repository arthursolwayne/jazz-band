
import pretty_midi

# Create a new MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define note values based on 160 BPM (each beat = 0.375s)
beat = 0.375

# Drums: kick=36, snare=38, hihat=42
# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat_idx in range(4):
        time = bar * 1.5 + beat_idx * beat
        if beat_idx == 0 or beat_idx == 2:
            # Kick on 1 and 3
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
        elif beat_idx == 1 or beat_idx == 3:
            # Snare on 2 and 4
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
        # Hihat on every eighth
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.1)
        drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Saxophone (Dante) - 4-note motif: Dm7 -> G7 -> Cm7 -> F7 (In D minor)
# Dm7: D, F, A, C
# G7: G, B, D, F
# Cm7: C, Eb, G, Bb
# F7: F, A, C, Eb

# Time of each bar: 1.5 seconds
# Each note is a quarter note (1 beat) = 0.375s
# Start at time 1.5s

# Bar 2 (1.5 - 3.0s)
# Dm7
note = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875)  # D
sax.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875)  # F
sax.notes.append(note)
note = pretty_midi.Note(velocity=85, pitch=67, start=1.5, end=1.875)  # A
sax.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.875)  # C
sax.notes.append(note)

# Bar 3 (3.0 - 4.5s)
# G7
note = pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375)  # G
sax.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375)  # B
sax.notes.append(note)
note = pretty_midi.Note(velocity=85, pitch=69, start=3.0, end=3.375)  # D
sax.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.375)  # F
sax.notes.append(note)

# Bar 4 (4.5 - 6.0s)
# Cm7
note = pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875)  # C
sax.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=63, start=4.5, end=4.875)  # Eb
sax.notes.append(note)
note = pretty_midi.Note(velocity=85, pitch=67, start=4.5, end=4.875)  # G
sax.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.875)  # Bb
sax.notes.append(note)

# Bass (Marcus) - Walking bass line with chromatic motion
# Bar 2 (1.5 - 3.0s): D -> Eb -> F -> G
note = pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875)  # D
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25)  # Eb
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.625)  # F
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=65, start=2.625, end=3.0)  # G

# Bar 3 (3.0 - 4.5s): A -> Bb -> B -> C
note = pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375)  # A
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=68, start=3.375, end=3.75)  # Bb
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.125)  # B
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=70, start=4.125, end=4.5)  # C

# Bar 4 (4.5 - 6.0s): D -> Eb -> F -> G
note = pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875)  # D
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=63, start=4.875, end=5.25)  # Eb
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.625)  # F
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=65, start=5.625, end=6.0)  # G

# Piano (Diane) - 7th chords, comping on offbeats
# Bar 2 (1.5 - 3.0s): Dm7 on beat 2 and 4
note = pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625)  # D
piano.notes.append(note)
note = pretty_midi.Note(velocity=85, pitch=64, start=2.25, end=2.625)  # F
piano.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625)  # A
piano.notes.append(note)
note = pretty_midi.Note(velocity=75, pitch=69, start=2.25, end=2.625)  # C

note = pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125)  # D
piano.notes.append(note)
note = pretty_midi.Note(velocity=85, pitch=64, start=3.75, end=4.125)  # F
piano.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.125)  # A
piano.notes.append(note)
note = pretty_midi.Note(velocity=75, pitch=69, start=3.75, end=4.125)  # C

# Bar 3 (3.0 - 4.5s): G7 on beat 2 and 4
note = pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125)  # G
piano.notes.append(note)
note = pretty_midi.Note(velocity=85, pitch=71, start=3.75, end=4.125)  # B
piano.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.125)  # D
piano.notes.append(note)
note = pretty_midi.Note(velocity=75, pitch=64, start=3.75, end=4.125)  # F

note = pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625)  # G
piano.notes.append(note)
note = pretty_midi.Note(velocity=85, pitch=71, start=5.25, end=5.625)  # B
piano.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.625)  # D
piano.notes.append(note)
note = pretty_midi.Note(velocity=75, pitch=64, start=5.25, end=5.625)  # F

# Bar 4 (4.5 - 6.0s): Cm7 on beat 2 and 4
note = pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.625)  # C
piano.notes.append(note)
note = pretty_midi.Note(velocity=85, pitch=63, start=5.25, end=5.625)  # Eb
piano.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.625)  # G
piano.notes.append(note)
note = pretty_midi.Note(velocity=75, pitch=71, start=5.25, end=5.625)  # Bb

note = pretty_midi.Note(velocity=90, pitch=60, start=6.0, end=6.375)  # C
piano.notes.append(note)
note = pretty_midi.Note(velocity=85, pitch=63, start=6.0, end=6.375)  # Eb
piano.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=67, start=6.0, end=6.375)  # G
piano.notes.append(note)
note = pretty_midi.Note(velocity=75, pitch=71, start=6.0, end=6.375)  # Bb

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("dante_intro.mid")

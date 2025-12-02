
import pretty_midi

# Create a new MIDI file with the given tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax (Dante)
bass = pretty_midi.Instrument(program=33)      # Bass (Marcus)
piano = pretty_midi.Instrument(program=0)      # Piano (Diane)
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums (Little Ray)

# Drums: MIDI note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Time per bar at 160 BPM
BEAT = 0.375  # seconds per beat
BAR = 1.5     # seconds per bar

# Bar 1: Drums only (0.0 - 1.5s)
# Little Ray sets the mood — tight, energetic, with a hint of tension
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=KICK, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=KICK, start=0.75, end=1.125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=SNARE, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=SNARE, start=1.125, end=1.5),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=HIHAT, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=HIHAT, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=HIHAT, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=HIHAT, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full ensemble (1.5 - 3.0s)
# Diane plays a Dm7 chord in the background (D F A C)
# Marcus walks a chromatic line starting on G, moving down
# You (Dante) play a short motif in the melody: D - Eb - F - G, then leave it hanging
# Little Ray continues with his tighter groove

# Piano: Dm7 on beats 2 and 4
piano_notes = [
    # Dm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.25),  # C
    # Dm7 on beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),   # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),   # A
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=3.0),   # C
]

for note in piano_notes:
    piano.notes.append(note)

# Bass: Chromatic walk from G to F (starting on G, ending on F)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=90, pitch=66, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),   # E
]

for note in bass_notes:
    bass.notes.append(note)

# Sax: D - Eb - F - G, starting on beat 1, ending on beat 4 (hanging on G)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # G
]

for note in sax_notes:
    sax.notes.append(note)

# Drums continue with the same pattern
for i in range(2):
    for note in drum_notes:
        new_note = pretty_midi.Note(note.velocity, note.pitch, note.start + 1.5 * (i + 1), note.end + 1.5 * (i + 1))
        drums.notes.append(new_note)

# Bar 3: Full ensemble (3.0 - 4.5s)
# Piano: Dm7 on beats 2 and 4
# Bass: Chromatic walk from G to F (again)
# Sax: Rest (no melody for now, just space)
# Drums continue

# Piano notes (same as bar 2)
for note in piano_notes:
    new_note = pretty_midi.Note(note.velocity, note.pitch, note.start + 1.5, note.end + 1.5)
    piano.notes.append(new_note)

# Bass notes (same as bar 2)
for note in bass_notes:
    new_note = pretty_midi.Note(note.velocity, note.pitch, note.start + 1.5, note.end + 1.5)
    bass.notes.append(new_note)

# Drums
for note in drum_notes:
    new_note = pretty_midi.Note(note.velocity, note.pitch, note.start + 3.0, note.end + 3.0)
    drums.notes.append(new_note)

# Bar 4: Full ensemble (4.5 - 6.0s)
# Piano: Dm7 on beats 2 and 4
# Bass: Chromatic walk from G to F
# Sax: Repeat the motif, but finish it — hold the G at the end
# Drums continue

# Piano notes (same as bar 2)
for note in piano_notes:
    new_note = pretty_midi.Note(note.velocity, note.pitch, note.start + 3.0, note.end + 3.0)
    piano.notes.append(new_note)

# Bass notes (same as bar 2)
for note in bass_notes:
    new_note = pretty_midi.Note(note.velocity, note.pitch, note.start + 3.0, note.end + 3.0)
    bass.notes.append(new_note)

# Drums
for note in drum_notes:
    new_note = pretty_midi.Note(note.velocity, note.pitch, note.start + 4.5, note.end + 4.5)
    drums.notes.append(new_note)

# Sax: Repeat the motif and hold the final G
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),   # G
]

for note in sax_notes:
    sax.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file to disk
midi.write("dante_intro.mid")

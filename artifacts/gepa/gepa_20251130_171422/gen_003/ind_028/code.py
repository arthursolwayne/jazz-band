
import pretty_midi

# Initialize the MIDI file with tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Bar 1 (0.0 - 1.5s): Only drums — Little Ray sets it up
# Rhythmic tension with open hi-hat, snare, and kick on the offbeats
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=HIHAT, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=KICK, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=HIHAT, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=SNARE, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4 (1.5 - 6.0s): Full quartet

# Bar 2: Saxophone motif — the question
sax_note = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875)  # D4
sax.notes.append(sax_note)

sax_note = pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25)  # E4
sax.notes.append(sax_note)

sax_note = pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625)  # F#4
sax.notes.append(sax_note)

sax_note = pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0)  # D4
sax.notes.append(sax_note)

# Bass: Chromatic walking line, descending from B4 to D4
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.875),  # B4
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.25),  # A4
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=80, pitch=62, start=2.625, end=3.0),  # D4
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comping with sharp, assertive rhythm
piano_notes = [
    # D7 chord (D, F#, A, C#) on the "and" of 2 and the "and" of 4
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # B4

    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),  # B4
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 2: Drums continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 3.0s)
for i in range(4):
    start = 1.5 + i * 0.375
    if i % 2 == 0:
        pretty_midi.Note(velocity=100, pitch=KICK, start=start, end=start + 0.375)
    else:
        pretty_midi.Note(velocity=100, pitch=SNARE, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=HIHAT, start=start, end=start + 0.375)

# Bar 3: Same pattern
for i in range(4):
    start = 3.0 + i * 0.375
    if i % 2 == 0:
        pretty_midi.Note(velocity=100, pitch=KICK, start=start, end=start + 0.375)
    else:
        pretty_midi.Note(velocity=100, pitch=SNARE, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=HIHAT, start=start, end=start + 0.375)

# Bar 4: Same pattern
for i in range(4):
    start = 4.5 + i * 0.375
    if i % 2 == 0:
        pretty_midi.Note(velocity=100, pitch=KICK, start=start, end=start + 0.375)
    else:
        pretty_midi.Note(velocity=100, pitch=SNARE, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=HIHAT, start=start, end=start + 0.375)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

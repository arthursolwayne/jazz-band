
import pretty_midi

# Create a MIDI file with initial tempo of 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum pitches
kick = 36
snare = 38
hihat = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(4):
    time = beat * 0.375
    if beat % 2 == 0:
        # Kick on beat 1 and 3
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.125))
    else:
        # Snare on beat 2 and 4
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + 0.125))
    # Hi-hat on every eighth
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=hihat, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Dm, chromatic approaches, no repeated notes
bass_notes = [
    (pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75)),  # D
    (pretty_midi.Note(velocity=100, pitch=63, start=1.75, end=2.0)),  # Eb
    (pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25)),  # C
    (pretty_midi.Note(velocity=100, pitch=61, start=2.25, end=2.5)),  # Db
    (pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75)),  # D
    (pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0)),  # E
    (pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.25)),  # Eb
    (pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5)),  # D
    (pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75)),  # F
    (pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.0)),  # E
    (pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.25)),  # E
    (pretty_midi.Note(velocity=100, pitch=65, start=4.25, end=4.5)),  # F
    (pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75)),  # E
    (pretty_midi.Note(velocity=100, pitch=63, start=4.75, end=5.0)),  # Eb
    (pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25)),  # D
    (pretty_midi.Note(velocity=100, pitch=61, start=5.25, end=5.5)),  # Db
    (pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75)),  # D
    (pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0)),  # E
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0)),  # D7
    (pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0)),
    (pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0)),
    (pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0)),
    (pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.5)),  # D7
    (pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5)),
    (pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.5)),
    (pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.5)),
    (pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.0)),  # D7
    (pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0)),
    (pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.0)),
    (pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.0)),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Your moment. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.75)),  # E
    (pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=2.0)),  # G
    (pretty_midi.Note(velocity=110, pitch=66, start=2.5, end=2.75)),  # E
    (pretty_midi.Note(velocity=110, pitch=69, start=2.75, end=3.0)),  # G
    (pretty_midi.Note(velocity=110, pitch=66, start=3.5, end=3.75)),  # E
    (pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.0)),  # G
    (pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.75)),  # F
    (pretty_midi.Note(velocity=110, pitch=71, start=4.75, end=5.0)),  # A
    (pretty_midi.Note(velocity=110, pitch=69, start=5.0, end=5.25)),  # G
    (pretty_midi.Note(velocity=110, pitch=66, start=5.25, end=5.5)),  # E
    (pretty_midi.Note(velocity=110, pitch=64, start=5.5, end=5.75)),  # D
    (pretty_midi.Note(velocity=110, pitch=62, start=5.75, end=6.0)),  # C
]

for note in sax_notes:
    sax.notes.append(note)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

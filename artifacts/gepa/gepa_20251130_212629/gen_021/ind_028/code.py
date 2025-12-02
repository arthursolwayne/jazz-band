
import pretty_midi

# Create a MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Saxophone
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define the duration of one bar in seconds
bar_length = 60.0 / 160  # 160 BPM → 0.375 seconds per beat (quarter note)

# Drums
drum_notes = [
    # Kick on beats 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=bar_length * 0.75),
    pretty_midi.Note(velocity=100, pitch=36, start=bar_length * 2.0, end=bar_length * 2.75),
    # Snare on beats 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=bar_length * 1.0, end=bar_length * 1.25),
    pretty_midi.Note(velocity=110, pitch=38, start=bar_length * 3.0, end=bar_length * 3.25),
    # Hi-hat on every eighth note
    *[
        pretty_midi.Note(velocity=90, pitch=42, start=bar_length * i, end=bar_length * i + bar_length / 4)
        for i in range(0, 4)
    ] + [
        pretty_midi.Note(velocity=90, pitch=42, start=bar_length * (i + 0.5), end=bar_length * (i + 0.75))
        for i in range(0, 4)
    ] + [
        # Syncopated hi-hat for tension
        pretty_midi.Note(velocity=90, pitch=42, start=bar_length * 1.75, end=bar_length * 1.875),
        pretty_midi.Note(velocity=90, pitch=42, start=bar_length * 3.875, end=bar_length * 4.0)
    ]
]
for note in drum_notes:
    drums.notes.append(note)

# Saxophone: Melodic motif in D minor (D, F, Eb, G, Eb, F, D)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=bar_length * 1.0, end=bar_length * 1.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=bar_length * 1.25, end=bar_length * 1.5),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=bar_length * 1.5, end=bar_length * 1.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=bar_length * 1.75, end=bar_length * 2.0),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=bar_length * 2.25, end=bar_length * 2.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=bar_length * 2.5, end=bar_length * 2.75),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=bar_length * 2.75, end=bar_length * 3.0),  # D
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in D minor
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=bar_length * 1.0, end=bar_length * 1.25),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=bar_length * 1.25, end=bar_length * 1.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=62, start=bar_length * 1.5, end=bar_length * 1.75),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=bar_length * 1.75, end=bar_length * 2.0),  # F
    pretty_midi.Note(velocity=80, pitch=65, start=bar_length * 2.25, end=bar_length * 2.5),  # G
    pretty_midi.Note(velocity=80, pitch=62, start=bar_length * 2.5, end=bar_length * 2.75),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=bar_length * 2.75, end=bar_length * 3.0),  # Bb
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Comping with Fm7 on beats 2 & 4
piano_notes = [
    # Fm7 (F, Ab, Bb, D)
    pretty_midi.Note(velocity=85, pitch=64, start=bar_length * 1.0, end=bar_length * 1.25),  # F
    pretty_midi.Note(velocity=85, pitch=66, start=bar_length * 1.0, end=bar_length * 1.25),  # Ab
    pretty_midi.Note(velocity=85, pitch=62, start=bar_length * 1.0, end=bar_length * 1.25),  # Bb
    pretty_midi.Note(velocity=85, pitch=67, start=bar_length * 1.0, end=bar_length * 1.25),  # D
    # Repeat on beat 4
    pretty_midi.Note(velocity=85, pitch=64, start=bar_length * 3.0, end=bar_length * 3.25),
    pretty_midi.Note(velocity=85, pitch=66, start=bar_length * 3.0, end=bar_length * 3.25),
    pretty_midi.Note(velocity=85, pitch=62, start=bar_length * 3.0, end=bar_length * 3.25),
    pretty_midi.Note(velocity=85, pitch=67, start=bar_length * 3.0, end=bar_length * 3.25),
]
for note in piano_notes:
    piano.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("4_bar_jazz_in_d.mid")

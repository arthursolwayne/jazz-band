
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# But with variation in dynamics and spacing
drum_notes = [
    # Bar 1
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=1.5),    # Hihat on 1
    pretty_midi.Note(velocity=60, pitch=42, start=0.375, end=1.5),  # Hihat on 2
    pretty_midi.Note(velocity=60, pitch=42, start=0.75, end=1.5),   # Hihat on 3
    pretty_midi.Note(velocity=60, pitch=42, start=1.125, end=1.5),  # Hihat on 4
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # Snare on 4
]

# Bar 2: Full quartet (1.5 - 3.0s)
# Saxophone motif: D - F# - B - A (Dorian mode, emotional and concise)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=95, pitch=66, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=105, pitch=71, start=2.25, end=2.625), # B
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=3.0),  # A

    # Bass line: Walking line with chromatic approaches
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=75, pitch=46, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=85, pitch=47, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=80, pitch=49, start=2.625, end=3.0),  # G

    # Piano: 7th chords, comp on 2 and 4
    pretty_midi.Note(velocity=75, pitch=67, start=1.5, end=1.875),  # D7 (F#)
    pretty_midi.Note(velocity=70, pitch=71, start=1.5, end=1.875),  # D7 (B)
    pretty_midi.Note(velocity=65, pitch=74, start=1.5, end=1.875),  # D7 (D)
    pretty_midi.Note(velocity=75, pitch=62, start=1.875, end=2.25),  # D7 (D)
    pretty_midi.Note(velocity=70, pitch=67, start=1.875, end=2.25),  # D7 (F#)
    pretty_midi.Note(velocity=65, pitch=71, start=1.875, end=2.25),  # D7 (B)
    pretty_midi.Note(velocity=75, pitch=62, start=2.625, end=3.0),   # D7 (D)
    pretty_midi.Note(velocity=70, pitch=67, start=2.625, end=3.0),   # D7 (F#)
    pretty_midi.Note(velocity=65, pitch=71, start=2.625, end=3.0),   # D7 (B)

    # Drums
    pretty_midi.Note(velocity=90, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=60, pitch=42, start=1.5, end=3.0),    # Hihat on 1-4
    pretty_midi.Note(velocity=60, pitch=42, start=1.875, end=3.0),
    pretty_midi.Note(velocity=60, pitch=42, start=2.25, end=3.0),
    pretty_midi.Note(velocity=60, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),  # Snare on 4 (out of bar)
]

# Bar 3: Full quartet (3.0 - 4.5s)
# Saxophone: Return motif with slight variation
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=95, pitch=66, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=105, pitch=71, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=110, pitch=69, start=4.125, end=4.5),  # A

    # Bass line: Chromatic variation
    pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=75, pitch=43, start=3.375, end=3.75),  # C#
    pretty_midi.Note(velocity=85, pitch=44, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=4.125, end=4.5),  # G

    # Piano: 7th chords, comp on 2 and 4
    pretty_midi.Note(velocity=75, pitch=67, start=3.0, end=3.375),  # D7 (F#)
    pretty_midi.Note(velocity=70, pitch=71, start=3.0, end=3.375),  # D7 (B)
    pretty_midi.Note(velocity=65, pitch=74, start=3.0, end=3.375),  # D7 (D)
    pretty_midi.Note(velocity=75, pitch=62, start=3.375, end=3.75),  # D7 (D)
    pretty_midi.Note(velocity=70, pitch=67, start=3.375, end=3.75),  # D7 (F#)
    pretty_midi.Note(velocity=65, pitch=71, start=3.375, end=3.75),  # D7 (B)
    pretty_midi.Note(velocity=75, pitch=62, start=3.75, end=4.125),  # D7 (D)
    pretty_midi.Note(velocity=70, pitch=67, start=3.75, end=4.125),  # D7 (F#)
    pretty_midi.Note(velocity=65, pitch=71, start=3.75, end=4.125),  # D7 (B)
    pretty_midi.Note(velocity=75, pitch=62, start=4.125, end=4.5),   # D7 (D)
    pretty_midi.Note(velocity=70, pitch=67, start=4.125, end=4.5),   # D7 (F#)
    pretty_midi.Note(velocity=65, pitch=71, start=4.125, end=4.5),   # D7 (B)

    # Drums
    pretty_midi.Note(velocity=90, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=60, pitch=42, start=3.0, end=4.5),    # Hihat on 1-4
    pretty_midi.Note(velocity=60, pitch=42, start=3.375, end=4.5),
    pretty_midi.Note(velocity=60, pitch=42, start=3.75, end=4.5),
    pretty_midi.Note(velocity=60, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),  # Snare on 4 (out of bar)
])

# Bar 4: Full quartet (4.5 - 6.0s)
# Saxophone: Resolve motif
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=105, pitch=67, start=4.875, end=5.25),  # F#
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625), # B
    pretty_midi.Note(velocity=105, pitch=69, start=5.625, end=6.0),  # A

    # Bass line: Chromatic variation
    pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=75, pitch=47, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=85, pitch=49, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=80, pitch=50, start=5.625, end=6.0),  # G#

    # Piano: 7th chords, comp on 2 and 4
    pretty_midi.Note(velocity=75, pitch=67, start=4.5, end=4.875),  # D7 (F#)
    pretty_midi.Note(velocity=70, pitch=71, start=4.5, end=4.875),  # D7 (B)
    pretty_midi.Note(velocity=65, pitch=74, start=4.5, end=4.875),  # D7 (D)
    pretty_midi.Note(velocity=75, pitch=62, start=4.875, end=5.25),  # D7 (D)
    pretty_midi.Note(velocity=70, pitch=67, start=4.875, end=5.25),  # D7 (F#)
    pretty_midi.Note(velocity=65, pitch=71, start=4.875, end=5.25),  # D7 (B)
    pretty_midi.Note(velocity=75, pitch=62, start=5.25, end=5.625),  # D7 (D)
    pretty_midi.Note(velocity=70, pitch=67, start=5.25, end=5.625),  # D7 (F#)
    pretty_midi.Note(velocity=65, pitch=71, start=5.25, end=5.625),  # D7 (B)
    pretty_midi.Note(velocity=75, pitch=62, start=5.625, end=6.0),   # D7 (D)
    pretty_midi.Note(velocity=70, pitch=67, start=5.625, end=6.0),   # D7 (F#)
    pretty_midi.Note(velocity=65, pitch=71, start=5.625, end=6.0),   # D7 (B)

    # Drums
    pretty_midi.Note(velocity=90, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=60, pitch=42, start=4.5, end=6.0),    # Hihat on 1-4
    pretty_midi.Note(velocity=60, pitch=42, start=4.875, end=6.0),
    pretty_midi.Note(velocity=60, pitch=42, start=5.25, end=6.0),
    pretty_midi.Note(velocity=60, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=38, start=6.0, end=6.375),  # Snare on 4 (out of bar)
])

# Adding notes to instruments
for note in drum_notes:
    drums.notes.append(note)

for note in sax_notes:
    sax.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_4bar_intro.mid")
